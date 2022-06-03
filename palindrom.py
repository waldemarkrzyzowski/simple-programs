# ender a word
expression = input("Enter an expression: ")

# create new variable and remove all spaces
new_expression =""
for letter in expression:
    if letter == " ":
        continue
    else:
        new_expression+=letter.upper()

i = 0
j = len(new_expression)-1
# while loop executes until index i and j are different
while (i != j):
    # check if letters are the same
    if new_expression[i] == new_expression[j]:
        i+=1
        j-=1
        continue
    else:
        print("Given expression is not a palindrome!")
        break
else:
    print("Expresion: ", expression, " is a palindrome.")
