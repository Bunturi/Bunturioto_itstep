def what_number(n):
    if n >= 0:
        lst = [i for i in range(1, n+1) if n % i == 0]
    else:
        lst = [i for i in range(n, 0, 1) if n % i == 0]

    if len(lst) <= 2:
        return f"{n} არის მარტივი რიცხვი"
    else:
        return f"{n} არის რთული რიცხვი და მისი გამყოფებია: {lst}"


result = what_number(int(input("შეიყვანე რიცხვი: ")))
print(result)
