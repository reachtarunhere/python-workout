def pig_latin(word):
    vowels = "aeiou"
    if word[0] in vowels:
        print(word + 'way')
    else:
        print(word[1:] + word[0] + 'ay')
