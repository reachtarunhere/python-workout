def copy_case(src, tgt):
    if src.isupper():
        return tgt.upper()
    elif src.istitle():
        return tgt.title()
    return tgt.lower()


def pig_latin(word):
    output = None
    if word[0] in "aeiou":
        output = word + "way"
    else:
        output = word[1:] + word[0] + "ay"
    return copy_case(word, output)


print(pig_latin("Tarun"))
