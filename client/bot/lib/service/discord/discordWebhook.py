from discord_webhook import DiscordWebhook,DiscordEmbed,AsyncDiscordWebhook
import usermanager.user_manager as user
import time

USERNAME_WEBHOOOK="Gluttony"
AVATAR_URL=""

def sendWebhook(disEmbed,webhookURL,content,id=None):
    """
    It takes a list of DiscordEmbed objects, a webhook URL, a content string, and an optional ID, and
    sends the webhook.
    
    :param disEmbed: A list of discord embeds
    :param webhookURL: The webhook URL
    :param content: The message content
    :param id: The id of the webhook
    """
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

async def sendAsyncWebhook():
    asyncWebhook=AsyncDiscordWebhook()
    try:
        await asyncWebhook.execute()
    except:
        pass
    pass

def buildEmbed(title,description):
    """
    This function takes a title and description and returns a DiscordEmbed object
    
    :param title: The title of the embed
    :param description: The description of the embed
    :return: A DiscordEmbed object
    """
    d=DiscordEmbed(title,description )
    
    return d
