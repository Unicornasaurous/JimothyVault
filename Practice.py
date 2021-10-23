from random import *
def find_index(l1, element):
    counter = -1
    numbois = []
    for index in l1:
        counter += 1
        if element == index:
            numbois.append(counter)
    return numbois

def find_number(l1, loc):
    counter2 = -1
    for index2 in l1:
        counter2 += 1
        if counter2 == loc:
             return index2
    
start_over = True

while start_over:
    def random_list_maker():
        random_list = []
        for i in range(10):
            n = randint(1, 10)
            random_list.append(n)
        return random_list
    listboi = random_list_maker()
    array_counter = -1
    print("There is an array of random numbers. The numbers go as followed: ")
    for rando in listboi:
        array_counter += 1
        print(str(array_counter) + ")" + " " + str(rando))

    choice = input("Would you like to know the index(location) of one of the numbers? y or n: ")

    repeat = True
    index = False
    index_number = False
    repeat2 = True
    repeat_counter = 0
    repeat_counter2 = 0

    while repeat:
        repeat_counter += 1
        if repeat_counter > 1:
            repeat_counter = 0
            choice = input("Learn English damnit. y or n: ")
        elif choice == "y":
            num = int(input("Which number? "))
            index = True
            repeat = False
        elif choice == "n":
            repeat = True
            choice2 = input("Would you like to know the number in a specific index? y or n: ")
            while repeat:
                repeat_counter2 += 1
                if repeat_counter2 > 1:
                    repeat_counter2 = 0
                    choice2 = input("Learn English damnit. y or n: ")
                elif choice2 == "y":
                    num2 = int(input("What index? "))
                    index_number = True
                    repeat = False
                elif choice2 == "n":
                    print("Okay. Have a nice day.")
                    repeat = False
                elif choice2 != "y" or "n":
                    repeat = True
        elif choice != "y" or "n":
            repeat = True
    
    repeat = True

    if index:
        result1 = find_index(listboi, num)
        print("The index of this number is: " + str(result1))
    elif index_number:
        result2 = find_number(listboi, num2)
        print("The number of this index is: " + str(result2))
    
    while repeat2:
        again = input("Do you want to start the script over? y or n:")
        if again == "y":
            repeat2 = False
            start_over = True
        if again == "n":
            print("Have a nice day.")
            exit()
        elif again != "y" or "n":
            print("Learn English damnit.")
        
