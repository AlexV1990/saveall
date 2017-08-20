#! /usr/bin/env python3

from dialog import Dialog
from utils.modconf import *
from utils.misc import *

if __name__ == '__main__':

  d = Dialog(dialog="dialog")
  d.set_background_title("Saveall script")

  de_menu_choixaction = "OK"

  #Vérification de la validité
  if check_conf_valid() == -1:
    d.msgbox("Fichier de configuration invalide.")
    de_menu_choixaction = "cancel"

  #Boucle jusqu'à quitter le menu
  while de_menu_choixaction != "cancel":

    # MENU1: choix de l'action à effectuer : lancer, gérer équipements, gérer fichiers
    de_menu_choixaction, tag_menu_choixaction = d.menu("Choix de l'action à effectuer", 
                          choices=[("1", "Lancer procédure de sauvegarde"), 
                          ("2", "Gérer équipements"), 
                          ("3", "Gérer liste des fichiers à sauvegarder")])

    #code retour du MENU1
    if de_menu_choixaction == "cancel":
        print ("Thanks for using saveall script")
    else:
      
      #
      # MENU2: GERER EQUIPEMENTS
      if tag_menu_choixaction == "2":

        # Choix de l'action
        de_menu2, tag_menu2 = d.menu("Gestion des équipements",
                           choices=[("20", "Ajouter un équipement"),
                                    ("21", "Supprimer un équipement")])
        
        #
        # Ajouter un équipement
        if tag_menu2 == "20":

          #Formulaire description équipement
          code_menu20, list_menu20 = d.form("Ajout d'un équipement",
                           elements=[("Nom", 1, 1, "", 1, 8, 25, 25),
                                     ("IP", 2, 1, "", 2, 8, 25, 25),
                                     ("Type", 3, 1, "", 3, 8, 25, 25),
                                     ("Login", 4, 1, "", 4, 8, 25, 25),
                                     ("MDP", 5, 1, "", 5, 8, 25, 25)])

          is_list_valid = check_list_equipment_valid(list_menu20)
          if is_list_valid  == 0:
            add_equipment_to_conf(list_menu20)
            d.msgbox("Equipement ajouté avec succès.")
          else:
            if is_list_valid == -1:
              d.msgbox("Equipement non ajouté: le nom fourni existe déjà.")
            if is_list_valid == -2:
              d.msgbox("Equipement non ajouté: l'IP fournie n'est pas valable")
            if is_list_valid == -3:
              d.msgbox("Equipement non ajouté: l'IP fournie existe déjà")
            if is_list_valid == -4: 
              d.msgbox("Equipement non ajouté: type non reconnu (DB, S ou R") 
            if is_list_valid == -5: 
              d.msgbox("Equipement non ajouté: tous les champs doivent être complétés.")
        #
        # Supprimer un équipement
        if tag_menu2 == "21":
          
          list_eq = get_list_equipment_from_conf()

          if len(list_eq) > 0:
            de_menu_deleq, tag_menu_deleq = d.menu("Choix de l'action à effectuer", choices= list_eq)
            if delete_equipment_from_conf(tag_menu_deleq) == 0:
              d.msgbox("Equipement supprimé avec succès")
            else:
              d.msgbox("Erreur lors de la suppression de l'équipement, équipement non supprimé")
          else:
            d.msgbox("Pas d'équipement à supprimer...")

      #
      # MENU3: GERER FICHIERS
      if tag_menu_choixaction == "3":

        # Choix de l'action
        de_menu3, tag_menu3 = d.menu("Gestion des équipements",
                           choices=[("30", "Ajouter un fichier"),
                                    ("31", "Supprimer un fichier")])

        #
        # Ajouter un fichier
        if tag_menu3 == "30":

          #Formulaire description fichier
          code_menu30, list_menu30 = d.form("Informations sur le fichier",
                           elements=[("Nom", 1, 1, "", 1, 8, 25, 25),
                                     ("Path", 2, 1, "", 2, 8, 25, 25),
                                     ("Type", 3, 1, "", 3, 8, 25, 25)])

          #
          #Choix des équipements sur lequel aller sauvegarder le fichier
          list_eq = get_list_equipment_from_conf_for_checklist()

          if len(list_eq) > 0: 
            code, tags = d.checklist("Equipement concerné", choices=list_eq, title="Sélection de l'équipement", backtitle="Sauvegarde de fichiers ")   
          else:
            d.msgbox("Pas d'équipement enregistré...")  

          #Ajout du fichier en conf
          list_menu30.append(tags)
          add_file_to_conf(list_menu30)
        
        #
        # Supprimer un fichier
        if tag_menu3 == "31":
         
          #
          #Choix du fichier à supprimer via un menu
          list_fic = get_list_files_from_conf()

          if len(list_fic) > 0:
            de_menu_delfic, tag_menu_delfic = d.menu("Choix du fichier à supprimer", choices= list_fic)
            if delete_file_from_conf(tag_menu_delfic) == 0:
              d.msgbox("Fichier supprimé avec succès")
            else:
              d.msgbox("Erreur lors de la suppression du fichier, fichier non supprimé")

          else:
              d.msgbox("Pas de fichier à supprimer...")

      else:
          "Thanks for using saveall script"