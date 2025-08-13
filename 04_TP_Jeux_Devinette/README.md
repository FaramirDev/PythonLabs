===========================================
## JEU DE DEVINETTE
===========================================

---

**1. DESCRIPTION**
--------------
Ce script Python implémente un simple jeu de devinette où le joueur doit
trouver un nombre secret compris entre 1 et 100. Le jeu donne des indices
("plus grand" ou "plus petit") à chaque essai et compte le nombre de tentatives.

**2. FONCTIONNALITÉS**
-------------------
- Génération aléatoire d'un nombre entre 1 et 100
- Système d'indices pour guider le joueur
- Compteur du nombre d'essais
- Messages de félicitations personnalisés
- Interface simple et intuitive


**3. COMMENT JOUER**
-----------------
**Etape 1 :** 
- Exécutez le script avec Python :
   python devinette.py

**Etape 2 :** 
- Le jeu vous demandera de deviner un nombre entre 1 et 100

**Etape 3 :** 
- À chaque essai, le jeu vous indiquera si le nombre secret est :
   - Plus grand que votre proposition
   - Plus petit que votre proposition

**Etape 4 :** 
- Continuez jusqu'à trouver le bon nombre

**Etape 5 :** 
- À la fin, le jeu vous félicitera et vous indiquera le nombre d'essais nécessaires


**4. EXEMPLE DE PARTIE**
```
--------------------
Devinez mon nombre compris entre 1 et 100 ! Bonne chance !!!
Tape ici ---->50
Arf ! dommage, le nombre secret est plus petit ! Réessayez !

Mince Réessayez ici --->25
Arf ! dommage, le nombre secret est plus grand ! Réessayez !

Mince Réessayez ici --->37
Arf ! dommage, le nombre secret est plus petit ! Réessayez !

Mince Réessayez ici --->30
Ouiiii Bravooooo !! Comment tu gères ! Tu as trouvé le bon nombre, et oui c'était bien 30 !!
Tu as réussi en 4 essais !!
```

**5. PERSONNALISATION**
-------------------
Vous pouvez facilement modifier ces paramètres dans le code :
- La plage de nombres en changeant les valeurs de min et max
  (actuellement min=1, max=100)
- Les messages de feedback pour les rendre plus personnalisés

**6. AMÉLIORATIONS POSSIBLES**
---------------------------
- Ajouter un système de scores
- Implémenter un mode difficile avec une plage plus large
- Ajouter un compte à rebours pour limiter le temps de jeu
- Garder un historique des meilleures performances
- Ajouter des niveaux de difficulté variables
- Implémenter un système de vies limitées
- Ajouter des indices supplémentaires après un certain nombre d'essais

**7. NOTES TECHNIQUES**
--------------------
- Utilise le module random pour générer le nombre secret
- Gère les entrées utilisateur avec validation basique
- Compte précisément le nombre d'essais
- Affiche des messages encourageants

**8. EXIGENCES SYSTÈME**
---------------------
- Python 3.x
- Aucune bibliothèque externe requise

**9. INSTALLATION**
---------------
1. Enregistrez le code dans un fichier nommé main_play.py
2. Exécutez simplement avec Python :
   python main_play.py

**10. CRÉDITS**
-----------
Jeu de devinette classique implémenté en Python par Faramir.

