import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, ttk
import os
import random
import pandas as pd

root = tk.Tk()
root.title("My Drama Tracker")
root.resizable(False,False)
root.geometry('800x800')

#GLOBALS
#globals for adding drama
add_name = tk.StringVar()
add_lang = tk.StringVar()
add_lang.set('Passed')
#globals for removeing drama
remove = tk.StringVar()
remove.set('Passed')
#globals for sorting watched dramas
sort1 = tk.IntVar()
sort2 = tk.IntVar()
sort3 = tk.IntVar()
#globals for adding finished drama
finished_name = tk.StringVar()
finished_lang = tk.StringVar()
finished_lang.set('Passed')
#globals for moving finished drama
move = tk.StringVar()
move.set('Passed')
#global for rating
rate = tk.StringVar(value=0)


#FUNCTIONS
#function to get random drama from entire list
def getRand():
    dramas = pd.read_csv("dramas.csv")
    drama = random.choice(dramas.loc[:,"Name"])
    pick.config(text=drama)

#function to move drama from "to-watch" to "finished"
def finished():
    pass

#function to display the "to-watch" list
def toWatchDisplay():
    for widget in leftframe.winfo_children():
        widget.destroy()
    leftframe.place_forget()
    
    leftframe.config(width=350, height=570)
    leftframe.place(anchor="nw",x=0,y=30)
    toWatchLabel = tk.Label(leftframe, text="Dramas To Watch: ", bg="mistyrose1",
                        font=10)
    toWatchLabel.place(anchor="nw", x=0, y=0)
    
    dramas = pd.read_csv("dramas.csv")
    for x, drama in enumerate(dramas.loc[:,"Name"]):
        height = (x*17) + 30
        temp = tk.Label(leftframe, text=drama, bg="mistyrose1")
        temp.place(anchor="nw", x=5, y=height)

#add drama functionality ("to-watch")
    #function to display add drama menu for "to-watch"
def addDramaFrame():
    addDrama_frame.place(anchor="nw", x=0, y=30)
    addDrama_frame.config(width=260, height=130)
    
    #name entry
    entry_label1 = tk.Label(addDrama_frame, text="Name: ", bg="mistyrose4")
    entry_label1.place(anchor="nw", y=10, x=10, width=60)
    
    entry1 = tk.Entry(addDrama_frame, textvariable=add_name)
    entry1.place(anchor="nw", y=10, x=80, width=150)
    
    entry_label2 = tk.Label(addDrama_frame, text="Language: ", bg="mistyrose4")
    entry_label2.place(anchor="nw", y=40, x=10, width=60)
    
    #lang entry
    langs = ["Korean", "Japanese", "Chinese", "Thai"]
    for i, x in enumerate(langs):
        opt = tk.Radiobutton(addDrama_frame, text=x, variable=add_lang,
                             value=x, bg="mistyrose4")
        if i == 0: opt.place(anchor="nw", x=80, y=40)
        if i == 1: opt.place(anchor="nw", x=80, y=60)
        if i == 2: opt.place(anchor="nw", x=150, y=40)
        if i == 3: opt.place(anchor="nw", x=150, y=60)
    
    #submit button
    add_button = tk.Button(addDrama_frame, text="Confirm", bg="white", fg="black",
                           command=addDrama, cursor="hand2")
    add_button.place(anchor="ne", y=100, x=235, height=20)
    
    #clear entry
    entry1.delete(0, END)
    
    #function to add drama from "to-watch"
def addDrama():
    name=add_name.get()
    if name == "":
        displayAddErrorFrame()
        return
    lang=add_lang.get()
    if lang == "Passed":
        displayAddErrorFrame()
        return
    if lang == "Korean": lang="K"
    elif lang == "Japanese": lang="J"
    elif lang == "Chinese": lang="C"
    elif lang == "Thai": lang="T"
    data = {
        'Name': [name],
        'Lang': [lang]
    }
    newDrama = pd.DataFrame(data)
    newDrama.to_csv("dramas.csv", mode='a', index=False, header=False)
    addDrama_frame.place_forget()
    toWatchDisplay()
    
    #function to display error message for add drama input
