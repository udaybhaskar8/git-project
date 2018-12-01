def introduce(name, age=0):
    msg = "My name is %s. " % name

    if age == 0:
       msg += "My age is secret."
    else:
       msg += "I am %s years old." % age
    return msg 
print(introduce('uday', 20))
print(introduce('rahul dravid'))