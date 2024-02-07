# დავალება N1

def squared_numbers(n):
    return tuple(i ** 2 for i in range(1, n+1))


result_1 = squared_numbers(10)
print(result_1)

#დავალება N2
def func(tpl1, tpl2):
    return tuple(set(tpl1 + tpl2)), list(set(tpl1).intersection(set(tpl2)))


tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)
result_2 = func(tuple1, tuple2)

print(f"combined_tuple: {result_2[0]}")
print(f"duplicated_values: {result_2[1]}")