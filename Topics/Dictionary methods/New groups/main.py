# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
kindergarten = dict.fromkeys(groups)
number_groups = int(input())
# number_groups = 4
counter = 0
while counter < number_groups:
    kids = int(input())
    # kids = 10
    counter += 1
    kindergarten[groups[counter - 1]] = kids
    
print(kindergarten)
