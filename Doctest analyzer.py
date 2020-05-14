import os
import platform

# Gets the OS Name 
def getOSName(): 
    OS_Name=platform.system()
    return OS_Name



# Takes in a string that represents 
# ONE test that failed. 
def findError(block):
    # splits the block by '\n', generating. a list of lines
    
    Split=block.split('\n')
    
    # strips the white space from each line of text in the list
    
    for element in range(len(Split)):
        Split[element]=Split[element].strip()

    # Looks for the line that contains 'Error:' in the list of lines.
    # Then, parses the line number that the error occurred on (this will be 
    # two lines before the line where 'Error:' occurs).
    
    Line=""
    Line2=""
    Line3=""
    line_number=0
    for element2 in range(len(Split)):
        word_checker=Split[element2].split()
        for element3 in word_checker:
            if "Error" in element3:
                Line=Line+str(Split[element2-2])
                Line3=Line3+str(Split[element2-1])
                Line2=Line2+str(Split[element2])
   
    Split2=Line.split(",")

    for element4 in range(len(Split2)):
        Split2[element4]=Split2[element4].strip()
    for element5 in Split2:
        if "line" in element5:
            line_number=element5+":"
    
    # returns a 3-tuple in the form of: 
    # (line number, code, error_type)
    
    Error_Tuple=(line_number,Line3,Line2)
    return Error_Tuple





# A function to run the doctest in 
# the terminal. 

def runDoctest(pyfile, docFilename):
    # IMPORTANT: you should write the command-line command
    # in accordance to the operating system you're using. 
    # Use the getOSName() function in here. 
    # You will either use python or python3 based on your OS.
    
    OS_Name=getOSName()
    if OS_Name=='Windows' or OS_Name=='Linux':
        os.system("python -m doctest -v {} > {}".format(pyfile,docFilename))
    if OS_Name=='Darwin':
        os.system("python3 -m doctest -v {} > {}".format(pyfile,docFilename))


    

# reads the text file that
# contains the result of the doctest. 

def getDoctestOutput(docFilename):
    # Read in the doctest output from the file

    Doctest=open(docFilename,"r")
    if Doctest.mode == 'r': # Verify that the file was opened
        Doctest_contents = Doctest.read()

    # Splits your full doctest string by the string 'Trying:'
    
    Doctest_Split=Doctest_contents.split('Trying:')

    # Filters the errors, stores in new list

    Errors_List=[]
    Errors=[]

    for element in Doctest_Split:
        if "ok" not in element:
            Errors_List.append(element)

    for element2 in Errors_List:
        Errors.append(findError(element2))
    Errors=Errors[1:len(Errors)]

    # appends a 4-tuple in the form of: 
    # (function, line number, code, error_type)

    flag=0
    Info_List=[]
    Name=[]
    for element3 in Errors_List:
        if flag==1:
            name_finder=element3.split("(")
            Name.append(name_finder[flag-1].strip())
        else:
            flag+=1
    Info_List=[((Name[element4],Errors[element4][0],Errors[element4][1],Errors[element4][2]))for element4 in range(len(Errors))]
          
    # Returns the list of tuples
    return Info_List if Info_List!=[] else "No error"





# Displays the error in an user friendly way

def main():
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
 
    File_Name=input("Enter the python file name: ")
    Doc_Name=input("Enter the txt file to store your output in: ")
    print("\n")
    runDoctest(File_Name, Doc_Name)
    Error_info=getDoctestOutput(Doc_Name)
    if Error_info!="No error":
        runDoctest(File_Name, Doc_Name)
        Error_info=getDoctestOutput(Doc_Name)
        for element in range(len(Error_info)):
            print(color.BOLD + color.BLUE + "Error in function: " + color.UNDERLINE +Error_info[element][0] + color.END)
            print(color.BOLD + str(Error_info[element][1]),"\n\n" + color.END)
            print(color.RED + color.BOLD + "\t",str(Error_info[element][2]),"\n\n" + color.END)
            print(color.GREEN  + color.BOLD + str(Error_info[element][3]),"\n\n" + color.END)
    else:
        print("No errors found")


main()











