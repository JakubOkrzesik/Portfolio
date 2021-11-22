import re 

message = "To be, or not to be, that is the question"

vowels = re.findall("[aeiou]",message)


print(len(vowels))