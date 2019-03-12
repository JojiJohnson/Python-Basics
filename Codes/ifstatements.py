 #decision making

is_male = False
is_tall = True #two boolean variables.

if is_male or is_tall:
     print("You are a male or tall or both ")
else:
     print("You are not a male or tall")

if is_male and is_tall:
    print ("you are male and tall")
elif is_male and not is_tall:
    print ("You are a male but not tall")
elif not is_male and is_tall:
    print ("You are not a male and is tall")
else:
    print ("You are not a male and not tall")



