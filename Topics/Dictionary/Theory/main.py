import random
numbers_of_friends = int(input("Enter the number of friends joining (including you):"))
print(numbers_of_friends)
if numbers_of_friends < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = [input() for x in range(numbers_of_friends)]
    print('Enter the total bill value:')
    final_bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == "No":
        print("No one is going to be lucky")
        split_value = round(final_bill / numbers_of_friends, 2)
        friends_dict = {friend: split_value for friend in friends}
        print(friends_dict)
    elif answer == "Yes":
        lucky = random.choice(friends)
        print(f"{lucky} is the lucky one!")
        split_value = round(final_bill / (numbers_of_friends - 1), 2)
        friends_dict = {friend: split_value for friend in friends if friend != lucky}
        lucky_dict = dict.fromkeys([lucky], 0)
        print(lucky_dict)
        print(friends_dict)
        print(lucky_dict.update(friends_dict))