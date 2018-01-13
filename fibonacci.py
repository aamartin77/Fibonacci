sequence = [0, 1, 1]
for i in range(10):
     sequence.append(sequence[-2] + sequence[-1])
print(sequence)
