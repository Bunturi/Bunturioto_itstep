import csv
# დავალება N1
with open("titanic.csv", "r") as csvfile:
    csv_dict_read = csv.DictReader(csvfile)
    survivors = [row for row in csv_dict_read if row["Survived"] == "1"]

with open("survived.csv", "w", newline="") as csvfile:
    header = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
              'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    writer = csv.DictWriter(csvfile, fieldnames=header)

    writer.writeheader()
    writer.writerows(survivors)

# დავალება N3

with open("organizations-100.csv", "r") as csvfile:
    csv_dict_read = csv.DictReader(csvfile)
    sorted_list = sorted([row for row in csv_dict_read], key=lambda x: x['Number of employees'])

with open("sorted_csv.csv", "w", newline="") as csvfile:
    header = ['Index', 'Organization Id', 'Name', 'Website', 'Country',
              'Description', 'Founded', 'Industry', 'Number of employees']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(sorted_list)

# დავალება N2

with open("organizations-100.csv", "r") as csvfile:
    csv_dict_read = csv.DictReader(csvfile)
    lst_for_https = [row for row in csv_dict_read if row["Website"][:5] == "https"]

    # გაფილტრული ცხრილიდან ვშლით არასაჭირო სვეტებს
    header = ['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']
    list_for_write = []

    for row in lst_for_https:
        mod_row = {key: value for key, value in row.items() if key in header}
        list_for_write.append(mod_row)

with open("ssl_companies.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)

    writer.writeheader()
    writer.writerows(list_for_write)
