# what happens when l type right always
where = input("Go left or right?")

while (where == "right"):
    where = input("Go left or right?")
    
print("You got out !")
#what happens when condition is always to be true

n= int(input("Enter an number that to be non negative"))

while(n>0):
    print("X")

#while(True):
   # print("noooooo")
#shows sad face when entered more than two times
   

where = input("Go left or right? ")

counter = 0

while where == "right":
    counter += 1  # Increment counter

    if counter == 2:
        print("ohnoo")

    where = input("Go left or right? ")  # Ask again

print("You got out!")
#for loop
for i in range(1,4,1):
    print(i)
for j in range(1,4,2):
    print(j*2)
for me in range(4,0,-1):
    print("$"*me)
#sum
mysum = 0
start = 3
end = 6
for i in range(start , end):
     mysum += i
print(mysum)


 
