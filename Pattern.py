'''print("Half piramid of star (*): ")
n=int(input("Enter the number of row : " ))
for i in range(n):
    for j in range(i+1):
        print("* ",end=" ")
    print()'''







'''rows = int(input("Please Enter the total Number of Rows"))
number = 1 #initialise by 1
print("Floyd's Triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print (number, end =' ')
        number = number + 1
    print()'''




n=5
for i in range(1,n+1):
    print(' ' * (n-i) + "*" * (2*i-1))

for i in range(n-1,0,-1):
    print(" "* (n-i)+"*"*(2*i-1))