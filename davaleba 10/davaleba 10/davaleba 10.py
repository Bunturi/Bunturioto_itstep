import random
# დავალება N1
def linear_search(lst_f_s,x):
    for i in range(len(lst_f_s)):
        if lst_f_s[i] == 7:
            return i
    return -1


def bubble_sort(lst_for_sort):
    length = len(lst_for_sort)
    for i in range(length):
        swapped = False
        for j in range(length-1):
            if lst_for_sort[j] > lst_for_sort[j+1]:
                lst_for_sort[j], lst_for_sort[j+1] = lst_for_sort[j+1], lst_for_sort[j]
                swapped = True
        if not swapped:
            break


def binary_search(lst_for_search, value):

    low = 0
    high = len(lst_for_search)-1

    while low > high:
        mid = (low+high)//2

        if lst_for_search[mid]< value:
            low = mid +1
        elif lst_for_search[mid] > value:
            high = mid -1
        else:
            return mid
    return -1


lst = [random.randint(-100, 100)*i for i in range(1, 101)]
print(f"საწყისი ლისტი {lst}")

num_for_search = random.randint(-1000,1000)
res_lin_search = linear_search(lst, num_for_search)
print(f"ხაზობრივის ძებნის შედეგი {res_lin_search} საძიებო რიცხვი {num_for_search}")

bubble_sort(lst)
print(f"ბაბლით სორტირებული ლისტი: {lst}")

num_for_search_2= random.randint(-1000,1000)
res_bin_search = binary_search(lst, num_for_search_2)
print(f"ბინარული ძიების შედეგი: {res_bin_search} საძიებო მეორე რიცხვი {num_for_search_2}")


# დავალება N2
print("დავალება N2")
def linear_search(lst_for_search, x):
    return -1 if not lst else [i for i in range(len(lst_for_search)) if x(lst_for_search[i])]


lst = [4, 15, 3, 4, 1, 20, 4]
l_search = lambda x: x % 3 == 0

res = linear_search(lst, l_search)
print(res)
