try:
    a = int(input("Enter the integer you want to go to: "))
    for i in range(1, a+1):
        print(i)
except:
    print("Please enter a integer not a float")
