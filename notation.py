
note = 100
note_finale = 100
continuer = True
fesse = 0
tete = 0
sein = 0
corp = 0

continuer_tete = 0
continuer_sein = 0
continuer_fesse = 0
continuer_corp = 0
continuer_note = 0
continuer_note_finale = 0


print("Bonjour, ce programme va maintenant vous demander de répondre a un formulaire afin de noter une jeune donzelle sur 21 points.")
print(" ")
print("Pour répondre a chaque question veuillez répondre par le numéro qui correspond à une caractéristique de la demoiselle.")



while continuer:


    while continuer_tete == 0:
        print(" ")
        demande_tete = input("testas = moche(1);basique(2);belle(3);très belle(4) : ")
        demande_tete = int(demande_tete)
        print(" ")
        if demande_tete == 4:
            tete = 4
        if demande_tete == 3:
            tete = 3
        if demande_tete == 2:
            tete = 2
        if demande_tete == 1:
            tete = 1
        continuer_tete = 1
    while continuer_sein == 0:
        demande_poitrine = input("boobs = plat(1);moyen(2);gros(3);parfait(4) : ")
        print(" ")
        demande_poitrine = int(demande_poitrine)
        if demande_poitrine == 4:
            sein = 4
        if demande_poitrine == 3:
            sein = 3
        if demande_poitrine == 2:
            sein = 2
        if demande_poitrine == 1:
            sein = 1
        continuer_sein = 1
    while continuer_fesse == 0:
        demande_fesses = input("cul = plat(1);la moyenne(2);gros(3);parfait(4) : ")
        print(" ")
        demande_fesses = int(demande_fesses)
        if demande_fesses == 4:
            fesse = 4
        if demande_fesses == 3:
            fesse = 3
        if demande_fesses == 2:
            fesse = 2
        if demande_fesses == 1:
            fesse = 1
        continuer_fesse = 1
    while continuer_corp == 0:
        demande_corpulence = input("corp = obèse(1);grosse(2);petit ventre(3);abdos(4) : ")
        print(" ")
        demande_corpulence = int(demande_corpulence)
        if demande_corpulence == 4:
            corp = 4
        if demande_corpulence == 3:
            corp = 3
        if demande_corpulence == 2:
            corp = 2
        if demande_corpulence == 1:
            corp = 1
        continuer_corp = 1
    while continuer_note == 0:
        if tete == 4 and sein == 4 and fesse == 4:
            note = 20
        if tete == 4 and sein == 3 and fesse == 4:
            note = 19
        if tete == 4 and sein == 4 and fesse == 3:
            note = 18
        if tete == 4 and sein == 3 and fesse == 3:
            note = 17
        if tete == 3 and sein == 4 and fesse == 4:
            note = 16
        if tete == 3 and sein == 3 and fesse == 3:
            note = 15
        if tete == 3 and sein == 2 and fesse == 4:
            note = 14
        if tete == 3 and sein == 3 and fesse == 2:
            note = 13
        if tete == 3 and sein == 2 and fesse == 2:
            note = 12
        if tete == 2 and sein == 3 and fesse == 3:
            note = 12
        if tete == 2 and sein == 2 and fesse == 2:
            note = 11
        if tete == 2 and sein == 1 and fesse == 2:
            note = 10
        if tete == 2 and sein == 2 and fesse == 1:
            note = 9
        if tete == 2 and sein == 1 and fesse == 1:
            note = 8
        if tete == 1 and sein == 2 and fesse == 2:
            note = 7
        if tete == 1 and sein == 1 and fesse == 1:
            note = 5
        if tete == 4 and sein == 1 and fesse == 1:
            note = 15
        if tete == 4 and sein == 2 and fesse == 2:
            note = 16
        if tete == 1 and sein == 3 and fesse == 3:
            note = 11
        if tete == 4 and sein == 4 and fesse == 1:
            note = 14
        if tete == 3 and sein == 3 and fesse == 1:
            note = 13
        if tete == 4 and sein == 1 and fesse == 4:
            note = 16
        if tete == 4 and sein == 1 and fesse == 2:
            note = 14
        if tete == 4 and sein == 2 and fesse == 3:
            note = 16
        if tete == 3 and sein == 1 and fesse == 3:
            note = 13
        if tete == 3 and sein == 2 and fesse == 1:
            note = 12
        if tete == 1 and sein == 2 and fesse == 3:
            note = 9
        if tete == 2 and sein == 2 and fesse == 4:
            note = 12
        if tete == 2 and sein == 1 and fesse == 3:
            note = 10
        if tete == 1 and sein == 4 and fesse == 4:
            note = 11
        if tete == 2 and sein == 4 and fesse == 4:
            note = 13
        if tete == 2 and sein == 2 and fesse == 3:
            note = 12
        if tete == 2 and sein == 3 and fesse == 2:
            note = 11
        if tete == 3 and sein == 4 and fesse == 1:
            note = 14
        if tete == 4 and sein == 1 and fesse == 3:
            note = 15
        if tete == 1 and sein == 3 and fesse == 4:
            note = 10
        if tete == 2 and sein == 3 and fesse == 4:
            note = 14
        if tete == 4 and sein == 3 and fesse == 1:
            note = 14
        if tete == 3 and sein == 4 and fesse == 2:
            note = 14
        if tete == 1 and sein == 4 and fesse == 1:
            note = 8
        if tete == 1 and sein == 1 and fesse == 4:
            note = 9
        if tete == 1 and sein == 1 and fesse == 3:
            note = 7
        if tete == 1 and sein == 3 and fesse == 1:
            note = 7

        continuer_note = 1





    while continuer_note_finale == 0:
        if corp == 4:
            note_finale = note + 1
        if corp == 3:
            note_finale = note - 2
        if corp == 2:
            note_finale = note - 6
        if corp == 1:
            note_finale = note - 11
        continuer_note_finale = 1
    if note_finale < 10:
        print(" ")
        print("la note finale est : ", note_finale, "putain elle est claquer au sol si tu la connais bien fuis la et si tu la connait pas change de troitoir.")

    if note_finale > 9 and note_finale < 16:
        print(" ")
        print("la note finale est ", note_finale, "ca passe.")

    if note_finale > 15 and note_finale < 20:
        print(" ")
        print("la note finale est ", note_finale, "c'est du lourd ca.")

    if note_finale > 19 and note_finale < 30:
        print(" ")
        print("la note finale est ", note_finale, "epouse la tout de suite putain c'est une gazelle.")
    if note_finale > 50 and note_finale < 200:
        print(" ")
        print("deso le programme n'est pas encore capable de noter ce specimen")

    continuer_tete = 0
    continuer_sein = 0
    continuer_fesse = 0
    continuer_corp = 0
    continuer_note = 0
    continuer_note_finale = 0
    print(" ")
    quitter = input("Souhaitez-vous continuer de noter des meufs (appuyez sur la touche enter pour rester a la table ou sur la touche n pour arreter) ? ")
    if quitter == "n" or quitter == "N":
        continuer = False










