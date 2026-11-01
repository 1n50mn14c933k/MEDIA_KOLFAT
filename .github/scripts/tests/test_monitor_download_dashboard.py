import importlib.util
import unittest
from datetime import datetime,timedelta,timezone
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"monitor_download_dashboard.py"
spec=importlib.util.spec_from_file_location("health",p)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
now=datetime(2026,10,29,12,0,tzinfo=timezone.utc)
def state(h=0.5):
    d=now-timedelta(hours=h)
    return {"schema_version":2,"last_checked_at_utc":d.isoformat(),
            "snapshots":[{"date":d.date().isoformat(),"counts":{"windows":12,"linux":0,"macos":None}}]}
def svg(s):
    if "last_checked_at_utc" in s:
        d=datetime.fromisoformat(s["last_checked_at_utc"])
        return "Last checked: "+d.strftime("%Y-%m-%d %H:%M UTC")
    return "Last snapshot: "+s["snapshots"][-1]["date"]+" UTC"
def runs(c="success"):
    return [{"head_branch":"main","status":"completed","conclusion":c,"created_at":"2026-10-29T11:30:00Z"}]
class Tests(unittest.TestCase):
    def test_healthy(self):
        s=state()
        self.assertTrue(m.evaluate(s,svg(s),runs(),now)["healthy"])
    def test_110_minutes_exact(self):
        s=state(110/60)
        self.assertTrue(m.evaluate(s,svg(s),runs(),now)["healthy"])
    def test_110_minutes_exceeded(self):
        s=state(111/60)
        self.assertFalse(m.evaluate(s,svg(s),runs(),now)["healthy"])
    def test_updater_failure(self):
        s=state()
        self.assertFalse(m.evaluate(s,svg(s),runs("failure"),now)["healthy"])
    def test_cancelled(self):
        s=state()
        self.assertFalse(m.evaluate(s,svg(s),runs("cancelled"),now)["healthy"])
    def test_missing_api(self):
        s=state()
        self.assertFalse(m.evaluate(s,svg(s),None,now)["healthy"])
    def test_svg_mismatch(self):
        self.assertFalse(m.evaluate(state(),"bad svg",runs(),now)["healthy"])
    def test_bad_counter(self):
        s=state()
        s["snapshots"][-1]["counts"]["windows"]=-10
        self.assertFalse(m.evaluate(s,svg(s),runs(),now)["healthy"])
    def test_old_data(self):
        s=state(70)
        self.assertFalse(m.evaluate(s,svg(s),runs(),now)["healthy"])
    def test_in_progress_never_masks_failure(self):
        s=state()
        r=runs("failure")+[{"head_branch":"main","status":"in_progress","created_at":"2026-10-29T10:00:00Z"}]
        self.assertFalse(m.evaluate(s,svg(s),r,now)["healthy"])
    def test_legacy_history_no_invented_time(self):
        s=state()
        del s["last_checked_at_utc"]
        self.assertTrue(m.evaluate(s,svg(s),runs(),now)["healthy"])
    def test_old_success_run_does_not_mask_missing_schedule(self):
        s=state()
        old=[{"head_branch":"main","status":"completed","conclusion":"success","created_at":"2026-10-29T09:00:00Z"}]
        self.assertFalse(m.evaluate(s,svg(s),old,now)["healthy"])
    def test_live_download_mismatch(self):
        s=state(1)
        live={"totals":{"windows":27,"linux":1,"macos":0},"active":{"windows":True,"linux":True,"macos":False}}
        report=m.evaluate(s,svg(s),runs(),now,live)
        self.assertFalse(report["healthy"])
        self.assertTrue(any("Live windows" in x for x in report["reasons"]))
    def test_recent_download_does_not_trigger_false_alarm(self):
        s=state(0.1)
        live={"totals":{"windows":27,"linux":0,"macos":0},"active":{"windows":True,"linux":True,"macos":False}}
        self.assertTrue(m.evaluate(s,svg(s),runs(),now,live)["healthy"])
if __name__=="__main__":unittest.main()
