from file_manager import writeFile
from service.discord.discordWebhook import sendWebhook,buildEmbed
from constant import WebhookEnum
#NOTE import the aycd module

class Win():

    def __init__(self,response):
        self.deconstruct(response)
        pass
    
    def deconstruct(self,response):
        pass
    
    def toFile(self,file,buffer):
        writeFile(file,buffer,"a")
       
    def toDiscordEmbedValue() -> tuple:
        pass
    
    def toAycdValue()->tuple:
        pass
    
    def sendWebhook(self,webhook:WebhookEnum,id,url,content):
        if webhook==WebhookEnum.DISCORD:
            values=self.toDiscordEmbedValue()
            disEmbed=buildEmbed()
            sendWebhook(url,content,id,disEmbed)
            pass
        else:
            raise NotImplementedError()
            pass
        pass
    
    pass