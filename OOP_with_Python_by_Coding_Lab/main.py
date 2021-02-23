import pickle


def create(todolist):
    item = input('What do you need to do? ')
    todolist.append(item)


def display(todolist):
    print('Your to do list: ')
    for i in range(len(todolist)):
        print(str(i+1) + '. ' + todolist[i])


def delete(todolist):
    display(todolist)
    try:
        position = int(input('Which item number do you want to delete? '))
        del todolist[position - 1]
        display(todolist)
    except:
        print('Invalid item number')


try:
    myFile = open('todolist.pickle', 'rb')
    myList = pickle.load(myFile)
    myFile.close()
except:
    myList = []
command = ''
while command != 'exit':
    command = input('''What would you like to do
                    C - create new item
                    V - view to do list
                    D - delete existing item
                    exit - exit the program
>>> ''')
    if command == 'C':
        create(myList)
    elif command == 'V':
        display(myList)
    elif command == 'D':
        delete(myList)
    elif command == 'exit':
        print('Have a nice day')
        myFile = open('todolist.pickle', 'wb')
        pickle.dump(myList, myFile)
        myFile.close()
    else:
        print('Invalid command')
