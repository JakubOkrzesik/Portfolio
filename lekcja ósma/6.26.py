import re

message = "To be, or not to be, that is the question"

words_count = re.findall("[\w-]+", message)

print(len(words_count))