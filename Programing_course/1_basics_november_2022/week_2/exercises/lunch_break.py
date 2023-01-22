# from math import ceil
#
# #User Input
#
# series_name = input()
# episode_lenght = int(input())
# lunch_break = int(input())
#
#
# # logic
# lunch_time = lunch_break / 8
# rest_time = lunch_break / 4
#
# time_to_watch = lunch_break - lunch_time - rest_time
#
#
# # Output
# if time_to_watch >= episode_lenght:
#     print(f"You have enough time to watch {series_name} and left "
#           f"with {ceil(time_to_watch - episode_lenght)} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_lenght - time_to_watch)} "
#           f"more minutes.")

from math import ceil

serial_name = input()
length_episode = int(input())
rest_time_length = int(input())

lunch_time = rest_time_length / 8
rest_time_for_chilling = rest_time_length / 4

# po vreme na pochivkata
in_rest_time = rest_time_length - lunch_time - rest_time_for_chilling

all_time_total_needed_for_episode = length_episode - in_rest_time

if in_rest_time >= length_episode:
    print(f"You have enough time to watch {str(serial_name)} and left with {ceil(in_rest_time - length_episode)} "
          f"minutes free time.")
else:

    print(f"You don't have enough time to watch {str(serial_name)}, you need {ceil(length_episode - in_rest_time)}"
          f" more minutes.")
