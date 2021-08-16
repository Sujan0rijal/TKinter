'''def binary_search(list,search_item):
    min = 0
    max = len(list)-1
    while min<=max:
        mid = (min+max)//2
        if list[mid]==search_item:
            return mid
        elif list[mid]>search_item:
            max = mid-1
        else:
            min=mid+1
    return 0

l = [0,1,2,10,20,30,40,50,60]
search=int(input("enter the element number: "))
ans = binary_search(l,search)
if ans==0:
    print("element is not found")
else:
    print(f"element is found in index {ans}")'''

def linear_search(list,search_item):
    for i in range(len(list)):
        if list[i] == search_item:
            return True
    return False

l =[2,4,1,5,3,7,6,9]
item = int(input("enter the element searched: "))
ans = linear_search(l,item)
if ans:
    print("found")
else:
    print("not found")
