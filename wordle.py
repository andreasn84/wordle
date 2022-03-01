correctword = [None] * 5

yellowchars = [[], [], [], [], []]
greychars = ['']

def countuniquechars(word):
    chars = set()
    for c in word:
        chars.add(c)
    return len(chars)

def lettersinword():
    letters = []
    for y in range(len(yellowchars)):
        chars = yellowchars[y]
        for char in chars:
            if char.isalpha():
                letters.append(char)
    return letters


def guessword(words, guess, result):
    for num, char in enumerate(result):
        if char == '_' and guess[num].isalpha():
            greychars.append(guess[num])
        if char.isupper() and guess[num].isalpha():
            yellowchars[num].append(char.lower())
        if char.islower() and guess[num].isalpha():
            correctword[num] = char

    wordstoremove = []
    for w in words:
        c=0
        for num, char in enumerate(w):
            if char in greychars:
                wordstoremove.append(w)
                continue
            if correctword[num] and correctword[num].isalpha() and char != correctword[num]:
                wordstoremove.append(w)
                continue
            if yellowchars[num] and char in yellowchars[num]:
                wordstoremove.append(w)
                continue
            letters = lettersinword()
            if char in letters:
                c += 1
        letters = lettersinword()
        if c == 0 and len(letters) > 0:
            wordstoremove.append(w)
            continue
    for w in wordstoremove:
        if w in words:
            words.remove(w)
    return words


def getworldlist():
    f = open('/usr/share/dict/words', 'r')

    startwords = set()
    for word in f:
        word = word.replace("\n", "")
        word = word.replace("'s", "")
        if len(word) == 5:
            startwords.add(word.lower())
    return startwords


words = getworldlist()


for i in range(1,6):
    print("Capital letter for yellow")
    print("Lowercase letter for green")
    print("Underline '_' for gray")
    print("------------")
    print(str(i) + "  word")
    guess = input()
    print(str(i) + " result")
    result = input()
    words = guessword(words, guess, result)
    print(words)
