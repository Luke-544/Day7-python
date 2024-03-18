#nested loops-the inner loop will finish all of its iterations
#              before finishing one iteration of the outer loop

#rows = int(input("Enter the number of rows: "))
#columns = int(input("Enter the number of columns: "))
#symbol = input("Enter the symbol to use: ")

#for i in range(rows):
 #   for j in range(columns):
  #      print(symbol, end="")
   # print()

#loop control statements in python
#they change the loop execution from its normal sequence
#they include: 
#break - used to terminate the loop entirely
#continue - skips to the next iteration of the loop
#pass - does nothing, just acts like a placeholder

#lets begin with the break statement
#while True:
 #   name = input("Enter your name: ")
  #  if name != "":
   #     break

#next is the continue statement
    
#phone_number = "011-2482-493"
#for i in phone_number:
  #  if i == "-":
 #       continue
#    print(i, end="")

for i in range(1,21):
    if i == 10:
        pass
    else:
        print(i, end="")

    

