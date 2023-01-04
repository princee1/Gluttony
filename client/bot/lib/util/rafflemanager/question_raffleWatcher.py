
def getRaffleChoices(listRaffle,listIndex):
    """
    It takes a list of raffle numbers and a list of indexes and returns a list of raffle that contains only 
    the ones that the user choosed
    
    :param listRaffle: The list of all the raffle choices
    :param listIndex: list of indexes of the listRaffle
    :return: A list of the raffle choices
    """
    listTemp=[]
    for x in listIndex:
        listTemp.append(listRaffle[x])
    del listRaffle
    return listTemp