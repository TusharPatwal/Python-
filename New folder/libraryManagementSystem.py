# library management sysytem
import pickle
import os

def append():
    file = open("data.txt", "ab")
    l = {}
    r = int(input("Enter the Id Number of the book: "))
    n = input("Enter Names of the book: ")
    m = input("Enter Author of the book: ")
    i = input("Enter wether it is issue or not: ")
    l["Id"] = r
    l["Name"] = n
    l["Author"] = m
    l["Issue"] = i
    pickle.dump(l, file)
    file.close()


def display():
    file = open("data.txt", "rb")
    l = {}
    try:
        while True:
            l = pickle.load(file)
            print(l)
    except EOFError:
        file.close()


def Search():
    file = open("data.txt", "rb")
    f = 1
    try:
        a = int(input("Enter the Id  Number: "))
        while True:
            l = pickle.load(file)
            if a == l["Id"]:
                print("Record Is Successfully exit")
                print(l)
                f = 0
    except EOFError:
        file.close()


def update():
    file = open("data.txt", "rb+s")
    l = {}
    f = 1
    try:
        a = int(input("Enter the Id Number: "))
        while True:
            p = file.tell()
            l = pickle.load(file)
            if a == l["Id"]:
                m1 = input("Enter Updated Issue: ")
                file.seek(p)
                l['Issue'] = m1
                pickle.dump(l, file)
            f = 0
    except EOFError:
        file.close()


def delete():
    file = open("data.txt", "rb")
    file1 = open("data1.txt", "wb")
    l = {}
    l1 = {}
    f = 1
    try:
        a = int(input("Enter Id Number: "))
        while True:
            l = pickle.load(file)
            if a != l["Id"]:
                l1 = l
                pickle.dump(l1, file1)
        f = 0
    except EOFError:
        file.close()
        file1.close()
    os.remove("data.txt")
    os.rename("data1.txt", "data.txt")
    if f == 1:
        print("Record is deleted.")


def main():
    ans = 'y'
    print("\tWelcome To Library Management System")
    while (ans != 'n'):
        print("\n1.Append")
        print("2.Display")
        print("3.Update")
        print("4.Delete")
        print("5.Search")
        print("6.Exit")
        opt = int(input("Enter Your Option : "))
        if opt == 1:
            append()
        elif opt == 2:
            display()
        elif opt == 3:
            update()
        elif opt == 4:
            delete()
        elif opt == 5:
            Search()
        elif opt == 6:
            break


if __name__ == "__main__":
    main()