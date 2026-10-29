import importlib.util
import unittest
from datetime import datetime,timedelta,timezone
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"monitor_download_dashboard.py"
spec=importlib.util.spec_from_file_location("health",p)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
now=datetime(2026,10,29,12,0,tzinfo=timezone.utc)
def state(h=8):
    d=now-timedelta(hours=h)
    return {"schema_version":2,"last_checked_at_utc":d.isoformat(),
            "snapshots":[{"date":d.date().isoformat(),"counts":{"windows":12,"linux":0,"macos":None}}]}
def svg(s):return "Last snapshot: "+s["snapshots"][-1]["date"]+" UTC"
def runs(c="success"):
    return [{"head_branch":"main","status":"completed","conclusion":c,"created_at":"2026-10-29T09:00:00Z"}]
class Tests(unittest.TestCase):
    def test_healthy(self):
        s=state()
        self.assertTrue(m.evaluate(s,svg(s),runs(),now)["healthy"])
    def test_48_hours_exact(self):
        s=state(48)
        self.assertTrue(m.evaluate(s,svg(s),runs(),now)["healthy"])
    def test_48_hours_exceeded(self):
        s=state(48.01)
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
if __name__=="__main__":unittest.main()
