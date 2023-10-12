counter = 0
while True:
    lineIn = input('place text here: ')
    if lineIn == 'end':
        break
    counter +=1
    print ('line',counter,'=',lineIn)
print ('you have exited the loop')

for i in range (10,16):
    if i == 13:
        continue
    print(i)