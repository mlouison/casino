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
    
# creation des differents cadres
zone_1 = Frame(fenetre)
zone_1.grid(row=1,column=1,padx=10,pady=10)

zone_2 = Frame(fenetre)
zone_2.grid(row=1,column=2,padx=10,pady=10)

# creation d’une etiquette dans le cadre zone_1
etiquette = Label(zone_1)
etiquette.configure(text="Bienvenue dans notre Casino !",fg="blue")
etiquette.grid(row=1,column=1,padx=10,pady=10)


# creation des boutons du cadre zone_2
bouton_1 = Button(zone_2)
bouton_1.configure(text="Connexion",bg="red", width="25", height="4")
bouton_1.grid(row=1,column=1)

bouton_2 = Button(zone_2)
bouton_2.configure(text="Nouveau compte",bg="white", width="25", height="4")
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

##    Création de zones
    zone_1 = Frame(fenetre2)
    zone_1.grid(row=1,column=1,padx=10,pady=10)

    zone_2 = Frame(fenetre2)
    zone_2.grid(row=1,column=2,padx=10,pady=10)

    #zone de saisie et étiquette pour la connexion
    etiquette = Label(zone_1)
    etiquette.configure(text="Entrer votre pseudo :",fg="blue")
    etiquette.grid(row=1,column=1,padx=10,pady=10)
    
    
    etiquette2 = Label(zone_1)
    etiquette2.configure(text="Entrer votre mot de passe : ",fg="blue")
    etiquette2.grid(row=2,column=1,padx=10,pady=10)
    
    
    etiquette3 = Label(zone_1)
    etiquette3.configure(text="",fg="blue")
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
                    etiquette3.configure(text="Vous êtes maintenant connecté",fg="red")
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
    bouton_3.configure(text="Valider",bg="red", width="25", height="3")
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

##    Création de zones
    zone_1 = Frame(fenetre3)
    zone_1.grid(row=1,column=1,padx=10,pady=10)

    zone_2 = Frame(fenetre3)
    zone_2.grid(row=1,column=2,padx=10,pady=10)

    #zone de saisie et étiquette pour la connexion
    etiquette = Label(zone_1)
    etiquette.configure(text="Entrer votre nouveau pseudo :",fg="blue")
    etiquette.grid(row=1,column=1,padx=10,pady=10)
    
    
    etiquette2 = Label(zone_1)
    etiquette2.configure(text="Entrer votre nouveau mot de passe : ",fg="blue")
    etiquette2.grid(row=2,column=1,padx=10,pady=10)
    
    etiquette3 = Label(zone_1)
    etiquette3.configure(text="",fg="blue")
    etiquette3.grid(row=3,column=1,padx=10,pady=10)
    
    

    pseudo = StringVar()
    entree_pseudo = Entry(zone_2, textvariable=pseudo.get(), width=30)
    entree_pseudo.grid(row=1,column=1,padx=10,pady=10)
    
    
    mdp = StringVar()
    entree_mdp = Entry(zone_2, textvariable=mdp.get(), width=30)
    entree_mdp.grid(row=2,column=1,padx=10,pady=10)


    


#Fonction qui permet la création d'un nouveau compte :  
    def Nouveau_compte (event) :
        global entree_pseudo,fenetre4, fenetre6,fenetre3, fenetre2, fenetre5, chemin1, pseudo_connexion, entree_mdp,new_pseudo,new_mdp,verif_pseudo,chemin, a,nb_argent, keyIndex, crypted,num, pseudo_connexion,argent
        a = 0
        chemin = "fichiers_texte/"
        chemin1 = "Wallet/"
    
    
        while a != 5 :

            new_pseudo = entree_pseudo.get()
            new_mdp = entree_mdp.get()
           
            try :
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
    bouton_4.configure(text="Valider",bg="red", width="25", height="3")
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
    global pseudo_connexion, fenetre4, fenetre6,fenetre3, fenetre2, fenetre5, fenetre6,argent,machine
    try:
        
        fenetre4.destroy()
        fenetre3.destroy()
        fenetre6.destory()
        machine.destroy()

    except:
        pass
    fenetre5 = Toplevel()
    fenetre5.title("Menu du joueur")      
    
    # creation des differents cadres
    zone_1 = Frame(fenetre5)
    zone_1.grid(row=1,column=1,padx=10,pady=10)

    zone_2 = Frame(fenetre5)
    zone_2.grid(row=1,column=2,padx=10,pady=10)
    
    zone_3 = Frame(fenetre5)
    zone_3.grid(row=2,column=2,padx=10,pady=10)
    
    zone_4 = Frame(fenetre5)
    zone_4.grid(row=2,column=1,padx=10,pady=10)
    
    zone_5 = Frame(fenetre5)
    zone_5.grid(row=3,column=1,padx=10,pady=10)
    
    zone_6 = Frame(fenetre5)
    zone_6.grid(row=3,column=2,padx=10,pady=10)
    
   
    

    # Utilisation de new pseudo et pseudo connexion car l'utilisateur peut soit venir de s'inscrire ou de se connecter
    etiquette = Label(zone_1)
    etiquette.configure(text="Bienvenue " + pseudo_connexion + " !" ,fg="blue")
    etiquette.grid(row=1,column=1,padx=10,pady=10)
    
    etiquette = Label(zone_2)
    etiquette.configure(text="Vous avez actuellement "+ str(nb_argent) + "$ !" ,fg="blue")
    etiquette.grid(row=1,column=1,padx=10,pady=10)



    # creation des boutons du cadre zone_2
    bouton_1 = Button(zone_3)
    bouton_1.configure(text="Blackjack",bg="red", width="25", height="4")
    bouton_1.grid(row=1,column=1)
    
    bouton_2 = Button(zone_4)
    bouton_2.configure(text="Machine à sous",bg="white", width="25", height="4")
    bouton_2.grid(row=2,column=1,padx=10,pady=10)
    
    bouton_3 = Button(zone_5)
    bouton_3.configure(text="La roulette",bg="white", width="25", height="4")
    bouton_3.grid(row=2,column=1,padx=10,pady=10)
    
    bouton_4 = Button(zone_6)
    bouton_4.configure(text="Soon",bg="white", width="25", height="4")
    bouton_4.grid(row=2,column=1,padx=10,pady=10)
    
    
    
    
    bouton_2.bind("<ButtonPress-1>",mas)

    
    
############################################################################
############################################################################
############################################################################
    
    
    
def mas (event) :
    global  canevas,tour,wallet, mise,actualiser_mise,nouvelle_mise,autorisation,nb_argent,argent

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
    bouton_1.configure(text="SPIN",bg = "#E6E6FA", width="6", height="4")
    bouton_1.grid(row=1,column=1,padx=10,pady=30)

    bouton_2 = Button(zone_2)
    bouton_2.configure(text="Retour au menu Jeu",bg = "#E6E6FA", width="16", height="4")
    bouton_2.grid(row=25,column=1,padx=10,pady=30)

    bouton_3 = Button(zone_2)
    bouton_3.configure(text="Valider",bg = "#E6E6FA", width="10", height="2")
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
    texte_argent =  canevas.create_text(400,10,text="Vous possèdez : "+str(nb_argent)+"$",fill="black" )


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
            texte_argent =  canevas.create_text(400,10,text="Vous possèdez : "+ str(nb_argent)+"$",fill="black" )
                
                
        
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
            texte_argent =  canevas.create_text(400,10,text="Vous possèdez : "+str(nb_argent)+"$",fill="black" )
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


    
    
    ##Le problème est avec les étiquettes et avec le bouton check.



# attente des evenements
fenetre.mainloop()