def displayAddErrorFrame():
    add_err.place(anchor="center", x=350, y=350)
    add_err.config(width=200, height=100)
    
    error_label = tk.Label(add_err, text="Please complete all fields.", font="Ariel 10 bold",
                           bg="white")
    error_label.place(anchor="center", x=100, y=40)
    
    accept_button = tk.Button(add_err, text="Okay", bg="mistyrose4", command=removeErrFrame)
    accept_button.place(anchor="se", x=190, y=90, width=40)
    
    #function to remove the error frame
def removeErrFrame():
    add_err.place_forget()

#remove drama functionality
    #function to display remove drama menu for "to-watch"
def removeDramaFrame():
    for widget in removeDrama_frame.winfo_children():
        widget.destroy()
    removeDrama_frame.place(anchor="nw", x=0, y=30)
    removeDrama_frame.config(width=350, height=570)
    
    dramas = pd.read_csv("dramas.csv")
    for x, drama in enumerate(dramas.loc[:,"Name"]):
        height = (x*20) + 5
        button = Radiobutton(removeDrama_frame, text=drama, variable=remove,
                             value=drama, bg="mistyrose2",
                             anchor=N)
        button.place(anchor="nw", x=5, y=height)
        
    submit_button = tk.Button(removeDrama_frame, text="Confirm",
                              bg="white", command=removeDrama, cursor="hand2")
    submit_button.place(anchor="se", x=340, y=560, width=60, height=30)

    #function to remove drama from "to-watch"
def removeDrama():
    dramas = pd.read_csv("dramas.csv")
    to_remove = remove.get()
    for x, drama in enumerate(dramas.loc[:,"Name"]):
        if drama == to_remove:
            dramas = dramas.drop(dramas.index[x])
    dramas.to_csv("dramas.csv", mode='w', index=False)
    removeDrama_frame.place_forget()
    toWatchDisplay()

# PLACEHOLDER
def sortDramas():
    pass

#function to display "finished" dramas


#add drama functionality ("finished")
    #function to display the add to finished list window
def addFinishedFrame():
    addFinished_frame.place(anchor="nw", x=350, y=30)
    addFinished_frame.config(width=300, height=180)
    
    enterLabel = tk.Label(addFinished_frame, text="Complete Fields: ", bg="mistyrose4",
                           font="Heltica 10 bold")
    enterLabel.place(anchor="nw", x=0, y=0)
    
    name_label = tk.Label(addFinished_frame, text="Name: ", bg="mistyrose4")
    name_label.place(anchor="nw", y=25, x=10, width=60)
    
    dramaname = tk.Entry(addFinished_frame, textvariable=finished_name)
    dramaname.place(anchor="nw", y=25, x=80, width=150)
    
    lang_label = tk.Label(addFinished_frame, text="Language: ", bg="mistyrose4")
    lang_label.place(anchor="nw", y=55, x=10, width=60)
    
    langs = ["Korean", "Japanese", "Chinese", "Thai"]
    for i, x in enumerate(langs):
        opt = tk.Radiobutton(addFinished_frame, text=x, variable=finished_lang,
                             value=x, bg="mistyrose4")
        if i == 0: opt.place(anchor="nw", x=80, y=55)
        if i == 1: opt.place(anchor="nw", x=80, y=75)
        if i == 2: opt.place(anchor="nw", x=150, y=55)
        if i == 3: opt.place(anchor="nw", x=150, y=75)
        
    submit = tk.Button(addFinished_frame, text="Confirm", bg="white",
                       command=ratingFrameForAdd)
    submit.place(anchor="nw", x=220, y=95, height=20)
    
    or_label = tk.Label(addFinished_frame, text="OR", bg="mistyrose4", font="Heltica 10 bold")
    or_label.place(anchor="center", x=150, y=130)
    
    choose = tk.Button(addFinished_frame, text='Choose From "To-Watch"', bg="white",
                       command=moveToFinishedFrame)
    choose.place(anchor="center", x=150, y=155, height=20)
    
    dramaname.delete(0, END)
 
    #function to display the options to move from "to-watch" to "finished" window
