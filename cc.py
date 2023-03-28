map = {}
numbers = [1,6,2,5,9,10,12,45,13,8]
target = 7
solutions = []
for i in range(len(numbers)):
    if target-numbers[i] in map:
        solutions.append((map[target - numbers[i]],i))
    else:
        map[numbers[i]] = i
        print(solutions)    