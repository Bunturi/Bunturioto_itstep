#დავალება N1
print('დავალება N1')
def tot(numbers):
    return sum(numbers)
res_tot = tot([100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10])
print(res_tot)

# დავალება N2
print('დავალება N2')
def split_total(number):
    return sum([int(i) for i in str(number)])
result = split_total(12345)
print(result)

#დავალება N3

print('დავალება N3 გზა N1')
def rev(txt):
    return txt[::-1]
z = rev("Hello")
print(z)
#რეკურსიით დავალეაბ N3
print('დავალება N3 რეკურსიით')
def txt(revers):
    if len(revers) <= 1:
        return revers
    else:
        return txt(revers[1:]) + revers[0]

result = txt("Hello")
print(result)

#დაქვალება N4
print('დავალება N4 რეკურსიით ფაქტორიალი')

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
res = factorial(10) #input-იც შეიძლებოდა აქ
print(f"ფაქტორიალი: {res}")