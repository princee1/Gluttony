import win32clipboard as clip
import sys
sys.path.insert(
    1, "C:/Users/david/Documents/Gluttony Workspace/Gluttony/client/bot/lib/util/fileInterface/")
# FIXME   arranger le module not found
#from ui.print_cli import print_error,print_succes



def getDataFromClipBoard() -> str:
    """
    It opens the Windows clipboard, gets the data, empties the clipboard, and closes the clipboard
    """
    clip.OpenClipboard()
    buffer: str = clip.GetClipboardData()
    clip.EmptyClipboard()
    clip.CloseClipboard()
    #print(buffer)
    return buffer


def writeInFile(buffer: str,inputMode):
    """
    It takes a string and a mode and writes the string to a file
    
    :param buffer: The string that you want to write in the file
    :type buffer: str
    :param inputMode: This is the mode in which the file is opened
    """
    writer = open("Proxy.txt", inputMode)
    for x in buffer.split("\n"):
        x = x.strip()
        writer.write(x+"\n")
    writer.close()


def writeProxyFromClipBoard(inputmode):
    """
    It takes the data from the clipboard and writes it to a file

    :param inputmode: 
    """
    try:
        proxies = getDataFromClipBoard()
    except TypeError:
        print("Clipboard is Empty")
        pass
    else:
        writeInFile(proxies,inputmode)

