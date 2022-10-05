print("Write a Python program to find the elements in a given set that are not in another set.")
print("Assume 2 set on your own")
list_1=["a", "b", "c", "d", "e"]
list_2=["a", "f", "c", "m"]
list3= set(list_2) - set(list_1)
print(list3)