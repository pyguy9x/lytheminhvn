'''
Reverse word if length >= 6
Coded by: Ly The Minh
All rights reserved (C) July-2021
'''
def dao_nguoc(sentence):
    return ' '.join([word[::-1] if len(word) >= 6 else word for word in sentence.split(' ')])
print(dao_nguoc("We don\'t talk anymore. We don\'t walk together"))
# Output
# We don't talk .eromyna We don't walk rehtegot
