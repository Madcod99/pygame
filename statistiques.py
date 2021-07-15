# from matplotlib import pyplot as plotter
# from matplotlib import numpy as np

def choosePlayer():
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk() 
    root.geometry('300x200+400+300')
    root.title("Statistiques")

    img = tk.PhotoImage(file=r"images/game_board.png")
    l = tk.Label(root, image=img)
    l.place(x=0, y=0)

    def action(event):
        select = listeCombo.get()
        showData(select)

    def quitter(event):
        root.destroy()

    tk.Label(root, text = "Joueur").place(x=150, y=20, anchor=tk.CENTER)
    
    listeProduits = getUsers()
    
    listeCombo = ttk.Combobox(root, values=listeProduits)
    
    listeCombo.current(0)

    listeCombo.place(x=150, y=40, anchor=tk.CENTER)

    btnAction = tk.Canvas(root, height = 80)
    img1 = tk.PhotoImage(file=r"images/stats_afficher.png")
    btnAction.create_image(95, 10, image=img1, anchor=tk.NW)
    btnAction.bind("<Button-1>", action)
    btnAction.place(x=150, y=100, anchor=tk.CENTER)

    btnQuitter = tk.Canvas(root, height = 80)
    img2 = tk.PhotoImage(file=r"images/stats_quitter.png")
    btnQuitter.create_image(100, 0, image=img2, anchor=tk.NW)
    btnQuitter.bind("<Button-1>", quitter)
    btnQuitter.place(x=150, y=200, anchor=tk.CENTER)

    #root.overrideredirect(1)
    root.mainloop()

def getData(player):
    try:
        file = open("stats/%s.txt"%player, "r")
        data = [list(map(float, i.split())) for i in file.read().split("\n")]
        data = [[j if j else 0.1 for j in i] for i in data]
        file.close()
        return data
    except:
        raise Exception("[ERREUR] Impossible de charger les données de '%s'"%player)

def showData(player):
    data = getData(player)
    figure, axis = plotter.subplots(1, 1)
    names = ["Victoires", "Nuls", "Défaites"]

    width = 0.2
    lineWidth = 2

    X1 = range(3)
    X2 = [x + width for x in X1]
    X3 = [x + width*2 for x in X1]

    axis.grid(zorder=0, axis="y")
    axis.bar(X1, data[0], color = 'g', width = width, linewidth = lineWidth, zorder = 3)
    axis.bar(X2, data[1], color = 'b', width = width, linewidth = lineWidth*2, zorder = 3)
    axis.bar(X3, data[2], color = 'r', width = width, linewidth = lineWidth*4, zorder = 3)    
    axis.legend(labels=["Victoires", "Nuls", "Défaites"])
    
    plotter.xticks([i + width for i in X1], ['Facile', 'Moyen', 'Difficile'])
    plotter.title("Statistiques de %s"%player)
    plotter.show()

def saveSession(player, level, etat):
    try:
        file = open("stats/%s.txt"%player, "r+")
        data = file.readlines()
    except:
        file = open("stats/%s.txt"%player, "w+")
        data = None

    file.close()

    if data:
        data = [i.replace("\n", "") for i in data]
        data = [list(map(int, i.split())) for i in data]
        data = [[j if j else 0 for j in i] for i in data]
    else:
        data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    data[level][etat] += 1
    
    out = []
    for line in data:
        line = map(str, line)
        out .append(" ".join(line))

    file = open("stats/%s.txt"%player, "w+")
    file.write("\n".join(out))
    file.close()

    updateUsers(player)

def updateUsers(player):
    users = getUsers()

    if player not in users:
        if users == [""] :
            users = []
        users.append(player)
    
    print("users : ", users)
    file = open("stats/.players.txt", "w+")
    file.write("\t".join(users))
    file.close()

def getUsers():
    file = open("stats/.players.txt", "r+")
    users = file.readline().split("\t")
    file.close()

    return users

if __name__ == "__main__":
    choosePlayer()
