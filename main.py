
if __name__ == '__main__':

	lifeguard_shifts = []
	with open("files/input/1.in") as f:
		lifeguard_count = int(f.readline())
		for lifeguard in range(0, lifeguard_count):
			start, end = f.readline().split(" ")
			lifeguard_shifts.append((int(start), int(end)))

	sorted_lifeguard_shifts = sorted(lifeguard_shifts, key=lambda shift: shift[0])
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

	file1 = open('files/output/1.out', 'w')
	file1.write(f"{overall_coverage - least_significant}")
	file1.close()
	print("execution completed")
