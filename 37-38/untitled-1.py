def count_inversions(sequence):
    inversions = 0
    n = len(sequence)
    for i in range(n):
        for j in range(i + 1, n):
            if sequence[i] > sequence[j]:
                inversions += 1
    return inversions


sequence = [1, 2, 5, 3, 4, 7, 6]
print(count_inversions(sequence))