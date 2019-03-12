#Cteating a dictionary in Python.


monthconv = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May"
    #keys can also be numbers
}

print  (monthconv["Apr"]) #accessing the entries in the dictionary with 3 letter unique key.
print (monthconv.get("Jan")) #another way of accessing entries inside the dictionary, by which we can give a default Msg when an invalid key is entered.
print (monthconv.get("Luv", "Not a valid key"))


