"""Creating a simple welcome pop-up window"""

import Tkinter
#NB Don't use the name of a module to name your .py file.

# Creating a window
fenetre = Tkinter.Tk()



# Creating a label (line of text)
champ_label = Tkinter.Label(fenetre, text="Hello world!")
# Showing the label inside the window
champ_label.pack()


# Creating a button
bouton_quitter = Tkinter.Button(fenetre, text="Quit", command=fenetre.quit)
# Showing the Button
bouton_quitter.pack()



# Starting the Tkinter loop, which will end once the window is closed
fenetre.mainloop()
