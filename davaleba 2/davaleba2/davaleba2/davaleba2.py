#დავალება 1
print("     დავალება N1")

num=int(input("შეიყვანეთ რიცხვი: "))

if num % 2 == 0:
    print("even")
else:
    print("odd")


# დავალება 2
print("     დავალება N2")

text=str(input("შეიყვანეთ ტექსტი: "))
s="small"
t="tall"
m="middle"

if s in text:
    print(s)
elif t in text:
    print(t)
elif m in text:
    print(m)
else:
    print("შეყვანილ ტექსტში საძიებო სიტყვები არ მოიძებნა")


#დაბალება 3

print("     დავალება N3")

x=float(input("შეიყვანეთ პირველი რიცხვი: "))
y=float(input("შეიყვანეთ მეორე რიცხვი: "))
opp=input("შეიყვანეთ ოპერატორი: ")

if opp == "+":
    print(f"{x}+{y}=",x+y)
elif opp == "-":
    print(f"{x}-{y}=",x-y)
elif opp =="*":
    print(f"{x}*{y}=",x*y)
elif opp =="**":
    print(f"{x}**{y}=",x**y)
elif opp =="/":
    if y==0:
        print("ნულზე გაყოფა არ შეიძლება")
    else:
        print(f"{x}/{y}=",x/y)
elif opp =="//":
    if y==0:
        print("ნულზე გაყოფა არ შეიძლება")
    else:
        print(f"{x}//{y}=",x//y)
elif opp =="%":
    if y==0:
        print("ნულზე გაყოფა არ შეიძლება")
    else:
        print(f"{x}%{y}=",x%y)
else:
    print("თვქენ არასწორად შიყვანეთ ოპერატორი, გთხოვთ აირჩიეთ შემდეგი ოპერატორებიდან + , - , * , ** , / , // , % ")
