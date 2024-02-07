#ეს უფრო კარგად გამოიყურება
def divider(n):
    return max([i for i in range(1,n) if (n % i) == 0])
result = divider(int(input("შეიყვანე რიცხვი: ")))
print(result)



#ეს უფრო სწრაფი იქნება ალბათ? რადგან პირელივე გამყოფზე ჩერდება
def divider_2(n):
    for i in range(n-1, 1, -1):
        if (n % i) == 0:
            return i
result_2 = divider_2(int(input("შეიყვანე რიცხვი: ")))
print(result_2)

