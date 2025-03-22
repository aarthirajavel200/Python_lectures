#concatenating
b=":"
c=")"
s1=b+2*c
print(s1)
f="a"
g=" b"
h="3"
s2=(f+g)*int(h)
print(s2)
#slicing
s="ABC d3f ghi"
print(s[3:len(s)-1])
print(s[4:0:1])
print(s[6:3])
#understanding input()
str1 ="I can _ better than you !"
str = input("Enter a verb")
str2 = str1.replace("_",str)
print(str2)
print(5*str)
#conditional statements
secret_num = 8924
guess_number = int(input("Guess the number"))
if(guess_number==secret_num):
     print(True)
else:
     print(False)
#fixing bugs in the code
x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))
if (x==y):
    print(x,"is the same as " ,y)
    print("These are equal!")
y=2
y=20
y=11
print(y)
answer=''
x=11
if (x==y):
    answer = answer + 'M'
elif (x>=y):
    answer =  answer + 'i'
else:
    answer = answer + 'T'
print(answer)
#debugging
secret_num = 8924
guess_number = int(input("Guess the number"))
if(guess_number==secret_num):
     print("same as the secret")
elif(guess_number>secret_num):
     print("too high")
else:
     print("too low")
     
     


     
     


