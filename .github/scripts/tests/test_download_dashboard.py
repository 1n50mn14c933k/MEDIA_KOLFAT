"""Source-level tests, no network, no real GitHub state changes."""
import importlib.util
import unittest
from datetime import date, datetime, timezone, timedelta
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/"update_download_dashboard.py"
spec=importlib.util.spec_from_file_location("dashboard",SCRIPT)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class DashboardTests(unittest.TestCase):
    def test_os_detection(self):
        cases={
          "MEDIA_KOLFAT_2.0.0_Setup.exe":"windows",
          "MEDIA_KOLFAT_Windows_2.2.msixbundle":"windows",
          "MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage":"linux",
          "MEDIA_KOLFAT_Linux_2.4.deb":"linux",
          "MEDIA_KOLFAT_macOS_2.6.dmg":"macos",
          "MEDIA_KOLFAT_macOS_2.6.pkg":"macos",
          "MEDIA_KOLFAT_macOS_2.6_arm64.zip":"macos",
          "MEDIA_KOLFAT_Linux_2.4_x64.tar.gz":"linux",
          "MEDIA_KOLFAT_2.0.0_SHA256.txt":None,
          "MEDIA_KOLFAT_Linux_SHA256.txt":None,
          "source.zip":None,
          "MEDIA_KOLFAT_User_Guide.pdf":None,
          "MEDIA_KOLFAT_2.4.0_Source.zip":None,
        }
        for filename,platform in cases.items():
            with self.subTest(filename=filename):
                self.assertEqual(mod.classify(filename),platform)
    def test_aggregate_including_prerelease_and_excluding_checksums(self):
        def asset(i,name,n):
            return {"id":i,"name":name,"download_count":n}
        releases=[
          {"tag_name":"v2.0.0","draft":False,"prerelease":False,"assets":[
             asset(1,"MEDIA_KOLFAT_2.0.0_Setup.exe",12),
             asset(2,"MEDIA_KOLFAT_2.0.0_SHA256.txt",200)]},
          {"tag_name":"v2.4.0-linux-beta","draft":False,"prerelease":True,"assets":[
             asset(3,"MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage",5)]},
          {"tag_name":"v2.5.0-mac-beta","draft":True,"prerelease":True,"assets":[
             asset(4,"MEDIA_KOLFAT_macOS_2.5.dmg",30)]},
        ]
        data=mod.collect(releases)
        self.assertEqual(data["totals"],{"windows":12,"linux":5,"macos":0})
        self.assertEqual(len(data["assets"]),2)
        self.assertEqual(data["active"],{"windows":True,"linux":True,"macos":False})
        svg=mod.draw([{"date":"2026-10-28","counts":{"windows":12,"linux":5,"macos":None}}],data)
        self.assertIn("Not released",svg)
        self.assertIn("WINDOWS",svg)
        self.assertIn("LINUX",svg)
        self.assertIn("macOS",svg)
        self.assertIn("MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage",svg)
        self.assertNotIn("SHA256.txt",svg)
    def test_history_migration_preserves_windows_and_unknown_os(self):
        old={"schema_version":1,"snapshots":[
          {"date":"2026-10-27","github_exe_downloads":12},
          {"date":"2026-10-28","github_exe_downloads":12}]}
        h=mod.read_history(old)
        self.assertEqual(h[0]["counts"],{"windows":12,"linux":None,"macos":None})
        obs={"totals":{"windows":13,"linux":2,"macos":0},
             "active":{"windows":True,"linux":True,"macos":False}}
        new=mod.update_history(h,obs,date(2026,10,29))
        self.assertEqual(mod.daily_rate(new,"windows"),1)
        self.assertIsNone(mod.daily_rate(new,"linux"))
        self.assertIsNone(mod.daily_rate(new,"macos"))
        new=mod.update_history(new,obs,date(2026,10,30))
        self.assertEqual(mod.daily_rate(new,"linux"),0)
        self.assertEqual(len(new),4)
    def test_same_day_replaces_and_counter_reset_not_rate(self):
        a={"date":"2026-10-27","counts":{"windows":15,"linux":None,"macos":None}}
        obs={"totals":{"windows":12,"linux":0,"macos":0},
             "active":{"windows":True,"linux":True,"macos":False}}
        h=mod.update_history([a],obs,date(2026,10,28))
        self.assertIsNone(mod.daily_rate(h,"windows"))
        h2=mod.update_history(h,obs,date(2026,10,28))
        self.assertEqual(len(h2),2)
    def test_hourly_rate_preserves_actual_observations(self):
        now=datetime(2026,11,1,9,23,tzinfo=timezone.utc)
        obs={"totals":{"windows":23,"linux":0,"macos":0},
             "active":{"windows":True,"linux":True,"macos":False}}
        old={"schema_version":2,"snapshots":[{"date":"2026-10-29",
             "counts":{"windows":12,"linux":0,"macos":None}}]}
        one=mod.record_hourly(old,obs,now)
        self.assertEqual(len(one),1)
        self.assertIsNone(mod.hourly_rate(one,"windows"))
        obs["totals"]["windows"]=27
        two=mod.record_hourly({"hourly_snapshots":one},obs,now+timedelta(hours=2))
        self.assertEqual(mod.hourly_rate(two,"windows"),2.0)
        self.assertEqual(mod.hourly_rate(two,"linux"),0.0)
        self.assertIsNone(mod.hourly_rate(two,"macos"))
        self.assertEqual(old["snapshots"][0]["counts"]["windows"],12)

    def test_hourly_rate_suppresses_resets_and_short_intervals(self):
        now=datetime(2026,11,1,9,23,tzinfo=timezone.utc)
        sample=lambda t,c:{"timestamp":t.isoformat().replace("+00:00","Z"),
                             "counts":{"windows":c,"linux":0,"macos":None}}
        first=sample(now,25)
        self.assertIsNone(mod.hourly_rate([first,sample(now+timedelta(minutes=10),26)],"windows"))
        self.assertIsNone(mod.hourly_rate([first,sample(now+timedelta(hours=1),24)],"windows"))

    def test_readme_badges_use_exact_release_assets(self):
        observation = mod.collect([
            {"tag_name": "v2.0.0", "draft": False, "assets": [
                {"id": 1, "name": "MEDIA_KOLFAT_2.0.0_Setup.exe", "download_count": 46},
                {"id": 2, "name": "MEDIA_KOLFAT_2.0.0_SHA256.txt", "download_count": 999}]},
            {"tag_name": "v2.4.0-linux-beta", "draft": False, "assets": [
                {"id": 3, "name": "MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage", "download_count": 3}]},
            {"tag_name": "v2.4.0-macos-beta", "draft": False, "assets": [
                {"id": 4, "name": "MEDIA_KOLFAT_macOS_Beta_2.4.0_arm64.dmg", "download_count": 1}]},
        ])
        self.assertEqual([mod.release_asset_count(observation, p) for p in mod.PLATFORMS],
                         [46, 3, 1])
        now = datetime(2026, 11, 5, 16, 0, tzinfo=timezone.utc)
        for p, expected in zip(mod.PLATFORMS, (46, 3, 1)):
            with self.subTest(platform=p):
                svg = mod.render_download_badge(p, expected, now)
                self.assertIn(f">{expected}</text>", svg)
                self.assertIn("DOWNLOADS", svg)
                self.assertIn("2026-11-05 16:00 UTC", svg)
                self.assertIn('width="160" height="32"', svg)

    def test_missing_asset_never_fabricates_zero(self):
        observation = mod.collect([])
        self.assertIsNone(mod.release_asset_count(observation, "windows"))
        svg = mod.render_download_badge(
            "windows", None, datetime(2026, 11, 5, tzinfo=timezone.utc))
        self.assertIn(">N/A</text>", svg)
        with self.assertRaises(ValueError):
            mod.render_download_badge("windows", -1,
                                      datetime(2026, 11, 5, tzinfo=timezone.utc))

    def test_invalid_asset_counts(self):
        for bad in (-1,True,"12"):
            with self.assertRaises(ValueError):
                mod.collect([{"draft":False,"assets":[{"id":1,"name":"test.exe",
                                                          "download_count":bad}]}])

if __name__ == "__main__":
    unittest.main()
