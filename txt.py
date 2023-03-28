numbers = [1,6,2,5,9,10,12,45,13,8]
target = 7
solutions = []
for idx in range(len(numbers)):
    num = numbers[idx]
   # print("Numbers ---",num)
    for idx2 in range(idx + 1,len(numbers)):
         num2 = numbers[idx2]
         if num + num2 == target:
             solutions.append((idx,idx2))
print(solutions)
for i in range(3):
    for j in range(3):
        print("I---",i,"J----",j)
    
    #print("\t\t",numbers[idx2])
    
    