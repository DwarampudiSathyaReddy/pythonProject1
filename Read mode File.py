fp1=open("Cse.text","r")
if fp1:
    print("File is opened successfully")
    fp1.seek(11,0)
    for i in fp1:
        print(i)
    ''' 
content=fp1.read(5)
print(content)
    '''
    fp1.close()