import datetime

# Overall time in hours, minutes, seconds
overall_time = datetime.timedelta(hours=9, minutes=18, seconds=18)

# Time duration of each part
part_duration = datetime.timedelta(hours=1, minutes=35, seconds=0)

# Calculate number of full parts
num_full_parts = overall_time // part_duration

# Calculate the remaining time after full parts
remaining_time = overall_time - num_full_parts * part_duration

# Initialize start time
start_time = datetime.datetime(1, 1, 1, 0, 0, 0)

# Iterate over each part
for i in range(num_full_parts):
    # Calculate end time
    end_time = start_time + part_duration

    # Adjust start time for Part 2 onwards
    if i > 0:
        start_time += datetime.timedelta(minutes=1)

    # Print or use the start and end times for each part
    print(f"Part {i + 1}:")
    print(f"Start time: {start_time.time()}")
    print(f"End time: {end_time.time()}")
    print()

    # Update start time for the next part
    start_time = end_time

# Print the last part with the remaining time
print(f"Part {num_full_parts + 1}:")
print(f"Start time: {start_time.time()}")
end_time = start_time + remaining_time
print(f"End time: {end_time.time()}")


