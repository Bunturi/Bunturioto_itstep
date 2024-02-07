def laep(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} ნაკიანი წელიწადია"
    else:
        return f"{year} არ არის ნაკიანი წელიწადი"


result = int(input("შეიყვანე წელი: "))
print(laep(result))