def moveToFinishedFrame():
    addFinished_frame.place_forget()
    
    for widget in removeDrama_frame.winfo_children():
        widget.destroy()
    
    move_frame.place(anchor="nw", x=0, y=30)
    move_frame.config(width=350, height=570)
    
    dramas = pd.read_csv("dramas.csv")
    for x, drama in enumerate(dramas.loc[:,"Name"]):
        height = (x*20) + 5
        button = Radiobutton(move_frame, text=drama, variable=move,
                             value=drama, bg="mistyrose4",
                             anchor=N)
        button.place(anchor="nw", x=5, y=height)
        
    submit_button = tk.Button(move_frame, text="Confirm",
                              bg="white", command=ratingFrameForMove, cursor="hand2")
    submit_button.place(anchor="se", x=340, y=560, width=60, height=30)
    
    #function to add drama to finished and remove from "to-watch" if needed
def addFinishedDrama():
    rating_frame.place_forget()
    addFinished_frame.place_forget()
    
    name=finished_name.get()
    if name == "":
        displayAddErrorFrame()
        return
    
    dramas = pd.read_csv("dramas.csv")
    for x, drama in enumerate(dramas.loc[:,"Name"]):
        if drama == name:
            dramas = dramas.drop(dramas.index[x])
    dramas.to_csv("dramas.csv", mode='w', index=False)
    
    lang=finished_lang.get()
    if lang == "Passed":
        displayAddErrorFrame()
        return
    if lang == "Korean": lang="K"
    elif lang == "Japanese": lang="J"
    elif lang == "Chinese": lang="C"
    elif lang == "Thai": lang="T"
    
    r=rate.get()
    data = {
        'Name': [name],
        'Lang': [lang],
        'Rating': [r]
    }
    finishedDrama = pd.DataFrame(data)
    finishedDrama.to_csv("finished.csv", mode='a', index=False, header=False)
    
    toWatchDisplay()
    
    #function to move drama from "to-watch" to "finished"
def moveDrama():
    rating_frame.place_forget()
    move_frame.place_forget()
    #remove from "to-watch"
    name = move.get()
    lang = None
    dramas = pd.read_csv("dramas.csv")
    for x, drama in enumerate(dramas.loc[:,"Name"]):
        if drama == name:
            lang = dramas.iloc[x]["Lang"]
            dramas = dramas.drop(dramas.index[x])
    dramas.to_csv("dramas.csv", mode='w', index=False)
    
    #add to "finished"
    r = rate.get()
    if lang == "Korean": lang="K"
    elif lang == "Japanese": lang="J"
    elif lang == "Chinese": lang="C"
    elif lang == "Thai": lang="T"
    data = {
        'Name': [name],
        'Lang': [lang],
        'Rating': [r]
    }
    finishedDrama = pd.DataFrame(data)
    finishedDrama.to_csv("finished.csv", mode='a', index=False, header=False)
    
    toWatchDisplay()

    #function to display window to ask for rating from addFinishedFrame
def ratingFrameForAdd():
    rating_frame.place(anchor="center", x=400, y=450)
    rating_frame.config(width=200, height=100)
    
    name = finished_name.get()
    title_label = tk.Label(rating_frame, text="Rate "+name, bg="white")
    title_label.place(anchor="center", x=100, y=20)

    rating_box = ttk.Spinbox(rating_frame, from_=0, to=10, textvariable=rate,
                             wrap=True)
    rating_box.place(anchor="center", x=100, y=50)
    
    submit = tk.Button(rating_frame, text="Confirm", bg="mistyrose4",
                       command=addFinishedDrama)
    submit.place(anchor="center", x=100, y=80, height=25)

    #function to display window to ask for rating from moveToFinishedFrame
def ratingFrameForMove():
    rating_frame.place(anchor="center", x=400, y=450)
    rating_frame.config(width=200, height=100)
    
    name = finished_name.get()
    title_label = tk.Label(rating_frame, text="Rate "+name, bg="white")
    title_label.place(anchor="center", x=100, y=20)

    rating_box = ttk.Spinbox(rating_frame, from_=0, to=10, textvariable=rate,
                             wrap=True)
    rating_box.place(anchor="center", x=100, y=50)
    
    submit = tk.Button(rating_frame, text="Confirm", bg="mistyrose4",
                       command=moveDrama)
    submit.place(anchor="center", x=100, y=80, height=25)


