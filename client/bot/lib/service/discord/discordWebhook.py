from discord_webhook import DiscordWebhook,DiscordEmbed,AsyncDiscordWebhook
#import usermanager.user_manager as user
import enum

USERNAME_WEBHOOOK="Gluttony"
AVATAR_URL=""

class ColorWebhook(enum.Enum):
    pass


def sendWebhook(webhookURL,content,id=None,disEmbed=[]):
    """
    It takes a list of DiscordEmbed objects, a webhook URL, a content string, and an optional ID, and
    sends the webhook.
    
    :param disEmbed: A list of discord embeds
    :param webhookURL: The webhook URL
    :param content: The message content
    :param id: The id of the webhook
    """
    webhook = DiscordWebhook(url=webhookURL,id=id,content=content,username=USERNAME_WEBHOOOK,avatar_url=AVATAR_URL
    )
    (webhook.add_embed(embed) for embed in disEmbed)
    webhook.allowed_mentions=[  
    ]
    try:
        response=webhook.execute()
    except:
        print(response)
        print("Failed to execute webhook")
    
    pass

async def sendAsyncWebhook():
    asyncWebhook=AsyncDiscordWebhook()
    try:
        await asyncWebhook.execute()
    except:
        pass
    pass

def buildEmbed(title,description,footer=None,color:ColorWebhook=None,thumbnail=None,author:dict=None,image=None,fields=[]):
    """
    This function takes a title and description and returns a DiscordEmbed object
    
    :param title: The title of the embed
    :param description: The description of the embed
    :return: A DiscordEmbed object
    """
    disEmbded=DiscordEmbed(title,description,color=str(color) )
    disEmbded.set_author(name=author["name"],url=author["url"])
    disEmbded.set_timestamp()
    disEmbded.set_image(image)
    disEmbded.set_thumbnail(thumbnail)
    disEmbded.set_footer(footer)
    (disEmbded.add_embed_field(name=field['name'],value=field['value'])for field in fields)
    
    return disEmbded

