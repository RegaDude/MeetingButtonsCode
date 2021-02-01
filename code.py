from tkinter import*
import webbrowser
import pickle

linksWindow = Tk()
linksWindow.geometry("250x380")
linksWindow.resizable(False,False)
#Code that sets the boxes to put the links in
meetingOneText=Label(linksWindow, text="Meeting one link")
    
meetingOneLinkEntry= Entry(linksWindow)
    

meetingOneText.grid(row=0, column=0)
meetingOneLinkEntry.grid(row=0,column=1)
    

meetingTwoText=Label(linksWindow, text="Meeting two link")



    
meetingTwoLinkEntry= Entry(linksWindow)
    
blankSpace=Label(linksWindow,text=" ")
blankSpace.grid(row=1, column=0)


meetingTwoText.grid(row=2, column=0)
meetingTwoLinkEntry.grid(row=2,column=1)
    



meetingThreeText=Label(linksWindow, text="Meeting three link")
meetingThreeText.grid(row=4, column =0)


meetingThreeLinkEntry= Entry(linksWindow)
    
blankSpace=Label(linksWindow,text=" ")
blankSpace.grid(row=3, column=0)


meetingThreeLinkEntry.grid(row=4,column=1)
    



meetingFourText=Label(linksWindow, text="Meeting four link")



    
meetingFourLinkEntry= Entry(linksWindow)
    
blankSpace=Label(linksWindow,text=" ")
blankSpace.grid(row=5, column=0)


meetingFourText.grid(row=6, column=0)
meetingFourLinkEntry.grid(row=6,column=1)
    


  
meetingFiveText=Label(linksWindow, text="Meeting five link")



    
meetingFiveLinkEntry= Entry(linksWindow)
    
blankSpace=Label(linksWindow,text=" ")
blankSpace.grid(row=7, column=0)


meetingFiveText.grid(row=8, column=0)
meetingFiveLinkEntry.grid(row=8,column=1)
    


    



meetingSixText=Label(linksWindow, text="Meeting six link")



    
meetingNameSixEntry= Entry(linksWindow)
meetingSixLinkEntry= Entry(linksWindow)
    
blankSpace=Label(linksWindow,text=" ")
blankSpace.grid(row=9, column=0)


meetingSixText.grid(row=10, column=0)
meetingSixLinkEntry.grid(row=10,column=1)
    



meetingSevenText=Label(linksWindow, text="Meeting seven link")



    

meetingSevenLinkEntry= Entry(linksWindow)
    
blankSpace=Label(linksWindow,text=" ")
blankSpace.grid(row=11, column=0)


meetingSevenText.grid(row=12, column=0)
meetingSevenLinkEntry.grid(row=12,column=1)
    


    



    




meetingEightText=Label(linksWindow, text="Meeting eight link")



    

meetingEightLinkEntry= Entry(linksWindow)
    
blankSpace=Label(linksWindow,text=" ")
blankSpace.grid(row=13, column=0)


meetingEightText.grid(row=14, column=0)
meetingEightLinkEntry.grid(row=14,column=1)
    


    
#Code that sets the link user enters to a variable
def MeetingOne():
    OpenOne = meetingOneLinkEntry.get()
    return OpenOne
def MeetingTwo():
    OpenTwo = meetingTwoLinkEntry.get()
    return OpenTwo
def MeetingThree():
    OpenThree = meetingThreeLinkEntry.get()
    return OpenThree
def MeetingFour():
    OpenFour = meetingFourLinkEntry.get()
    return OpenFour
def MeetingFive():
    OpenFive = meetingFiveLinkEntry.get()
    return OpenFive
def MeetingSix():
    OpenSix = meetingSixLinkEntry.get()
    return OpenSix
def MeetingSeven():
    OpenSeven = meetingSevenLinkEntry.get()
    return OpenSeven
def MeetingEight():
    OpenEight= meetingEightLinkEntry.get()
    return OpenEight

#Part of code that saves links into your computer
#so you can load them later
def SaveCOMMAND():
    OpenOne = MeetingOne()
    OpenTwo = MeetingTwo()
    OpenThree = MeetingThree()
    OpenFour = MeetingFour()
    OpenFive = MeetingFive()
    OpenSix = MeetingSix()
    OpenSeven = MeetingSeven()
    OpenEight = MeetingEight()
    pickle_out = open("save.pickle", "wb")
    pickle.dump({"1": OpenOne,"2":OpenTwo, "3":OpenThree,"4":OpenFour,"5":OpenFive,"6":OpenSix,"7":OpenSeven,"8":OpenEight,}, pickle_out)
    pickle_out.close 
     
