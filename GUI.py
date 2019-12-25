import csv
import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.minsize(700, 500)
root.title("Bio Informatics")

photo = PhotoImage(file="background1.gif")
background = Label(root, image=photo)
background.pack()


def filepath():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select your 'fasta File",
                                               filetypes=(("fasta files", "*.fa"), ("all files", "*.*")))

    label = Label(text=root.filename, fg="red").pack()
    file = open(root.filename)

    with open('mycords.csv', 'w', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow(['Name', 'x-cor', 'y-cor'])

        with open('sampledna.fa') as f:
            for line in f:
                a, b, c, d, e, f, g, h, i, j = line.split(":")
                instrument = a
                run_number = b
                flowcell_ID = c
                lane = d
                title = e
                x_pos = f
                y_pos = g
                is_filtered = h
                control = i
                index_sequence = j
                writer.writerow([title, x_pos, y_pos])

        thelabel = Label(topframe, text="")
        thelabel.pack()
        button2 = Button(topframe, text="RUN FILE", command=killer, fg="green")
        button2.pack()
        thelabel = Label(topframe, text="")
        thelabel.pack()
        thelabel = Label(topframe, text="Filepath:")
        thelabel.pack()


def killer():
    root.quit()
    # os.system("open: " + '/Users/QueenB/QGIS_4900/4900dB.qgz')

    os.startfile('/Users/QueenB/QGIS_4900/4900dB.qgz')

topframe = Frame(root)

topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

thelabel = Label(topframe, text="Geomapping Biological Samples")
thelabel.config(font=("Calibri", 17))
thelabel.pack()

thelabel = Label(topframe, text="")
thelabel.pack()

button1 = Button(topframe, text="Browse a File", command=filepath)
button1.pack()

root.mainloop()