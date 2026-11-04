"""Regression tests: do not fabricate views or sum unique visitors across days."""
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from collect_repo_visitors import build_snapshot, periods, select_period


class RepositoryVisitorTests(unittest.TestCase):
    def test_completed_day_and_week(self):
        self.assertEqual(tuple(map(str, periods(datetime(2026, 11, 4, 12, tzinfo=timezone.utc)))),
                         ("2026-11-03", "2026-10-26", "2026-11-01"))

    def test_monday_uses_previous_complete_week(self):
        self.assertEqual(tuple(map(str, periods(datetime(2026, 11, 9, 12, tzinfo=timezone.utc)))),
                         ("2026-11-08", "2026-11-02", "2026-11-08"))

    def test_weekly_unique_visitors_are_native_github_metric(self):
        now = datetime(2026, 11, 4, 12, tzinfo=timezone.utc)
        day = {"views": [{"timestamp": "2026-11-03T00:00:00Z", "count": 12, "uniques": 4}]}
        week = {"views": [{"timestamp": "2026-10-26T00:00:00Z", "count": 48, "uniques": 9}]}
        snapshot = build_snapshot(now, day, week)
        self.assertEqual(snapshot["daily"]["unique_visitors"], 4)
        self.assertEqual(snapshot["weekly"]["unique_visitors"], 9)
        self.assertEqual(snapshot["weekly"]["views"], 48)

    def test_missing_data_is_unavailable_not_zero(self):
        result = select_period({"views": []}, "views",
                               datetime(2026, 11, 3, tzinfo=timezone.utc).date())
        self.assertIsNone(result["unique_visitors"])
        self.assertIsNone(result["views"])

    def test_reject_bad_or_ambiguous_traffic(self):
        day = datetime(2026, 11, 3, tzinfo=timezone.utc).date()
        for data in [{"count": 2, "uniques": 4}, {"count": -1, "uniques": 0},
                     {"count": "3", "uniques": 1}, {"count": 2, "uniques": True}]:
            with self.subTest(data=data), self.assertRaises(ValueError):
                select_period({"views": [{"timestamp": "2026-11-03T00:00:00Z", **data}]}, "views", day)


if __name__ == "__main__":
    unittest.main()
