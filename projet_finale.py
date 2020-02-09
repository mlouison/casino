# -*- coding: utf-8 -*-
"""
Système d'identification avec interface graphique.
"""



# importation de la bibliotheque graphique Tkinter et modules
import os
from tkinter import *
import time
import random
from PIL import Image, ImageTk
from tkinter import font


############################################################################
############################################################################
############################################################################

#Code de la fenêtre principale :


# creation d"une fenetre
fenetre = Tk()
fenetre.title("Menu Identification")
fenetre.configure(bg="#00008B")         
    
# creation des differents cadres
zone_1 = Frame(fenetre)
zone_1.grid(row=1,column=1,padx=10,pady=10)
zone_1.configure(bg="#00008B")

zone_2 = Frame(fenetre)
zone_2.grid(row=1,column=2,padx=10,pady=10)
zone_2.configure(bg="#00008B")


# creation d’une etiquette dans le cadre zone_1
etiquette = Label(zone_1)
etiquette.configure(text="Bienvenue dans notre Casino !",fg="pink",bg="#00008B")
etiquette.grid(row=1,column=1,padx=10,pady=10)


# creation des boutons du cadre zone_2
bouton_1 = Button(zone_2)
bouton_1.configure(text="Connexion",bg="pink", width="25", height="4")
bouton_1.grid(row=1,column=1)

bouton_2 = Button(zone_2)
bouton_2.configure(text="Nouveau compte",bg="pink", width="25", height="4")
bouton_2.grid(row=2,column=1,padx=10,pady=10)



############################################################################
############################################################################
############################################################################
############################################################################




#Création de la fenêtre connexion : 



#Variable utilisé pour la connexion :
pseudo_connexion = ""
mdp_connexion = ""
pseudo2 = ""
mdp = ""
keyIndex = 0




#Fenêtre connexion :
def menu_2 (event):
    global entree_pseudo1,entree_mdp1,fenetre4, fenetre6,fenetre3, fenetre2, fenetre5
    fenetre.withdraw()
    try:
        fenetre2.destroy()
        fenetre3.destroy()
       
    except:
        pass
    fenetre2 = Toplevel()
    fenetre2.title("Se connecter")
    fenetre2.configure(bg="#00008B")  

##    Création de zones
    zone_1 = Frame(fenetre2)
    zone_1.grid(row=1,column=1,padx=10,pady=10)
    zone_1.configure(bg="#00008B")

    zone_2 = Frame(fenetre2)
    zone_2.grid(row=1,column=2,padx=10,pady=10)
    zone_2.configure(bg="#00008B")
    #zone de saisie et étiquette pour la connexion
    etiquette = Label(zone_1)
    etiquette.configure(text="Entrer votre pseudo :",fg="pink",bg="#00008B")
    etiquette.grid(row=1,column=1,padx=10,pady=10)
    
    
    etiquette2 = Label(zone_1)
    etiquette2.configure(text="Entrer votre mot de passe : ",fg="pink",bg="#00008B")
    etiquette2.grid(row=2,column=1,padx=10,pady=10)
    
    
    etiquette3 = Label(zone_1)
    etiquette3.configure(text="",fg="pink",bg="#00008B")
    etiquette3.grid(row=3,column=1,padx=10,pady=10)

    
    pseudo1 = StringVar()
    entree_pseudo1 = Entry(zone_2, textvariable=pseudo1.get(), width=30)
    entree_pseudo1.grid(row=1,column=1,padx=10,pady=10)
    
    
    mdp1 = StringVar()
    entree_mdp1 = Entry(zone_2, textvariable=mdp1.get(), width=30)
    entree_mdp1.grid(row=2,column=1,padx=10,pady=10)

    

    c  = 0

#Fonction qui permet de savoir si le compte existe
    def connexion (event ) :
        global entree_pseudo1,entree_mdp1,pseudo_connexion,mdp_connexion,pseudo,mdp,chemin,c,nb_argent,fenetre4, fenetre6,fenetre3, fenetre2, fenetre5
        c  = 0
        chemin = "fichiers_texte/"
        chemin1 = "Wallet/"
     
        while c != 5 :
            pseudo_connexion = entree_pseudo1.get()
            mdp_connexion = entree_mdp1.get()
            
            try :
#                On essaye de voir si le pseudo existe
                pseudo2 = chemin + pseudo_connexion + ".txt"
                
                
#                Cryptage de mot de passe : Dédicasse à Blaise de Vigenère
                mdp_connexion = mdp_connexion.upper()
                key = "montaye"
                
                lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                
                keyIndex = 0
                # Le message crypté va se retrouver dans "crypted"
                mdp_crypted = ""
                for k in mdp_connexion :
              
                    num = lettres.find(k)
      
                    if num != -1:
                        num += lettres.find(key[keyIndex])
                        num %= len(lettres)
                        mdp_crypted += lettres[num]
                        keyIndex += 1
                     
                        if keyIndex == len(key):
                            keyIndex = 0
                   
                    else:
                        mdp_crypted += k
                argent = open(chemin1 + pseudo_connexion + ".txt")
                nb_argent = argent.read()
                argent.close
                        

                fichier = open(pseudo2,"r", encoding="utf8")
                if fichier.readline().strip() == mdp_crypted :
                    etiquette3.configure(text="Vous êtes maintenant connecté",fg="green")
                    c = 5
                    menu_4(event)
                else :
                    
                    etiquette3.configure(text="Votre mdp est incorrect",fg="red")
                    fichier.close()
                    c = 5

            except :
                etiquette3.configure(text="Ce pseudo n'existe pas",fg="red")
                c = 5
            
                    
                
          
   # creation du bouton valider qui active la fonction "connexion"
    bouton_3 = Button(zone_2)
    bouton_3.configure(text="Valider",bg="pink", width="25", height="3")
    bouton_3.grid(row=3,column=1)
    bouton_3.bind("<ButtonPress-1>",connexion)


############################################################################
############################################################################
############################################################################

 
#Création de la fenêtre inscription :
    

#Variable utilisé pour l'inscription    
new_pseudo = ""
new_mdp =""
verif_pseudo = ""
chemin = ""   
a = 0


#Fenêtre pour l'inscription
def menu_3 (event):
    
    global entree_pseudo, entree_mdp, a,fenetre4, fenetre6,fenetre3, fenetre2, fenetre5
    fenetre.withdraw()
    
    try:
        fenetre3.destroy()
        fenetre2.destroy()
        
       
    except:
        pass
    fenetre3 = Toplevel()
    fenetre3.title("Se connecter")
    fenetre3.configure(bg="#00008B")

##    Création de zones
    zone_1 = Frame(fenetre3)
    zone_1.grid(row=1,column=1,padx=10,pady=10)
    zone_1.configure(bg="#00008B")

    zone_2 = Frame(fenetre3)
    zone_2.grid(row=1,column=2,padx=10,pady=10)
    zone_2.configure(bg="#00008B")

    #zone de saisie et étiquette pour la connexion
    etiquette = Label(zone_1)
    etiquette.configure(text="Entrer votre nouveau pseudo :",fg="pink",bg="#00008B")
    etiquette.grid(row=1,column=1,padx=10,pady=10)
    
    
    etiquette2 = Label(zone_1)
    etiquette2.configure(text="Entrer votre nouveau mot de passe : ",fg="pink",bg="#00008B")
    etiquette2.grid(row=2,column=1,padx=10,pady=10)
    
    etiquette3 = Label(zone_1)
    etiquette3.configure(text="",fg="pink",bg="#00008B")
    etiquette3.grid(row=3,column=1,padx=10,pady=10)
    
    

    pseudo = StringVar()
    entree_pseudo = Entry(zone_2, textvariable=pseudo.get(), width=30)
    entree_pseudo.grid(row=1,column=1,padx=10,pady=10)
    
    
    mdp = StringVar()
    entree_mdp = Entry(zone_2, textvariable=mdp.get(), width=30)
    entree_mdp.grid(row=2,column=1,padx=10,pady=10)


    


