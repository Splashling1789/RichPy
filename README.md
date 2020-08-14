## Usage
This file contains some string variables with ANSI codes to change the foreground color, the background color and the text style. The variable names are composed by 2 letters followed by the name of the color/style.

- **BG_(color)** for changing the background color
- **FG_(color)** for changing the text color
- **ST_(style)** for changing the text style

If you want to reset the color and style of the text, use **RESET** string for set things back to normal

### Colors
- **BLACK**
- **RED**
- **GREEN**
- **YELLOW**
- **BLUE**
- **MAGENTA**
- **CYAN**
- **WHITE**

Also, if you add BRIGHT in before the color name, you will get the bright version of the color e.g. BG_BRIGHTRED.

### Styles
- **BOLD**
- **UNDERLINE**
- **REVERSED** (it reverse the background color with the text color)

### The ConsoleColor() method
This method will require two parameters, an integer which will be the color number form 0 to 255, and a bool, that if is false the color will set in the text foreground, and if is true, will set in background. e.g. ConsoleColor(56, True) will set the color 56 to the text background

## Examples
<code>import RichPy as rp</code>
<code>print(rp.FG_BLUE + rp.ST_BOLD + "I'm Blue!" + rp.RESET)</code>

This will return the text blue and bold, and then will reset the text format

<code>import RichPy as *</code>
<code>print(BG_BRIGHTYELLOW + FG_CYAN + "The sun with the party lights..." + RESET)</code>

This will return the text cyan and the background bright yellow and then will reset the text format
