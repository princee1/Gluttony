

def file_to_list(file: str):
    """
    It reads a file and returns a list of the lines in the file
    
    :param file: str
    :type file: str
    :return: A list of strings.
    """
    list = []
    cpt = 0
    reader=open(file,'r')
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
    """
    It writes a list to a file
    
    :param file: The file to write to
    :type file: str
    :param data: list
    :type data: list
    :return: None
    """
    writer = open(file, "w")
    for element in data:
        writer.write(str(element)+"\n")
    writer.close()
    return None

   
def deleteElement_inFile(element:str,file:str):
    """
    It takes a string and a file name as input, and deletes all instances of the string from the file
    
    :param element: the element to be deleted
    :type element: str
    :param file: the file you want to delete the element from
    :type file: str
    """
    #raise NotImplemented
    list=file_to_list(file)
    #print(list)
    for x in range(0,list.count(element)):
        list.remove(element)
    #print(list)
    write_list(file,list)
    
def writeBufferFile(filename:str,buffer:str,inputMode):
    """
    This function takes a filename, a buffer, and an input mode, and writes the buffer to the file
    
    :param filename: The name of the file you want to write to
    :type filename: str
    :param buffer: The string to be written to the file
    :type buffer: str
    :param inputMode: The mode in which the file is opened
    """
    with open(filename,f"{inputMode}") as file:
        file.write(buffer)
        file.close()
    

