from e05_pig_latin import pig_latin


def pl_sentence(sentence):
    return " ".join(pig_latin(w) for w in sentence.split())
