import random
import string
# დავალება N1
print("დავალება N1")

with open("text_file_1.txt", "w") as file:
    # რანდომ ტექსტით შევსება 1000 ხაზით და დანომვრა
    for i in range(1, 1001):
        length = random.randint(0, 30)
        txt = ''.join(random.choices(string.ascii_letters, k=length))
        file.writelines(f"{i}.{txt}\r")

# ფაილის წაკითხვა და ხაზების რაოდენობის დაბეჭდვა
with open("text_file_1.txt", "r") as file:
    lines = file.readlines()
    # print(len(lines))
    row = 0
    count = 0

    for line in lines:
        row += 1
        if row < 10 and len(line) > 3:
            count += 1
        elif row < 100 and len(line) > 4:
            count += 1
        elif row < 1001 and len(line) > 5:
            count += 1

    print(f"სულ ხაზების რაოდენობა არის {row}, აქედან შევსებულია მხოლოდ {count}")


# დავალება N2
print("დავალება N2")

row = {2: "two",
       8: "eight",
       10: "ten",
       13: "thirteen",
       17: "seventeen"}

with open("text_file_2.txt", "w") as file:
    for i in range(1, 18):
        if i in row:
            file.writelines(f"{i}. {row[i]}\r")
        else:
            file.writelines(f"{i}\r")


# დავალება N3
print("დავალება N3")

with open("text_file_1.txt", "r") as file_1:
    with open("text_file_2.txt", "r") as file_2:
        with open("text_append.txt", "w") as file_3:
            file_3.write(file_1.read() + "\n" + file_2.read())
