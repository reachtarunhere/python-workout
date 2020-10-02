from string import punctuation


def pig_latin_punctuation(word):

    if word[-1] in punctuation:
        word, end_symbol = word[:-1], word[-1]
    else:
        word, end_symbol = word, ""

    if word[0] in "aeiou":
        output = word + "way"
    else:
        output = word[1:] + word[0] + "ay"

    return output + end_symbol


print(pig_latin_punctuation("tarun!"))
