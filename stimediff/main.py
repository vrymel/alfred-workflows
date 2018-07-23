import sys
from datetime import datetime

query = sys.argv[1]
segments = query.split(" ")
start_time = segments[0]
end_time = segments[1]
format = '%H%M'

timedelta = datetime.strptime(end_time, format) - datetime.strptime(start_time, format)
hours_interval = timedelta.total_seconds() / 60 / 60

sys.stdout.write(str(hours_interval))
