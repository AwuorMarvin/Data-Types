def data_type(arg):
    if type(arg) is str:
        return len(arg)
    elif type(arg) is None:
        return 'no value'
    elif type(arg) is int:
        if arg < 100:
            return 'less than 100'
        elif arg > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    elif type(arg) is bool:
        return arg
    elif type(arg) is list:
        try:
            return arg[2]    #This exception handles the output should there be no 3rd index in the list
        except IndexError:
            return None
    else:
        return 'no value'