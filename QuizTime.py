#Lucas Huls & Jasper Tempelman - QuizTime ©
import tkinter as tk

root = tk.Tk()
root.title("Python Quiz By Lucas en Jasper")
root.geometry("1000x500")
root.configure(background='gray', borderwidth=2, relief="solid")
score = 0

photoplay = tk.PhotoImage(file = r"C:\QuizTime\Play.png")
photoimage1 = photoplay.subsample(5, 5)
photocredits = tk.PhotoImage(file = r"C:\QuizTime\Credits.png")
photoimage2 = photocredits.subsample(5, 5)
photoexit = tk.PhotoImage(file = r"C:\QuizTime\Exit.png")
photoimage3 = photoexit.subsample(5, 5)
photocheck = tk.PhotoImage(file = r"C:\QuizTime\Check.png")
photoimage4 = photocheck.subsample(5, 5)
photook = tk.PhotoImage(file = r"C:\QuizTime\Ok.png")
photoimage5 = photook.subsample(5, 5)
photologo = tk.PhotoImage(file = r"C:\QuizTime\logo.png")
photoimage6 = photologo.subsample(1, 1)

logo = tk.Label(root, image = photoimage6, borderwidth=0).pack()
welkom = tk.Label(root, fg="white", bg="gray", font=150, text="Welkom bij de Quiz!").pack()
letop = tk.Label(root, fg="white", bg="gray", font=150, text="Let op! Deze Quiz is hoofdlettergevoelig!").pack()


#Vraag1
def startquiz():
    global a1
    global vraag1
    vraag1 = tk.Toplevel()
    vraag1.geometry("900x300")
    vraag1.configure(background='gray')
    q1 = tk.Label(vraag1, fg="white", bg="gray", font=172, text="Wie zijn de ontwikkelaars van deze game?").pack()
    a1 = tk.Entry(vraag1, fg="black", bg="white", font=172, width=50)
    a1.pack()
    knop = tk.Button(vraag1, image = photoimage4, bg="gray", borderwidth=0, command=check1).pack()


def check1():
    global volgende1
    global score
    if a1.get() == "Lucas en Jasper":
        correct = tk.Label(vraag1, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag1, image = photoimage5, bg="gray", borderwidth=0, command=volgende1).pack()
        score =  score + 1
    elif a1.get() == "Jasper en Lucas":
        correct = tk.Label(vraag1, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag1, image = photoimage5, bg="gray", borderwidth=0, command=volgende1).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag1, bg="gray", fg="white", text="Incorrect").pack()


#Vraag2
def volgende1():
    global a2
    global vraag2
    vraag2 = tk.Toplevel()
    vraag2.geometry("900x300")
    vraag2.configure(background='gray')
    vraag1.destroy()
    q2 = tk.Label(vraag2, fg="white", bg="gray", font=172, text="Hoe heet onze opleiding?").pack()
    a2 = tk.Entry(vraag2, font=172, width=50)
    a2.pack()
    knop = tk.Button(vraag2, image = photoimage4, bg="gray", borderwidth=0, command=check2).pack()


def check2():
    global score
    if a2.get() == "Applicatieonwikkelaar":
        correct = tk.Label(vraag2, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag2, image = photoimage5, bg="gray", borderwidth=0, command=volgende2).pack()
        score =  score + 1
    elif a2.get() == "Applicatie en Media Ontwikkelaar":
        correct = tk.Label(vraag2, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag2, image = photoimage5, bg="gray", borderwidth=0, command=volgende2).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag2, bg="gray", fg="white", text="Incorrect").pack()


#Vraag3
def volgende2():
    global a3
    global vraag3
    vraag3 = tk.Toplevel()
    vraag3.geometry("900x300")
    vraag3.configure(background='gray')
    vraag2.destroy()
    q3 = tk.Label(vraag3, font=172, fg="white", bg="gray", text="In welke stad volgen wij deze opleiding?").pack()
    a3 = tk.Entry(vraag3, font=172, width=50)
    a3.pack()
    knop = tk.Button(vraag3, image = photoimage4, bg="gray", borderwidth=0, command=check4).pack()


def check4():
    global score
    if a3.get() == "Hengelo":
        correct = tk.Label(vraag3, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag3, image = photoimage5, bg="gray", borderwidth=0, command=volgende3).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag3, bg="gray", fg="white", text="Incorrect").pack()


