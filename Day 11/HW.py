from tracker import get_record
from datetime import datetime
import json

record1 = get_record(
    "Paris",
    "Amazing food",
    "15-05-2023"
)

record2 = get_record(
    "Tokyo",
    "Loved the culture",
    "20-08-2024"
)

record3 = get_record(
    "Rome",
    "Beautiful architecture",
    "10-03-2022"
)

records = [record1, record2, record3]

for record in records:
    date_obj = datetime.strptime(record["date"],"%d-%m-%Y")
    
record["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(records)

print(json_data)

records_back = json.loads(json_data)

print("\nTravel Records:")
for record in records_back:
    print(record)