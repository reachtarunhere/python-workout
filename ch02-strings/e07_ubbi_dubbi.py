def ubbi_dubbi(word):
    # u first becaue other charcters will introduce u's that we shouldn't replace
    new_word = ''
    for c in word:
        if c in 'aeiou':
            new_word += 'ub'
        new_word += c
    return new_word
