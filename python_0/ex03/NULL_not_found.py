def NULL_not_found(object: any) -> int:
    types = {
        type(None): [None, "Nothing:"],
        float: "Cheese:",
        int: [0, "Zero:"],
        str: ['', "Empty:"],
        bool: [False, "Fake:"]
    }
    if type(object) in types and (types[type(object)])[0] == object:
        print((types[type(object)])[1], object, type(object))
        return (0)
    elif object != object:
        print(types[float], object, type(object))
        return (0)
    else:
        print("Type not Found")
        return 1
