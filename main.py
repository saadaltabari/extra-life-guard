

def _read_lifeguard_schedule_file(file_name: str) -> list:
	"""
	Read the lifeguard schedule form an input file.

	:param file_name: str, the name of the file to read.
	:return: list(tuple), a list of tuples representing every
	lifeguard's start and end time, ordered by start date
	"""
	lifeguard_shifts = []
	with open(file_name) as f:
		lifeguard_count = int(f.readline())
		for lifeguard in range(0, lifeguard_count):
			shift_start, shift_end = f.readline().split(" ")
			lifeguard_shifts.append((int(shift_start), int(shift_end)))

	return sorted(lifeguard_shifts, key=lambda shift: shift[0])


def _compute_max_coverage(case_number: int) -> int:
	"""
	Calculate the maximum time that can be coverd by the lifeguards
	if one of the life guards had to be fired.

	:param case_number: int, the number of the input case to compute.
	:return: int, representing the maximum time that can be covered.
	"""
	sorted_lifeguard_shifts = \
		_read_lifeguard_schedule_file(file_name=f"files/input/{case_number}.in")
	lifeguard_significances = []

	pre_start, pre_end = sorted_lifeguard_shifts.pop(0)
	significance = pre_end - pre_start
	overall_coverage = significance
	while sorted_lifeguard_shifts:
		start, end = sorted_lifeguard_shifts.pop(0)
		if end < pre_end:
			lifeguard_significances.append(0)
			continue
		if start < pre_end:
			significance = significance - (pre_end - max(start, pre_start))
			start = pre_end

		lifeguard_significances.append(significance)
		significance = end - start
		overall_coverage += significance
		pre_start = start
		pre_end = end

	lifeguard_significances.append(significance)

	lifeguard_significances.sort()
	least_significant = lifeguard_significances.pop(0)
	return overall_coverage - least_significant


def _write_output_file(output: str, file_name: str):
	"""
	Writes a single line of output to a file.

	:param output: str, the output to write to the file
	:param file_name: str, the output file's name
	:return:
	"""
	file1 = open(file_name, 'w')
	file1.write(output)
	file1.close()


if __name__ == '__main__':

	for case in range(1, 11):
		print(f"Computing case ({case})")
		result = _compute_max_coverage(case)
		_write_output_file(output=f"{result}", file_name=f"files/output/{case}.out")
		print(f"Case ({case}) completed. See output file.")
