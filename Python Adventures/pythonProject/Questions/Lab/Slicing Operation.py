# lst = [1,2,3,4,5,6]
#
# def display(lst):
#     print(lst)
#
# def add_items(lst, idx, ele):
#     lst[idx:idx] = [ele]
#     display(lst)
#
# def remove_items(lst, idx):
#     del lst[idx]
#     display(lst)
# add_items(lst,2,100)
# remove_items(lst, 2)

arr = [1,2,3,4,5,6]

def display(arr):
    print(arr)
def add_items(arr,idx, ele):
    arr[idx:idx] = [ele]
    display(arr)
def remove_ele(arr, idx):
    del arr[idx]
    display(arr)

display(arr)
add_items(arr,0,100)
remove_ele(arr,4)
