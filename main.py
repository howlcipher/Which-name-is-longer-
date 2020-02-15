#the first name entered
first_Name = str(input("Type the first name: "))

#the second name entered
second_Name = str(input("Type the second name: "))


#compares the names in length
def compare_Names(f, s):
    #f is longer
    if len(f) > len(s):
        print(
            "{}'s name is longer.  {} is {} character(s) long, while {} is only {} character(s) long."
            .format(f, f, len(f), s, len(s)))

    #they are the same length
    elif len(f) == len(s):
        print(
            "{} and {} are both the same length.  They are {} character(s) long.".
            format(f, s, len(s)))
    #second name is longer
    else:
        print(
            "{}'s name is longer.  {} is {} character(s) long, while {} is only {} characters long."
            .format(s, s, len(s), f, len(f)))


#takes two strings
compare_Names(first_Name, second_Name)
