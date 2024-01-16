# Modular Exponentiation

base = int(input("Base: "))
expo = int(input("Exponent: "))
mod = int(input("Mod: "))

# Function to find modular exponent
def find_mod_expo(base, exponent, mod):
    ans = 1

    while (exponent>0):
        # If exponent is odd, multiply base with the ans
        if exponent%2 != 0:
            ans = (ans*base)%mod

        # exponent is even.
        base = (base*base)%mod
        exponent = int(exponent)/2

    return ans

print("Modular Exponent: "+str(find_mod_expo(base, expo, mod)))