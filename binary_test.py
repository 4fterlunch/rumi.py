from binary import binToDec, decToBin

def main():
	arr = [1,1,0,1,0,0,0,1,1]
	l = len(arr)
	print("running binToDec on", arr)
	dec = binToDec(arr,l)
	print(dec)
	print("running decToBin on", dec)
	bin = decToBin(dec)
	print(bin)
	assert arr == bin

if __name__ == "__main__":
	main()
