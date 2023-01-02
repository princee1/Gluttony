from discord_webhook import DiscordWebhook,DiscordEmbed
import usermanager.user_manager as user
import time

USERNAME_WEBHOOOK="Gluttony"
AVATAR_URL=""

def sendWebhook(disEmbed,webhookURL,content,id=None):
    webhook = DiscordWebhook(webhookURL,id,content,USERNAME_WEBHOOOK,AVATAR_URL
    )
    (webhook.add_embed(embed) for embed in disEmbed)
    webhook.allowed_mentions=[  
    ]
    try:
        response=webhook.execute()
    except:
        print("Failed to execute webhook")
    
    pass

def buildEmbed(title,description):
    d=DiscordEmbed(title,description )
    
    return d
    pass
