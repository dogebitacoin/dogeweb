#
# Complete the 'findCharacteristic' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER choice
#  2. STRING edges
# 

def findCharacteristic(choice, edges):
    edgess = edges.split(' ')
    if choice == 1:
        count = 0
        for i in range(0, len(edgess)):
            if edgess[i][0] == edgess[i][1]:
                count += 1
            elif edgess[i][::-1] in edgess:
                count += 0.5
        return round(count)
    if choice == 2:
        rez2 =0
        rez = 0
        index = 0
     
        edgess.sort()
        rezrez = 0
        print (edgess)
        
        for i in range(0,len(edgess)-1):
            if edgess[i][0] == edgess[i+1][0]:
                
                rez2 += 1
            else:
                if rez2 > rez:
                    rez = rez2
                   
                    
                    index = i - rez2
                rez2 = 0
            
        for i in range(index, rez+1):
            rezrez += int(edgess[i])
        return rezrez


    if choice == 3:
        count = 0
        
        for x in edgess:
            
            for y in edgess:
                if x[1] == y[0]:
                    count += 1
        return count

            



data = [
[2, "12 13 23 31 34 41"],
# The integer choice in this case is 2, which means the program is expected to find the maximum number of edges starting at any specific vertex. If there is a tie, choose the vertex that is first numerically. Return the sum of all edges that start at that vertex (number 2 of the problem) 
[1, "12 23 34 11 21 32 45 53 95 43 99 29 91"],
[3, "12 23 34 41 31 52 45 61 14 21 33 55 13 54 32 56 36"],
[1, "12 11 33 34 43 55 52 41 31 25 88 79 98 45 13 42 87 35 51 21 14 78"],
[2, "12 11 33 34 43 55 52 41 31 25 88 79 98 45 13 42 87 35 51 21 14 78"]
]

for choice, edges in data:
   print(findCharacteristic(choice, edges))

