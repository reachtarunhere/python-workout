def pig_latin_two_or_more(word):

    def two_or_more_vowels():
        return len(set(word).intersection(set("aeiou"))) >= 2

    if two_or_more_vowels():
        output = word + "way"
    else:
        output = word[1:] + word[0] + "ay"

    return output


print(pig_latin_two_or_more("wine"))
print(pig_latin_two_or_more("wind"))
