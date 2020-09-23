def sum_intable(items):

    def make_int(i):
        try:
            return int(i)
        except TypeError:
            return 0

    return sum(make_int(i) for i in items)


print(sum_intable([1, 2.4, float]))
