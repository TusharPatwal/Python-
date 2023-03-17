def tushar2(n):
    f1 = 0
    f2 = 1
    print(f1,f2, end=" ")
    for i in range(n):
        f3 = f1+f2 
        f1 = f2
        f2 = f3 
        print(f3, end = " ")

if __name__ == "__main__":
    tushar2(7)