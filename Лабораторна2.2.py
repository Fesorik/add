def f1_search(x,search_k):
    vile = 0
    top = len(x)-1
    search_res = False
    while vile <= top and not search_res:
        mid = (vile + top)//2
        guess = x[mid]
        if guess == search_k:
            search_res = True
            return search_res
        if guess > search_k:
            top = mid-1
        else:
            vile=mid+1
    return search_res
x=[4, 9, 21, 12, 32, 144, 55, 59, 21]
value = 144
result = f1_search(x,value)
if result:
    print("Елемент не знайдено")
else:
    print("Елемент знайдено")