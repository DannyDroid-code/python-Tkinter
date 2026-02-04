# # importing required module
# from tkinter import *
# from gtts import gTTS

# # this module helps to
# # play the converted audio
# import os

# # create tkinter window
# root = Tk()

# # styling the frame which helps to
# # make our background stylish
# frame1 = Frame(root,bg="lightPink",height="150")

# # plcae the widget in gui window
# frame1.pack(fill=X)

# frame2 = Frame(root,bg="lightgreen",height="750")
# frame2.pack(fill=X)

# # styling the label which show the text
# # in our tkinter window
# label = Label(frame1, text="Text to Speech",font="bold, 30",bg="lightpink")

# label.place(x=180, y=70)

# # entry is used to enter the text
# entry = Entry(frame2, width=45,bd=4, font=14)

# entry.place(x=130, y=52)
# entry.insert(0, "")


# # define a function which can
# # get text and convert into audio
# def play():
#     # Language in which you want to convert
#     language = "en"

#     # Passing the text  and language,
#     # here we have  slow=False. Which tells
#     # the module that the converted audio should
#     # have a high speed

#     myobj = gTTS(text=entry.get(),lang=language,slow=False)

#     # give the name as you want to
#     # save the audio
#     myobj.save("convert.wav")
#     os.system("convert.wav")


# # cereate a button which holds
# # our play function using command = play
# btn = Button(frame2, text="SUBMIT",width="15", pady=10,font="bold, 15",
#              command=play, bg='yellow')

# btn.place(x=250, y=130)

# # give a title
# root.title("text_to_speech_convertor")

# # we can not change the size
# # if you want you can change
# root.geometry("650x550+350+200")

# # start the gui
# root.mainloop()






from tkinter import *
import speech_recognition as sr     # import the library
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *


Window= Tk()
#add title
Window.title("Speech to Text")
#add dimensions 
Window.geometry("800x400")

#heading 
heading1 = Label(Window, text = "Voice Notepad",font = "bold, 30 ")
heading1.grid(row=0,column=1,padx=20,pady=20)
#label and entry box for enter the text
#label1= Label(Window, text = "Click Button to record your speech:")
#label1.grid(row=1,column=0,padx=10)
#Text label
Output_text = Text(Window, height= 4, width = 40)
Output_text.grid(row=1,column=1,pady = 20,padx=20)

#function     
def Translate():
    r = sr.Recognizer()                 # initialize recognize
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything ")
        audio = r.listen(source)        # listen to the source
        try:
            text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        except:
            text="Sorry could not recognize your voice"
        Output_text.delete(1.0, END)
        Output_text.insert(END,text)

        
def save():
    #get file using dialog
    #default extension is optional, here will add .txt if missing
    fout=asksaveasfile(defaultextension=".txt") #if filename selected
    if fout:
        print(Output_text.get(1.0,END),file=fout)      
    else:
        messagebox.showinfo("Warning", "Text not saved")

  

# our Translate function using command = Translate 
trans_btn = Button(Window, text = 'Click on me!..\nTo start recording',
                  command = Translate,width=20)
trans_btn.grid(row=1,column=0,pady = 20,padx=20)
save_button = Button(Window, text='Save the Text',width=20,command=save)
save_button.grid(row = 1, column = 2,pady = 10,columnspan=3)
# start the gui 
Window.mainloop() 