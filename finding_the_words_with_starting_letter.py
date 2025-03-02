food = ['pizza','nuggets','hotdog','noodles','pasta','burger']
letter = input('Enter starting letter : ')
for x in food:
    if x.startswith(letter):
        print(x)