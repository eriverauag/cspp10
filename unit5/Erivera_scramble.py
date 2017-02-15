import random
#state a word that I want to be scrambled

w = "word"

#pick the word and write out a scramble function
def scramble_word(w):
#turn the letters into a list to be able to be scrambled

    split = list(w)
    first_l = split[0]
    last_l = split[-1]
    l_takeout = split[0:-1]
    random.shuffle(l_takeout)
    l_takeout.insert(0,first_l)
    l_takeout.append(last_l)
    scramble = ''.join(l_takeout)
    print(scramble)
scramble_word(w)
