num_list = []
for i in range(3):
    num = int(input("Enter a number :"))
    num_list.append(num)
even_list = []
for num in num_list:
    if num %2==0:
        even_list.append(num)
        print(even_list)