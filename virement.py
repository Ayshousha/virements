import logging
from datetime import date

# Configure logging
log_file='/log/execution.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log the start of execution
logging.info('Script execution started.')

# Open files
source= open("virements.txt", 'r', encoding="utf-8")
destination=open('FMANDAT.MUT', 'w+')

try:
    today = date.today().strftime("%d/%m/%Y")
    destination.write("DEBUT FICHIER MUT " + today + "\n")
    lignes = source.readlines()
    dic={"Code_mouvement":'', "RIB":'', "Raison_sociale":'', "Montant_du_virement":'', "Code_opération":''}
    resultat=[]
    
    for i in range(0,len(lignes)):
        if i ==0:
            ligne=str(lignes[i])
            dic["Code_mouvement"]=str("D")
            dic["RIB"]=str("10104059109504278843")
            dic["Raison_sociale"]=str("MUTUELLELELECTRICITEGAZ  ")
            dic["Montant_du_virement"]=ligne[28:43]
            dic["Code_opération"]=str("VOAU")
            resultat.append(dic.copy())
        else:
            ligne=str(lignes[i])
            dic["Code_mouvement"]=str("B")
            dic["RIB"]=ligne[105:125] 
            dic["Raison_sociale"]=ligne[125:150]
            dic["Montant_du_virement"]=ligne[28:43]
            dic["Code_opération"]=str("VOAU")
            resultat.append(dic.copy())
            
    for i in range(len(resultat)):
        print(resultat[i])
        destination.write(resultat[i].get("Code_mouvement") + resultat[i].get("RIB")+resultat[i].get("Raison_sociale")+resultat[i].get("Montant_du_virement")+resultat[i].get("Code_opération"))
        destination.write("\n")

    destination.write("FIN FICHIER MUT "+today)
    
    # Log success message
    logging.info('Execution completed successfully.')
    
except Exception as e:
    # Log error message
    logging.error(f'An error occurred: {str(e)}')

finally:
    # Close files
    source.close()
    destination.close()
