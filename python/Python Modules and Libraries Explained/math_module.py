import math

radius = 8  # given radius
circumference = 2 * math.pi * radius  # formula for circumference
print(f"The circumference of the pizza is: {circumference:.2f} inches")

from datetime import datetime, timedelta

# Office start time
office_time = datetime.strptime("09:30 AM", "%I:%M %p")

# Travel time
travel_time = timedelta(minutes=45)

# Calculate departure time
departure_time = office_time - travel_time

# Print result
print("Maya should leave home at:", departure_time.strftime("%I:%M %p"))