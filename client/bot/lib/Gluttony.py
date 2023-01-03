import pyfiglet as fig

bot_name = "GLUTTONY - CLI"
asterix_count = 2
fig_font = ['nipples', 'smslant', 'smisome1', 'lean', 'larry3d', 'block']
presentation=bot_name
try: 
    presentation = fig.Figlet(font='smisome1', width=200).renderText(bot_name)
    print(presentation)
except:
    pass
    

