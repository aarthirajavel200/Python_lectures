#floating point approxmiation 

x=0
for i in range(10):
    x+=0.1
print(x==1)
print(x,"==",10*0.1)
#always use close enough not ==
#some examples
#example1:
x=0
for i in range(10):
    x+=0.125
print(x== 1.25)
#different values for x
x = 24
ep =0.01
num_guess = 0
guess = 0.0
increment = 0.0001
while abs(guess**2 -x)>=ep :
    guess+=increment
    num_guess+=1
if (num_guess == 10,00):
  print("the square root is",guess)
  print(abs(guess**2 -x))
x=0.625
p=0
while((2**p)*x)%1!=0:
    print("Remainder=" +str((2**p)*x-int((2**p)*x)))
    p+=1
num = int(x*(2**p))
result = ''
if num==0:
    result ='0'
while num>0:
    result = str(num)+result
    num = num//2
for i in range(p-len(result)):
    result = '0'+result
result = result[0:-p] +  '-' + result[-p:]
print("the binary representation of the decimal" +str(x)+'is' +" " +str(result))
#Approxmiation methods:
x=36
ep = 0.01
num_guess = 0.0001
guess = 0.0
increment = 0.0001
while abs(guess**2 -x)>=ep:
    print("Failed on square root of ",x)
else:
    print(guess,"is close to square root of ",x)



