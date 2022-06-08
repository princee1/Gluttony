import os

properties='Properties.properties'
settings='Settings.json'

generalFiles=["Bulk_names.txt,user-agents.txt,Proxy.txt,Domains.txt,randomfname.txt,randomlnames.txt"]
footsitesFiles=["ActivationToken.txt,Accounts.csv,Settings.json"]    
adidasFiles=["Accounts.csv,Settings.json"]

def fileCreator(filename):
    open(f"{filename}","x")

def initFile(filename,buffer):
    pass