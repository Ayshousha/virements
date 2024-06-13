def partie(ch):
    # Suppression de la chaîne "110117000"
    ch = ch.replace('110117000', '')
    
    # Inversion des chaînes spécifiques
    ch = ch.replace('17001000000302388764', 'TEMP_REPLACEMENT_1')
    ch = ch.replace('2024FOCHI0384OPERATION CHIRURGICAL', 'TEMP_REPLACEMENT_2')
    ch = ch.replace('TEMP_REPLACEMENT_1', '000131104012086006134058494')
    ch = ch.replace('TEMP_REPLACEMENT_2', '2024LP548965000LP REMBOURSEMENTDESFRAISMED')
    
    # Extraction de la sous-chaîne et insertion à la position 9
    sous_chaine = ch[18:24]
    ch = ch[:9] + sous_chaine + ch[9:]
    
    l = len(ch[125:163])
    ch1 = ch[125:163].replace(' ', '')
    n = l - len(ch1)
    for i in range(n):
        ch1 = ch1 + " "
    ch = ch[:125] + ch1 + ch[163:]
    ch = "110104   " + ch
    return ch

fichier1 = r"C:\Users\aysha\Desktop\attijari\source\source.txt"
fichier2 = r"C:\Users\aysha\Desktop\attijari\destination\destination.txt"

with open(fichier1, 'r', encoding='utf-8') as f1, open(fichier2, 'w', encoding='utf-8') as f2:
    for i, ligne in enumerate(f1):
        # Suppression de la chaîne "110117000"
        ligne = ligne.replace('110117000', '')
        
        # Inversion des chaînes spécifiques pour toutes les lignes
        ligne = ligne.replace('17001000000302388764', 'TEMP_REPLACEMENT_1')
        ligne = ligne.replace('2024FOCHI0384OPERATION CHIRURGICAL', 'TEMP_REPLACEMENT_2')
        ligne = ligne.replace('TEMP_REPLACEMENT_1', '04012086006134058494')
        ligne = ligne.replace('TEMP_REPLACEMENT_2', '2024LP548965000LP REMBOURSEMENTDESFRAISMED')
        
        if i == 0:
            # Soustraction du dernier chiffre de la première ligne par 1
            if ligne.strip():  # Vérifier que la ligne n'est pas vide
                # Trouver le dernier caractère numérique
                for j in range(len(ligne)-1, -1, -1):
                    if ligne[j].isdigit():
                        dernier_chiffre = int(ligne[j]) - 1  # Convertir en entier et soustraire 1
                        nouveau_dernier_chiffre = str(dernier_chiffre)  # Reconvertir en chaîne
                        ligne = ligne[:j] + nouveau_dernier_chiffre + ligne[j+1:]  # Reconstruire la ligne
                        break
            
            ligne_modifiee = "110104   " + ligne
        else:
            # Extraction de la sous-chaîne et insertion à la position 9
            sous_chaine = ligne[18:24]
            ligne = ligne[:9] + sous_chaine + ligne[9:]
            ligne_modifiee = partie(ligne)
        
        f2.write(ligne_modifiee)