#Fonction qui permet la création d'un nouveau compte :  
    def Nouveau_compte (event) :
        global entree_pseudo,fenetre4, fenetre6,fenetre3, fenetre2, fenetre5, chemin1, pseudo_connexion, entree_mdp,new_pseudo,new_mdp,verif_pseudo,chemin, a,nb_argent, keyIndex, crypted,num, pseudo_connexion
        a = 0
        chemin = "fichiers_texte/"
        chemin1 = "Wallet/"
    
    
        while a != 5 :

            new_pseudo = entree_pseudo.get()
            new_mdp = entree_mdp.get()
           
            try :
#                On essaye de voir si le pseudo existe déjà
                verif_pseudo = chemin + new_pseudo + ".txt"
                fichier = open(verif_pseudo,"r", encoding="utf8")
                etiquette3.configure(text="Pseudo déjà existant",fg="red")
                a = 5
          
                
        
            except :
          
                ### CREATION FICHIER NOUVEAU COMPTE :
                chemin = "fichiers_texte/"
                chemin1 = "Wallet/"
                nom = chemin + new_pseudo +".txt"
                fichier = open(nom,"w", encoding="utf8")
                
                
                
                
#                Cryptage de mot de passe :
                new_mdp = new_mdp.upper()
                key = "montaye"
                
                lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                
                keyIndex = 0
                # Le message crypté va se retrouver dans "crypted"
                mdp_crypted = ""
                for k in new_mdp :
              
                    num = lettres.find(k)
      
                    if num != -1:
                        num += lettres.find(key[keyIndex])
                        num %= len(lettres)
                        mdp_crypted += lettres[num]
                        keyIndex += 1
                     
                        if keyIndex == len(key):
                            keyIndex = 0
                   
                    else:
                        mdp_crypted += k
                        
                                
                texte = mdp_crypted
                
                fichier.write(texte)
                fichier.close()

##              Creation du porte monnaie accrédité de 1000$ :
                nom = chemin1 + new_pseudo +".txt"
                fichier = open(nom,"w", encoding="utf8")
                texte2 = "1000"
                fichier.write(texte2)
                fichier.close()
                argent = open(chemin1 + new_pseudo + ".txt")
                nb_argent = argent.read()
                argent.close
                pseudo_connexion = new_pseudo
            
                menu_4(event)
                a = 5
               
               
                
    
    # Bouton valider nouveau compte
    bouton_4 = Button(zone_2)
    bouton_4.configure(text="Valider",bg="pink", width="25", height="3")
    bouton_4.grid(row=3,column=1)
    bouton_4.bind("<ButtonPress-1>",Nouveau_compte)
    
   

      
    
############################################################################
############################################################################
############################################################################
    
##On assigne une fonction à des boutons : 

bouton_2.bind("<ButtonPress-1>",menu_3)

bouton_1.bind("<ButtonPress-1>",menu_2)



############################################################################
############################################################################
############################################################################




#Menu du menu du joueur

def menu_4(event) :
    global pseudo_connexion, fenetre4, fenetre6,fenetre3, fenetre2, fenetre5, fenetre6
   
    try:
        
        fenetre4.destroy()
        fenetre3.destroy()
        fenetre6.destroy()
        machine.destroy()

    except:
        pass
    fenetre5 = Toplevel()
    fenetre5.title("Menu du joueur")
    fenetre5.configure(bg="#00008B")     
    
    # creation des differents cadres
    zone_1 = Frame(fenetre5)
    zone_1.grid(row=1,column=1,padx=10,pady=10)
    zone_1.configure(bg="#00008B")

    zone_2 = Frame(fenetre5)
    zone_2.grid(row=1,column=2,padx=10,pady=10)
    zone_2.configure(bg="#00008B")
    
    zone_3 = Frame(fenetre5)
    zone_3.grid(row=2,column=2,padx=10,pady=10)
    zone_3.configure(bg="#00008B")
    
    zone_4 = Frame(fenetre5)
    zone_4.grid(row=2,column=1,padx=10,pady=10)
    zone_4.configure(bg="#00008B")
    
    
    
   
    

    # Utilisation de new pseudo et pseudo connexion car l'utilisateur peut soit venir de s'inscrire ou de se connecter
    etiquette = Label(zone_1)
    etiquette.configure(text="Bienvenue " + pseudo_connexion + " !" ,fg="pink",bg="#00008B")
    etiquette.grid(row=1,column=1,padx=10,pady=10)
    
    etiquette = Label(zone_2)
    etiquette.configure(text="Vous avez actuellement "+ str(nb_argent) + "$ !" ,fg="pink",bg="#00008B")
    etiquette.grid(row=1,column=1,padx=10,pady=10)



    # creation des boutons du cadre zone_2
    bouton_1 = Button(zone_3)
    bouton_1.configure(text="Blackjack",bg="pink", width="25", height="4")
    bouton_1.grid(row=1,column=1)
    
    bouton_2 = Button(zone_4)
    bouton_2.configure(text="Machine à sous",bg="pink", width="25", height="4")
    bouton_2.grid(row=2,column=1,padx=10,pady=10)
    

    
    
    chemin1 = "Wallet/"
    nom = chemin1 + pseudo_connexion +".txt"
    argent = open(nom,"w", encoding="utf8")
    argent.write(str(nb_argent))
    argent.close()
    bouton_1.bind("<ButtonPress-1>",blackjack)
    bouton_2.bind("<ButtonPress-1>",mas)


    
    
############################################################################
############################################################################
############################################################################
    
    
    
def blackjack (event) :
    global  fenetre5,fenetre3,fenetre6,etiquette_mise, valeur_carte_croupier, chemin1,pseudo_connexion, jeton3,argent, nb_argent, tour,jeton,jeton2,x9,y9, x6, y6, x7, y7, valeur_carte_joueur, valeur_jeu_carte, valeur_carte_random, carte_croupier, liste_jeux, jeu_random, illustration1, illustration2, illustration3, illustration4, illustration5, texte_1, texte_2,x7,y7,x6,y6
    chemin1 = "Wallet/"
   
    fenetre5.withdraw()
    try:
        fenetre6.destroy()
        fenetre5.destroy()
        fenetre4.destory()
        machine.destroy()

    except:
        pass

    

    #### CRÉATION DE LA FENETRE
    fenetre6 = Toplevel()
    fenetre6.title("BlackJack L&M")
    fenetre6.configure(bg = "#00008B")
    
    # creation des differents cadres
    zone_1 = Frame(fenetre6)
    zone_1.grid(row=1,column=1,padx=10,pady=10)
    zone_1.configure(bg ="#016241")
    
    
    
    zone_2 = Frame(fenetre6)
    zone_2.grid(row=1,column=35,padx=10,pady=10,)
    zone_2.configure(bg ="#00008B")
                     
                     
    
