### TP Analyse les logs des Users
## Objectif : A partir d'une liste de connexions, Determiner :
## 1. Le Nombre Total d'Acces par User
## 2. Les Users les plus actifs (>3 Acces)

## Data :
logs = ["alice", "bob", "alice", "charlie", "bob", "bob", "david", "bob"]


### Nombre D'acces par User
data_user_log = {}

for user in logs:
    if user in data_user_log:
        data_user_log[user] += 1
    else: 
        data_user_log[user] = 1

##3 Filtrage USER > 3
data_user_log_actif = {}

for user in data_user_log:
    if data_user_log[user] > 3:
        data_user_log_actif[user] = data_user_log[user]
    

## Affichage Resultat USER :
print("\n---- ALL USER ----") 
for user in data_user_log:
    print(f"\nUser : {user}\nAcces : {data_user_log[user]}")

print("\n---- USER Actif ----")
## Affichage Resultat Filtrage: 
for user in data_user_log_actif: 
    print(f"\nUser : {user}\nAcces : {data_user_log_actif[user]}")