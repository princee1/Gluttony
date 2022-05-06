from pypresence import *
import time
applicationID='929427634373394452'
from print_cli import print_succes,print_error,print_desc
import discord 


#TODO Implemeter le discord prescence



def discordRP():
    
    #print_desc("Connecting to discord...")
    try:
        presence=Presence(applicationID)
        presence.connect()
        presence.update(
        details="Alpha Version",
        large_text="Footsites Account Generator",
        small_text="Version: 1.0.0" 
        )
        print_succes("\n * Discord Rich Presence Connected ! *\n")
    except ValueError:
        print_error("Aborting...")
    except KeyboardInterrupt:
        print_error("Aborting...")
    except:
        print_error("\n * Error while connecting to discord presence *\n")
    #time.sleep(100)

        