#    Création des boutons
    bouton_1 = Button(zone_2)
    bouton_1.configure(text="Check",bg = "pink", width="10", height="4")
    bouton_1.grid(row=2,column=1,padx=10,pady=30)
    
    bouton_2 = Button(zone_2)
    bouton_2.configure(text="Stand",bg = "pink", width="10", height="4")
    bouton_2.grid(row=25,column=1,padx=10,pady=30)
    
    bouton_3 = Button(zone_2)
    bouton_3.configure(text="Start",bg = "pink", width="12", height="8")
    bouton_3.grid(row=1,column=1,padx=10,pady=30)
    
    bouton_4 = Button(fenetre6)
    bouton_4.configure(text="Miser",bg = "pink", width="10", height="4")
    bouton_4.grid(row=3,column=3,padx=10,pady=30)
    
    bouton_5 = Button(zone_2)
    bouton_5.configure(text="Retour menu",bg = "pink", width="10", height="4")
    bouton_5.grid(row=26,column=1,padx=10,pady=30)
    bouton_5.bind("<ButtonPress-1>",menu_4)

    
    
    # =============================================================================
    # #Quelques variables  :
    # =============================================================================
    
    #Jeton 1 et 2 servent a ne pas pouvoir appuyer plusieurs fois sur le bouton sans raison
    jeton = 0
    argent = 1000
    jeton2 = 0
    jeton3 = 0
    
    #Caractéristiques de polices :
    carac_font=font.Font(family='Futura', size=20, weight='bold')
    
    
    
    
    #zone de saisie et étiquette 
    etiquette = Label(fenetre6)
    etiquette.configure(text="Vous possédez actuellement sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
    etiquette.grid(row=2,column=1,padx=1,pady=1)
    
    
    
    etiquette1 = Label(fenetre6)
    etiquette1.configure(text="Entrez votre mise :",fg="pink",bg = "#00008B",font = carac_font)
    etiquette1.grid(row=3,column=1,padx=5,pady=5)
    
    
    etiquette2 = Label(fenetre6)
    etiquette2.configure(text="",fg="pink",bg = "#00008B",font = carac_font)
    etiquette2.grid(row=1,column=2,padx=5,pady=5)

    etiquette_mise = Label(fenetre6)
    
    
    
    
 
    
    #Mise entrée :
    mise = StringVar()
    entree_mise = Entry(fenetre6, textvariable=mise.get(), width=30)
    entree_mise.grid(row=3,column=2,padx=5,pady=5)
    
    
    
    
    # creation d’une zone de dessin dans le cadre zone_1
    canevas = Canvas(zone_1)
    
    
    
#    Image redimensionné pour le fond du blackjack
    im = Image.open("blackjack.png")
    im = im.resize((20,20))
    
    illustration = ImageTk.PhotoImage(file = "blackjack_red.png")

    canevas.create_image(0,0,image=illustration, anchor=NW)
    canevas.configure(width=500,height=300, bg ="#016241")
    
    
    canevas.pack()
  
    
    #############################################################################################
    #############################################################################################
    #############################################################################################
    
    
    # =============================================================================
    # ##Variable affectés a des cartes + variables en général
    # =============================================================================
  
    chemin = "img_cartes2/"
    
    #Coordonées des différentes cartes : 
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    x5 = 0
    y5 = 0
    x6 = 0
    y6 = 0
    x7 = 0
    y7 = 0
    x9 = 0
    y9 = 0
 
    
    ##Outil pour donner plusieurs fonction pour un même bouton.
    tour = 0
    
    ##Création des cartes et de leurs familles 
    familles = ["pique","carreau","coeur","trèfle"]
    cartes = ["As",2,3,4,5,6,7,8,9,10,"Valet","Dame","Roi"]
    
    
    
    
    # =============================================================================
    # ##Création des 6 jeux de carte :
    # =============================================================================
    
    ##Jeu de cartes 1 
    jeu = []
    for k in range (len(cartes)) :
        for k2 in range (len(familles)) :
            jeu.append(str(cartes[k]) + "_de_" + str(familles[k2]))
    
    ##Jeu de cartes 2
    jeu2 = []
    for k in range (len(cartes)) :
        for k2 in range (len(familles)) :
            jeu2.append(str(cartes[k]) + "_de_" + str(familles[k2]))
    
    
    ##Jeu de cartes 3 
    jeu3 = []
    for k in range (len(cartes)) :
        for k2 in range (len(familles)) :
            jeu3.append(str(cartes[k]) + "_de_" + str(familles[k2]))
    
    
    
    ##Jeu de cartes 4
    jeu4 = []
    for k in range (len(cartes)) :
        for k2 in range (len(familles)) :
            jeu4.append(str(cartes[k]) + "_de_" + str(familles[k2]))
    
    
    ##Jeu de cartes 5
    jeu5 = []
    for k in range (len(cartes)) :
        for k2 in range (len(familles)) :
            jeu5.append(str(cartes[k]) + "_de_" + str(familles[k2]))
    
    
    ##Jeu de cartes 6
    jeu6 = []
    for k in range (len(cartes)) :
        for k2 in range (len(familles)) :
            jeu6.append(str(cartes[k]) + "_de_" + str(familles[k2]))
    
    
    
    #############################################################################################
    #############################################################################################
    #############################################################################################
            
    
    # =============================================================================
    # #Fonction de départ :
    # =============================================================================
    
    def carte_départ (event) :
        global illustration,valeur_carte_croupier,nb_argent, jeton,jeton2,x9,y9, x6, y6, x7, y7, valeur_carte_joueur, valeur_jeu_carte, valeur_carte_random, carte_croupier, liste_jeux, jeu_random, illustration1, illustration2, illustration3, illustration4, illustration5, texte_1, texte_2,x7,y7,x6,y6
        
     
        
#        Le jeton sert a pouvoir commencer la partie seulement si l'on a miser
        if jeton == 1 :
            
#            On supprime l'ancien canevas pour recommencer la partie
            canevas.delete("all")
            illustration = ImageTk.PhotoImage(file = "blackjack_red.png")
            canevas.create_image(0,0,image=illustration, anchor=NW)
            canevas.configure(width=500,height=300, bg ="#016241")
            canevas.pack()
            
            ##Carte 1 du joueur numéro 1:
            a = random.randint(0,51)
            liste_jeux = [jeu,jeu2,jeu3,jeu4,jeu5,jeu6]
            jeu_random = random.choice(liste_jeux)
            valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
            
            carte_random = jeu_random[a]
            valeur_carte = valeur_jeu_carte[a]
           
          
            #    Chargement de l'image carte random numéro 1:
            im1 = Image.open(chemin + carte_random + ".jpg")
            # redimensionnement de l'imge
            im1 = im1.resize((60,80))
            # sauvegarde de l'image redimensionnee
            im1.save(chemin + carte_random + "_red.jpg")
            
        #    Crétion de la carte dans le canvas avec ses coordonées
            illustration1 = ImageTk.PhotoImage(file= chemin + carte_random + "_red.jpg")
            id_im = canevas.create_image(0, 0, image=illustration1, anchor=NW)
            x = 10
            y = 165
            canevas.coords(id_im,x,y)
        
            
        
            
            
             ##Carte 2 du joueur :
            b = random.randint(0,51)
            random.shuffle(liste_jeux)
            jeu_random1 = random.choice(liste_jeux)
            valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
            
            carte_random2 = jeu_random1[b]
            valeur_carte2 = valeur_jeu_carte[b]
           
            
            #    Chargement de l'image carte random numéro 2:
            im2 = Image.open(chemin + carte_random2 + ".jpg")
            # redimensionnement de l'imge
            im2 = im2.resize((60,80))
            # sauvegarde de l'image redimensionnee
            im2.save(chemin + carte_random2 + "_red.jpg")
            
        #    Crétion de la carte dans le canvas avec ses coordonées
            illustration2 = ImageTk.PhotoImage(file= chemin + carte_random2 + "_red.jpg")
            id_im2 = canevas.create_image(0, 0, image=illustration2, anchor=NW)
            x2 = 10
            y2 = 187
            canevas.coords(id_im2,x2,y2)
            
        
            
            ##Carte croupier :
            c = random.randint(0,51)
            random.shuffle(liste_jeux)
            jeu_random2 = random.choice(liste_jeux)
            valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
            
            
            carte_croupier = jeu_random2[c]
            valeur_carte_croupier = valeur_jeu_carte[c]
           
            
             #    Chargement de l'image carte random numéro 2:
            im3 = Image.open(chemin + carte_croupier + ".jpg")
            # redimensionnement de l'imge
            im3 = im3.resize((60,80))
            # sauvegarde de l'image redimensionnee
            im3.save(chemin + carte_croupier + "_red.jpg")
            
        #    Crétion de la carte dans le canvas avec ses coordonées
            illustration3 = ImageTk.PhotoImage(file= chemin + carte_croupier + "_red.jpg")
            id_im3 = canevas.create_image(0, 0, image=illustration3, anchor=NW)
            x9 = 10
            y9 = 23
            canevas.coords(id_im3,x9,y9)
            
        
            
        
        
            im4 = Image.open(chemin + "Dos_de_carte.jpg" )
            im4 = im4.resize((60,80))
            im4.save(chemin + "Dos_de_carte_red.jpg")
            illustration4 = ImageTk.PhotoImage(file= chemin + "Dos_de_carte_red.jpg")
            id_im4 = canevas.create_image(0, 0, image=illustration4, anchor=NW)
            x4 = 90
            y4 = 90
            canevas.coords(id_im4,x4,y4)
            
            
            
            illustration5 = ImageTk.PhotoImage(file= chemin + "Dos_de_carte_red.jpg")
            id_im5 = canevas.create_image(0, 0, image=illustration5, anchor=NW)
            x5 = 150
            y5 = 90
            canevas.coords(id_im5,x5,y5)
        
            
            #    On affiche les images
            canevas.image = illustration2, illustration1, illustration3, illustration4, illustration5
            canevas.grid(row=5,column=1)
            
            
            
            valeur_carte_joueur = valeur_carte + valeur_carte2
            
        #    Création de texte pour afficher les valeurs du jeu du joueur et du croupier : 
            x6 = 190
            y6 = 230
            texte_1 = canevas.create_text(x6, y6,text="La valeur de votre jeu est : " + str(valeur_carte_joueur),fill="pink" )
          
        
            x7 = 200
            y7 = 40
            texte_2 = canevas.create_text(x7, y7,text="La valeur du jeu du croupier est : " + str(valeur_carte_croupier),fill="pink" )
        
            jeton = 0
            jeton2 = 1
            
    
    bouton_3.bind("<ButtonPress-1>",carte_départ)
    
    
    
    
    
    
    
    
    
    
    
    # =============================================================================
    # Fonction check :
    # =============================================================================
    
    
    def check (event) : 
        global valeur_carte_joueur,chemin1, pseudo_connexion, nb_argent,jeton2,jeton3,illustration8, illustration9, illustration10, illustration11, texte_3, texte_5, texte_6, texte_4, tour, valeur_carte_croupier, valeur_jeu_carte, liste_jeux, illustration6,illustration7,x9,y9, texte_1, texte_2, texte1, texte2, texte3, texte4
        
#        Le jeton 2 sert a pouvoir appuyer sur le bouton check seulement quand on a commencé la partie
        if jeton2 == 1 : 
            
#            La variable tour sert a savoir ou mettre exactement la carte du joueur et celle du croupier
            if tour == 1 :
                 
                     
                #       Changement de la valeur de l'as pour une valeur de jeu suppérieur a 10
                if valeur_carte_joueur > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]   
        
        
                #    Carte joueur
                d = random.randint(0,51)
                random.shuffle(liste_jeux)
                jeu_random3 = random.choice(liste_jeux)
                carte_random3 = jeu_random3[d]
                valeur_carte4 = valeur_jeu_carte[d]
        
        
        
                #    Chargement de l'image carte random numéro 2:
                im8 = Image.open(chemin + carte_random3 + ".jpg")
                # redimensionnement de l'imge
                im8 = im8.resize((60,80))
                # sauvegarde de l'image redimensionnee
                im8.save(chemin + carte_random3 + "_red.jpg")
        
                #    Crétion de la carte dans le canvas avec ses coordonées
                illustration8 = ImageTk.PhotoImage(file= chemin + carte_random3 + "_red.jpg")
                id_im8 = canevas.create_image(0, 0, image=illustration8, anchor=NW)
                x8 = 10
                y8 = 231
                canevas.coords(id_im8,x8,y8)
            
                #    On affiche les images
                canevas.image = illustration1, illustration2, illustration4, illustration5, illustration6, illustration7, illustration8
                canevas.grid(row=5,column=1)
            
        
        
                valeur_carte_joueur = valeur_carte_joueur + valeur_carte4
        
            
            
            
                #    Carte Croupier
                if valeur_carte_croupier > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                else :
                    valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        
        
        
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
            
                     #    Chargement de l'image carte random numéro 2:
                    im9 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im9 = im9.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im9.save(chemin + carte_croupier2 + "_red.jpg")
            
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration9 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im9 = canevas.create_image(0, 0, image=illustration9, anchor=NW)
                    x9 = 10
                    y9 = 67
                    canevas.coords(id_im9,x9,y9)
            
            
                    #    On affiche les images
                    canevas.image = illustration1, illustration2, illustration4, illustration5, illustration6, illustration7, illustration8, illustration9
                    canevas.grid(row=5,column=1)
                    
                canevas.delete(texte_3)
                canevas.delete(texte_4)
                texte_5 =  canevas.create_text(x6, y6,text="La valeur de votre jeu est : " + str(valeur_carte_joueur),fill="pink" )
                texte_6 =  canevas.create_text(x7, y7,text="La valeur du jeu du croupier est : " + str(valeur_carte_croupier),fill="pink" )
        
                    
                    
        
            elif tour == 0 :
                
                 #    Changement de la valeur de l'as pour une valeur de jeu suppérieur a 10
                if valeur_carte_joueur > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
               
        
                #    Carte joueur
                d = random.randint(0,51)
                random.shuffle(liste_jeux)
                jeu_random3 = random.choice(liste_jeux)
                carte_random3 = jeu_random3[d]
                valeur_carte4 = valeur_jeu_carte[d]
                
                
                
                #    Chargement de l'image carte random numéro 2:
                im6 = Image.open(chemin + carte_random3 + ".jpg")
                # redimensionnement de l'imge
                im6 = im6.resize((60,80))
                # sauvegarde de l'image redimensionnee
                im6.save(chemin + carte_random3 + "_red.jpg")
        
                #    Crétion de la carte dans le canvas avec ses coordonées
                illustration6 = ImageTk.PhotoImage(file= chemin + carte_random3 + "_red.jpg")
                id_im6 = canevas.create_image(0, 0, image=illustration6, anchor=NW)
                x8 = 10
                y8 = 209
                canevas.coords(id_im6,x8,y8)
                    
                #    On affiche les images
                canevas.image = illustration6
                canevas.grid(row=5,column=1)
                    
        
                
                valeur_carte_joueur = valeur_carte_joueur + valeur_carte4
        
                    
                    
                    
                    
                    
                #    Carte Croupier
                if valeur_carte_croupier > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                else :
                    valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                
                
                
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                     #    Chargement de l'image carte random numéro 2:
                    im7 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im7 = im7.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im7.save(chemin + carte_croupier2 + "_red.jpg")
                    
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration7 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im7 = canevas.create_image(0, 0, image=illustration7, anchor=NW)
                    x9 = 10
                    y9 = 45
                    canevas.coords(id_im7,x9,y9)
                    
                    
                    #    On affiche les images
                    canevas.image = illustration1, illustration2, illustration4, illustration5, illustration6, illustration7
                    canevas.grid(row=5,column=1)
                    
                    
