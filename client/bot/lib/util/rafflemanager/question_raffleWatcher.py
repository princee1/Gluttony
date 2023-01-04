
def getRaffleChoices(listRaffle,listIndex):
    listTemp=[]
    for x in listIndex:
        listTemp.append(listRaffle[x])
    del listRaffle
    return listTemp