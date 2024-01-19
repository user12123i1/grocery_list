#isaac Lowenstein
#shopping List Pt. 2 
#1/12/24


shoppinglist = [] 
print("""welcome to the shopping list! type in numbers 1-5 for options 
      
1. Add a task to the shopping list  
2. View the current shopping list 
3. Mark a task as completed 
4. Remove a task from the shopping list 
5. Remove all tasks from the shopping list
6. Sort the list alphabetically
7. Print the # of Items on the shopping List  
8. Exit the program  
    """)
while True: 
    choice = int(input("what do you want to do?(1-8)"))
    if choice == 1: 
        shoppinglist.append(input("add to list:"))
    if choice == 2:
        print(shoppinglist)
    if choice == 3: 
        completed = str(input("which list item have you completed?"))
        completedIndex = shoppinglist.index(completed)
        shoppinglist[completedIndex]  =  "[X]" + completed 
    if choice == 4: 
        remove = input("which list item would you like to remove?(name the exact list item!)")
        if remove in shoppinglist: 
            shoppinglist.remove(remove)
        else: 
            print("item not in list")
            remove = input("which list item would you like to remove?(name the exact list item!)")
    if choice == 5: 
        shoppinglist.clear() 
    if choice == 6: 
        shoppinglist.sort()
    if choice == 7: 
        print(len(shoppinglist))

    if choice == 8: 
        break
    if choice not in range (1,8):
        print("pick 1-8")