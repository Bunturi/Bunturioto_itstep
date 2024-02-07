# დავალება 1
print("დავალება N1")


def func(txt):
    return {i: txt.split(" ").count(i) for i in set(txt.split(" "))}
# ესე დაწერე უფრო მართებულია თუ ზემოთ როგორც მიწერია?
# def func(txt):
#     lst = txt.split(" ")
#     return {i: lst.count(i) for i in set(lst)}


txt_1 = 'The wind howled and howled all night long'
res = func(txt_1)
print(res)

# დავალება 2
print("დავალება N2")


def calculator(operator, x, y):
    if operator not in ['+', '-', '*', '/']:
        return "არასწორი ოპერატორი"

    if operator == "/" and y == 0:
        return "ნულზე გაყოფა არ შეიძლება"

    operations = {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y
    }  # იგივე ლოგიკით სხვა ოპერატორების შეყვანა შეიძლება

    return operations[operator]


op = input("შეიყვანე ოპერატორი(+, -, *, /) : ")
num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))

res = calculator(op, num1, num2)
print(res)
