
class python_switch:
    def switch(self, day_of_week):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(day_of_week), lambda: default)()
 
    def case_1(self):
        return "Monday"
 
    def case_2(self):
        return "Tuesday"
 
    def case_3(self):
        return "Wednesday"
 
s = python_switch()
print(s.switch(1))
print(s.switch(0))
print(s.switch(2))
print(s.switch(3))
# -------Output-----------
# Monday
# Incorrect day
# Tuesday
# Wednesday