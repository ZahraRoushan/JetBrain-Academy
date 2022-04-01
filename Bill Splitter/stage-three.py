"""
*** Stage 3/4: The Lucky One ***

Description

In this stage, you need to add a new feature to the project — pick one name from the dictionary at random; this person's
share will be paid by others. Make it a lucky day for somebody!
Make sure you give your users a choice whether they want to use this feature or not. Don't turn it on by default.
After picking a random name, print it so that everyone knows who is the lucky one.

------------
Objectives
In this stage your program should perform the following steps together with the steps of the previous stage:

1- In case of an invalid number of people, "No one is joining for the party" is expected as an output;
2- Otherwise, ask the user whether they want to use the "Who is lucky?" feature;
3- Take input from the user;
4- If a user wants to use the feature (Yes), choose a name from the dictionary keys at random and print the following:
{Name} is the lucky one!;
5- If the user enters anything else, print No one is going to be lucky.

Do not print the output of the previous stage (see examples).

------------
Example 1: The feature is used

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> Yes

Jem is the lucky one!

------------
Example 2: The feature is skipped

Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> No

No one is going to be lucky

------------
Example 3: Invalid input

Enter the number of friends joining (including you):
> 0

No one is joining for the party

------------
"""

import random

print("Enter the number of friends joining (including you):")
num = int(input())
if num <= 0:
    print("No one is joining for the party")
else:
    print('Enter the name of every friend (including you), each on a new line:')
    invitees = [input() for i in range(num)]

    bill = int(input('Enter the total bill value:\n'))
    luck_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if luck_feature == 'Yes':
        lucky = random.choice(invitees)
        print(lucky, 'is the lucky one!')
    else:
        print('No one is going to be lucky')
        
