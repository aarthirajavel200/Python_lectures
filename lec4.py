#finding unique elements in a given string

s = input()  # Take input string
char_count = {}
sum=0
unique_chars = set()# Dictionary to store counts
  # Set to store unique characters
 #Print unique characters (those that appear only once)
for char  in s:
    if char not in unique_chars:
         sum = sum+1
         unique_chars.add(char)
print(sum)
  
#finding even numbers for a given range:
for i in range(5):
    if i%2==0:
        print(i)
for i in range(10):
    if i%2==0:
        print(i)
for i in range(2,9,3):
    if i%2==0:
        print(i)
for i in range(-4,6,2):
    if i%2==0:
        print(i)
for i in range(5,6):
    if i%2==0:
        print(i)
#finding secret number
secret =7
for i in range(1,11):
    if i == secret:
        print("yes,it's",i)
secret =7
found = False
for i in range(1,11):
    if i == secret:
        print("yes,it's",i)
        found = True
    if not found:
        print("not found")
        
