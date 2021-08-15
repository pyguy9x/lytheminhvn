# from termcolor import colored, cprint
# cprint('Hello, World!', 'green', 'on_blue')

# BLUE = '34m'
# HEADER = '95m'
# OKBLUE = '94m'
# OKCYAN = '96m'
# OKGREEN = '92m'
# WARNING = '93m'
# FAIL = '91m'
# ENDC = '0m'
# BOLD = '1m'
# UNDERLINE = '4m'
#colors
ResetAll = "0m"

Bold       = "1m"
Dim        = "2m"
Underlined = "4m"
Blink      = "5m"
Reverse    = "7m"
Hidden     = "8m"

ResetBold       = "21m"
ResetDim        = "22m"
ResetUnderlined = "24m"
ResetBlink      = "25m"
ResetReverse    = "27m"
ResetHidden     = "28m"

Default      = "39m"
Black        = "30m" 
# BrightBlack = "30;1m" => ;1 <=> Brighten color
Red          = "31m"
Green        = "32m"
Yellow       = "33m"
Blue         = "34m"
Magenta      = "35m"
Cyan         = "36m"
LightGray    = "37m"
DarkGray     = "90m"
LightRed     = "91m"
LightGreen   = "92m"
LightYellow  = "93m"
LightBlue    = "94m"
LightMagenta = "95m"
LightCyan    = "96m"
White        = "97m"

BackgroundBlack = '40m'
BackgroundRed = '41m'
BackgroundGreen = '42m'
BackgroundYellow = '43m'
BackgroundBlue = '44m'
BackgroundBlueBold = '92;1m\033[1m'
BackgroundMagenta = '45m'
BackgroundCyan = '46m'
BackgroundWhite = '47m'
message = 'hello friends'

White_bgBlue = '44;1m\033[97m' # Text: white, Background: blue
White_bgViolet = '44;1m\033[45m' # Text: white, Background: violet
White_bgCyan = '44;1m\033[46m' # Text: white, Background: cyan
White_bgGray = '44;1m\033[47m' # Text: white, Background: gray
# dct = display color text
def dct(color, text): 
    colored_text = f"\033[{color}{text}\033[{ResetAll}"
    return colored_text


# print(dct(BackgroundBlue, message))
print(dct(BackgroundBlueBold, message))
print(dct(White_bgBlue, "Helo"))
print(dct(White_bgCyan, "Helo"))
print(dct(White_bgViolet, "Helo"))
print(dct(White_bgGray, "Helo"))

print("\033[34;1m Những màu sắc rực rỡ \033[0m") # Blue
print("\033[44;1m\033[97m Những màu sắc rực rỡ \033[0m") # Blue bg
print("\033[44;1m\033[45m Những màu sắc rực rỡ \033[0m") # Violet bg
print("\033[44;1m\033[46m Những màu sắc rực rỡ \033[0m") # Cyan bg
print("\033[44;1m\033[47m Những màu sắc rực rỡ \033[0m") # Gray bg

print("\033[1m BOLD \033[0m\033[4m Underline \033[0m\033[7m Reversed \033[0m") # Bold underline revesed