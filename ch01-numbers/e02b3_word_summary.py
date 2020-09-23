from statistics import mean


def word_summary(words):
    word_lens = [len(w) for w in words]
    return (min(word_lens), max(word_lens), mean(word_lens))


print(word_summary(["what", "a", "day"]))
