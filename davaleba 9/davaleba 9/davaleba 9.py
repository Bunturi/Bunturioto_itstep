import random
# დავალება N1

lst = [random.randint(-100, 100)*i for i in range(1, 101)]
print(f"საწყისი ლისტი {lst}")
lst.sort()
print(f"ზრდადობით {lst}")
down = sorted(lst, reverse=True)
print(f"კლებადობით {down}")

# დავალება N2

print("დავალება N2")


def bubble(lst_f_sort):
    length = len(lst_f_sort)
    for i in range(length):
        swapped = False
        for j in range(length-1):
            if lst_f_sort[j] > lst_f_sort[j+1]:
                lst_f_sort[j], lst_f_sort[j+1] = lst_f_sort[j+1], lst_f_sort[j]
                swapped = True
        if not swapped:
            break


def quicksort(lst_f):
    if len(lst_f) <= 1:
        return lst_f
    else:
        pivot = lst_f.pop()
        left = [x for x in lst_f if x >= pivot]
        right = [x for x in lst_f if x < pivot]
        return quicksort(left) + [pivot] + quicksort(right)


lst_2 = [random.randint(-100, 100) * i for i in range(1, 101)]
print(f"საწყისი ლისტი: {lst_2}")


bubble(lst_2)
print(f"ბაბლსორტი ზრდადობით: {lst_2}")


sorted_lst = quicksort(lst_2)
print(f"ქუიქსორტი კლებადობით: {sorted_lst}")
