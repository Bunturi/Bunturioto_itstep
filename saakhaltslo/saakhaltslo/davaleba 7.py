def mnt(lst):
    if not lst:
        return f"{lst} ლისტი ცარიელია"
    elif sorted(lst)[0] == sorted(lst)[-1]:
        return f"{lst} ლისტი შედგება დუბლიკატებისგან"
    elif lst == sorted(lst):
        return f"{lst} ლისტი მონოტონურია და დალაგებულია ზრდადობით"
    elif lst == sorted(lst, reverse=True):
        return f"{lst} ლისტი მონოტონურია და დალაგებულია კლებადობით"
    else:
        return f"{lst} ლისტი არა მონოტონურია"


lst_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
lst_2 = [1, 2, 4, 3, 5, 7, 6, 9, 1]
lst_3 = []
lst_4 = [1, 1, 1, 1, 1, 1, 1, 1]

rslt_1 = mnt(lst_0)
rslt_2 = mnt(lst_1)
rslt_3 = mnt(lst_2)
rslt_4 = mnt(lst_3)
rslt_5 = mnt(lst_4)

print(rslt_1)
print(rslt_2)
print(rslt_3)
print(rslt_4)
print(rslt_5)
