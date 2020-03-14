from math import floor
# function binToDec(A, n)
#	r <- 0
#	l <- n
#	while l > 0 do
#		r <- r + A[n - l] << l - 1
#		l <- l - 1
#	return r
#
def binToDec(binaryArray, n):
	result = 0
	l = n
	while l > 0:
		result += binaryArray[n-l] << l-1
		l -= 1
	return result

# function decToBin(d)
#	n <- 0	
#	while d != 0 do
#		X[n] <- d % 2
#		d <- floor(d/2)
#		n <- n + 1
#	return (Xn1,Xn2,...,Xn-1)
#
def decToBin(d):
	r = []
	n = 0
	while d != 0:
		r.append(d % 2)
		d  = floor(d/2)
		n += 1
	return reverseBin(r,n)

# function reverseBin(a, n)
#	l <- n
#	while n - l < l do
#		x <- a[n - l]
#		a[n - l] <- a[l - 1]
#		a[l - 1] <- x
#		l <- l - 1
#	return a
def reverseBin(a, n):
	l = n
	while n-l < l:
		x = a[n-l]
		a[n-l] = a[l-1]
		a[l-1] = x
		l -= 1
	return a