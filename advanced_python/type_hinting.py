# checking for consistency using the mypy package module

def myfunction(myparameter: int) ->int:
    return myparameter + 23
def otherfunction(otherparameter :str):
    print(otherparameter)
otherfunction(myfunction(23))

# hint on returning a list of integers
def dosth(param:list[int]):
    pass