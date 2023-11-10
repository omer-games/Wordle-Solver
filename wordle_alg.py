import urllib.request
from random import randrange
from colored import fg, attr
import os

os.system('Title Wordle Solve by Omer826')

filename, headers = urllib.request.urlretrieve("http://www.freescrabbledictionary.com/sowpods/download/sowpods.txt", filename="sowpods.txt")

words = []
not_working_words = []

with open(filename, "r") as f:

    for line in f:
        word = line.strip()

        if len(word) == 5:
            words.append(word.lower())

works = 0


Final_word = words[randrange(0, 12477)]

not_in_word = []
in_word = []
in_place = []

in_wordT = []
in_placeT = []

use_words = words.copy()


print(fg('blue') + '\n', Final_word + attr('reset'), end='')

loop = 0

while loop < 6:

    print('''
        ''')
    
    for uword in list(use_words):

        for j in range(5):
            
            if uword[j] in not_in_word:

                use_words.remove(uword)
                break
        try:
            for i in in_placeT:

                if i[0] not in uword:

                    use_words.remove(uword)

                indices = []

                for k in range(5):

                    if uword[k] == i[0]:
                        indices.append(k)

                if i[1] not in indices:
                    use_words.remove(uword)

            for i in in_wordT:

                if i[0] not in uword:
                    use_words.remove(uword)

                if i[1] == uword.index(i[0]):
                    use_words.remove(uword)

        except ValueError:
            pass     

    if loop == 0:
        inp_word = 'tubes'

    elif loop == 1:
        inp_word = 'fling'

    elif loop == 2:
        inp_word = 'champ'

    elif loop == 3 and len(set(in_word)) + len(set(in_place)) - len((set(in_word) & set(in_place))) < 4:
        inp_word = 'wordy'
        
    else:
        inp_word = use_words[randrange(0, len(use_words))]
        
    if len(inp_word.lower()) == 5 and inp_word.lower() in words:
        is_word = True

    elif len(inp_word.lower()) != 5:

        is_word = False
        print("This word don't have 5 letters")

    try: 
        use_words.remove(inp_word)

    except ValueError:
        pass

    if is_word:

        loop += 1

        for i in range(5):

            if inp_word[i] == Final_word[i]:
                print(fg('green') + inp_word[i] + attr('reset'), end='')

                in_place.append(inp_word[i])
                in_placeT.append((inp_word[i], i))

            elif Final_word.count(inp_word[i]) > 1:
                print(fg('yellow') + inp_word[i] + attr('reset'), end='')

                in_word.append(inp_word[i])
                in_wordT.append((inp_word[i], i))

            elif inp_word[i] in Final_word:
                print(fg('yellow') + inp_word[i] + attr('reset'), end='')

                in_word.append(inp_word[i])
                in_wordT.append((inp_word[i], i))

            else:
                print(fg('white') + inp_word[i] + attr('reset'), end='')
                not_in_word.append(inp_word[i])

        if inp_word == Final_word:
            print('\nCongratulations, you found the word :D')
            works += 1
            win = True
            break


delay = input('\nPress enter to exit')