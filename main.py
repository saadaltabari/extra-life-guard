
if __name__ == '__main__':

	lifeguard_shifts = []
	with open("files/1.in") as f:
		lifeguard_count = int(f.readline())
		for lifeguard in range(0, lifeguard_count):
			start, end = f.readline().split(" ")
			lifeguard_shifts.append((int(start), int(end)))

	sorted_lifeguard_shifts = sorted(lifeguard_shifts, key=lambda shift: shift[0])
	lifeguard_significances = []
	overall_coverage = 0

	pre_start, pre_end = sorted_lifeguard_shifts.pop(0)
	significance = pre_end - pre_start
	while sorted_lifeguard_shifts:
		start, end = sorted_lifeguard_shifts.pop(0)
		if end < pre_end:
			print(0)
			exit()
		if start < pre_end:
			significance = significance - (pre_end - max(start, pre_start))
			start = pre_end

		overall_coverage += significance
		lifeguard_significances.append(significance)
		significance = end - start
		pre_start = start
		pre_end = end

	lifeguard_significances.append(significance)
	overall_coverage += significance

	lifeguard_significances.sort()
	least_significant = lifeguard_significances.pop(0)
