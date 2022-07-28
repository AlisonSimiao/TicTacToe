import os

class GColor:  # Gnome supported
    END = "\x1b[0m"

    @staticmethod
    def RGB(R, G, B, Foreground=True):  # R: 0-255  ,  G: 0-255  ,  B: 0-255
        FB_G = 38  # Effect on foreground
        if Foreground != True:
            FB_G = 48  # Effect on background
        return "\x1b[" + str(FB_G) + ";2;" + str(R) + ";" + str(G) + ";" + str(B) + "m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_error(msg):
    print(GColor.RGB(234, 32, 84), msg, GColor.END)

def print_success(msg):
    print(GColor.RGB(0, 132, 0), msg, GColor.END)
    
def print_elemento(msg):
    print(GColor.RGB(253, 233, 16), msg, GColor.END,sep="",end="")

def print_color(r,g,b,msg):
    print(GColor.RGB(r,g,b), msg, GColor.END,sep="",end="")
    
def rows(tam):
    print()
    for i in range(0, tam):
        print_elemento("~")