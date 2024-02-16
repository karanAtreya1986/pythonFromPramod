#Palindrome Checker:
word = str(input("Enter a string\n"))

def palindromeChecker(word):
    word = word.lower()
    size = len(word)
    c = ''
    for i in range(size - 1, -1, -1):
        c = c + word[i]
    # print(c)
    if (c == word):
        print("String is palindrome", c)
    else:
        print("String is not palindrome", c)

palindromeChecker(word)
