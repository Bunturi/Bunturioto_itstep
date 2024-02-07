#დავალება N1
print("დავალება N1")

def check(a,b):
    if(sorted(a)==sorted(b)):
        print("ტექსტი არის ანაგრამი")
    else:
        print("ტექსტი არ არის ანაგრამი")

txt_1 = str(input("შეიყვანეთ პირელი ტექსტი: ")).lower()
txt_2 = str(input("შეიყვანეთ მეორე ტექსტი: ")).lower()

check(txt_1,txt_2)
#დავალება N2
print("დავალება N2")
def fun(txt,sym):
    n = 0
    for char in txt:
        if char == sym:
            n += 1
    return n

text = str(input("შეიყვანე ტექსტი: "))
symbol = str(input("შეიყვანე სიმბოლო: "))

total = fun(text,symbol)
print(total)

#დავალება N3
print("დავალება N3")

def fib(n):
    f = [0, 1]
    while len(f) < n:
        next_number=f[-1] + f[-2]
        f.append(next_number)
    return f
length = int(input("შეიყვანე რაოდენობა: "))
res = fib(length)
print(f"ფიბონაჩის რიცხები {res}")


