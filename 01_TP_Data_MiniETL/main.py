### Creation Mini ETL sans Pandas
## 1. Lire le Fichier
## 2. Filter
## 3. Nettoyer
## 4. Transformer
## 5. Save version Clean

## DATA : 
path_data_brut = "01_TP_Data_MiniETL/data/employes.csv"
path_data_clean = "01_TP_Data_MiniETL/data/employes_clean.csv"

with open(path_data_brut, "r") as f:
    readlines = f.readlines()

data_work = readlines

## == Filtrage & Clean ==
## RECUP ONLY DATA ok
data_clean = []
data_clean_temp = []


for data in data_work:
    data_split = data.strip().split(',') 
    if len(data_split) == 5 and "" not in data_split:
        data_clean_temp.append(data_split)
         
for data in data_clean_temp:
    if data == data_clean_temp[0]:
        data_clean.append(data)

    elif data != data_clean_temp[0]:
        try: 
            age = int(data[2])
            data_clean.append(data)
        except ValueError:
            pass

print(data_clean)


### ECRIRE DE CSV Clean
with open(path_data_clean, "w") as f:
    for data in data_clean:
        f.write(f"{data}\n")

 