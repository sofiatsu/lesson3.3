lst = [1,2,3]
l_lst = len(lst)

if (l_lst % 2) == 0:
    print(lst[:(l_lst // 2)], lst[(l_lst // 3):])
else:
    print(lst[:(l_lst // 2 + 1)], lst[(l_lst // 2 + 1):])