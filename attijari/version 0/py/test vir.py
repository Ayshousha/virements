from functools import partial


source= open("virements.txt", 'r')
destination=open('attijari.vir', 'w+')
destination.write("\n")
dic={"Code_mouvement":'', "RIB":'', "Date":'', "Montant":'', "Code_opération":'',"partie1":"","partie2":"","partie3":"",}
resultat=[]

lignes = source.readlines()
for i in range(0,len(lignes)):
    if i ==0:
        ligne=str(lignes[i])
        dic["Code_mouvement"]="110104"
        dic["Date"]=ligne[10:17]
        dic["RIB"]=ligne[18:38]
        dic["Montant"]=ligne[37:46]
        dic["Nb_dossiers"]=ligne[47:]
        resultat.append(dic.copy())
    else:
        ligne=str(lignes[i])     
    code_mouvement = "110104"
    partie1 = ligne[10:74]
    partie2 = ligne[101:140]
    partie3 = ligne[164:243]=str("2024LP548965000LP REMBOURSEMENTDESFRAISMED")
    resultat.append(dic.copy())

for i in range(len(resultat)):
    print(resultat[i])
    destination.write ( resultat[i].get("Code_mouvement") +"   "+ resultat[i].get("partie1")+"                          "+resultat[i].get("partie2")+"                          "+resultat[i].get("partie3"))
    destination.write("\n")