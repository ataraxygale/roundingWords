

# your one-liner here to get just the first half (rounded down)

import math

word=input('Enter your word here to be halved and output: \n')

#length halved with math.floor
lenHalf=(len(word))/2
roundedDown=math.floor(lenHalf)

#list to create index of word
wordIndex=list(word)

#Prints first half of word as a list
print("As a list: ", wordIndex[:roundedDown])

#Prints first half of word as a string
print("As a string: ", word[:roundedDown])

#Prints second half of word as a list
print("As a list: ", wordIndex[roundedDown:])

#Prints second half of sowrd as a string
print("As a string: ", word[roundedDown:])







