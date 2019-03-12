list1 = ["Kevin", "Tom", "Jim","Mike"]
list2 = [1,2,3,4,5,6,7,8,9,10,77,548,14]
print (list1)
print (list2)
list1.extend(list2)
print ("Extend func", list1)
list1.append("Jerry")
print ("Append func", list1)
list1.insert(3, "Oscar")
print ("Insert func", (list1)) #Inserts "Oscar" at index 3 in list1.
list2.remove (5)
list1.remove("Kevin") #removes the string "Kevin" from list1.
print (list2)
print (list1)
list1.clear() #clears every element in list1.
print ("List1",list1)
list2.pop() #eliminates the last element from list2.
print ("pop func", list2)
print (list2.index(3)) #to check weather a particular data is in the list.
list1 = ["Kevin", "Tom", "Jim","Jim","Mike"]
print (list1.count("Jim")) #counts the no of times the particular data is found in the list2.
list1.sort() #sorts in ascending order
print(list1)
list1.reverse() #reverse the list
print(list1)
list3=list1.copy() #copies the list
print(list3)