#Vraag4
def volgende3():
    global a4
    global vraag4
    vraag4 = tk.Toplevel()
    vraag4.geometry("900x300")
    vraag4.configure(background='gray')
    vraag3.destroy()
    q4 = tk.Label(vraag4, font=172, fg="white", bg="gray", text="Wat doen we het meest op school?").pack()
    a4 = tk.Entry(vraag4, font=172, width=50)
    a4.pack()
    knop = tk.Button(vraag4, image = photoimage4, bg="gray", borderwidth=0, command=check5).pack()


def check5():
    global score
    if a4.get() == "Scrum":
        correct = tk.Label(vraag4, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag4, image = photoimage5, bg="gray", borderwidth=0, command=volgende4).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag4, bg="gray", fg="white", text="Incorrect").pack()


#Vraag5
def volgende4():
    global a5
    global vraag5
    vraag5 = tk.Toplevel()
    vraag5.geometry("900x300")
    vraag5.configure(background='gray')
    vraag4.destroy()
    q5 = tk.Label(vraag5, font=172, fg="white", bg="gray", text="In welk jaar eindigt onze opleiding?").pack()
    a5 = tk.Entry(vraag5, font=172, width=50)
    a5.pack()
    knop = tk.Button(vraag5, image = photoimage4, bg="gray", borderwidth=0, command=check6).pack()


def check6():
    global score
    if a5.get() == "2022":
        correct = tk.Label(vraag5, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag5, image = photoimage5, bg="gray", borderwidth=0, command=volgende5).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag5, bg="gray", fg="white", text="Incorrect").pack()


#Vraag6
def volgende5():
    global a6
    global vraag6
    vraag6 = tk.Toplevel()
    vraag6.geometry("900x300")
    vraag6.configure(background='gray')
    vraag5.destroy()
    q6 = tk.Label(vraag6, font=172, fg="white", bg="gray", text="Vind je de opleiding leuk?").pack()
    q6 = tk.Label(vraag6, font=172, fg="white", bg="gray", text="A. Ja").pack()
    q6 = tk.Label(vraag6, font=172, fg="white", bg="gray", text="B. Nee").pack()
    a6 = tk.Entry(vraag6, font=172, width=10)
    a6.pack()
    knop = tk.Button(vraag6, image = photoimage4, bg="gray", borderwidth=0, command=check7).pack()


def check7():
    global score
    if a6.get() == "A":
        correct = tk.Label(vraag6, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag6, image = photoimage5, bg="gray", borderwidth=0, command=volgende6).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag6, bg="gray", fg="white", text="Incorrect").pack()


#Vraag7
def volgende6():
    global a7
    global vraag7
    vraag7 = tk.Toplevel()
    vraag7.geometry("900x300")
    vraag7.configure(background='gray')
    vraag6.destroy()
    q7 = tk.Label(vraag7, font=172, fg="white", bg="gray", text="In welke taal is deze programma geschreven?").pack()
    q7 = tk.Label(vraag7, font=172, fg="white", bg="gray", text="A. Javascript").pack()
    q7 = tk.Label(vraag7, font=172, fg="white", bg="gray", text="B. HTML").pack()
    q7 = tk.Label(vraag7, font=172, fg="white", bg="gray", text="C. Python").pack()
    a7 = tk.Entry(vraag7, font=172, width=10)
    a7.pack()
    knop = tk.Button(vraag7, image = photoimage4, bg="gray", borderwidth=0, command=check8).pack()


def check8():
    global score
    if a7.get() == "C":
        correct = tk.Label(vraag7, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag7, image = photoimage5, bg="gray", borderwidth=0, command=volgende7).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag7, bg="gray", fg="white", text="Incorrect").pack()


#Vraag8
def volgende7():
    global a8
    global vraag8
    vraag8 = tk.Toplevel()
    vraag8.geometry("900x300")
    vraag8.configure(background='gray')
    vraag7.destroy()
    q8 = tk.Label(vraag8, font=172, fg="white", bg="gray", text="In welk schooljaar zitten we nu?").pack()
    q8 = tk.Label(vraag8, font=172, fg="white", bg="gray", text="A. 1e").pack()
    q8 = tk.Label(vraag8, font=172, fg="white", bg="gray", text="B. 4e").pack()
    q8 = tk.Label(vraag8, font=172, fg="white", bg="gray", text="C. 2e").pack()
    a8 = tk.Entry(vraag8, font=172, width=10)
    a8.pack()
    knop = tk.Button(vraag8, image = photoimage4, bg="gray", borderwidth=0, command=check9).pack()


