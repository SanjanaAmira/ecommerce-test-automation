
import csv
from pathlib import Path

csv_file = Path("test_cases.csv")

if not csv_file.exists():
    print("ERROR: test_cases.csv was not found.")
    raise SystemExit(1)

required_columns = [
    "Test Case ID",
    "Title",
    "Preconditions",
    "Test Steps",
    "Test Data",
    "Expected Result",
    "Actual Result",
    "Status",
    "Notes",
]

# Optional columns that are allowed but not required
optional_columns = ["Automated?"]

with csv_file.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    
    # Check if all required columns are present
    if reader.fieldnames:
        missing_cols = set(required_columns) - set(reader.fieldnames)
        extra_cols = set(reader.fieldnames) - set(required_columns) - set(optional_columns)
        
        if missing_cols:
            print(f"ERROR: Missing required columns: {missing_cols}")
            raise SystemExit(1)
        
        if extra_cols:
            print(f"WARNING: Unexpected columns (will be ignored): {extra_cols}")
    else:
        print("ERROR: CSV headers do not match the expected columns.")
        print("Found:", reader.fieldnames)
        raise SystemExit(1)

    rows = list(reader)

if not rows:
    print("ERROR: No test cases found.")
    raise SystemExit(1)

seen_ids = set()
errors_found = False

for row_number, row in enumerate(rows, start=2):
    test_id = row["Test Case ID"].strip()
    errors = []

    if not test_id:
        errors.append("Missing test case ID")
    elif test_id in seen_ids:
        errors.append("Duplicate test case ID")
    else:
        seen_ids.add(test_id)

    for column in required_columns[:6]:
        if not row[column].strip():
            errors.append(f"Missing value in '{column}'")

    if row["Status"].strip() not in ("Pass", "Fail", "Not Run"):
        errors.append("Status must be Pass, Fail, or Not Run")

    if errors:
        errors_found = True
        print(f"Row {row_number} ({test_id or 'Unknown ID'}): ERROR - "
              + "; ".join(errors))
    else:
        print(f"{test_id}: OK")

if errors_found:
    print("\nCSV check failed. Fix the errors above.")
    raise SystemExit(1)

print(f"\nCSV check passed! {len(rows)} test cases checked.")
