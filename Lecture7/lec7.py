#to check even number or not
def even_number(num):
    if(num%2)==0:
        print("It is an even number")
    else:
        print("It is not an even number")
even_number(2)
even_number(3)
        
#optimized code
def even_number(num):
    return(num%2)==0
print(even_number(2))
print(even_number(3))
#to print sum of odd numbers within a range

def odd_num(a,b):
    sum=0
    for i in range(a,b+1):
       if (i%2==1):
               sum+=1
    print(sum)
           
odd_num(1,2)
odd_num(5,8)
#to find whether a string is palindrome or not
def pali_1(str):
  if (str[::-1]==str):
      return True
  else:
      return False

str1 = input("enter a palindrome")
sr = pali_1(str1)
print(sr)
