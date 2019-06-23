"""
https://www.interviewcake.com/question/python3/merging-ranges?course=fc1&section=array-and-string-manipulation

In HiCal, a meeting is stored as a tuple of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]
"""

def is_overlapped(schedule1, schedule2):
	if schedule1[1] >= schedule2[0]:
		return True
	return False

def merge_schedules(schedule1, schedule2):
	first = schedule1[0]
	second = max(schedule1[1], schedule2[1])
	return (first, second)

def merge_range(schedules):
	ordered_schedules = sorted(schedules)
	merged_schedules = list()

	n = len(ordered_schedules)
	merged_schedules.append(ordered_schedules[0])
	for i in range(1, n):
		sch1 = merged_schedules[-1]
		sch2 = ordered_schedules[i]
		if is_overlapped(sch1, sch2):
			merged_schedule = merge_schedules(sch1, sch2)
			merged_schedules[-1] = merged_schedule
		else:
			merged_schedules.append(sch2)

	return merged_schedules

assert [(1, 4)] == merge_range([(1, 3), (2, 4)])
assert [(1, 3)] == merge_range([(1, 2), (2, 3)])
assert [(1, 5)] == merge_range([(1, 5), (2, 3)])
assert [(0, 1), (3, 8), (9, 12)] == merge_range([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
