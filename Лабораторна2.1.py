def f1_sort(s):
    if len(s) <= 1:
        return s
    vi = s[0]
    less = list(filter(lambda x: x < vi, s))
    mid = [i for i in s if i == vi]
    more = list(filter(lambda x: x > vi, s))
    return f1_sort(less) + mid + f1_sort(more)
print(f1_sort([7, 6, 10, 5, 9, 8, 3, 4]))