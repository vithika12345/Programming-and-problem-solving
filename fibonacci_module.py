def generate_fibonacci_sequence(count):
	if count<=0:
		return[]
	elif count == 1:
		return[0]
	elif count==2:
		return[0,1]
	sequence=generate_fibonacci_sequence(count-1)
	sequence.append(sequence[-1]+sequence[-2])
	return sequence
