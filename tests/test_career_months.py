"""Check month-union calculation without treating it as career eligibility."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path(os.environ.get("TEAM_LEAD_SKILL_DIR", ROOT / "skills/team-lead-resume"))
SCRIPT = SKILL / "scripts/career_months.py"


class CareerMonthsTest(unittest.TestCase):
    def run_case(self, periods, as_of="2026-10"):
        self.assertTrue(SCRIPT.is_file(), "career_months.py is not implemented")
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "periods.json"
            source.write_text(json.dumps(periods), encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(source), "--as-of", as_of],
                                  capture_output=True, text=True, check=False)

    def success(self, periods, as_of="2026-10"):
        result = self.run_case(periods, as_of)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_overlap_and_excluded_research(self):
        result = self.success([
            {"label": "A", "start": "2017-01", "end": "2022-06", "include": True},
            {"label": "B", "start": "2021-09", "end": "2026-10", "include": True},
            {"label": "Research", "start": "2015-03", "end": "2016-12", "include": False,
             "reason": "Relevance and employment basis unconfirmed"},
        ])
        self.assertEqual(result["months"], 118)
        self.assertEqual((result["years"], result["remaining_months"]), (9, 10))
        self.assertEqual(result["raw_included_months"], 128)
        self.assertEqual(result["overlap_months"], 10)
        self.assertEqual(len(result["excluded"]), 1)

    def test_disjoint_periods_and_gap(self):
        result = self.success([
            {"start": "2020-01", "end": "2020-02", "include": True},
            {"start": "2020-04", "end": "2020-04", "include": True},
        ])
        self.assertEqual(result["months"], 3)
        self.assertEqual(result["overlap_months"], 0)
        self.assertEqual(len(result["unique_ranges"]), 2)

    def test_current_ends_at_explicit_as_of(self):
        result = self.success([{"start": "2026-08", "end": None, "include": True}])
        self.assertEqual(result["months"], 3)
        self.assertEqual(result["as_of"], "2026-10")

    def test_duplicate_interval_counts_once(self):
        row = {"start": "2020-01", "end": "2020-12", "include": True}
        result = self.success([row, row])
        self.assertEqual(result["months"], 12)
        self.assertEqual(result["overlap_months"], 12)

    def test_empty_records(self):
        self.assertEqual(self.success([])["months"], 0)

    def test_inclusion_must_be_explicit_boolean(self):
        for flag in (None, "true", 1):
            result = self.run_case([{"start": "2020-01", "end": "2020-12", "include": flag}])
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("Traceback", result.stderr)

    def test_bad_dates_and_future_end(self):
        for start, end in (("2020-13", "2021-01"), ("2021-02", "2020-01"),
                           ("2020-01", "2027-01"), ("2020-1", "2021-01")):
            result = self.run_case([{"start": start, "end": end, "include": True}])
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("Traceback", result.stderr)

    def test_excluded_record_needs_reason(self):
        result = self.run_case([{"start": "2020-01", "end": "2020-12", "include": False}])
        self.assertEqual(result.returncode, 2)

    def test_missing_end_is_not_implicitly_current(self):
        result = self.run_case([{"start": "2020-01", "include": True}])
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
