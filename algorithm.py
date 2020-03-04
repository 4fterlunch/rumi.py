# Algorithm library
# Rux and Michael
# March 2020 -

def gcd(a, b):
    if b is 0:
        return a
    else:
        return gcd(b, a%b)
