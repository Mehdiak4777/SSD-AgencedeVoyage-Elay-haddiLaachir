class Date:
    def __init__(self, jour, mois, annee):
        # Constructeur de la classe Date
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def saisir_date(self, message):
        # Méthode pour saisir une date
        print(message)
        self.jour = input("Jour : ")
        self.mois = input("Mois : ")
        self.annee = input("Année : ")
        return f"{self.jour}/{self.mois}/{self.annee}"

class OffreVoyage:
    def __init__(self, ref_offre, ville_depart, ville_arrivee):
        # Constructeur de la classe OffreVoyage
        self.ref_offre = ref_offre
        self.ville_depart = ville_depart
        self.ville_arrivee = ville_arrivee

    def saisir_offre_voyage(self):
        # Méthode pour saisir les détails d'une offre de voyage
        self.ref_offre = input("Entrer la référence de l'offre : ")
        self.ville_depart = input("Entrer la ville de départ : ")
        self.ville_arrivee = input("Entrer la ville d'arrivée : ")

    def afficher_offre_voyage(self):
        # Méthode pour afficher les détails d'une offre de voyage
        print(f"Ref_Offre: {self.ref_offre}\nVille de départ: {self.ville_depart}\nVille d'arrivée: {self.ville_arrivee}")

    def __str__(self):
        return "Offre: Voyage"

    def bloquer_offre(self):
        # Méthode pour bloquer une offre
        self.etat_offre = 'Bloquée'
        print('Cette offre est Bloquée')

class Hebergement:
    def __init__(self, date_debut, nbre_de_nuit, type_hebergement, prix_nuit):
        # Constructeur de la classe Hebergement
        self.date_debut = Date(0, 0, 0)
        self.nbre_de_nuit = nbre_de_nuit
        self.type_hebergement = type_hebergement
        self.prix_nuit = prix_nuit

    def saisir_hebergement(self):
        # Méthode pour saisir les détails d'un hébergement
        self.date_debut.saisir_date("Entrer la date de début : ")
        self.nbre_de_nuit = input("Entrer le nombre de nuit : ")
        self.type_hebergement = input("Entrer le type d'hébergement (déjeuner, demi-pension, pension complète) : ")
        self.prix_nuit = input("Entrer le prix de la nuit : ")

    def afficher_hebergement(self):
        # Méthode pour afficher les détails d'un hébergement
        print(f"Date de début hébergement: {self.date_debut}\nNombre de nuit: {self.nbre_de_nuit}\nType d'hébergement: {self.type_hebergement}\nPrix de la nuit: {self.prix_nuit}")

    def bloquer_offre(self):
        # Méthode pour bloquer une offre
        self.etat_offre = 'Bloquée'
        print('Cette offre est Bloquée')

    def ligne_hebergement(self):
        return f"Date de début hébergement : {self.date_debut},\nNombre de nuit : {self.nbre_de_nuit},\nType d'hébergement : {self.type_hebergement},\nPrix de nuit : {self.prix_nuit}"

    def sauvegarder_dans_fichier(self, nom_fichier):
        with open(nom_fichier, 'a') as f:
            f.write(self.ligne_hebergement())

