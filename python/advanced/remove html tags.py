import re
def remove_html(txt):
    return re.sub(r'<[^>]*>', '', txt)
 
txt = "<p class=\"par\">This is an example</p>"
print(remove_html(txt))
# output
# This is an example