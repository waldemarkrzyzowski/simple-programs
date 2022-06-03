# given an expression
expression = "Wpisz cokolwiek tutaj"

# define variables
words = 1
letters = 0

# create a for loop which counts all words and letters
for i in expression:
    i = i.lower()
    if i ==' ':
        words += 1
    else:
        letters+=1
        
# print results
print("Number of words in the expression", words)
print("Number of letters in the expression", letters)
  
