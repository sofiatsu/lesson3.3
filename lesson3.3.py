lst = list(input("list"))
l = len(lst)

if (l % 2) == 0:
    print(lst[:(l // 2)], lst[(l // 2):])
else:
    print(lst[:(l // 2+1)], lst[(l // 2+1):])

