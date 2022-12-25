from pypresence import *
import time,discord
from print_cli import success,error,desc
import threading as td

#TEST  le discord prescence

APPLICATION_ID='929427634373394452'
MAX_RETRY=5
user_discordRP={"state":"Allo","details":"Allo","small-text":"allo","large-text":"allo"}
presence=Presence(APPLICATION_ID)

def connect_RP():
    desc("Connecting to discord...")
    count=1
    connected=False
    while (count!=MAX_RETRY):
        try:
            time.sleep(500)
            presence.connect()
            connected= True
            success("\n * Discord Rich Presence Connected ! *\n")
        except ValueError:
            error("Aborting...")
            count= 5
        except KeyboardInterrupt:
            error("Aborting...")
            count =5
        except:
            error("* Error while connecting to discord presence *")
            desc(f"Trying again{count}/{MAX_RETRY}")
            count+=1
        finally:
            pass
    else:
        pass
    return connected

def update_RP():
    SLEEP_TIME=1
    while(True):
        time.sleep(SLEEP_TIME)
        try:
            presence.update(state=user_discordRP["state"],
                        details=user_discordRP["details"],
                        large_text=user_discordRP["large_text"],
                        small_text=user_discordRP["small_text"])
        except:
            error("* Error while updating presence*\nClosing the connection...")
            presence.close()
            pass

def updateValue(key,newValue):
    user_discordRP.update(key,newValue)
    pass

def start_discordRP():
    if(connect_RP()):
        thread = td.Thread(target=update_RP,name="Update_RP")
        thread.start()
    else:
        ##Error
        pass
