# the list "walks" is already defined
# your code here
# count = 0
# total = 0
# for walk in walks:
#     count += 1
#     total += walk['distance']
# print(int(total / count))

print(sum(walk["distance"] for walk in walks) // len(walks))