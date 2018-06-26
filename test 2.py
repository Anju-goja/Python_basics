#WAP INPUT FORM THE USER NAME , AGE , MARKS

username=input('enter your name')
print(len(username))

if (len(username)==0):
    print ("name is invalid or empty")
else:
    print ("found")
    print(username)
    age=input('enter your age')
    print(age)
    marks=input('enter ur marks')
    print (marks)


#CHECK AGE 18 ABOVE ELIGIBLE ELSE NOT ELIGIBLE

    n=int(input("enter your age"))
    if (n>=18):
        print('eligible')
    else:
        print("not eligible")

#CHECK KI AGAR MARKS 40 ABOVE THEN PASS ELSE FAIL

    n=int(input("marks"))
    if(n>40):
        print ("pass")
    else:
        print("fail")


#Additional name should not be empty
