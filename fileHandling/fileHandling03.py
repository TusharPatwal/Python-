import pickle
import os


def append():
    file = open("sms.txt", "ab")
    d = {}
    r = int(input("Enter the Roll Number of the Student "))
    n = input("Enter Names of the student")
    m = int(input("Enter Marks of the students"))
    d["Roll"] = r
    d["Name"] = n
    d["Marks"] = m
    pickle.dump(d, file)
    file.close()


def display():
    file = open("sms.txt", "rb")
    d = {}
    try:
        while True:
            d = pickle.load(file)
            print(d)
    except EOFError:
        file.close()


def Search():
    file = open("sms.txt", "rb")
    f = 1
    try:
        a = int(input("Enter the Roll  Number"))
        while True:
            d = pickle.load(file)
            if a == d["Roll"]:
                print("Record Is Successfully exit")
                print(d)
                f = 0
    except EOFError:
        file.close()


def update():
    file = open("sms.txt", "rb+")
    d = {}
    f = 1
    try:
        a = int(input("Enter the Roll Number"))
        while True:
            p = file.tell()
            d = pickle.load(file)
            if a == d["Roll"]:
                m1 = int(input("Enter Updated Marks"))
                file.seek(p)
                d['Marks'] = m1
                pickle.dump(d, file)
            f = 0
    except EOFError:
        file.close()


def delete():
    file = open("sms.txt", "rb")
    file1 = open("sms1.txt", "wb")
    d = {}
    d1 = {}
    f = 1
    try:
        a = int(input("Enter Roll Number"))
        while True:
            d = pickle.load(file)
            if a != d["Roll"]:
                d1 = d
                pickle.dump(d1, file1)
        f = 0
    except EOFError:
        file.close()
        file1.close()
    os.remove("sms.txt")
    os.rename("sms1.txt", "sms.txt")
    if f == 1:
        print("Sorry!! Record is not exist")


def main():
    ans = 'y'
    print("*"*100)
    print("\t\t\t\tWelcome To Student Management System")
    print("*"*100)
    while (ans != 'n'):
        print("\t\t\t\t1.Append")
        print("\t\t\t\t2.Display")
        print("\t\t\t\t3.Update")
        print("\t\t\t\t4.Delete")
        print("\t\t\t\t5.Search")
        print("\t\t\t\t6.Exit")
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