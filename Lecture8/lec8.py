#und#erstanding return statement
def  even_number(i):
    i%2 ==0
even_number(2)
even_number(4)
even_number(3)
#try
def add(x,y):
      return x+y
def mult(x,y):
      return x*y
print(add(2,3))
print(mult(3,4))
print(mult(4,5))
#try it:2
def triangular(n):
     total = 0
     for i in range(1,n+1):
         total = total+i
         if total == n:
           return True
     return False
#a n#the number is said to be triangular when the set of numbers within its range  equals to the given number
print(triangular(1))
print(triangular(2))

#try 
import math

def bisection_sqrt(n, epsilon=0.1):
    """Approximate square root of n using the bisection method."""
    if n == 0 or n == 1:  # Edge cases
        return n

    low = 0
    high = n
    guess = (high + low) / 2.0  

    while abs(guess ** 2 - n) >= epsilon:  # Keep refining guess
        if guess ** 2 < n:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0  

    return guess  # Approximate sqrt of n

def count_nums_with_sqrt_close_to(n, epsilon):
    """Count how many integers up to n have sqrt values close to an integer."""
    count = 0

    for i in range(1, n + 1):
        approx_sqrt = bisection_sqrt(i, epsilon)  # Get bisection root
        nearest_integer = round(approx_sqrt)  # Find closest integer

        if abs(approx_sqrt - nearest_integer) <= epsilon:
            count += 1

    return count

# Get user input
n = int(input("Enter a value: "))
result = count_nums_with_sqrt_close_to(n, 0.1)
print("Count of numbers whose sqrt is close to an integer:", result)
#finding count of odd numbers between numbers 
def sum_odd(a,b):
  sum = 0
  for i in range(a,b+1):
    if i%2 == 1:
      print("it is odd")
      sum+=1
  return sum
low = 2
high = 7
sum1 = sum_odd(low,high)
print(sum1)
#defining formal parameter and actual parameter 
#formal parameter is function scope and actual parameter global scoped 
def f(x):
  x = x+1
  print(x)
  return x 
y = f(3)
#understanding functions scope 
def f(y):
  x = 1
  x+=1
  print(x)
x = 5
f(x)
print(x)
#here no assignment in function scope 
def f(y):
  print(x)
  print(x+1)
x = 5
f(x)
print(x)
#accessing before assignment 
def f(y):
  x+=1
x=5
#h(x)
#print(x)#error because you are trying to modify the value of the main scope 
#function as parameter 
def calc(op,x,y):
  return op(x,y)
def add(a,b):
  return a+b
def div(a,b):
  if (b!=0):
    print(b/a)
calc(add,2,3)
#try it 
def calc(op,x,y):
  return op(x,y)
def div(a,b):
  if b!=0:
    return a/b
  print("denom was 0.")
res = calc(div,2,0)
    
def func_a():
  print("inside func_a")
  
def func_b(y):
  print("inside func_b")
  return y
def fun_c(f,z):
  print("inside  func_c")
  return(f(z))
print(func_a())
print(5+func_b(2))
print(fun_c(func_b,3))
#iteration try it 
# 
def apply(criteria, n):

    return sum(1 for i in range(n + 1) if criteria(i))

# Example usage:
print(apply(lambda x: x % 2 == 0, 10))  # Counts even numbers from 0 to 10

