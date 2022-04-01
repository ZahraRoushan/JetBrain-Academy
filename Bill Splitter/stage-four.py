"""
*** Stage 4/4: Party is over ***

Description

It's the right time to update your dictionary with new split values to make our "Who is lucky?" feature better.
First, we need to recalculate the split value for everyone. Make sure that our lucky one pays 0.
Recalculate the split value for n-1 people where n is the total length of the dictionary
and update the values in the dictionary with the new split value for everyone.
If a user decides not to use the "Who is lucky" feature, print the original dictionary.
------------
Objectives
In this stage your program should perform the following steps together with the steps of the previous stage:

1- In case of an invalid number of people, "No one is joining for the party" is expected as an output;
2- Otherwise, if the user choice is Yes, re-split the bill according to the feature;
3- Round the split value to two decimal places;
4- Update the dictionary with new split values and 0 for the lucky person;
5- Print the updated dictionary;
6- If the user entered anything else instead of Yes, print the original dictionary.

------------
Example 1: The feature is used

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
> Yes

Jem is the lucky one!

{'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25, 'Jason': 25}

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

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}

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

        invitees = dict.fromkeys(invitees, 0)
        for friend in invitees:
            if friend != lucky:
                invitees[friend] = round(bill / (num - 1), 2)
    else:
        print('No one is going to be lucky')
        invitees = dict.fromkeys(invitees, round(bill / num, 2))

    print(invitees)
