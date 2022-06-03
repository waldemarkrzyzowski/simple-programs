# Enter your birth year
data_urodzenia = input("Enter your birth year: ")

# create a list and append each digit from the birth year
data = []
for cyfra in data_urodzenia:
    data.append(cyfra)

# loop while executes until lenght of wynik != 1
wynik ='00'
while len(wynik)!= 1:
    wynik = 0
    # sum each digit in list data
    for cyfra in data:
        wynik += int(cyfra)
    # remove list data and convert variable wynik to string and create a list data
    del data
    wynik = str(wynik)
    data = []
    # check if lenght wynik > 1 if true append each digit from variable wynik to the list data else print result
    if len(wynik)>1:
        for cyfra in wynik:
            data.append(cyfra)
    else:
        print("The result is : ", wynik)
        break
