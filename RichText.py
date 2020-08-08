def ConsoleColor(color, IsBG):
    if IsBG == False:
        return "\u001b[38;5;" + str(color) + "m"
    elif IsBG == True:
        return "\u001b[48;5;" + str(color) + "m"
FG_BLACK = "\u001b[30m"
FG_RED = "\u001b[31m"
FG_GREEN = "\u001b[32m"
FG_YELLOW = "\u001b[33m"
FG_BLUE = "\u001b[34m"
FG_MAGENTA = "\u001b[35m"
FG_CYAN = "\u001b[36m"
FG_WHITE = "\u001b[37m"
FG_BRIGHTBLACK = "\u001b[30;1m"
FG_BRIGHTRED = "\u001b[31;1m"
FG_BRIGHTGREEN = "\u001b[32;1m"
FG_BRIGHTYELLOW = "\u001b[33;1m"
FG_BRIGHTBLUE = "\u001b[34;1m"
FG_BRIGHTMAGENTA = "\u001b[35;1m"
FG_BRIGHTCYAN = "\u001b[36;1m"
FG_BRIGHTWHITE = "\u001b[37;1m"
BG_BLACK = "\u001b[40m"
BG_RED = "\u001b[41m"
BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
BG_BLUE = "\u001b[44m"
BG_MAGENTA = "\u001b[45m"
BG_CYAN  = "\u001b[46m"
BG_WHITE = "\u001b[47m"
BG_BRIGHTBLACK = "\u001b[40;1m"
BG_BRIGHTRED = "\u001b[41;1m"
BG_BRIGHTGREEN = "\u001b[42;1m"
BG_BRIGHTYELLOW = "\u001b[43;1m"
BG_BRIGHTBLUE = "\u001b[44;1m"
BG_BRIGHTMAGENTA = "\u001b[45;1m"
BG_BRIGHTCYAN  = "\u001b[46;1m"
BG_BRIGHTWHITE = "\u001b[47;1m"
ST_BOLD = "\u001b[1m"
ST_UNDERLINE = "\u001b[4m"
ST_REVERSED = "\u001b[7m"
RESET = "\u001b[0m"