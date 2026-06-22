# EasyMaintenance
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-blue.svg)

## 🖥️ Présentation
Ce projet est un logiciel d’aide à la maintenance PC, développé en Python dans le cadre d’un Travail de Fin d’Études (TFE).  
L’application utilise CustomTkinter pour proposer une interface moderne et simple d’utilisation.

L’objectif est de regrouper plusieurs outils de maintenance Windows dans une interface centralisée et accessible.

## 🎓 Contexte TFE
Ce logiciel a été réalisé dans le cadre d’un Travail de Fin d’Études, avec pour objectif de proposer un outil simple permettant d’effectuer des opérations de maintenance Windows sans devoir utiliser manuellement les commandes système.

## ✨ Fonctionnalités actuelles

### 1. Informations système
Affiche les informations principales du PC :
- Version de Windows  
- Quantité de RAM  
- Informations générales sur la machine  

### 2. Stockage
Affiche tous les disques disponibles (ex : C:\, D:\, etc.) avec :
- Espace total  
- Espace utilisé  
- Espace libre  

### 3. Maintenance
Exécute plusieurs actions de maintenance via une fenêtre CMD :
- Nettoyage des fichiers temporaires  
- sfc /scannow  
- DISM /RestoreHealth  
- chkdsk /scan  
- Réinitialisation du cache DNS  
- Réinitialisation réseau  
- Redémarrage du service Windows Update  

## 🚀 Lancement du logiciel
Pour le moment, l’application se lance depuis Visual Studio Code via la commande :

```bash
python main.py
```

## 📄 Licence — CC BY‑NC 4.0
Ce projet est distribué sous licence Creative Commons Attribution – Non Commercial 4.0.

Vous êtes autorisé à :
- utiliser le logiciel  
- copier le logiciel  
- modifier le logiciel  

À condition de :
- créditer le projet original  
- ne pas vendre le logiciel  
- ne pas vendre le code  
- ne jamais proposer une version payante  

Le projet doit rester entièrement gratuit.
