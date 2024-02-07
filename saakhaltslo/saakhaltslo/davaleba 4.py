# კეისრის კოდი
lst = 'abcdefghijklmnopqrstuvwxyz'


def code(txt, num):
    new_txt = ""
    for char in txt:
        if (lst.index(char) + num) < 26:
            new_txt += (lst[lst.index(char) + num])
        else:
            new_txt += (lst[(lst.index(char) + num) % 26])
    return new_txt


text = str(input("შეიყვანეთ ტექსტი: ")).lower()
number = int(input("შეიყვანეთ რიცხვი: "))
result = code(text, number)
print(result)
