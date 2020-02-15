#the first name entered
first_Name = str(input("Type the first name: "))

#the second name entered
second_Name = str(input("Type the second name: "))


#compares the names in length
def compare_Names(f, s):
    #first name is longer
    if len(f) > len(s):
        dif = len(f) - len(s)
        print(
            "{}'s name is longer.  {} is {} character(s) long, while {} is only {} character(s) long.  With a difference of {}."
            .format(f, f, len(f), s, len(s), dif))

    #the names are the same length
    elif len(f) == len(s):
        print(
            "{} and {} are both the same length.  They are {} character(s) long."
            .format(f, s, len(s)))

    #second name is longer
    else:
        dif = len(s) - len(f)
        print(
            "{}'s name is longer.  {} is {} character(s) long, while {} is only {} characters long.  With a difference of {}."
            .format(s, s, len(s), f, len(f), dif))


#takes two strings and compares them by length, displays their character count, and which is the longer
compare_Names(first_Name, second_Name)
