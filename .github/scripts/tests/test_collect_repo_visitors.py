"""Regression tests for weekly GitHub-reported visitor and page-view badges."""
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from collect_repo_visitors import build_snapshot, previous_complete_week, weekly_metrics, render_badge, format_week_range


class RepositoryVisitorTests(unittest.TestCase):
    def test_previous_completed_week(self):
        self.assertEqual(tuple(map(str, previous_complete_week(datetime(2026, 11, 4, 19, tzinfo=timezone.utc)))),
                         ("2026-10-26", "2026-11-01"))

    def test_monday_week_boundary(self):
        self.assertEqual(tuple(map(str, previous_complete_week(datetime(2026, 11, 9, 10, tzinfo=timezone.utc)))),
                         ("2026-11-02", "2026-11-08"))

    def test_one_week_one_source_for_both_metrics(self):
        now = datetime(2026, 11, 4, 19, tzinfo=timezone.utc)
        response = {"views": [{"timestamp": "2026-10-26T00:00:00Z", "uniques": 4, "count": 87}]}
        result = build_snapshot(now, response)
        self.assertEqual(result["weekly"]["unique_visitors"], 4)
        self.assertEqual(result["weekly"]["views"], 87)
        self.assertNotIn("daily", result)

    def test_missing_week_is_unavailable(self):
        day = previous_complete_week(datetime(2026, 11, 4, tzinfo=timezone.utc))[0]
        self.assertEqual(weekly_metrics({"views": []}, day),
                         {"unique_visitors": None, "views": None})

    def test_bad_counts_are_rejected(self):
        day = previous_complete_week(datetime(2026, 11, 4, tzinfo=timezone.utc))[0]
        for count, uniques in [(2, 4), (-1, 0), ("3", 1), (2, True)]:
            with self.subTest(count=count, uniques=uniques), self.assertRaises(ValueError):
                weekly_metrics({"views": [{"timestamp": day.isoformat() + "T00:00:00Z",
                                           "count": count, "uniques": uniques}]}, day)

    def test_date_range_across_year_boundary(self):
        self.assertEqual(format_week_range("2026-12-28", "2027-01-03"),
                         "28 Dec 2026 – 3 Jan 2027 · UTC")

    def test_missing_metric_renders_dash_not_zero(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "missing.svg"
            render_badge("GitHub repository page views", None, "2026-10-26", "2026-11-01", path)
            svg = path.read_text(encoding="utf-8")
            self.assertIn(">—</text>", svg)
            self.assertIn("26 Oct – 1 Nov 2026 · UTC", svg)

    def test_badges_preserve_exact_labels_and_numbers(self):
        with tempfile.TemporaryDirectory() as temp:
            for label, number in [("Unique GitHub repository visitors", 4),
                                  ("GitHub repository page views", 87)]:
                path = Path(temp) / "badge.svg"
                render_badge(label, number, "2026-10-26", "2026-11-01", path)
                svg = path.read_text(encoding="utf-8")
                self.assertIn(label, svg)
                self.assertIn(f">{number}</text>", svg)
                self.assertIn('width="370" height="48"', svg)
                self.assertIn("26 Oct – 1 Nov 2026 · UTC", svg)
                self.assertIn('y="36"', svg)


if __name__ == "__main__":
    unittest.main()
