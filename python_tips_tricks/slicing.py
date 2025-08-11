numbers= [23,43,23,1,78,43,54,53,34]
# print(numbers[::-3])

lastfour = slice(-4,None)
print(numbers[lastfour])

firstfour = slice(4)
print(numbers[firstfour])

everyother = slice(0,None,2)
print(numbers[everyother])

something = slice(2,7,2)
print(numbers[something])

mytext = "hello world how are you?"
print(mytext[something])