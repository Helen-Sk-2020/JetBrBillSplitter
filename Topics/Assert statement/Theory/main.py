#  You can experiment here, it won’t be checked
word = 'cat'
assert word != "cat"
print("Your word is", word)

word = 'cat'
message = "'cat' is the wrong word!"
assert word != "cat", message
print("Your word is", word)
