import csv
from datetime import datetime, timedelta
import random

# Define the date range
start_date = datetime(2023, 1, 1)  # Adjust the start date as needed
end_date = start_date + timedelta(days=29)  # 30 days of data

# Create CSV file with headers
csv_file_path = 'temperature_data.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Temperature']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write headers
    writer.writeheader()

    # Generate random temperature data for each day
    current_date = start_date
    while current_date <= end_date:
        # Generate random temperature (assuming a range of 0 to 35 degrees Celsius for demonstration)
        temperature = round(random.uniform(0, 35), 2)

        # Write date and temperature to CSV
        writer.writerow({'Date': current_date.strftime('%Y-%m-%d'), 'Temperature': temperature})

        # Move to the next day
        current_date += timedelta(days=1)

print(f"CSV data has been generated and saved to: {csv_file_path}")
