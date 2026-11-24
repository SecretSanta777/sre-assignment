import json
import sys


def fill_values(tests, results_by_id):
    for test in tests:
        test_id = test["id"]

        if "value" in test and test_id in results_by_id:
            test["value"] = results_by_id[test_id]

        fill_values(test.get("values", []), results_by_id)


values_path, tests_path, report_path = sys.argv[1:]

with open(values_path, encoding="utf-8-sig") as values_file:
    results = json.load(values_file)

with open(tests_path, encoding="utf-8-sig") as tests_file:
    report = json.load(tests_file)

results_by_id = {}
for item in results["values"]:
    results_by_id[item["id"]] = item["value"]

fill_values(report["tests"], results_by_id)

with open(report_path, "w", encoding="utf-8") as report_file:
    json.dump(report, report_file, ensure_ascii=False, indent=2)
