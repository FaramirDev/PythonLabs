===========================================
## ANALYSEUR DE TEXTE - README
===========================================

---

## 1. DESCRIPTION
--------------
Ce programme Python analyse un texte saisi par l'utilisateur et fournit :
- Le nombre de mots
- Le nombre de lettres (sans compter les espaces)
- Le nombre d'espaces
- Le nombre total de caractères
- La fréquence d'apparition de chaque lettre

## 2. FONCTIONNALITÉS
-------------------
- Analyse complète d'un texte en temps réel
- Calcul précis du nombre de mots et de lettres
- Détection des fréquences d'apparition des lettres
- Affichage clair et organisé des résultats
- Gestion des majuscules/minuscules

## 3. UTILISATION
--------------
**Etape 1 :** 
Exécutez le script avec Python :
   python main_analyse_texte.py

**Etape 2 :** 
Le programme vous demandera d'entrer un texte à analyser

**Etape 3 :** 
Après avoir saisi votre texte, le programme affichera :
   - Le nombre de mots
   - Le nombre de lettres (sans espaces)
   - Le nombre d'espaces
   - Le nombre total de caractères
   - La fréquence d'apparition de chaque lettre

## 4. EXEMPLE D'UTILISATION
```
------------------------
=== ANALYSEUR DE TEXTE ===
Veuillez entrer votre texte à analyser : Bonjour tout le monde

--- RÉSULTATS DE L'ANALYSE ---
Nombre de mots : 4
Nombre de lettres (sans espaces) : 15
Nombre d'espaces : 3
Nombre total de caractères : 18

Fréquence des lettres :
  - 'b' : 1 fois
  - 'd' : 1 fois
  - 'e' : 2 fois
  - 'j' : 1 fois
  - 'l' : 1 fois
  - 'm' : 1 fois
  - 'n' : 2 fois
  - 'o' : 3 fois
  - 'r' : 1 fois
  - 't' : 2 fois
  - 'u' : 1 fois

```


## 7. EXIGENCES
------------
- Python 3.x
- Aucune bibliothèque externe requise


## 9. NOTES TECHNIQUES
--------------------
- Le programme convertit tout en minuscules pour l'analyse
- Les espaces sont comptés mais pas inclus dans l'analyse des lettres
- Les caractères spéciaux et la ponctuation sont ignorés
- Le programme utilise des dictionnaires pour stocker les fréquences
