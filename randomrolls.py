import random

print("Hello there traveler. Would you like to play a game with my magical rolling dice. The weather is wicked outside and it is the time to gamble.")
print("Would you like like to make a random roll with a 6-sided dice or a 20-sided dice?")

i = 0

while i == 0:
    choice = input("Choose your dice\n6 \nor 20?")
    
    if choice == "6": 
        print(random.randint(1, 6))
    
    elif choice == "20": 
        print(random.randint(1,20))
        
    roll_again = input('Would you like to roll again (y/n)?')
    
    if roll_again == 'y':
        i = 0
    else:
        i = 1
