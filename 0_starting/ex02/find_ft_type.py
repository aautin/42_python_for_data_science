# def all_thing_is_obj(object: any) -> int:
#     obj_type = type(object)
#     if obj_type == str:
#         print(object, "is in the kitchen :", obj_type)
#     elif obj_type == tuple:
#         print("Tuple :", obj_type)
#     elif obj_type == dict:
#         print("Dict :", obj_type)
#     elif obj_type == set:
#         print("Set :", obj_type)
#     elif obj_type == list:
#         print("List :", obj_type)
#     else:
#         print("Type not found")
#     return 42

def all_thing_is_obj(object: any) -> int:
    match object:
        case list():
            print("List :", type(object))
        case tuple():
            print("Tuple :", type(object))
        case set():
            print("Set :", type(object))
        case dict():
            print("Dict :", type(object))
        case str():
            print(object, "is in the kitchen :", type(object))
        case _:
            print("Type not found")
    return 42