class OffreTransportAllerSimple(OffreVoyage):
    def __init__(self, ref_offre, ville_depart, ville_arrivee, date, prix):
        # Constructeur de la classe OffreTransportAllerSimple
        super().__init__(ref_offre, ville_depart, ville_arrivee)
        self.date = Date(0, 0, 0)
        self.prix = prix

    def saisir_aller_simple(self):
        # Méthode pour saisir les détails d'une offre de transport aller simple
        self.saisir_offre_voyage()
        self.prix = input("Entrer le prix : ")
        self.date.saisir_date("Entrer la date de départ : ")

    def update_price(self, prix):
        # Méthode pour mettre à jour le prix d'une offre de transport aller simple
        self.prix = prix

    def update_date(self):
        # Méthode pour mettre à jour la date de départ d'une offre de transport aller simple
        self.date = Date(0, 0, 0)
        self.date.saisir_date("Entrer la nouvelle date")

    def affichage_aller_simple(self):
        # Méthode pour afficher les détails d'une offre de transport aller simple
        print(f"Ville de départ: {self.ville_depart}\nVille d'arrivée: {self.ville_arrivee}\nDate de départ: {self.date}\nPrix: {self.prix}")

    def bloquer_offre(self):
        # Méthode pour bloquer une offre
        self.etat_offre = 'Bloquée'
        print('Cette offre est Bloquée')

    def ligne_transport_aller_simple(self):
        return f"Référence du offre: {self.ref_offre},\nVille de départ: {self.ville_depart},\nVille d'arrivée: {self.ville_arrivee},\nDate de départ: {self.date},\nPrix: {self.prix}"

    def sauvegarder_dans_fichier(self, nom_fichier):
        with open(nom_fichier, 'a') as f:
            f.write(self.ligne_transport_aller_simple())
            
class Offre_Transport_Aller_Retour(Offre_Transport_Aller_Simple):
 def _init_(self, Ref_offre, Ville_depart, Ville_arrivee, date, date_arrivee, Prix):
 # Appeler le constructeur de la classe mère (Offre_Transport_Aller_Simple)
 super()._init_(Ref_offre, Ville_depart, Ville_arrivee, date, Prix)
 
 # Initialiser l'attribut date_arrivee en tant qu'objet Date avec les valeurs par défaut
 self.date_arrivee = Date(0, 0, 0)
 def Saisir_Aller_Retour(self):
# Appeler la méthode Saisir_Aller_simple de la classe parent pour traiter les entrées communes 
 self.Saisir_Aller_simple()
# Saisissez l'attribut spécifique de la date de retour
 self.date_arrivee = self.date_arrivee.Saisir_Date("Entrer la date d'arrivee : ")
 def Affichage_Aller_Retour(self):
# Appeler la méthode Affichage_Aller_simple de la classe parentale pour afficher les informations 
communes
 self.Affichage_Aller_simple()
 # Afficher l'attribut spécifique de la date de retour
 print('la date d arrivee :', self.date_arrivee)
 def Bloquer_Offre(self):
# Définir l'attribut etat_offre à 'Bloquer' et imprimer un message
 self.etat_offre = 'Bloquee'
 print('Cette offre est Bloquee')
 def ligneTransportAR(self):
# Retourne une chaîne formatée avec des informations sur l'offre de transport
 return (
 f"Reference du offre : {self.Ref_offre}, \n"
 f"Ville de depart : {self.Ville_depart},\n "
 f"Ville d'arrivee: {self.Ville_arrivee},\n "
 f"Date de depart : {self.date},\n "
 f"Date d'arrivee : {self.date_arrivee},\n"
 f"Prix :{self.Prix},\n"
 )
class Formule_complet(Offre_Transport_Aller_Retour, Hebergement):
 def _init_(self, Ref_offre='', Ville_depart='', Ville_arrivee='', date=Date(0, 0, 0), Prix=0, 
date_depart=Date(0, 0, 0),
 Type='', date_arrivee=Date(0, 0, 0), Date_debut=Date(0, 0, 0), Nbre_de_nuit=0, 
Prix_nuit=0):
 # Appeler les constructeurs de classes mères pour initialiser les attributs
 Offre_Transport_Aller_Retour._init_(self, Ref_offre, Ville_depart, Ville_arrivee, date, 
date_depart, date_arrivee,Prix)
 Hebergement._init_(self, Date_debut, Nbre_de_nuit, Type, Prix_nuit)
 def Saisir_Complet(self):
# Appeler des méthodes à partir de classes parentales pour gérer des entrées spécifiques
 self.Saisir_Aller_Retour()
 self.Saisir_Hebergement()
 def Affichage_Complet(self):
 # Appeler les méthodes des classes parentales pour afficher des informations spécifiques
 self.Affichage_Aller_Retour()
 self.Afficher_Hebergement()
 def SauvegarderDansFichier(self, NomFichier):
