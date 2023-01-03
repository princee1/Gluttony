from enum import Enum

names = "Bulk_names.txt"
domain = "Domains.txt"
proxy = "Proxy.txt"
rnd_lname = "randomlname.txt"
rnd_fname = "randomfname.txt"
user_agents="user-agents.txt"

class ModuleEnum(Enum):
    FOOTSITE=0
    ADIDAS=1
    
class WebhookEnum(Enum):
    DISCORD=0
    AYCD=1
    