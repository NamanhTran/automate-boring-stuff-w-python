spam = ['apples', 'bananas', 'tofu', 'cats']

for i in range(len(spam)):
    if i == len(spam) - 1:
        print("and " + spam[i])
    else:
        print(spam[i] + ", ", end="")