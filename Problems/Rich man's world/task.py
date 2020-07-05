k = int(input())
interestRate = 1.071
i = k
govProtection = 700000
numberOfYears = 0
while i < govProtection:
	i *= interestRate
	numberOfYears += 1
print(numberOfYears)
