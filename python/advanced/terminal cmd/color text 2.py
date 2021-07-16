import sys, time
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        # print(code)
    print(u"\u001b[0m")

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")

print(u"\u001b[1m BOLD \u001b[0m\u001b[4m Underline \u001b[0m\u001b[7m Reversed \u001b[0m")
print(u"\u001b[1m\u001b[31m Red Bold \u001b[0m")
print(u"\u001b[4m\u001b[44m Blue Background Underline \u001b[0m")
def loading():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
    
loading()

def loading():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.01)
        width = int((i + 1) / 4)
        bar = "[" + "#" * width + " " * (25 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print()
    
loading()