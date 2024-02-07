#დავალება 1

print("დავალეაბ N1")


while True:
    number=int(input("შეიყვანე რიცხვი: "))

    # თუ რიცხვი დადებითია
    if number > 0:
        while number > 0:
            print(number)
            number-=1

    #თუ რიცხვი უარყოფითია
    elif number < 0:
        while number < 0:
            print(number)
            number+=1

    #თუ ნულია
    else:
        print("თქვენ შიეყვანეთ რიცხვი: 0")

    #თავიდან გინდა თუ არა რომ ჩაწერო რიცხვი
    #[lower() აღმოვაჩინე როცა Yes ჩაბერე და არ იმუშავა
    while True:
        again = input("კიდევ შეიყვან რიცხვს? yes/no ").lower()
        if again == "yes" or again == "no":
             break

    if again != "yes":
        print("დროებით!")
        break


#დავალება N2

print("დავალება N2")

total_sum=0

while True:
    numb=int(input("შეიყვანეთ რიცხვი: "))
#დადებითი რიცხვის დამატება
    if numb > 0:
        total_sum+=numb
#უარყოფითის ან 0-ის გამოტოვება. აქ pass გამოვიყენე თუმცა 0ის დამატეაბც შილებოდა
    else:
        pass
        #total_sum+=0
#ინფუთის შემოწმება მართებულ სიტყვაზე
    while True:
        next_numb = input("დაუმადებთ კიდევ რიცხვს თუ გაჩვენოთ ჯამი? yes/sum ").lower()
        if next_numb == "sum" or next_numb == "yes":
            break
#შესაბამისი მოქმედება ჯამი ან თავიდან რიცხვის შეყვანა
    if next_numb !="yes":
        print(f"თქვენს მიერ შეყვანილი დადებითი რიცხვების ჯამია {total_sum}.")
        break

#დავალება N3 (while-ით და else-ით) ქვემოთ შემდეგ else-ის აგრეშეც მაქვს გაკეთებული

print("დავალეაბ N3 while-ით და else-ით")

import random
x=1
y=100

while True:
    num = random.randrange(x,y+1)
    life=5


    while life > 1:
        #შესაყვანი რიცხვის შემოწმება არის თუ არა მოცმეულ შუალედში.თუ არაა თავიდან იკითხავს
        while True:
            guess_num = int(input(f"შეიყვანეთ რიცხვი {x} დან {y}-ის ჩათვლით: "))
            if guess_num >= x and guess_num<=y:
                break
        if num == guess_num:
            print("თქვენ მოიგეთ!")
            break
        else:
            life -= 1
            if num > guess_num:
                print(f"კიდევ სცადეთ!თქვენი რიცხვი გამოსაცნობ რიცხვზე დაბალია! თქვენ დაგრჩათ {life} ცდა!")
            else:
                print(f"კიდევ სცადეთ!თქვენი რიცხვი გამოსაცნობ რიცხვზე მაღალია! თქვენ დაგრჩათ {life} ცდა!")
    else:
        while True:
            guess_num = int(input(f"შეიყვანეთ რიცხვი {x} დან {y}-ის ჩათვლით: "))
            if guess_num >= x and guess_num <= y:
                break
        if num == guess_num:
            print("თქვენ მოიგეთ!")
            break
        else:
            print(f"თქვენ წააგეთ! გამოსაცნობი რიცხვი იყო {num}")
#ინფუთის შემოწმება მართებულ სიტყვაზე თამაშის თავიდან დასაწყეაბდ
    while True:
        again = input("კიდევ ითამაშებთ? yes/no ").lower()
        if again == "yes" or again == "no":
            break

    if again !="yes":
        print("დროებით!")
        break

#დავალება N3  else-ის გარეშე

print("დავალეაბ N3 else-ის გარეშე")
import random
x=1
y=100

while True:
    num = random.randrange(x,y+1)
    life=5

    print(num)
    while True:
        # შესაყვანი რიცხვის შემოწმება არის თუ არა მოცმეულ შუალედში.
        while True:
            guess_num = int(input(f"შეიყვანეთ რიცხვი {x} დან {y}-ის ჩათვლით: "))
            if guess_num >= x and guess_num <= y:
                break
        if num == guess_num:
            print("თქვენ მოიგეთ!")
            break
        else:
            life -= 1
            if life == 0:
                print(f"თქვენ წააგეთ! გამოსაცნობი რიცხვი იყო {num}")
                break
            else:
                if num > guess_num:
                    print(f"კიდევ სცადეთ!თქვენი რიცხვი გამოსაცნობ რიცხვზე დაბალია! თქვენ დაგრჩათ {life} ცდა!")
                else:
                    print(f"კიდევ სცადეთ!თქვენი რიცხვი გამოსაცნობ რიცხვზე მაღალია! თქვენ დაგრჩათ {life} ცდა!")

    #ინფუთის შემოწმება მართებულ სიტყვაზე თამაშის თავიდან დასაწყეაბდ
    while True:
        again = input("კიდევ ითამაშებთ? yes/no ").lower()
        if again == "yes" or again == "no":
            break

    if again !="yes":
        print("დროებით!")
        break