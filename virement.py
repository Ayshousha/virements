from datetime import date

# Open the source and destination files
source = open("virements.txt", 'r')
destination = open('FMONDAT.MUT', 'w+')

# Get today's date in the required format
today = date.today().strftime("%d/%m/%Y")

# Write the header to the destination file
destination.write("DEBUT FICHIER MUT " + today + "\n")

# Read all lines from the source file
lignes = source.readlines()

# Define a dictionary template to store the transaction details
dic = {
    "Code_mouvement": '',
    "RIB": '',
    "Raison_sociale": '',
    "Montant_du_virement": '',
    "Code_opération": ''
}

# List to hold all transaction details
resultat = []

# Process each line from the source file
for i in range(len(lignes)):
    ligne = lignes[i]
    
    if i == 0:
        # For the first line, set specific values
        dic["Code_mouvement"] = "D"
        dic["RIB"] = "10104059109504278843"
        dic["Raison_sociale"] = "MUTUELLELELECTRICITEGAZ  "
        dic["Montant_du_virement"] = ligne[28:43].strip()
        dic["Code_opération"] = "VOAU"
    else:
        # For subsequent lines, extract values from specific positions
        dic["Code_mouvement"] = "B"
        dic["RIB"] = ligne[105:125].strip()
        dic["Raison_sociale"] = ligne[125:150].strip()
        dic["Montant_du_virement"] = ligne[28:43].strip()
        dic["Code_opération"] = "VOAU"
    
    # Append a copy of the dictionary to the result list
    resultat.append(dic.copy())

# Write each transaction detail to the destination file
for entry in resultat:
    destination.write(
        entry["Code_mouvement"] +
        entry["RIB"] +
        entry["Raison_sociale"] +
        entry["Montant_du_virement"] +
        entry["Code_opération"] +
        "\n"
    )

# Write the footer to the destination file
destination.write("FIN FICHIER MUT " + today + "\n")

# Close the files
source.close()
destination.close()
