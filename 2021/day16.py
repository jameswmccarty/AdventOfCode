#!/usr/bin/python


if __name__ == "__main__":

	x_form = {	'0':'0',
				'1':'8',
				'2':'4',
				'3':'C',
				'4':'2',
				'5':'A',
				'6':'6',
				'7':'E',
				'8':'1',
				'9':'9',
				'A':'5',
				'B':'D',
				'C':'3',
				'D':'B',
				'E':'7',
				'F':'F'}

	version_count = 0

	# abuse string conversion
	def read_n_bin(n,stream):
		if n == 0:
			return 0
		segment = int(n*'1',2) & stream
		out = ''
		for _ in range(n):
			if segment & 0x1:
				out += '1'
			else:
				out += '0'
			segment = segment >> 1
		return int(out,2)

	def read_n_str(n,stream):
		segment = int(n*'1',2) & stream
		out = ''
		for _ in range(n):
			if segment & 0x1:
				out += '1'
			else:
				out += '0'
			segment = segment >> 1
		return out

	def parse_packets(packet):
		global version_count
		bits_processed = 0
		V = read_n_bin(3,packet)
		version_count += V
		packet = packet >> 3
		bits_processed += 3
		T = read_n_bin(3,packet)
		packet = packet >> 3
		bits_processed += 3
		if T == 4: # found literal value
			end_found = False
			L = ''
			while not end_found:
				if read_n_bin(1,packet) != 1:
					end_found = True
				packet = packet >> 1
				bits_processed += 1
				L += read_n_str(4,packet)
				packet = packet >> 4
				bits_processed += 4
			return bits_processed
		else: # found an operator
			length_type_id = read_n_bin(1,packet)
			packet = packet >> 1
			bits_processed += 1
			if length_type_id == 0:
				length = read_n_bin(15,packet)
				packet = packet >> 15
				bits_processed += 15
				segment = read_n_str(length,packet)
				packet = packet >> length
				bits_processed += length
				segment = segment[::-1]
				segment = int(segment,2)
				sub_seg_total = 0
				while sub_seg_total < length:
					round_total = parse_packets(segment)
					sub_seg_total += round_total
					segment = segment >> round_total
			elif length_type_id == 1:
				num_packets = read_n_bin(11,packet)
				packet = packet >> 11
				bits_processed += 11
				for i in range(num_packets):
					processed = parse_packets(packet)
					packet = packet >> processed
					bits_processed += processed
		return bits_processed

	def compute_packets(packet):
		bits_processed = 0
		V = read_n_bin(3,packet)
		packet = packet >> 3
		bits_processed += 3
		T = read_n_bin(3,packet)
		packet = packet >> 3
		bits_processed += 3
		if T == 4: # found literal value
			end_found = False
			L = ''
			while not end_found:
				if read_n_bin(1,packet) != 1:
					end_found = True
				packet = packet >> 1
				bits_processed += 1
				L += read_n_str(4,packet)
				packet = packet >> 4
				bits_processed += 4
			return (bits_processed,int(L,2))
		else: # found an operator
			length_type_id = read_n_bin(1,packet)
			packet = packet >> 1
			bits_processed += 1
			sub_values = []
			if length_type_id == 0:
				length = read_n_bin(15,packet)
				packet = packet >> 15
				bits_processed += 15
				segment = read_n_str(length,packet)
				packet = packet >> length
				bits_processed += length
				segment = segment[::-1]
				segment = int(segment,2)
				sub_seg_total = 0
				while sub_seg_total < length:
					round_total, sub_val = compute_packets(segment)
					sub_seg_total += round_total
					segment = segment >> round_total
					sub_values.append(sub_val)
			elif length_type_id == 1:
				num_packets = read_n_bin(11,packet)
				packet = packet >> 11
				bits_processed += 11
				for i in range(num_packets):
					processed, sub_val = compute_packets(packet)
					packet = packet >> processed
					bits_processed += processed
					sub_values.append(sub_val)
			if T == 0:
				return (bits_processed, sum(sub_values))
			if T == 1:
				total = 1
				for val in sub_values:
					total *= val
				return (bits_processed, total)
			if T == 2:
				return (bits_processed, min(sub_values))
			if T == 3:
				return (bits_processed, max(sub_values))
			if T == 5:
				return (bits_processed, 1 if sub_values[0] > sub_values[1] else 0)
			if T == 6:
				return (bits_processed, 1 if sub_values[0] < sub_values[1] else 0)
			if T == 7:
				return (bits_processed, 1 if sub_values[0] == sub_values[1] else 0)


	# Part 1 Solution
	packet = "04005AC33890"
	with open("day16_input","r") as infile:
		packet = infile.read().strip()
	initial_len = len(packet)
	packet = packet[::-1]
	packet = ''.join([ x_form[x] for x in packet ])
	stream = int(packet,16) & int('F'*initial_len,16)

	parse_packets(stream)
	print(version_count)

	# Part 2 Solution
	print(compute_packets(stream)[1])


