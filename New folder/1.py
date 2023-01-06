
def tushar1(str2):
    str1 = "aeiouAEIOU"
    count = 0
    for i in str2:
        if i in str1:
            count += 1
    print(count)

str2 = input("Enter the string: ")
tushar1(str2)