#                On supprime les textes pour afficher la nouvelle valeur du jeu
                canevas.delete(texte_1)
                canevas.delete(texte_2)
                texte_3 =  canevas.create_text(x6, y6,text="La valeur de votre jeu est : " + str(valeur_carte_joueur),fill="pink" )
                texte_4 =  canevas.create_text(x7, y7,text="La valeur du jeu du croupier est : " + str(valeur_carte_croupier),fill="pink" )
                    
                    
            
        
            elif tour == 2 : 
                
                #    Changement de la valeur de l'as pour une valeur de jeu suppérieur a 10
                if valeur_carte_joueur > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
               
        
                #    Carte joueur
                d = random.randint(0,51)
                random.shuffle(liste_jeux)
                jeu_random3 = random.choice(liste_jeux)
                carte_random3 = jeu_random3[d]
                valeur_carte4 = valeur_jeu_carte[d]
                
                
                
                #    Chargement de l'image carte random numéro 2:
                im10 = Image.open(chemin + carte_random3 + ".jpg")
                # redimensionnement de l'imge
                im10 = im10.resize((60,80))
                # sauvegarde de l'image redimensionnee
                im10.save(chemin + carte_random3 + "_red.jpg")
        
                #    Crétion de la carte dans le canvas avec ses coordonées
                illustration10 = ImageTk.PhotoImage(file= chemin + carte_random3 + "_red.jpg")
                id_im10 = canevas.create_image(0, 0, image=illustration10, anchor=NW)
                x10 = 10
                y10 = 253
                canevas.coords(id_im10,x10,y10)
                    
                #    On affiche les images
                canevas.image = illustration1, illustration2, illustration4, illustration5, illustration6, illustration7, illustration8, illustration10
                canevas.grid(row=5,column=1)
                    
        
                
                valeur_carte_joueur = valeur_carte_joueur + valeur_carte4
        
                    
                    
                    
                    
                    
                #    Carte Croupier
                if valeur_carte_croupier > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                else :
                    valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                
                
                
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                     #    Chargement de l'image carte random numéro 2:
                    im11 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im11 = im11.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im11.save(chemin + carte_croupier2 + "_red.jpg")
                    
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration11 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im11 = canevas.create_image(0, 0, image=illustration11, anchor=NW)
                    x9 = 10
                    y9 = 87
                    canevas.coords(id_im11,x9,y9)
                    
                    
                    #    On affiche les images
                    canevas.image = illustration11, illustration2, illustration4, illustration5, illustration6, illustration7, illustration8, illustration9, illustration10, illustration1
                    canevas.grid(row=5,column=1)
                    
                    
                canevas.delete(texte_5)
                canevas.delete(texte_6)
                texte_7 =  canevas.create_text(x6, y6,text="La valeur de votre jeu est : " + str(valeur_carte_joueur),fill="pink" )
        
                texte_8 =  canevas.create_text(x7, y7,text="La valeur du jeu du croupier est : " + str(valeur_carte_croupier),fill="pink" )
                    
                
                    
                    
