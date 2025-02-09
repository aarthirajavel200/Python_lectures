
#fINDING SQUARE ROOT THAT IS APPROXMIATE

x = 54321 
ep  = 0.01
num_guesses = 0
guess = 0.0 
increment = 0.0001
while (abs(guess ** 2-x))>= ep and guess**2<=x:
    guess += increment
    num_guesses+=1
print(f'{num_guesses} is the total no of guesses ')
if(abs(guess ** 2)-x)>= ep:
    print("the square root  of " f'{x} is' ,guess)
else:
    print("Failed to fetch the square root")
    
#try it 1.
    #you are guessing a 4 digit pin code.The only feedback the phone tells you is whether your guess is correct or not .Can you use bisection search to quickly and correctly guess the code .

#answer 
#we can't use bisection search here because it clearly tells that the feedback will be only like either the guess is correct or wrong but bisection is actually tend to provide whether the particular guees is too high or low so here brute force is suitable .

#so here 10000 possible pins between (0000 to 9999)
#worst case scenario is 10,000 attempts 
#average case is 5000 attempts 

#try it 2: you are playing an extreme guessing game to guess a numberexactly.A friend has a decimal number between 0 and 10 .The feedback to say is whether it is too high or too low.Can you use bisection search here
   #ANSWER 
   # Yes here we can use the bisection search as it clearly states that the feedback provided will be like too low or too high so based on that we can find the middle value again and again until the difference between the actual value and the predicted value is low 

x = 54321
num_guess = 0
ep = 0.01  # Epsilon (acceptable error)
low = 0
high = x
guess = (high + low) / 2.0

while abs(guess**2 - x) >= ep:  # Corrected stopping condition
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0  # Update guess after refining bounds
    num_guess += 1  # Increment guess count

print(f'{num_guess} guesses were done to find the square root')
print("The estimated square root is:", guess)
#Square root for all x values 
x = 0.5 
ep  = 0.01
if x>=1:
    low = 1.0
    high = x
else:
    low = x
    high= 1.0
guess = (high+low)/2
while (abs(guess ** 2-x))>= ep: 
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0  # Update guess after refining bounds
    num_guess += 1  # Increment guess count
print(f'{str(guess)} is close to {str(x)}')

#square root for values between 0 and 1 :
x = 0.5 
ep  = 0.01
low = 0
high = 1 
guess = (high+low)/2
while (abs(guess ** 2-x))>= ep:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0  # Update guess after refining bounds
    num_guess += 1  # Increment guess count
print(f'{str(guess)} is close to {str(x)}')
#cube root of positive cubes
cube = 27
low = 0
high = cube
ep = 0.01
num_guess = 0
guess = (high+low)/2.0
while abs(guess**3-cube)>=ep:
    if (guess**3)<cube :
        low = guess
    else:
        high = guess
    guess = (high+low)/2.0
    num_guess+=1
print(f'{num_guess} is taken to find the cube root')
print("the cube root of cube is ",guess)
#Newton Raphson
ep = 0.01
k =24.0
guess = k/2.0
num_guess = 0
while (guess*guess - k)>=ep:
    num_guess+=1
    guess = guess -(((guess**2)-k)/(2*guess))
print("num_guesses = " + str(num_guesses))
print("square root of " + str(k) +"is about " + str(guess))






