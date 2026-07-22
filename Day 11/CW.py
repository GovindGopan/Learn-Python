from tripdata import get_trip
from datetime import datetime
import json

trip1 = get_trip("Paris", "15-05-2023", "Amazing food")
trip2 = get_trip("Tokyo", "20-08-2024", "Loved the culture")
trips = [trip1, trip2]

for trip in trips:
    date_obj = datetime.strptime(trip["date"],"%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

jason_data = json.dumps(trips)

print(jason_data)
