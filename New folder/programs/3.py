def tushar3():
    lst1 = []
    for i in range(10):
        a = int(input(f"Enter the {i}th index number: "))
        lst1.append(a)

    print(lst1)

    lst2 = [] # for even numbers
    lst3 = [] # for odd numbers

    for i in lst1:
        if (i%2==0):
            lst2.append(i)
        else:
            lst3.append(i)

    print(lst2)
    print(lst3)
    
tushar3()