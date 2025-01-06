#TASK 1
#8)if input is 1 (or) 10 (or) 2 (or) 8 (or) 3 output will be Favorite number
#if input is 7 (or) 4 (or) 6 (or) 5 (or) 9 output will be not  Favorite number


a=int(input("Enter the value: "))
if(a==1 or a==10 or a==2 or a==8 or a==3):
    print("It is favourite number")
elif(a==7 or a==4 or a==6 or a==5 or a==9):
    print("It is not a favourite number")
else:
    print("Invalid Input")