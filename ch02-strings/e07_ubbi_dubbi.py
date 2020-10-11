def ubbi_dubbi(word):
    # u first becaue other charcters will introduce u's that we shouldn't replace
    for vowel in 'uaeio':
        word = word.replace(vowel, f'ub{vowel}')
    return word
