"""Source-level tests, no network, no real GitHub state changes."""
import importlib.util
import unittest
from datetime import date
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
    def test_invalid_asset_counts(self):
        for bad in (-1,True,"12"):
            with self.assertRaises(ValueError):
                mod.collect([{"draft":False,"assets":[{"id":1,"name":"test.exe",
                                                          "download_count":bad}]}])

if __name__ == "__main__":
    unittest.main()