#            tour prend +1 pour savoir le nombre de fois que l'on a appuyer sur le bouton check
            tour += 1
           
            
        
#            On regarde en comparrant la valeur des cartes pour savoir qui a gagné
#            L'argent est enregistré dans le dossier wallet du joueur
            
            if valeur_carte_joueur > 21 :
                etiquette2.configure(text="Perdu ! - " + mise_joueur + "$",fg="red",bg = "#00008B",font = carac_font)
                jeton3 = 1
                etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                jeton2 = 0
                nom = chemin1 + pseudo_connexion +".txt"
                argent = open(nom,"w", encoding="utf8")
                argent.write(str(nb_argent))
                argent.close()



                
                                     
            elif valeur_carte_croupier > 21 and valeur_carte_joueur > 21 : 
                etiquette2.configure(text="Egalité !",fg="pink",bg = "#00008B",font = carac_font)
                jeton3 = 1
                nb_argent = float(nb_argent) + float(mise_joueur)
                etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                jeton2 = 0
                nom = chemin1 + pseudo_connexion +".txt"
                argent = open(nom,"w", encoding="utf8")
                argent.write(str(nb_argent))
                argent.close()

    
    
    
    
            elif valeur_carte_croupier > 17 and valeur_carte_joueur > 17 :
                if valeur_carte_croupier == valeur_carte_joueur :
##                    Code couleur hexadecimal B=11
                    etiquette2.configure(text="Egalité !",fg="pink",bg = "#00008B",font = carac_font)
                    jeton3 = 1
                    nb_argent = float(nb_argent) + float(mise_joueur)
                    etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                    jeton2 = 0
                    nom = chemin1 + pseudo_connexion +".txt"
                    argent = open(nom,"w", encoding="utf8")
                    argent.write(str(nb_argent))
                    argent.close()

    
    
    
                                     
            elif valeur_carte_joueur < 22 and valeur_carte_croupier > 21 :
                mise_gagnante = 1.5*float(mise_joueur)
                etiquette2.configure(text="Gagné ! + " + str(mise_gagnante) + "$",fg="green",bg = "#00008B",font = carac_font)
                nb_argent = float(nb_argent) + float(mise_joueur) + float(mise_gagnante)
                jeton3 = 1
                etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                jeton2 = 0
                nom = chemin1 + pseudo_connexion +".txt"
                argent = open(nom,"w", encoding="utf8")
                argent.write(str(nb_argent))
                argent.close()

    

        
    
    #     
    #On affecte la fonction check au bouton : 
    bouton_1.bind("<ButtonPress-1>",check)
    
    
    
    
    
    
    
    
    
    
    
    # =============================================================================
    # Fonction stand :
    # =============================================================================
    
    
    def stand (event) :
        global valeur_carte_croupier, texte_5, x9, y9,jeton3,argent, cavenas,jeton2, jeton, nb_argent, chemin1, pseudo_connexion
        
#        Le jeton2 sert a ne pas pouvoir appuyer sur le bouton stand avant de commencer la partie
        if jeton2 == 1 :
        
            
