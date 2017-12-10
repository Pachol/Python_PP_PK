import random

numbers = []
for i in range(50):
     numbers.append(random.randint(0,1000))

def BubbleSort(data):
     for i in range(len(data)-1, 0, -1):
         for j in range(i):
             if data[j] > data[j+1]:
                 data[j], data[j+1] = data[j+1], data[j]

BubbleSort(numbers)


temp = numbers
sorted(temp)
if temp == numbers:
     print "Succes"