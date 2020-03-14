from numeric import gcd

def main():
    gcd_test = gcd(5,10)
    print("gcd using 5,10: ",gcd_test)
    assert gcd_test == 5,"gcd incorrect, returned {0}".format(gcd_test)

if __name__ == "__main__":
	main()