#            On observe la coordonnées de la dernière carte du croupier pour savoir ou placer sa prochaine carte
            if y9 == 23 :
                
                
            
                 #    Carte Croupier
                if valeur_carte_croupier > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                else :
                    valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                
                
                
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                   
                    
                    #    Chargement de l'image carte croupier numéro 2:
                    im12 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im12 = im12.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im12.save(chemin + carte_croupier2 + "_red.jpg")
                    
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration12 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im12 = canevas.create_image(0, 0, image=illustration12, anchor=NW)
                    x9 = 10
                    y9 = 45
                    canevas.coords(id_im12,x9,y9)
                    
                    #    On affiche les images
                    canevas.image = illustration2, illustration1, illustration3, illustration4, illustration5, illustration12
                    canevas.grid(row=5,column=1)
            
            
            
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                   
                    
                    #    Chargement de l'image carte croupier numéro 2:
                    im13 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im13 = im13.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im13.save(chemin + carte_croupier2 + "_red.jpg")
                    
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration13 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im13 = canevas.create_image(0, 0, image=illustration13, anchor=NW)
                    x9 = 10
                    y9 = 67
                    canevas.coords(id_im13,x9,y9)
                    
                    #    On affiche les images
                    canevas.image = illustration2, illustration1, illustration3, illustration4, illustration5, illustration12, illustration13
                    canevas.grid(row=5,column=1)
            
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                   
                    
                    #    Chargement de l'image carte croupier numéro 2:
                    im14 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im14 = im14.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im14.save(chemin + carte_croupier2 + "_red.jpg")
                    
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration14 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im14 = canevas.create_image(0, 0, image=illustration14, anchor=NW)
                    x9 = 10
                    y9 = 89
                    canevas.coords(id_im14,x9,y9)
                    
                    #    On affiche les images
                    canevas.image = illustration14, illustration1, illustration3, illustration4, illustration5, illustration12, illustration13, illustration2
                    canevas.grid(row=5,column=1)
            
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                
                canevas.delete(texte_1)
                canevas.delete(texte_2)
                texte_finale =  canevas.create_text(x6, y6,text="La valeur de votre jeu  est : " + str(valeur_carte_joueur),fill="pink" )
                texte_finale2 =  canevas.create_text(x7, y7,text="La valeur du jeu du croupier est : " + str(valeur_carte_croupier),fill="pink" )
        
                    
                
                
                
            elif y9 == 45 :
                
                
                
                  #    Carte Croupier
                if valeur_carte_croupier > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                else :
                    valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                
                
                
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                   
                    
                    #    Chargement de l'image carte croupier numéro 2:
                    im12 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im12 = im12.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im12.save(chemin + carte_croupier2 + "_red.jpg")
                    
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration12 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im12 = canevas.create_image(0, 0, image=illustration12, anchor=NW)
                    x9 = 10
                    y9 = 67
                    canevas.coords(id_im12,x9,y9)
                    
                    #    On affiche les images
                    canevas.image = illustration1, illustration2, illustration4, illustration5, illustration6, illustration7, illustration12
                    canevas.grid(row=5,column=1)
                    
                    
                
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                   
                    
                    #    Chargement de l'image carte croupier numéro 2:
                    im13 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im13 = im13.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im13.save(chemin + carte_croupier2 + "_red.jpg")
                    
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration13 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im13 = canevas.create_image(0, 0, image=illustration13, anchor=NW)
                    x9 = 10
                    y9 = 89
                    canevas.coords(id_im13,x9,y9)
                    
                    #    On affiche les images
                    canevas.image = illustration13, illustration2, illustration4, illustration5, illustration6, illustration7, illustration12, illustration1
                    canevas.grid(row=5,column=1)
                    
                    
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                    
                canevas.delete(texte_3)
                canevas.delete(texte_4)
                texte_finale =  canevas.create_text(x6, y6,text="La valeur de votre jeu  est : " + str(valeur_carte_joueur),fill="pink" )
                texte_finale2 =  canevas.create_text(x7, y7,text="La valeur du jeu du croupier est : " + str(valeur_carte_croupier),fill="pink" )
        
                
                    
                    
            
            
            else :
                
                  #    Carte Croupier
                if valeur_carte_croupier > 10 :
                    valeur_jeu_carte = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                else :
                    valeur_jeu_carte = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
                
                
                
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                   
                    
                    #    Chargement de l'image carte croupier numéro 2:
                    im12 = Image.open(chemin + carte_croupier2 + ".jpg")
                    # redimensionnement de l'imge
                    im12 = im12.resize((60,80))
                    # sauvegarde de l'image redimensionnee
                    im12.save(chemin + carte_croupier2 + "_red.jpg")
                    
                    #    Crétion de la carte dans le canvas avec ses coordonées
                    illustration12 = ImageTk.PhotoImage(file= chemin + carte_croupier2 + "_red.jpg")
                    id_im12 = canevas.create_image(0, 0, image=illustration12, anchor=NW)
                    x9 = 10
                    y9 = 89
                    canevas.coords(id_im12,x9,y9)
                    
                    #    On affiche les images
                    canevas.image = illustration1, illustration2, illustration4, illustration5, illustration6, illustration7, illustration12
                    canevas.grid(row=5,column=1)
                    
                    
               
                 
                
                if valeur_carte_croupier < 17 :
                    e = random.randint(0,51)
                    random.shuffle(liste_jeux)
                    jeu_random4 = random.choice(liste_jeux)
                    carte_croupier2 = jeu_random4[e]
                    valeur_carte_croupier2 = valeur_jeu_carte[e]
                    valeur_carte_croupier = valeur_carte_croupier + valeur_carte_croupier2
                    
                    
                canevas.delete(texte_5)
                canevas.delete(texte_6)
                texte_finale =  canevas.create_text(x6, y6,text="La valeur de votre jeu  est : " + str(valeur_carte_joueur),fill="pink" )
                texte_finale2 =  canevas.create_text(x7, y7,text="La valeur du jeu du croupier est : " + str(valeur_carte_croupier),fill="pink" )
    
                
         
                
                
            
            if valeur_carte_croupier > 21 :
                mise_gagnante = 1.5*float(mise_joueur)
                etiquette2.configure(text="Gagné ! + " + str(mise_gagnante) + "$",fg="green",bg = "#00008B",font = carac_font)
                nb_argent = float(nb_argent) + float(mise_joueur) + float(mise_gagnante)
                jeton3 = 1
                etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                jeton2 = 0
                nom = chemin1 + pseudo_connexion +".txt"
                argent = open(nom,"w", encoding="utf8")
                argent.write(str(nb_argent))
                argent.close()

    
    
    
    
#    On compare les cartes pour savoir qui a gagné
            
            
            elif valeur_carte_croupier > 21 and valeur_carte_joueur > 21 : 
                etiquette2.configure(text="Egalité !",fg="pink",bg = "#00008B",font = carac_font)
                jeton3 = 1
                nb_argent = float(nb_argent) + float(mise_joueur)
                etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                jeton2 = 0
                nom = chemin1 + pseudo_connexion +".txt"
                argent = open(nom,"w", encoding="utf8")
                argent.write(str(nb_argent))
                argent.close()

    
    
    
           
                                                                  
            elif valeur_carte_joueur > valeur_carte_croupier :
                mise_gagnante = 1.5*float(mise_joueur)
                etiquette2.configure(text="Gagné ! + " + str(mise_gagnante) + "$",fg="green",bg = "#00008B",font = carac_font)
                nb_argent = float(nb_argent) + float(mise_joueur) + float(mise_gagnante)
                jeton3 = 1
                etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                jeton2 = 0
                nom = chemin1 + pseudo_connexion +".txt"
                argent = open(nom,"w", encoding="utf8")
                argent.write(str(nb_argent))
                argent.close()

    
    
    
                                     
                                     
            elif valeur_carte_joueur == valeur_carte_croupier :
                etiquette2.configure(text="Egalité !",fg="red",bg = "#00008B",font = carac_font)
                jeton3 = 1
                nb_argent = float(nb_argent) + float(mise_joueur)
                etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                jeton2 = 0
                nom = chemin1 + pseudo_connexion +".txt"
                argent = open(nom,"w", encoding="utf8")
                argent.write(str(nb_argent))
                argent.close()

    
    
    
                                     
                                     
            else :
                etiquette2.configure(text="Perdu ! - " + mise_joueur + "$",fg="red",bg = "#00008B",font = carac_font)
                jeton3 = 1
                etiquette.configure(text="Vous possédez sur votre compte : " + str(nb_argent) + "$",fg="pink",bg = "#00008B",font = carac_font)
                jeton2 = 0
                nom = chemin1 + pseudo_connexion +".txt"
                argent = open(nom,"w", encoding="utf8")
                argent.write(str(nb_argent))
                argent.close()

    
           
    #On affecte la fonction check au bouton : 
    bouton_2.bind("<ButtonPress-1>",stand)
    
    
    
    

    
    
    # =============================================================================
    # #Fonction pour miser :
    # =============================================================================
    def miser (event) :
        global jeton, mise_joueur,nb_argent, jeton3, tour, argent,chemin1, etiquette_mise
        
