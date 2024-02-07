#დავალება N1
print("დავალება N1")

txt=str(input("შეიყვანე ტექსტი: ")).lower()
rev=""
for i in range(len(txt)-1,-1,-1):
   rev+=txt[i]
if txt==rev:
    print("შეყვანილი ტექსტი არის პალინდრომი")
else:
    print("შეყვანილი ტექსტი არ არის პალინდრომი")


#დავალება N2
print("დავალება N2")

text=str(input("შეიყვანე ტექსტი: "))

for char in text:
    t_ascii = ord(char)
    print(t_ascii,end=" ")