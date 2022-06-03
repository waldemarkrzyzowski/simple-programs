#Enter a text1 and text2
wyraz = input("Enter a text1: ")
drugi_wyraz = input("Enter a text2: ")

# create a list and append each letter with text1
wyr =[]
for litera in wyraz:
    wyr.append(litera)

# check if each letter with text2 is in list wyr
for litera in drugi_wyraz:
    if litera in wyr:
        wyr.remove(litera)
        continue
    else:
        print("Given test is not anagram!")
        break
else:
    print("Given text is anagram.")