#        On crée ce jeton comme démarage du jeu, le joueur ne peut appuyer sur start sans avoir misé
        jeton = 1
        mise_joueur = entree_mise.get()
    
       

        if float(mise_joueur) > float(nb_argent) or float(mise_joueur) < 0 :
            
            etiquette_mise.configure(text="Ce n'est pas possible !!!",fg="pink",bg = "#00008B",)
            jeton = 0
             
      
        else :

            nb_argent = float(nb_argent) - float(mise_joueur)
            nom = chemin1 + pseudo_connexion +".txt"
            argent = open(nom,"w", encoding="utf8")
            argent.write(str(nb_argent))
            argent.close()


            
            etiquette_mise.configure(text="Votre mise est de "+str(mise_joueur)+"$",fg="pink",bg = "#00008B",)
            etiquette_mise.grid(row=2,column=2,padx=5,pady=5)
            
            

#Le jeton 3 signifie la fin de la partie on réinitialise alors toutes les variables utilisé précédemment     
        if jeton3 == 1 :
    
            tour = 0
                
            
        jeton3 = 0    
        
        
    
    
    bouton_4.bind("<ButtonPress-1>",miser)
    
    
    
    fenetre.mainloop()
    
    
############################################################################
############################################################################
############################################################################
############################################################################   
    
