ch=input("entere the operation that you need to perform.choose's' for sum,'d' for difference,'e' to exit")
if ch!='e':
         num1=int(input("enter the 1st number:"))
         num2=int(input("enter the 2nd number:"))


         if ch=='s':
             print("sum of the numbers:",num1+num2)
         if ch=='d':
             print("diff of numbers:",num1-num2)

else:
    print("exiting")
