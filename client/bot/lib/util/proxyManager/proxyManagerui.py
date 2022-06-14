import proxyClipBoard as pclip
import ui.question_ui as qui


modeDict={
    0:"a",
    1:"w"
}
listOption=["[x] - Append Proxy List","[x] - Override Proxy List"]


def main():
    try:
        modeIndex = qui.listOption("Select the update method",listOption)
    except:
        pass
    else:
        pclip.writeProxyFromClipBoard(modeDict.get(modeIndex))
        
        