def check9():
    global score
    if a8.get() == "A":
        correct = tk.Label(vraag8, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag8, image = photoimage5, bg="gray", borderwidth=0, command=volgende8).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag8, bg="gray", fg="white", text="Incorrect").pack()


#Vraag9
def volgende8():
    global a9
    global vraag9
    vraag9 = tk.Toplevel()
    vraag9.geometry("900x300")
    vraag9.configure(background='gray')
    vraag8.destroy()
    q9 = tk.Label(vraag9, font=172, fg="white", bg="gray", text="Vind je de Quiz leuk?").pack()
    q9 = tk.Label(vraag9, font=172, fg="white", bg="gray", text="A. Ja").pack()
    q9 = tk.Label(vraag9, font=172, fg="white", bg="gray", text="B. Nee").pack()
    a9 = tk.Entry(vraag9, font=172, width=10)
    a9.pack()
    knop = tk.Button(vraag9, image = photoimage4, bg="gray", borderwidth=0, command=check10).pack()


def check10():
    global score
    if a9.get() == "A":
        correct = tk.Label(vraag9, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag9, image = photoimage5, bg="gray", borderwidth=0, command=volgende9).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag9, bg="gray", fg="white", text="Incorrect").pack()


#Vraag10
def volgende9():
    global a10
    global vraag10
    vraag10 = tk.Toplevel()
    vraag10.geometry("900x300")
    vraag10.configure(background='gray')
    vraag9.destroy()
    q10 = tk.Label(vraag10, font=172, fg="white", bg="gray", text="In welke taal is de website geschreven?").pack()
    q10 = tk.Label(vraag10, font=172, fg="white", bg="gray", text="A. HTML").pack()
    q10 = tk.Label(vraag10, font=172, fg="white", bg="gray", text="B. CSS").pack()
    q10 = tk.Label(vraag10, font=172, fg="white", bg="gray", text="C. HTML + CSS").pack()
    a10 = tk.Entry(vraag10, font=172, width=10)
    a10.pack()
    knop = tk.Button(vraag10, image = photoimage4, bg="gray", borderwidth=0, command=check11).pack()


def check11():
    global score
    if a10.get() == "C":
        correct = tk.Label(vraag10, bg="gray", fg="white", text="Correct").pack()
        volgende1 = tk.Button(vraag10, image = photoimage5, bg="gray", borderwidth=0, command=afsluiting).pack()
        score =  score + 1
    else:
        incorrect = tk.Label(vraag10, bg="gray", fg="white", text="Incorrect").pack()


def quit():
    root.destroy()


def afsluiting():
    global score
    exitscreen = tk.Toplevel()
    exitscreen.geometry("900x300")
    vraag10.destroy()
    exitscreen.configure(background='gray')
    scoremax = str(10)
    scoretext = tk.Label(exitscreen, fg="white", bg="gray", text="Score: " + str(score) + " / " + scoremax)
    scoretext.pack()
    terug = tk.Button(exitscreen, text="Afsluiten", command=quit).pack()   


def info():
    infoscreen = tk.Toplevel()
    infoscreen.geometry("900x300")
    infoscreen.configure(background='gray')
    Jasper = tk.Label(infoscreen, fg="white", font=182, bg="gray", text="Jasper Tempelman").pack()
    Jasperemail = tk.Label(infoscreen, fg="white", font=172, bg="gray", text="0275910@student.rocvantwente.nl").pack()
    Lucas = tk.Label(infoscreen, fg="white", font=182, bg="gray", text="Lucas Huls").pack()
    Lucasemail = tk.Label(infoscreen, fg="white", font=172, bg="gray", text="0320242@student.rocvantwente.nl").pack()
    terug = tk.Button(infoscreen, image = photoimage3, font=172, bg="gray", borderwidth=0, command=quit).pack()

introknop = tk.Button(root, image = photoimage1, bg="gray", borderwidth=0, command=startquiz).pack()
info = tk.Button(root, image = photoimage2, bg="gray", borderwidth=0, command=info).pack()
Quit = tk.Button(root, image = photoimage3, bg="gray", borderwidth=0, command=quit).pack()

tk.mainloop()