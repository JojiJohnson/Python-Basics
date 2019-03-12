# a class inside a class.

# We can use all the functions of a class inside another class.

# consider two classes, 'Chef' and 'Chinese_chef'. The class 'Chef' can be used inside the class 'Chinese_chef'.

from Chef import Chef
from chinese_chef import Chinese_chef

mychef = Chef()
mychef.make_special_dish()

myChinesechef = Chinese_chef()
myChinesechef.make_fried_rice()

myChinesechef.make_chicken()