def mas (event) :
    global  canevas,tour,wallet, mise,actualiser_mise,nouvelle_mise,autorisation,nb_argent,argent
    fenetre5.withdraw()
    try :
        fenetre6.destroy()
    except :
        pass
    #variable importante pour la suite
    chemin1 = "Wallet/"
     
    #Code de la fenêtre principale :

    # creation d"une fenetre
    machine = Toplevel()
    machine.title("Machine à sous")
    machine.configure(bg = "#00008B")
                      
    # creation des differents cadres
    zone_1 = Frame(machine)
    zone_1.grid(row=1,column=1,padx=10,pady=10)
    zone_1.configure(bg ="#00008B")

    zone_2 = Frame(machine)
    zone_2.grid(row=1,column=35,padx=10,pady=10,)
    zone_2.configure(bg ="#00008B")
        
    # creation des boutons du cadre zone_2
    bouton_1 = Button(zone_2)
    bouton_1.configure(text="SPIN",bg = "pink", width="6", height="4")
    bouton_1.grid(row=1,column=1,padx=10,pady=30)

    bouton_2 = Button(zone_2)
    bouton_2.configure(text="Retour au menu Jeu",bg = "pink", width="16", height="4")
    bouton_2.grid(row=25,column=1,padx=10,pady=30)

    bouton_3 = Button(zone_2)
    bouton_3.configure(text="Valider",bg = "pink", width="10", height="2")
    bouton_3.grid(row=17,column=1,padx=10,pady=3)



    # création de l'étiquette qui indique quel est la mise de base   
    etiquette_mise_base = Label(zone_2)
    etiquette_mise_base.configure(text="La mise de base est de 5$",bg="#00008B",fg="pink")
    etiquette_mise_base.grid(row=15,column=1,padx=10,pady=10)

    # création de l'étiquette qui indique la zone de saisie pour augmenter la mise  
    etiquette_mise_changer = Label(zone_2)
    etiquette_mise_changer.configure(text="Entrez ici une mise différente si vous le souhaitez : ",bg="#00008B",fg="pink")
    etiquette_mise_changer.grid(row=16,column=1,padx=10,pady=10)

    # création de l'étiquette qui indique si nous avons gagné
    etiquette_resultat = Label(zone_2)
    etiquette_resultat.configure(text="",bg="#00008B",fg="pink")
    etiquette_resultat.grid(row=18,column=1,padx=10,pady=10)


    #zone de saisie pour changer la mise
    mise = StringVar()
    entree_mise = Entry(zone_2, textvariable=mise.get(), width=5)
    entree_mise.grid(row=16,column=2,padx=5,pady=5)



    canevas = Canvas(zone_1)


    #création et redimensionnement des futures images
    im = Image.open("images/image1.png")
    im = im.resize((80,80))
    im.save(("images/image1_redim.png"))

    im2 = Image.open("images/image2.png")
    im2 = im2.resize((80,80))
    im2.save(("images/image2_redim.png"))

    im3 = Image.open("images/image3.png")
    im3 = im3.resize((80,80))
    im3.save(("images/image3_redim.png"))

    im4 = Image.open("images/image4.png")
    im4 = im4.resize((70,70))
    im4.save(("images/image4_redim.png"))

    #On transforme ces images en images Tkinter
    illustration1 = ImageTk.PhotoImage(file="images/image1_redim.png")
    illustration2 = ImageTk.PhotoImage(file="images/image2_redim.png")
    illustration3 = ImageTk.PhotoImage(file="images/image3_redim.png")

    #chargement de l'image de fond de la zone_1
    illustration = Image.open("images/blackjack_red_pr_medhi.png")
    illustration = illustration.resize((500,300))
    illustration.save(("images/blackjack_red_pr_medhi_redim.png"))
    illustration = ImageTk.PhotoImage(file = "images/blackjack_red_pr_medhi_redim.png")
    canevas.create_image(0,0,image=illustration, anchor=NW)

    canevas.configure(width=500,height=300, bg ="#00008B")

    # Création de la zone de texte indiquant l'argent que l'on possède 
    texte_argent =  canevas.create_text(400,10,text="Vous possèdez : "+str(nb_argent)+"$",fill="pink" )


    # Cette variable autorise ou non la machine à se mettre en marche si on possède la somme autorisée
    autorisation = True
    actualiser_mise = False


    canevas.pack()




    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################







    ### Création de la fonction qui fera activer la roue 

    def spin (event) :
        global  canevas,tour,wallet, mise,actualiser_mise,nouvelle_mise,autorisation,nb_argent
        
        
        
        ### Le tour servira comme compteur
        tour= 0
        
        if autorisation == True :
            if actualiser_mise == True :
                mise = nouvelle_mise
            else :
                mise = 5
            nom = chemin1 + pseudo_connexion +".txt"
            argent = open(nom,"w", encoding="utf8")
            nb_argent = float(nb_argent) - float(mise)
            argent.write(str(nb_argent))
            ### créations des coordonnées des futures images
            x = 10
            x2 = 145
            x3 = 280
            y = 0
            y2 = 100
            
            ### On détruit les images du spin précédents si il y en a eu un     
             
            canevas.delete("all")
            
            
            canevas.create_image(0,0,image=illustration, anchor=NW)
            canevas.configure(width=500,height=300, bg ="#00008B")
            texte_argent =  canevas.create_text(400,10,text="Vous possèdez : "+ str(nb_argent)+"$",fill="pink" )
                
                
        
        ### Si elles n'existent pas on passe cette instruction    
        
            
            # On crée chaque images et on les placent
            id_im = canevas.create_image(x, y, image=illustration1, anchor=NW)
            id_im2 = canevas.create_image(x2, y, image=illustration2, anchor=NW)
            id_im3 = canevas.create_image(x3, y, image=illustration3, anchor=NW)
            
            id_im4 = canevas.create_image(x, y2, image=illustration2, anchor=NW)
            id_im5 = canevas.create_image(x2, y2, image=illustration1, anchor=NW)
            id_im6 = canevas.create_image(x3, y2, image=illustration3, anchor=NW)
            
            # Ceci est l'animation du déroulement des images 
            #Condition qui va faire tourner en boucle les images tant que le compteur sera inférieur à 75
            while tour < 75 :
                    
                if y == 150 or y2 == 285:
                    a = False 
                    
                if y == 0 or y2 == 135 :
                    a = True 
                if a : #Si les conditions des coordonnées sont vraies, les images font descendre
                    y = y+5
                    y2 = y+100
                    canevas.coords(id_im,x,y)
                    canevas.coords(id_im2,x2,y)
                    canevas.coords(id_im3,x3,y)
                    
                    
                        
                    canevas.coords(id_im4,x,y2)
                    canevas.coords(id_im5,x2,y2)
                    canevas.coords(id_im6,x3,y2)
                    
                        
                        
                        
                else : #Sinon elles vont se supprimer et remonter, ce qui donnera un effet de déroulement
                   
                    #On supprime les images qui sont en bas du canvas
                    canevas.delete(id_im)
                    canevas.delete(id_im2)
                    canevas.delete(id_im3)
                   
                    canevas.delete(id_im4)
                    canevas.delete(id_im5)
                    canevas.delete(id_im6)
                    
                    # On redonne les coordonnées de base à y et a y2
                    y = 0
                    y2 = 100 
                    
                    
                    liste_fruit_chiffre = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4]
                    # On donne une  valeur à chaque variable grâce au random
                    a = random.randint(0,30)
                    b = random.randint(0,30)
                    c = random.randint(0,30)
                    
                    d = random.randint(0,30)
                    e = random.randint(0,30)
                    f = random.randint(0,30)
                    
                    var1 = liste_fruit_chiffre[a]
                    var2 = liste_fruit_chiffre[b]
                    var3 = liste_fruit_chiffre[c]
                    
                    var4= liste_fruit_chiffre[d]
                    var5= liste_fruit_chiffre[e]
                    var6= liste_fruit_chiffre[f]
                    
                    # Ces variables sont utilisées pour chargées une nouvelle image aléatoirement 
                    illu = ImageTk.PhotoImage(file="images/image" + str(var1) +"_redim.png" )
                    illu2 = ImageTk.PhotoImage(file="images/image" + str(var2) +"_redim.png" )
                    illu3 = ImageTk.PhotoImage(file="images/image" + str(var3) +"_redim.png" )
                    
                    illu4 = ImageTk.PhotoImage(file="images/image" + str(var4) +"_redim.png" )
                    illu5 = ImageTk.PhotoImage(file="images/image" + str(var5) +"_redim.png" )
                    illu6 = ImageTk.PhotoImage(file="images/image" + str(var6) +"_redim.png" )
                    
                    # On fait réapparaitre les canvas qu'on avait supprimé avec de nouvelles images et avec les coordonnées de base
                    id_im = canevas.create_image(x, y, image = illu , anchor=NW)
                    id_im2 = canevas.create_image(x2, y, image = illu2, anchor=NW)
                    id_im3 = canevas.create_image(x3, y, image = illu3, anchor=NW)
                    
                    id_im4 = canevas.create_image(x, y2, image = illu4, anchor=NW)
                    id_im5 = canevas.create_image(x2, y2, image = illu5, anchor=NW)
                    id_im6 = canevas.create_image(x3, y2, image = illu6, anchor=NW)
                    
                    # Le compteur de tour prend +1
                    tour = tour +1
                    
                    #le temps d'arret entre chaque actualisation de coordonnée est de un centième de seconde
                    time.sleep(0.01)
                
                # On actualise le canvas 
                canevas.update()
                if tour == 75 :
                
        
                    
                    illu = ImageTk.PhotoImage(file="images/image" + str(var1) +"_redim.png" )
                    illu2 = ImageTk.PhotoImage(file="images/image" + str(var2) +"_redim.png" )
                    illu3 = ImageTk.PhotoImage(file="images/image" + str(var3) +"_redim.png" )
                    
        
                    id_im_fin = canevas.create_image(x+20, 110, image = illu , anchor=NW)
                    id_im2_fin = canevas.create_image(x2+20, 110, image = illu2, anchor=NW)
                    id_im3_fin = canevas.create_image(x3+20, 110, image = illu3, anchor=NW)
                    
        
                    canevas.image = illu, illu2, illu3
                    
                    
                    # Instauration des règles 
                    if var1 == var2 and var1 == var3 and var1==1 :
                        nb_argent = float(nb_argent) + float(mise)*1.5 +float(mise) 
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        etiquette_resultat.configure(text="Vous avez gagné 1.5x votre mise !",bg="#00008B",fg="pink")
                        
                    
                    elif var1 == var2 and var1 == var3 and var1==2 :
                        nb_argent = float(nb_argent) + float(mise)*5 +float(mise)
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        etiquette_resultat.configure(text="Vous avez gagné 5x votre mise !",bg="#00008B",fg="pink")
                       
                    
                    elif var1 == var2 and var1 == var3 and var1==3 :
                        nb_argent = float(nb_argent) + float(mise)*7.5 +float(mise)
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        etiquette_resultat.configure(text="Vous avez gagné 7.5x votre mise !",bg="#00008B",fg="pink")
                        
                        
                    elif var1 == var2 and var1 == var3 and var1==4 :
                        nb_argent = float(nb_argent) + float(mise)*50 +float(mise)
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        etiquette_resultat.configure(text="Vous avez gagné 50x votre mise !",bg="#00008B",fg="pink")
                        print("Vous avez désormais " + str(wallet) +"$")
                        
                    elif var1 == var2 and var1 != var3 and var1 ==1 :
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        etiquette_resultat.configure(text="Vous avez perdu !",bg="#00008B",fg="pink")
                        
                        
                    elif var1 == var2 and var1 != var3 and var1==2 :
                        print("Le quart de votre mise vous est rendu!")
                        nb_argent = float(nb_argent) + float(mise)*0.25
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        etiquette_resultat.configure(text="Le quart de votre mise vous est rendu !",bg="#00008B",fg="pink")
                        
                        
                    elif var1 == var2 and var1 != var3 and var1==3 :                        
                        etiquette_resultat.configure(text="Le tiers de votre mise vous est rendu!",bg="#00008B",fg="pink")
                        nb_argent = float(nb_argent) + float(mise)*(1/3)
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        
                        
                    elif var1 == var2 and var1 != var3 and var1==4 :
                        etiquette_resultat.configure(text="Votre mise vous est rendu!",bg="#00008B",fg="pink")
                        nb_argent = float(nb_argent) + float(mise)
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        
                        
                    elif var1 != var2 and var2 != var3 :
                        etiquette_resultat.configure(text="Vous avez perdu votre mise !",bg="#00008B",fg="pink")
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        
                    elif var1 != var2 and var1 == var3 :
                        etiquette_resultat.configure(text="Vous avez perdu votre mise !",bg="#00008B",fg="pink")
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                    
                    elif var1 != var2 and var2 == var3 :
                        etiquette_resultat.configure(text="Vous avez perdu votre mise !",bg="#00008B",fg="pink")
                        nom = chemin1 + pseudo_connexion +".txt"
                        argent = open(nom,"w", encoding="utf8")
                        argent.write(str(nb_argent))
                        
                    canevas.update()
            actualiser_mise = False
            etiquette_mise_base.configure(text="La mise de base est de 5$",bg="#00008B",fg="pink")
            
            canevas.delete(texte_argent)
            texte_argent =  canevas.create_text(400,10,text="Vous possèdez : "+str(nb_argent)+"$",fill="pink" )
            autorisation = True
            
            
            
            
            
    #################################################################
    #################################################################    
    #################################################################    
    #################################################################    
    ################################################################# 



               
    def bouton_valider (event):
        global mise,actualiser_mise,nouvelle_mise,autorisation,nb_argent
        
        nouvelle_mise = entree_mise.get()
        actualiser_mise = True
        
        if float(nouvelle_mise) > float(nb_argent) :
            etiquette_mise_base.configure(text="Vous ne possédez pas cette somme.",bg="#00008B",fg="pink")
            autorisation = False                              
             
        else :    
            etiquette_mise_base.configure(text="Votre nouvelle mise est de : " + str(nouvelle_mise) +  "$",bg="#00008B",fg="pink")
            autorisation = True
        
        

            
    bouton_1.bind("<ButtonPress-1>",spin)
    bouton_2.bind("<ButtonPress-1>",menu_4)
    bouton_3.bind("<ButtonPress-1>",bouton_valider)
    machine.mainloop()












# attente des evenements
fenetre.mainloop()




