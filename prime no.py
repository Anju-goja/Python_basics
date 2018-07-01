'''
n= int (input("enter any number"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
if flag==0:
    print ("Prime")
else:
    print("not prime")

n= int (input("enter any number"))
count=0
for i in range(1,n):
    if (n%i==0):
        count=count+1
        print(n,"was divided by ", i ,"and now the count is",count)
if count==1:
    print("prime")
else:
    print("not prime")

'''


#Wap which accepts a number from the user and prints the list of prime numbers upo that number
'''
for i in range(2, 10):
    isPrime = True
    
    for num in range(2, i):
        if i % num == 0:
            isPrime = False

    if isPrime:
        print(i)

'''








#example :   if a user enters 10 : --->>>>>>output should be >>>>>2,3,5,7



'''WAP which prints the following output:
*                   *
**                 * *              
***               * * *
****
'''
'''
n = int(input('Enter number of lines '))

for i in range(1, n + 1):
    print((n - i) * ' ' + i * '* ')
'''
n= int (input("enter the lines"))
for i in range(1,n+1):
  print((n-i)*'' +i*"*")