# Écrire des informations spécifiques à un fichier
 with open(NomFichier, 'a') as F:
 F.write(self.ligneTransportAR())
 F.write(self.ligneHebergement())
 def Bloquer_Offre(self):
# Définir l'attribut etat_offre à 'Bloquer' et imprimer un message
 self.etat_offre = 'Bloquee'
 print('Cette offre est Bloquee')
class Reservation:
 def _init_(self):
 # Initialiser les attributs pour la reservation
 self.Ref_reservation = ''
 self.Type_Offre = ""
 self.Ref_Offre = ""
 self.Date_depart = Date(0, 0, 0)
 self.Date_de_retour = Date(0, 0, 0)
 self.Genre = ''
 self.Nom = ''
 self.prenom = ''
 self.Pays = ''
 self.n_passport = ''
 self.Etat_Reservation = "en cours"
 self.prix_hebergement = 0
 self.prix_voyage_simple = 0
 self.prix_voyage_AR = 0
 self.Total_A_Payer = 0
 def CreateReservation(self):
 # Collecter des informations pour créer une réservation basée sur l'entrée de l'utilisateur
 self.Ref_reservation = input("Entrer le referance de reservation : ")
 print("List des offres : ")
 print("1 - Voyage A")
 print("2 - Voyage A/R")
 print("3 - Accommodation")
 print("4 - Formule complet")
 choice = int(input("Choix:"))
 self.Type_Offre = choice
 self.Ref_Offre = input("Entrer le reference du offre : ")
 self.Date_depart = self.Date_depart.Saisir_Date('Entrer la date de depart')
 if choice == 2 or choice == 4:
 self.Date_de_retour = self.Date_de_retour.Saisir_Date('Entrer la date de retour')
 self.Genre = input("Entrer le genre: ")
 self.Nom = input("Entrer le Nom: ")
 self.prenom = input("Entrer le Prenom: ")
 self.Pays = input("Entrer la nationalite : ")
 self.n_passport = input("Entrer le Numero de passport : ")
 if choice == 1:
 self.prix_voyage_simple = input("Entrer le prix du voyage simple : ")
 self.Total_A_Payer = self.prix_voyage_simple
 elif choice == 2:
 self.prix_voyage_AR = input("Entrer le prix du voyage Aller-Retour : ")
 self.Total_A_Payer = self.prix_voyage_AR
 elif choice == 3:
 self.prix_hebergement = input("Entrer le prix d hebergement : ")
 self.Total_A_Payer = self.prix_hebergement
 elif choice == 4:
 self.prix_voyage_AR = input("Entrer le prix du voyage Aller-Retour : ")
 self.prix_hebergement = input("Entrer le prix d hebergement : ")
 self.Total_A_Payer = self.prix_voyage_AR + self.prix_hebergement
 def Confirmer_reservation(self):
# Définir l'attribut État_Réservation à "Confirme"
 self.Etat_Reservation = "Confirmee"
 def Annuler_reservation(self):
# Définir l'attribut Etat_Réservation comme « Annulé »
 self.Etat_Reservation = "Annulee"
 def LigneReservation(self):
 return (
 f"Reference de reservation : {self.Ref_reservation}, \n"
 f"Type d offre : {self.Type_Offre},\n"
 f"Referene du offre : {self.Ref_Offre},\n"
 f"Date de depart : {self.Date_depart},\n"
 f"Date de retour : {self.Date_de_retour},\n"
 f"Le genre : {self.Genre},\n"
 f"Le nom : {self.Nom},\n"
 f"Le prenom : {self.prenom},\n"
 f"Le pays : {self.Pays},\n"
 f"N_Passport : {self.n_passport},\n"
 f"Etat de reservation : {self.Etat_Reservation},\n

