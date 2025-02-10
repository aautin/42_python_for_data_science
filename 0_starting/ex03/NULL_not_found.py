def NULL_not_found(object: any) -> int:
    if type(object) is type(None):
        print("Nothing: None", type(object))
    elif type(object) is float and str(object) == "nan":
        print("Cheese: nan", type(object))
    elif type(object) is int and object == 0:
        print("Zero: 0", type(object))
    elif type(object) is str and object == "":
        print("Empty: ", type(object))
    elif type(object) is bool and object == False:
        print("Fake: False", type(object))
    else:
        print("Type not Found")
        return 1
    return 0