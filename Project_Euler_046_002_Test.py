A = [True]*(5 * 10 ** 5)
Primes = []
for i in xrange(2, int((5 * 10 ** 5) ** 0.5)):
    if A[i] == True:
        Primes.append(i)
        for j in xrange(i * i, 5 * 10 ** 5, i):
            A[j] = False
for i in xrange(int((5 * 10 ** 5) ** 0.5), 5 * 10 ** 5):
    if A[i] == True:
        Primes.append(i)
Flag = True
N = 1
while Flag:
	N += 2
	if A[N]:
		continue
	j = 0
	while Primes[j] <= N:
		if ((float(N - Primes[j]) / 2) ** 0.5).is_integer():
			break
		j += 1
	else:
		print N
		Flag = False
Wait = raw_input()