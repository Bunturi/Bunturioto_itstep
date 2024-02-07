from functools import reduce
# დავალება N1
print("დავალება N1")


def new_list(lst_1, lst_2):
    return list(zip(lst_1, lst_2))


result_1 = new_list([1, 2, 3], ['a', 'b', 'c'])
print(result_1)

# დავალება N2
print("დავალება N2")

num_lst = [1, 2, 3, 4, 5, 6, 7]
result_2 = list(filter(lambda a: a % 2 != 0, num_lst))
print(result_2)

# დავალება N3
print("დავალება N3")

num_l = [1, 2, -3, -4, 5, -6, -7, -8, -9, -10]
result_3 = list(filter(lambda x: x > 0, num_l))
print(result_3)

# დავალება N4
print("დავალება N4")

words = ["airamzissizmaria", "oto", "atami", "drosha"]
result_4 = list(filter(lambda x:  x == x[::-1], words))
print(f"პალინდრომებია: {result_4}")

# დავალება N5
print("დავალება N5")
try:
    lst_input = ["a", "b", 1, 2, 3, 4, 5]
    result_5 = reduce(lambda x, y: x * y, lst_input)
    print(result_5)
except TypeError:
    print("გთხოთ აუცილებალდ შეიყვანოთ რიცხვი, აღნიშნული მოქმედბეა ხორციელდბეა მხოლოდ რიცხვებზე")


# დავალება N6
print("დავალება N6")
try:
    params = ['hello', 'world', 'coding', 'nod']
    ending = 'ing'
    result_6 = list(filter(lambda x: x.endswith(ending), params))
    print(result_6)
except TypeError:
    print("გთხოთ აუცილებალდ შეიყვანოთ სიტყვები")
