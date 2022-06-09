import win32clipboard as clip
from fileInterface.text_interface import writeBufferFile,proxy
buffer:str=""

def getDataFromClipBoard():
    """
    It opens the Windows clipboard, gets the data, empties the clipboard, and closes the clipboard
    """
    clip.OpenClipboard()
    buffer=clip.GetClipboardData()
    clip.EmptyClipboard()
    clip.CloseClipboard()
    print(buffer)
    return buffer
    
def writeProxyFromClipBoard():
    proxies=getDataFromClipBoard()
    writeBufferFile(proxy,proxies,"w")
    pass

def writeProxyFromClipBoardAppend():
    proxies=getDataFromClipBoard()
    writeBufferFile(proxy,proxies,"a")
    pass

getDataFromClipBoard()
