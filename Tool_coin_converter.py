import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Convertisseur de pièces")

# Ajout d'un label simple
label = tk.Label(fenetre, text="Bienvenue dans le convertisseur de pièces !")
label.pack(padx=20, pady=10)

# Liste d'exemple pour les menus déroulants
pieces = ["Or", "Argent", "Cuivre"]

# Frame principale pour aligner tout sur une ligne
frame_main = tk.Frame(fenetre)
frame_main.pack(padx=20, pady=10)

# Frame colonne gauche
frame_left = tk.Frame(frame_main)
frame_left.pack(side=tk.LEFT, padx=5)
# Premier menu déroulant
var1 = tk.StringVar(fenetre)
var1.set(pieces[0])
menu1 = tk.OptionMenu(frame_left, var1, *pieces)
menu1.pack(pady=2)
# Entrée pour la première pièce (en dessous du menu)
entry_var1 = tk.StringVar()
entry1 = tk.Entry(frame_left, textvariable=entry_var1, width=10)
entry1.pack(pady=2)

# Label <=> entre les deux colonnes
label_arrow = tk.Label(frame_main, text="=>")
label_arrow.pack(side=tk.LEFT, padx=10)

# Frame colonne droite
frame_right = tk.Frame(frame_main)
frame_right.pack(side=tk.LEFT, padx=5)
# Deuxième menu déroulant
var2 = tk.StringVar(fenetre)
var2.set(pieces[1])
menu2 = tk.OptionMenu(frame_right, var2, *pieces)
menu2.pack(pady=2)
# Texte lié à la variable texte (remplace l'entrée utilisateur)
texte = "Valeur affichée à droite"  # Modifie cette variable selon tes besoins
label_texte = tk.Label(frame_right, text=texte)
label_texte.pack(pady=2)


# Boucle principale
fenetre.mainloop()