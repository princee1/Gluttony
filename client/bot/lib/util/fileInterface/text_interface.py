from util import to_path

names = "Bulk_names.txt"
domain = "Domains.txt"
proxy = "Proxy.txt"
rnd_lname = "randomlname.txt"
rnd_fname = "randomfname.txt"
email = "Emails to confirm.txt"
user_agents="user-agents.txt"


def file_to_list(file: str):
    list = []
    cpt = 0
    reader=open(to_path(file),'r')
    for x in reader:
        size = len(x)
        #if cpt != 0:
        #   size -= 1
        size-=1
        list.append(x[0:size])
        cpt += 1
    reader.close()
    
    return list

def write_list(file: str, data: list):
    writer = open(to_path(file), "w")
    for element in data:
        writer.write(str(element)+"\n")
    writer.close()
    return None

def deleteElement_inFile(element:str,file:str):
    #raise NotImplemented
    list=file_to_list(file)
    
    #print(list)
    for x in range(0,list.count(element)):
        list.remove(element)
    #print(list)
    write_list(file,list)
    


#deleteElement_inFile('''JMFbVH50XMWSD7JSeLxAF88CPIT9GWbAP7Op5BE2ZIA/kIQhWVsTquWsdW7puzmB3g77glWWglAwlq8/TwPDw2kSXQ1GFAqAkFhid8Jyd0foeCNx+3r66oKGDnmjMa3QOKbOU9uA89BK4jmVUym24Tq/lS8/mUF1eZPg32XnzGs=''',email)
