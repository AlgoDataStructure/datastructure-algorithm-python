
# O(n) time | O(1) space
def getNthFib(n):
	defaultArray = [0,1]
	count = 3
	while count <= n:
		sumNo = defaultArray[0] + defaultArray[1]
		defaultArray[0] = defaultArray[1]
		defaultArray[1] = sumNo
		count = count + 1
	if n == 1:
		return defaultArray[0]
	else:
		return defaultArray[1]
