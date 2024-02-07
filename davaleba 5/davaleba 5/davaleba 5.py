import random

# დავალება N1
print("დავალება N1")

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]
tot = mylist[3] + mylist[9] + mylist[14]
print(tot)

# დავალება N1........................................................................
# გაზა N2, ლისტად რომ გადავცეთ იბდექსები ვთქატ ბევრი რომ იყოს

print("დავალება N1 დიდი ლისტში რომ მოვიძიოთ ლისტად გადაცემული ინდექსები")
mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]
my_index = [3, 9, 14]
total = 0

for i in my_index:
    total += mylist[i]
print(total)

# დავალება N2.........................................................................
print("დავალება N2")

# ლისტის სიგრძე რანდომად
set_length = round(random.random() * random.randint(20, 100))
print(f"ლისტის შედგება {set_length} რიცხვისგან")

# ლისტის შექმნა და შევსება რანდომ რიცხვებით
numbers = [round(random.random() * random.randint(10, 1000)) for i in range(set_length)]
print(f"რანდომად გენერირებული ლისტი {numbers}")

minimum = min(numbers)
maximum = max(numbers)

print(f"ლისტში მინიმუმი არს {minimum} და მაქსიმუმი არის {maximum}")

# დავალება N3...................................................................
print("დავალება N3")

my_llist = [43, '22', 12, 66, 210, ["hi"]]
# A
print(f"A. 210 ის ინდექსია {my_llist.index(210)}")
# B
my_llist[-1].append("hello")
print(f"B. ბოლო ელემენტში hello-ს დამატება {my_llist}")
# C
# del my_llist[2] # ესეც გავაკეთე
x = my_llist.pop(2)
print(f"C. მეორე პოზიციის {x}-ის გარეშე {my_llist}")
# D
my_list_2 = my_llist.copy()
my_list_2.clear()
print(f"D. პირველი ლისტი {my_llist} და მეორე ლისტი {my_list_2}")

# დავალება N4...................................................................
print("დავალება N4")

# 3x3 ზე მატრიცის შექმნა 1დან 9ის ჩათვლით
matrix = [[1 + j + i * 3 for j in range(3)] for i in range(3)]
print(matrix)

# ტრასნპონირება ინდექსების შებრუნება
new_matrix = [[matrix[l][k] for l in range(len(matrix[k]))] for k in range(len(matrix))]
print(new_matrix)
