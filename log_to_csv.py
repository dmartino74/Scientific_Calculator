import re
import csv

log_path = 'calculator.log'
csv_path = 'calculator_output.csv'

# Match lines like: 2025-10-11 22:20:10,841 - INFO - Result: -4.0
pattern = r'^(.*?) - (\w+) - (.*?): (.*)$'

with open(log_path, 'r') as log_file, open(csv_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Timestamp', 'Level', 'Type', 'Value'])

    for line in log_file:
        match = re.search(pattern, line)
        if match:
            timestamp, level, msg_type, value = match.groups()
            writer.writerow([timestamp, level, msg_type, value])

print(f"CSV saved to {csv_path}")
