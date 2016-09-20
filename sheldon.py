# make a list 
my_list = []

# usage
print("What should we pick up at the store")
print("Enter DONE to stop adding items")

while True:
    # ask for new items
    new_item = input("> ")
   

    if new_item == 'DONE':
        break

    # add new items to our list
    my_list.append(new_item)






# print

print("List")
for item in my_list:
    print(item)
