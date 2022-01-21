import sys
def MERGE_SORT(list, p, r):
    if p < r:
        q =(p + r ) // 2
        MERGE_SORT(list, p, q)
        MERGE_SORT(list, q + 1, r)
        MERGE(list, p, q, r)
def MERGE(list, p, q, r):
    range1 = (q-p) + 1
    range2 = r - q
    Left = [None]*range1
    Right = [None]*range2
    for i in range(0, range1):
        Left[i] = list[p + i]
    for j in range(0, range2):
        Right[j] = list[q + 1 + j]
    i = 0
    j = 0
    k = p
    while i < range1 and j < range2:
        if Left[i] <= Right[j]:
            list[k] = Left[i]
            i += 1
        else:
            list[k] = Right[j]
            j += 1
        k += 1

    while i < range1:
        list[k] = Left[i]
        i += 1
        k += 1

    while j < range2:
        list[k] = Right[j]
        j += 1
        k += 1

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")), 3
    phone_book = []
    for i in range(rows):
        print()
        print("********************************************************************")
        print("\t\t\t\t\tEnter Contact %d Details" % (i + 1))
        print("********************************************************************")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("               Enter name: ")))
            if j == 1:
                temp.append(int(input("               Enter phone number: ")))
            if j == 2:
                temp.append(str(input("               Enter relation status: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        phone_book.append(temp)
    print("********************************************************************")
    print(phone_book)
    return phone_book


def menu():
    print("********************************************************************")
    print()
    print("\t\t\t Please Choose One Of The Following Options")
    print("********************************************************************")
    print("               1. Add a new contact")
    print("               2. Remove an existing contact")
    print("               3. Delete all contacts")
    print("               4. Search for a contact")
    print("               5. Display all contacts")
    print("               6. Exit phonebook")
    print("********************************************************************")
    choice = int(input("Please enter your choice: "))
    return choice

def add_contact(pb):
    print("********************************************************************")
    print()
    print("\t\t\t\t\tAdd New Contact Number")
    print("********************************************************************")
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("               Enter name: ")))
        if i == 1:
            dip.append(int(input("               Enter phone number: ")))
        if i == 2:
            dip.append(str(input("               Enter relation status: ")))
    pb.append(dip)
    print("********************************************************************")
    print("                      Successfully Added")
    return pb

def remove_existing(pb):
    print("********************************************************************")
    print()
    print("\t\t\t\t\tDelete A Contract Number")
    print("********************************************************************")
    print()
    query = str(input("Please enter the name: "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print("********************************************************************")
            print("            ",pb.pop(i),end=";")
            print(" Successfully Deleted")
            return pb
    if temp == 0:
        print("********************************************************************")
        print("Sorry, you have entered an invalid .Please recheck and try again later.")
        return pb
def delete_all(pb):
    print("********************************************************************")
    print()
    print("\t\t\t\t\tDelete All Contact Numbers")
    print("********************************************************************")
    print("                      Successfully Deleted")
    return pb.clear()
def search_existing(pb):
    print("********************************************************************")
    print()
    print("\t\t\t\t\tSearch A Contract Number")
    print("********************************************************************")
    print("Enter search criteria:\n.......................\n                1. Name\n                2. Phone Number\n")
    choice = int(input("Please enter: "))
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Please enter the name: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
        query = int(input("Please enter the phone number: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])

    else:
        print("********************************************************************")
        print("Invalid search criteria.",end="")
        return -1
    if check == -1:
        return -1
    else:
        display_Search(temp)
        return check
def display_Search(pb):
    print("********************************************************************")
    print("Here Information:")
    print(".................")
    for i in range(len(pb)):
        print("              ",pb[i])

def display_all(pb):
    print("********************************************************************")
    print()
    print("\t\t\t\t\tDisplay Contract Numbers")
    print("********************************************************************")

    MERGE_SORT(pb, 0,len(pb)-1)
    if not pb:
        print("List is empty: []")
    else:
        Rk = 0
        for i in range(len(pb)):
            Rk=Rk+1
            print(Rk,". ",pb[i])


def thanks():
    print("********************************************************************")
    print("  Thank You For Using Phone Book System And Please visit again!")
    print("********************************************************************")
    print()
    sys.exit("\t\t\t\t  Goodbye, have a nice day ahead!")
    print("********************************************************************")

print("********************************************************************")
print("              ***Welcome to our Phone Book system***")
print("********************************************************************")
print()
pb = initial_phonebook()
ch = 1
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("********************************************************************")
            print("The contact does not exist.Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks()