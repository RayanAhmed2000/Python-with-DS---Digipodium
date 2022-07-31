#slicing a string in Python

s='digipodium'

slice1=s[4:7]      #slicing pod from digipodium
print(slice1)

slice2=s[:4]      #slicing digi from digipodium s[0:4] and s[:4] are the same 
print(slice2)

slice3=s[4:]      #slicing podium from digipodium s[4:9] and s[4:] are the same
print(slice3)

slicex=s[:-4]      #slicing pod from digipodium
print(slicex)