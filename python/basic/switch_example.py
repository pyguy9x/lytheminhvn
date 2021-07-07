def week(x):
    switcher={
        1:'Sunday',
        2:'Monday', #<< here
        3:'Tuesday',
        4:'Wednesday',
        5:'Thursday',
        6:'Friday',
        7:'Saturday'
     }
    return switcher.get(x, "nothing")
 
print(week(2))
def one():
    return "one"
 
def two():
    return "two"
 
def test(x):
    switcher = {
        1: one(),
        2: two()
    }
    return switcher.get(x, "nothing")
 
print(test(2)) # => two
print(test(4)) # => nothing
# -------Output-----------
# Monday
# two
# nothing