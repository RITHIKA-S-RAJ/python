#file =open("numbers.txt",'r')
#contents = file.read()
#contents = contents.split(',')
#for element in contents:
 #   if element % 2 == 0:
#print(element)
#file.close()


with open("numbers.txt") as numbers:
    contents = numbers.read()
    contents = contents.split(",")
    print(contents)

for element in contents:
    if int(element) % 2 == 0:
        with open("evens.txt", "a") as file2:
            file2.write(element)
            file2.write("\n")

# for num in file_write:
#     if int(num) % 2 == 0:
#         file_write.write(num)
#         file_write.write("\n")
#         print(num)
        


#for element in contents:
 #   if int(element.strip())%2 == 0:
  #      print(element.strip())











