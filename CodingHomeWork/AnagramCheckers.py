#Anagram Check

str1=input("Enter first string\n")
str2=input("Enter second string\n")

if(len(str1)!=len(str2)):
    print("Strings not same length hence not Anagram")
    exit()

str3=str1.lower();
str4=str2.lower();

str3=str3.replace(" ", "")
str4=str4.replace(" ", "")

str3Sorted=sorted(str3)
str4Sorted=sorted(str4)

if(str3Sorted==str4Sorted):
    print("Anagram")
else:
    print("Not Anagram")