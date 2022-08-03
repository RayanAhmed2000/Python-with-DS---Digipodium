data= ""  #empty string
while True:
    line=input("Line =")
    if not line:
        break
    data +=line+" "

print("you have entered the following data")
print(data)