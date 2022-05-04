import print_cli as cp
import pyfiglet as fig
from test import*
from discord_presence import discordRP
from mainExecutionManager import main
import subprocess as sp


bot_name = "GLUTTONY - CLI"
asterix_count = 20
fig_width = 200
fig_font = ['nipples', 'smslant', 'smisome1', 'lean', 'larry3d', 'block']
presentation=bot_name
try: 
    presentation = fig.Figlet(font='smisome1', width=200).renderText(bot_name)
except:
    pass
    
#os.system('color 1f')
cp.print_principalOption(presentation)
cp.print_desc(
    "*******************************************************************************************************************")
cp.print_desc(
    "*******************************************************************************************************************")
discordRP()
try:
    main()
except ValueError:
    cp.print_error("Aborting...")
except KeyboardInterrupt:
    cp.print_error("Aborting...")


