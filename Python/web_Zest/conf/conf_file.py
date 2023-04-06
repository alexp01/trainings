
menu = {"Se déplacer" : ["Préparer un itinéraire",
                         "Télécharger les horaires",
                         "Télécharger les plans",
                         "Moovit",
                         "Réserver un service à la demande",
                         "Service Mobizest",
                         "Scolaire & Périscolaire",
                         "Réseau TER"
                         "Ligne 608 Nice - Menton",
                         "Ligne 110 Aéroport - Menton",
                         "TAD ROYA"],
        "E-boutique" : ["Accès E-boutique"],
        "Titres et tarifs": ["Quel titre choisir ?",
                             "Titres et tarifs",
                             "E-boutique",
                             "Agence de la gare routière",
                             "Guichet unique de Beausoleil",
                             "Dépositaire ticket 10 voyages",
                             "Pass Sud Azur",
                             "Avantages Club Zest"],
        "Tourisme" : None,
        "Contact" : None}

url = {"Accès E-boutique" : ["https://zest.airwebpass.com/", "https://zest.airwebpass.com/auth/"],
       "Télécharger les horaires" : "https://www.zestbus.fr/telecharger-les-horaires/"}

user1 = "tomhank1601@gmail.com"
user1_psw = "Tomhank2011#"

cards = [{"name" : "4111 1111 1111 1111", "month" : "Mai", "year" : "2025", "ccv" : "123" }]

card_errors = {"no_card" : "Numéro de carte absent", "expiration_fail" : "Date d'expiration invalide", "crypto_fail" : "Cryptogramme visuel vide ou invalide"}

lignes = [
"LIGNE 1 : Résédas - Gare routière - Marché - Frontière",
"LIGNE 2 : Suillet - Lycée P.M. Curie - Gare routière - Marché",
"LIGNE 3 : Val de Borrigo - Oliveraie - Gare routière - Marché",
"LIGNE 4 : Menton Gare Routière - Annonciade",
"LIGNE 5 : Menton Gare routière - EHPAD Gastaldy",
"LIGNE 6 : Castellar - Pinède Haute - Baousset ou Ciappes - Gare routière",
"LIGNE 7 : Gorbio - Azur Parc - Gare routière",
"LIGNE 8 : Menton Gare routière - Trabuquet - St Louis - Marché - Gare routière",
"LIGNE 10 : Sainte Agnès - Les oliviers - Vento - Menton Gare Routière",
"LIGNE 11 : La Turbie mairie - Stade du Devens - Beausoleil Eglise - Monaco Gare Pont Ste Dévôte",
"LIGNE 12 : Beausoleil Ténao - Eglise - Monaco Casino - Pont Ste Dévôte - Malbousquet - Les Platanes",
"LIGNE 13 : Beausoleil Ténao - Collège Bellevue - Eglise - Monaco Casino - Malbousquet",
"LIGNE 15 : Sospel - Castillon - Monti - Menton Gare Routière",
"LIGNE 18 : Monaco SNCF - Beausoleil Eglise - Roquebrune Mairie - Carnolès - Menton Pont St-Louis",
"LIGNE 21/22 : Vieux Roquebrune - St-Roman - Mairie - Carnolès - Peglion - Vieux Roquebrune",
"LIGNE 24 : Monaco SteDévôte - Beausoleil Eglise - Vieux Roquebrune - Carnolès - Menton Gare Routière",
"LIGNE 25 : Tende - Breil sur Roya - Vintimille - Menton Gare routière",
"Navettes Cimetières N1, N2 et N4",
"Navettes Stade du Devens : N3A et N3B",
"LIGNE N5 : Boucle de La Turbie",
"LIGNE B : Beausoleil Les Serres - Palais Gallia",
"LIGNE F : Moulinet - La Vasta - Sospel",
"LIGNE G : Cabbé gare - Mont Gros piste d'envol",
"LA NAVETTE",
"Lignes Touristiques - La desserte des sites remarquables",
"Circuits Scolaires",
"LIGNE H : Mairie de Beausoleil - École Ténao",
"Navette Marché de Sospel"
]

cities = [
"Beausoleil",
"Breil sur Roya",
"Castellar",
"Castillon",
"Fontan",
"Gorbio",
"La Brigue",
"La Turbie",
"Menton",
"Monaco",
"Roquebrune-Cap-Martin",
"Sainte-Agnès",
"Saorge",
"Sospel",
"Tende",
"Vintimille",
]

points = [
"Gare Routière de Menton",
"Plage de Sablettes",
"Marché de Menton",
"Garavan",
"Collège Vento",
"Casino de Menton",
"Casino de Monaco",
"Marché de Beausoleil",
"Carnolès",
"Marché de Carnolès",
"Vieux Roquebrune",
"Monastère de Saorge",
"Musée des Merveilles"
]

tickets_categories = [
"Tout sélectionner",
"Création support",
"Duplicata support",
"Tout public",
"Jeune",
"Tarif réduit",
"Ramassage scolaire"
]

ticket_categories = { "Création support" : [
                    { "name" : "Carte sans contact Zest", "price" : "2,00 €"}] ,
                    "Duplicata support" : [
                    { "name" : "Duplicata carte sans contact Zest", "price" : "10,00 €"}] ,
                    "Tout public": [
                    { "name" : "10 voyages (hors ligne 100)", "price" : "15,00 €"},
                    { "name" : "7 jours (hors ligne 100)", "price" : "13,00 €"},
                    { "name" : "1 mois Tout Public (hors ligne 100) avril", "price" : "38,00 €"},
                    { "name" : "1 an Tout Public (hors ligne 100)", "price" : "350,00 €"}],
                    "Jeune": [
                    { "name" : "1 mois Jeune -18 ans (hors ligne 100) avril", "price" : "12,00 €"},
                    { "name" : "1 an Jeune -18 ans", "price" : "112,00 €"},
                    { "name" : "1 mois Jeune 18 - 26 ans (hors ligne 100) avril", "price" : "12,00 €"},
                    { "name" : "1 an Jeune 18 - 26 ans", "price" : "112,00 €"}],
                    "Tarif réduit": [
                    { "name" : "1 mois Avantage (hors ligne 100) avril", "price" : "19,00 €"},
                    { "name" : "1 mois CMU - CSS (hors ligne 100) avril", "price" : "17,50 €"},
                    { "name" : "1 mois Citron (hors ligne 100) avril", "price" : "0,00 €"}],
                    "Ramassage scolaire": [
                    { "name" : "1 an ramassage scolaire", "price" : "10,00 €"}]}
