function longest_palindromic_subsequence(string):
    N = length(string)
    L = 2D array of size N x N, filled with 0s
    
    for i = 0 to N-1:
        L[i][i] = 1

    for i = 2 to N:
        for j = 0 to N-i:
            k = j + i - 1

            if seq[j] == seq[k] and i == 2:
                L[j][k] = 2
            else if seq[j] == seq[k]:
                L[j][k] = L[j + 1][k - 1] + 2
            else:
                L[j][k] = max(L[j + 1][k], L[j][k - 1])

    subsequence = empty array
    i = 0
    j = N - 1
    while i < N and j >= 0:
        if seq[i] == seq[j]:
            append seq[i] to subsequence
            i = i + 1
            j = j - 1
        else if j > 0 and L[i][j - 1] >= L[i + 1][j]:
            j = j - 1
        else:
            i = i + 1

    return concatenate elements of subsequence into a string
