def dblct(lst):
    new_lst = []
    for i in sorted(lst):
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


lst_input = [1, 2, 3, 4, 5, 4, 5, 8, 10, 1, 2, 3, 1, 3, 1]
rslt = dblct(lst_input)
print(rslt)