# basic layout
base = tk.Frame(root, width=800, height=800, bg="black")
base.place(relwidth=1, relheight=1)

frame1 = tk.Frame(base, bg="white", width=700, height=700)
frame1.place(relx=.5, rely=.5, anchor="center")


    ## generating screen at bottom
bottomframe = tk.Frame(frame1, bg="mistyrose3", width=700, height=100,
                       highlightbackground="black", highlightthickness=2)
bottomframe.place(anchor="sw", x=0, y=700)

generate_button = tk.Button(bottomframe, text="Generate", bg="mistyrose4", 
                            font="Dotum 10", command=getRand, cursor="hand2")
generate_button.place(anchor="sw", y=100, x=0, height=100, width=200)

pick = tk.Label(bottomframe, text=None, bg="mistyrose3", fg="black",
                font="Dotum 15")
pick.place(anchor="s", y=75, x=450, width=400, height=45)



    ## top options bar
topframe = tk.Frame(frame1, bg="black", width=700, height=30,
                    highlightbackground="black", highlightthickness=2)
topframe.place(anchor="nw", y=0, x=0)

add_button = tk.Button(topframe, text="Add Drama", bg="mistyrose4",
                       command=addDramaFrame, cursor="hand2")
add_button.place(width=175, anchor="nw", x=0)

remove_button = tk.Button(topframe, text="Remove Drama", bg="mistyrose4",
                          command=removeDramaFrame, cursor="hand2")
remove_button.place(width=175, x=175)

finished_button = tk.Button(topframe, text="Add Finished Drama", bg="mistyrose4", 
                            command=addFinishedFrame , cursor="hand2")
finished_button.place(width=150, x=350)

sort_menu = tk.Menubutton(topframe, text="Sort by: ", bg="mistyrose4", cursor="hand2")
sort_menu.menu = tk.Menu(sort_menu, tearoff="off")
sort_menu["menu"] = sort_menu.menu
sort_menu.menu.add_checkbutton(label="ranking", variable=sort1,
                               activebackground="mistyrose3")
sort_menu.menu.add_checkbutton(label="reversed ranking", variable=sort2,
                               activebackground="mistyrose3")
sort_menu.menu.add_checkbutton(label="none", variable=sort3, 
                               activebackground="mistyrose3")
sort_menu.place(anchor="w", width=200, height=25, x=500, y=12)


    ## "to-watch" frame
leftframe = tk.Frame(frame1, highlightbackground="black", 
                     highlightthickness=1, bg="mistyrose1")
leftframe.place(anchor="nw",x=0,y=30)

toWatchDisplay()


    ## "finished" frame
rightframe = tk.Frame(frame1, highlightbackground="black", 
                     highlightthickness=1, bg="mistyrose1", width=350, height=570)
rightframe.place(anchor="nw", x=350, y=30)



    ## optional frames
addDrama_frame = tk.Frame(frame1, bg="mistyrose4",
                          highlightbackground="black", highlightthickness=2)
addDrama_frame.place(anchor="nw", x=0, y=30)

removeDrama_frame = tk.Frame(frame1, bg="mistyrose2", highlightbackground="black",
                             highlightthickness=2)
removeDrama_frame.place(anchor="nw", x=0, y=30)

add_err = tk.Frame(frame1, bg="white", highlightbackground="black", highlightthickness=2)
add_err.place(anchor="center", x=350, y=275)

addFinished_frame = tk.Frame(frame1, bg="mistyrose4", highlightbackground="black", 
                             highlightthickness=2)
addFinished_frame.place(anchor="nw", x=350, y=30)

move_frame = tk.Frame(frame1, bg="mistyrose4", highlightbackground="black", 
                             highlightthickness=2)
move_frame.place(anchor="nw", x=0, y=30)

rating_frame = tk.Frame(frame1, bg="white", highlightbackground="black", 
                             highlightthickness=2)
rating_frame.place(anchor="center", x=400, y=450)

root.mainloop()
