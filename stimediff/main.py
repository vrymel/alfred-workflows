import sys

query = sys.argv[1]
segments = query.split(" ")
start_time = segments[0]
end_time = segments[1]

sys.stdout.write("{} - {}".format(start_time, end_time))
