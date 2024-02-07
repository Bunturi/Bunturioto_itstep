import random
p_point = 0
c_point = 0

while True:
    choices = ["rock", "paper", "scissor"]

    # ეს იდეაში ფუნქციის გარეშეც დაიწერეობდა აქ^^
    def win(compiuter, player):
        if compiuter == player:
            return f"ფრე! თქვენ ორივემ აირჩიეთ {compiuter}"
        elif ((compiuter == "rock" and player == "paper") or
              (compiuter == "paper" and player == "scissor") or
              (compiuter == "scissor" and player == "rock")):
            return f"თქვენ მოიგეთ! თქვენ აირჩეით {player}, ხოლო კომპიუტერმა {compiuter}."
        else:
            return f"თქვენ წააგეთ! თქვენ აირჩეით {player}, ხოლო კომპიუტერმა {compiuter}."

    # კომპიუტერის არჩევანი (ესეც შეიძლებოდა ფუნქციაში ჩაგვესვა)
    comp = random.choice(choices)

    # მოთამაშის არჩევანი და ვალიდურობა (ესეც შეიძლებოდა ფუნქციაში ჩაგვესვა)
    plyr = None
    while plyr not in choices:
        plyr = input("ამოირჩიე: rock, paper, scissor?: ").lower()

    result = win(comp, plyr)
    print(result)

    # ანგარიშის დათვლა
    if result == f"თქვენ მოიგეთ! თქვენ აირჩეით {plyr}, ხოლო კომპიუტერმა {comp}.":
        p_point += 1
    elif result == f"თქვენ წააგეთ! თქვენ აირჩეით {plyr}, ხოლო კომპიუტერმა {comp}.":
        c_point += 1
    print(f"ანგარიშია: კომპიუტერი: {c_point}, თქვენ: {p_point}")

    # თავიდან თამაში და ვალიდურობა
    while True:
        again = input("ითამაშებ თავიდან? (yes/no): ").lower()
        if again == "yes" or again == "no":
            break
    if again != "yes":
        break
# ანგარიშის გამოცხადება და დამშვიდობება:დ
if c_point > p_point:
    print(f"დროებით! თამაში დასრულდა ანგარიშით {c_point}:{p_point}. კომპიუტერმა მოიგო! სხვა დროს მოიგებთ^^")
elif c_point < p_point:
    print(f"დროებით! თამაში დასრულდა ანგარიშით {p_point}:{c_point}. თქვენს მოიგეთ! გილოცავთ!")
