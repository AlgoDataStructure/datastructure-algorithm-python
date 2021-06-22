
# O(n) time | O(1) space
def getNthFib(n):
	defaultArray = [0,1]

	if n == 1:
		return defaultArray[0]

	count = 3
	while count <= n:
		sum = defaultArray[0] + defaultArray[1]
		defaultArray[0] = defaultArray[1]
		defaultArray[1] = sum
		count = count + 1
	return defaultArray[1]