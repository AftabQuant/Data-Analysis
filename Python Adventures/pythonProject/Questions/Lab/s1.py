lst = [1,2,3,4,5,6]

def display(lst):
    print(lst)

def add_items(lst, idx, ele):
    lst[idx:idx] = [ele]
    display(lst)

def remove_items(lst, idx):
    del lst[idx]
    display(lst)
add_items(lst,2,100)
remove_items(lst, 2)
