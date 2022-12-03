bookList = list()

menu = """
[1] Add book
[2] Take out book
[3] List the books
[Q] Exıt
"""

def addBook(book, list):
    list += [book]
    print("Book added")
    input("Press 'enter' for main menu.")

def takeOutBook():
    pass

def toList(list):
    for i in list:
        print("Book name  ------>>>>   {}".format(i))

    input("Press 'enter' for main menu.")

def exit():
    quit()

while True:
    print(menu)

    choice=input("What is your choice?: ")

    if choice=="1":
        bookName = input("Book name: ")
        addBook(bookName, bookList)

    elif choice=="2":
        takeOutBook()


    elif choice=="3":
        toList(bookList)

    elif choice == "q" or choice == "Q" :
        exit()

    else:
        print("You entered incorrectly.")
        input("Press 'enter' for main menu.")