def SaveCOMMANDTwo():
    OpenOne2 = MeetingOne()
    OpenTwo2 = MeetingTwo()
    OpenThree2 = MeetingThree()
    OpenFour2 = MeetingFour()
    OpenFive2 = MeetingFive()
    OpenSix2 = MeetingSix()
    OpenSeven2 = MeetingSeven()
    OpenEight2 = MeetingEight()
    pickle_out = open("saveTwo.pickle", "wb")
    pickle.dump({"1": OpenOne2,"2":OpenTwo2, "3":OpenThree2,"4":OpenFour2,"5":OpenFive2,"6":OpenSix2,"7":OpenSeven2,"8":OpenEight2,}, pickle_out)
    pickle_out.close 
    
    

def picke():
    pickle_in = open("save.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenOne = example_dict["1"]
    return OpenOne





def pickse():
    pickle_in = open("save.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenTwo = example_dict["2"]
    return OpenTwo


def pickeThree():
    pickle_in = open("save.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenThree = example_dict["3"]
    return OpenThree


def pickeFour():
    pickle_in = open("save.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenFour = example_dict["4"]
    return OpenFour


#part of code that loads in a file
def pickeFive():
    pickle_in = open("save.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenFive= example_dict["5"]
    return OpenFive

def pickeSix():
    pickle_in = open("save.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenSix= example_dict["6"]
    return OpenSix    

def pickeSeven():
    pickle_in = open("save.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenSeven= example_dict["7"]
    return OpenSeven

def pickeEight():
    pickle_in = open("save.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenEight= example_dict["8"]
    return OpenEight


def pickeTwo():
    pickle_in = open("saveTwo.pickle", "rb")
    example_dictTwo = pickle.load(pickle_in)
    OpenOne = example_dictTwo["1"]
    return OpenOne





def pickseTwo():
    pickle_in = open("saveTwo.pickle", "rb")
    example_dictTwo = pickle.load(pickle_in)
    OpenTwo = example_dictTwo["2"]
    return OpenTwo


def pickeThreeTwo():
    pickle_in = open("saveTwo.pickle", "rb")
    example_dictTwo = pickle.load(pickle_in)
    OpenThree = example_dictTwo["3"]
    return OpenThree


def pickeFourTwo():
    pickle_in = open("saveTwo.pickle", "rb")
    example_dictTwo = pickle.load(pickle_in)
    OpenFour = example_dictTwo["4"]
    return OpenFour



def pickeFiveTwo():
    pickle_in = open("saveTwo.pickle", "rb")
    example_dictTwo = pickle.load(pickle_in)
    OpenFive= example_dictTwo["5"]
    return OpenFive

def pickeSixTwo():
    pickle_in = open("saveTwo.pickle", "rb")
    example_dictTwo = pickle.load(pickle_in)
    OpenSix= example_dictTwo["6"]
    return OpenSix    

def pickeSevenTwo():
    pickle_in = open("saveTwo.pickle", "rb")
    example_dictTwo = pickle.load(pickle_in)
    OpenSeven= example_dictTwo["7"]
    return OpenSeven

def pickeEightTwo():
    pickle_in = open("saveTwo.pickle", "rb")
    example_dict = pickle.load(pickle_in)
    OpenEight= example_dict["8"]
    return OpenEight










def MeetingOneOpenTwo():
    OpenOne2 = pickeTwo()
    if OpenOne2 == "NONE":
        dummi = "1"
    else:
        webbrowser.open_new_tab(OpenOne2)

def MeetingOneOpensTwo():
    OpenTwo2 = pickseTwo()
    if OpenTwo2 == "NONE":
        dummi = "1"
    else:
        webbrowser.open_new_tab(OpenTwo2)
    

def MeetingThreeOpenTwo():
    OpenThree2 = pickeThreeTwo()
    if OpenThree2 == "NONE":
        dummi = "1"
    else:
        webbrowser.open_new_tab(OpenThree2) 


def MeetingFourOpenTwo():
    OpenFour2 =  pickeFourTwo()
    if OpenFour2 == "NONE":
        dummi = "1"
    else:
        webbrowser.open_new_tab(OpenFour2)


def MeetingFiveOpenTwo():
    OpenFive2 = pickeFiveTwo()
    if OpenFive2 == "NONE":
        dummi = "1"
    else:
        webbrowser.open_new_tab(OpenFive2)

def MeetingSixOpenTwo():
    OpenSix2 = pickeSixTwo()
    if OpenSix2 == "NONE":
        dummi = "1"
    else:
        webbrowser.open_new_tab(OpenSix2)

def MeetingSevenOpenTwo():
    OpenSeven2 = pickeSevenTwo()
    if OpenSeven2 == "NONE":
        dummi = "1"
    else:
        webbrowser.open_new_tab(OpenSeven2)


def MeetingEightOpenTwo():
    OpenEight2 = pickeEightTwo()
    if OpenEight2 == "NONE":
        dummi = "1"
    else:
        webbrowser.open_new_tab(OpenEight2)




def MeetingOneOpen():
    OpenOne = picke()
    if OpenOne == "NONE":
        dummi = "2"
    else:
        webbrowser.open_new_tab(OpenOne)

def MeetingOneOpens():
    OpenTwo = pickse()
    if OpenTwo == "NONE":
        dummi = "2"
    else:
        webbrowser.open_new_tab(OpenTwo)

def MeetingThreeOpen():
    OpenThree = pickeThree()
    if OpenThree == "NONE":
        dummi = "2"
    else:    
        webbrowser.open_new_tab(OpenThree)


def MeetingFourOpen():
    OpenFour =  pickeFour()
    if OpenFour == "NONE":
        dummi = "2"
    else:
        webbrowser.open_new_tab(OpenFour)


def MeetingFiveOpen():
    OpenFive = pickeFive()
    if OpenFive == "NONE":
        dummi = "2"
    else:
        webbrowser.open_new_tab(OpenFive)

def MeetingSixOpen():
    OpenSix = pickeSix()
    if OpenSix == "NONE":
        dummi = "2"
    else:
        webbrowser.open_new_tab(OpenSix)

def MeetingSevenOpen():
    OpenSeven = pickeSeven()
    if OpenSeven == "NONE":
        dummi = "2"
    else:
        webbrowser.open_new_tab(OpenSeven)


def MeetingEightOpen():
    OpenEight = pickeEight()
    if OpenEight == "NONE":
        dummi = "2"
    else:
        webbrowser.open_new_tab(OpenEight)



def MeetingsWindow():
    
    buttons = Tk()
    day = Label(buttons, text="A Day")
    Buttonone = Button(buttons,text="1", command=MeetingOneOpen)
    ButtonTwo = Button(buttons,text="2", command=MeetingOneOpens)
    ButtonThree = Button(buttons, text="3", command=MeetingThreeOpen)
    ButtonFour = Button(buttons, text="4", command=MeetingFourOpen)
    ButtonFive = Button(buttons, text="5", command=MeetingFiveOpen)
    ButtonSix = Button(buttons, text="6",command=MeetingSixOpen)
    ButtonSeven = Button(buttons, text = "7", command=MeetingSevenOpen)
    ButtonEight = Button(buttons,text= "8", command=MeetingEightOpen)
    day.pack(fill = X)
    Buttonone.pack(fill=X)
    ButtonTwo.pack(fill=X)
    ButtonThree.pack(fill=X)
    ButtonFour.pack(fill=X)
    ButtonFive.pack(fill=X)
    ButtonSix.pack(fill=X)
    ButtonSeven.pack(fill=X)
    ButtonEight.pack(fill=X)
    buttons.mainloop()
    

def MeetingsWindowTwo():
    
    buttonsTwo = Tk()
    day = Label(buttonsTwo,text="B Day")
    Buttonone = Button(buttonsTwo,text="1", command=MeetingOneOpenTwo)
    ButtonTwo = Button(buttonsTwo,text="2", command=MeetingOneOpensTwo)
    ButtonThree = Button(buttonsTwo, text="3", command=MeetingThreeOpenTwo)
    ButtonFour = Button(buttonsTwo, text="4", command=MeetingFourOpenTwo)
    ButtonFive = Button(buttonsTwo, text="5", command=MeetingFiveOpenTwo)
    ButtonSix = Button(buttonsTwo, text="6",command=MeetingSixOpenTwo)
    ButtonSeven = Button(buttonsTwo, text = "7", command=MeetingSevenOpenTwo)
    ButtonEight = Button(buttonsTwo,text= "8", command=MeetingEightOpenTwo)
    day.pack(fill = X)
    Buttonone.pack(fill=X)
    ButtonTwo.pack(fill=X)
    ButtonThree.pack(fill=X)
    ButtonFour.pack(fill=X)
    ButtonFive.pack(fill=X)
    ButtonSix.pack(fill=X)
    ButtonSeven.pack(fill=X)
    ButtonEight.pack(fill=X)
    buttonsTwo.mainloop()
    
    



def purify():
    SaveCOMMAND()
    picke()

def purifyTwo():
    SaveCOMMANDTwo()
    pickeTwo()


SaveOneButton= Button(linksWindow, text="Save 1", command=purify)
SaveOneButton.place(relx=0.101,rely=0.88)


LoadOneButton= Button(linksWindow, text="Load 1", command=MeetingsWindow)
LoadOneButton.place(relx=0.28,rely=0.88)

SaveOneButton= Button(linksWindow, text="Save 2", command=purifyTwo)
SaveOneButton.place(relx=0.469,rely=0.88)


LoadOneButton= Button(linksWindow, text="Load 2", command=MeetingsWindowTwo)
LoadOneButton.place(relx=0.645,rely=0.88)
































linksWindow.mainloop()








