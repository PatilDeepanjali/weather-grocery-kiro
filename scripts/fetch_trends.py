import json
import csv

input_file = "dashboard/grocery_trends.csv"
output_file = "dashboard/trends.json"

records = []

# Read CSV and convert to JSON-friendly structure
with open(input_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert numeric fields from string to int
        record = {
            "date": row["date"],
            "metrics": {
                "noodles": int(row["noodles"]),
                "soup": int(row["soup"]),
                "cold_drink": int(row["cold_drink"]),
                "ice_cream": int(row["ice_cream"]),
                "tea": int(row["tea"])
            }
        }
        records.append(record)

# Save as JSON
with open(output_file, "w") as f:
    json.dump(records, f)

print("trends saved (from CSV dataset)")
