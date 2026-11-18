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

    def test_ledger_counts_all_versions_and_platforms_after_deletion(self):
        now=datetime(2026,11,18,19,0,tzinfo=timezone.utc)
        releases=[
          {"tag_name":"v2.0.0","assets":[{"id":1,"name":"setup.exe","download_count":81}]},
          {"tag_name":"v2.4.0-linux","assets":[{"id":2,"name":"media-linux.AppImage","download_count":3}]},
          {"tag_name":"v2.4.0-macos","assets":[{"id":3,"name":"media-macos.dmg","download_count":1}]},
        ]
        current=mod.collect(releases)
        prior=[{"date":"2026-11-17","counts":{"windows":81,"linux":3,"macos":1}}]
        first=mod.build_ledger({},current,now,prior)
        self.assertEqual(first["totals"],{"windows":81,"linux":3,"macos":1})
        after=mod.collect([
          {"tag_name":"v2.5.0","assets":[{"id":4,"name":"new-setup.exe","download_count":7}]},
          {"tag_name":"v2.5.0-linux","assets":[{"id":5,"name":"new-linux.AppImage","download_count":4}]},
          {"tag_name":"v2.5.0-macos","assets":[{"id":6,"name":"new-macos.dmg","download_count":2}]},
        ])
        ledger=mod.build_ledger(first,after,now+timedelta(hours=1),prior)
        self.assertEqual(ledger["totals"],{"windows":88,"linux":7,"macos":3})
        self.assertEqual(len([x for x in ledger["assets"] if x["state"]=="retired"]),3)
        self.assertEqual(len([x for x in ledger["assets"] if x["state"]=="published"]),3)
        result=mod.lifetime_observation(after,ledger)
        self.assertEqual(result["totals"]["windows"],88)
        self.assertEqual(result["totals"]["linux"],7)
        self.assertEqual(result["totals"]["macos"],3)
        self.assertEqual(len(result["assets"]),3)
        for osname,count in result["totals"].items():
            svg=mod.render_download_badge(osname,count,now)
            self.assertIn(str(count) + "</text>",svg)

    def test_ledger_reappearance_does_not_double_count(self):
        now=datetime(2026,11,18,19,0,tzinfo=timezone.utc)
        old=mod.collect([{"tag_name":"v2.0.0","assets":[
            {"id":11,"name":"media.exe","download_count":9}]}])
        saved=mod.build_ledger({},old,now)
        gone=mod.build_ledger(saved,mod.collect([]),now+timedelta(minutes=5))
        self.assertEqual(gone["totals"]["windows"],9)
        self.assertEqual(gone["assets"][0]["state"],"retired")
        returned=mod.build_ledger(gone,mod.collect([{"tag_name":"v2.0.0","assets":[
            {"id":11,"name":"media.exe","download_count":11}]}]),now+timedelta(minutes=20))
        self.assertEqual(returned["totals"]["windows"],11)
        self.assertEqual(returned["assets"][0]["state"],"published")

    def test_ledger_prevents_unverified_loss_and_counter_reset(self):
        now=datetime(2026,11,18,19,0,tzinfo=timezone.utc)
        old=mod.collect([{"tag_name":"v2.0.0","assets":[
            {"id":11,"name":"media.exe","download_count":9}]}])
        ledger=mod.build_ledger({},old,now)
        with self.assertRaises(ValueError):
            mod.build_ledger(ledger,mod.collect([{"tag_name":"v2.0.0","assets":[
                {"id":11,"name":"media.exe","download_count":8}]}]),now)
        with self.assertRaises(ValueError):
            mod.build_ledger({},mod.collect([]),now,[
                {"date":"2026-11-17","counts":{"windows":9,"linux":None,"macos":None}}])
        with self.assertRaises(ValueError):
            mod.build_ledger({"schema_version":12,"assets":[]},old,now)
        with self.assertRaises(ValueError):
            mod.build_ledger(ledger,mod.collect([{"tag_name":"v2.0.0","assets":[
                {"id":11,"name":"other.exe","download_count":9}]}]),now)

    def test_checksum_and_draft_not_seeded_into_ledger(self):
        now=datetime(2026,11,18,19,0,tzinfo=timezone.utc)
        live=mod.collect([
          {"tag_name":"v2.0.0","draft":False,"assets":[
            {"id":10,"name":"app.exe","download_count":3},
            {"id":11,"name":"app_SHA256.txt","download_count":100}]},
          {"tag_name":"v2.6.0","draft":True,"assets":[
            {"id":12,"name":"new-app.exe","download_count":20}]}
        ])
        ledger=mod.build_ledger({},live,now)
        self.assertEqual([x["id"] for x in ledger["assets"]],[10])
        self.assertEqual(ledger["totals"]["windows"],3)

    def test_lifetime_badges_do_not_need_hardcoded_release_tags(self):
        now=datetime(2026,11,18,19,0,tzinfo=timezone.utc)
        for osname,num in (("windows",81),("linux",3),("macos",1)):
            with self.subTest(platform=osname):
                svg=mod.render_download_badge(osname,num,now)
                self.assertIn("lifetime GitHub downloads",svg)
                self.assertIn(f">{num}</text>",svg)
                self.assertIn('width="160" height="32"',svg)
        self.assertIn(">N/A</text>",mod.render_download_badge("macos",None,now))
        with self.assertRaises(ValueError):
            mod.render_download_badge("windows",-1,now)

    def test_invalid_asset_counts(self):
        for bad in (-1,True,"12"):
            with self.assertRaises(ValueError):
                mod.collect([{"draft":False,"assets":[{"id":1,"name":"test.exe",
                                                          "download_count":bad}]}])

if __name__ == "__main__":
    unittest.main()
