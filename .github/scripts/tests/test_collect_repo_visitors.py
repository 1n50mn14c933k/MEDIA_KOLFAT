"""Regression tests for GitHub's native rolling 14-day Traffic API metrics."""
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from collect_repo_visitors import (
    API_URL, build_snapshot, rolling_14_day_window, traffic_metrics,
    render_badge, format_period, readme_with_fresh_badge_urls,
)


class RepositoryVisitorTests(unittest.TestCase):
    def test_rolling_14_day_window_inclusive(self):
        start, end = rolling_14_day_window(datetime(2026, 11, 10, 19, tzinfo=timezone.utc))
        self.assertEqual((str(start), str(end)), ("2026-10-28", "2026-11-10"))
        self.assertEqual((end - start).days, 13)

    def test_utc_midnight_boundary(self):
        now = datetime(2026, 11, 10, 0, 15, tzinfo=timezone(timedelta(hours=1)))
        start, end = rolling_14_day_window(now)
        self.assertEqual((str(start), str(end)), ("2026-10-27", "2026-11-09"))

    def test_naive_datetime_rejected(self):
        with self.assertRaises(ValueError):
            rolling_14_day_window(datetime(2026, 11, 10))

    def test_native_14_day_totals_are_not_summed(self):
        now = datetime(2026, 11, 10, 19, tzinfo=timezone.utc)
        payload = {
            "count": 123, "uniques": 8,
            "views": [
                {"timestamp":"2026-11-09T00:00:00Z", "count":100,"uniques":7},
                {"timestamp":"2026-11-10T00:00:00Z", "count":23,"uniques":7},
            ]
        }
        snapshot = build_snapshot(now, payload)
        self.assertEqual(snapshot["schema_version"], 3)
        self.assertEqual(snapshot["rolling_14_days"]["views"], 123)
        self.assertEqual(snapshot["rolling_14_days"]["unique_visitors"], 8)
        self.assertEqual(snapshot["rolling_14_days"]["start_date"], "2026-10-28")
        self.assertEqual(snapshot["rolling_14_days"]["end_date"], "2026-11-10")
        self.assertNotIn("weekly", snapshot)
        self.assertIn("per=day", API_URL)

    def test_no_daily_records_with_native_zero_is_valid(self):
        self.assertEqual(traffic_metrics({"count":0,"uniques":0,"views":[]}),
                         {"unique_visitors":0, "views":0})

    def test_missing_top_level_totals_rejected(self):
        for payload in [{"views":[]}, {"count":2,"views":[]},
                        {"uniques":1,"views":[]}, {"count":3,"uniques":1},
                        {"views":"wrong","count":3,"uniques":1}, None]:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                traffic_metrics(payload)

    def test_bad_counters_are_rejected(self):
        for count, uniques in [(2,4),(-1,0),("3",1),(2,True),(2,-1),
                               (None,0),(0,1),(2,3.0)]:
            with self.subTest(count=count,uniques=uniques), self.assertRaises(ValueError):
                traffic_metrics({"views":[],"count":count,"uniques":uniques})

    def test_year_boundary_period(self):
        self.assertEqual(format_period("2026-12-25","2027-01-07"),
                         "25 Dec 2026 – 7 Jan 2027 · UTC")

    def test_period_must_have_14_inclusive_days(self):
        with self.assertRaises(ValueError):
            format_period("2026-11-01","2026-11-10")

    def test_missing_badge_metric_is_dash_not_zero(self):
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/"test.svg"
            render_badge("Unique GitHub repository visitors",None,"2026-10-28","2026-11-10",target)
            svg=target.read_text(encoding="utf-8")
            self.assertIn(">—</text>",svg)
            self.assertIn("28 Oct – 10 Nov 2026 · UTC",svg)
            self.assertIn("last 14 days",svg)

    def test_both_14_day_badges_preserve_style_and_figures(self):
        with tempfile.TemporaryDirectory() as folder:
            for label, metric in [
                ("Unique GitHub repository visitors",8),
                ("GitHub repository page views",123),
            ]:
                path=Path(folder)/"traffic.svg"
                render_badge(label,metric,"2026-10-28","2026-11-10",path)
                svg=path.read_text(encoding="utf-8")
                self.assertIn(label,svg)
                self.assertIn(f">{metric}</text>",svg)
                self.assertIn('width="370" height="48"',svg)
                self.assertIn("28 Oct – 10 Nov 2026 · UTC",svg)


    def test_cache_version_changes_both_urls_without_changing_click_targets(self):
        source = """<a href="https://github.com/owner/repo/graphs/traffic"><img src="assets/repository-visitors-weekly.svg"></a>
<a href="https://github.com/owner/repo/graphs/traffic"><img src="assets/repository-pageviews-weekly.svg"></a>"""
        updated = readme_with_fresh_badge_urls(source, "2026-11-10T19:59:55Z")
        self.assertIn('src="assets/repository-visitors-weekly.svg?v=20261110T195955Z"', updated)
        self.assertIn('src="assets/repository-pageviews-weekly.svg?v=20261110T195955Z"', updated)
        self.assertEqual(updated.count('href="https://github.com/owner/repo/graphs/traffic"'), 2)
        newer = readme_with_fresh_badge_urls(updated, "2026-11-11T10:17:00Z")
        self.assertIn("weekly.svg?v=20261111T101700Z", newer)
        self.assertNotIn("20261110T195955Z", newer)
        self.assertEqual(readme_with_fresh_badge_urls(newer, "2026-11-11T10:17:00Z"), newer)

    def test_cache_version_rejects_missing_or_duplicate_references(self):
        with self.assertRaises(ValueError):
            readme_with_fresh_badge_urls('<img src="assets/repository-visitors-weekly.svg">', "2026-11-10T19:59:55Z")
        with self.assertRaises(ValueError):
            readme_with_fresh_badge_urls(
                '<img src="assets/repository-visitors-weekly.svg">' * 2
                + '<img src="assets/repository-pageviews-weekly.svg">',
                "2026-11-10T19:59:55Z"
            )

    def test_invalid_cache_timestamp_rejected(self):
        with self.assertRaises(ValueError):
            readme_with_fresh_badge_urls(
                '<img src="assets/repository-visitors-weekly.svg">'
                + '<img src="assets/repository-pageviews-weekly.svg">',
                "wrong"
            )


if __name__ == "__main__":
    unittest.main()
