num=100
i=0
while i<num :
    if i==60:
        break                #break will end while loop when i==60
    print(i,end=' ')
    i+=5


num2=100
i=0
while i<num2 :
    if i==60:
        continue                #continue will skip while loop when i==60
    print(i,end=' ')            #this part will be skipped
    i+=5                        #this part will be skipped



