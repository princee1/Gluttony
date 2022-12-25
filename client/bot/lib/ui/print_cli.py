from clint.textui import indent, colored, puts, puts_err

def error(value,newLine:bool=True):
    '''
    Color: Red
    '''
    puts_err(colored.red(string=value),newLine)

def success(value,newLine:bool=True):
    '''
    Color: Green
    '''
    puts(colored.green(string=value),newLine)

def desc(value,newLine:bool=True):
    '''
    Color: White
    '''
    puts(colored.white(string=value),newLine)

def status(value,newLine:bool=True):
    '''
    Color: Cyan
    '''
    puts(colored.cyan(value),newLine)

def print_principalOption(value,newLine:bool=True):
    '''Color: Magenta'''
    puts(option(value),newLine)

def print_info(value,newLine:bool=True):
    '''
    Color: Yellow
    '''
    puts(colored.yellow(value),newLine)
    

def freePrint(value,newLine:bool=True):
    puts(value,newLine)
    
    
def option(value):
    return colored.magenta(value)

def coloredString(value,color):
    return colored.ColoredString(color,value)