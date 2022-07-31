#input and traversal odf string in python

x="digipodium"

print("x=",x)

print(x[0],x[1],x[2],x[3],x[4],x[5])  #front traversal

print(x[-1],x[-2],x[-3],x[-4],x[-5],x[-6])  #reverse traversal

print(x[-15]) #trying to access index that is not present will result in IndexError: string index out of range

