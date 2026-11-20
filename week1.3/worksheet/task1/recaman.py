# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

sequence = [0] # starts at 0
k = 1

while len(sequence) < L:
    last = sequence[len(sequence)-1]
    n = last - k

    # check if its already in there
    found = False
    for item in sequence:
        if item == n:
            found = True

    if n > 0 and found == False:
        sequence.append(n)
    else:
        # add instead
        n = last + k
        sequence.append(n)

    k = k + 1

[print(item) for item in sequence]    