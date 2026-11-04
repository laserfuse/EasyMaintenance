# 🌟 EasyMaintenance
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-blue.svg)

EasyMaintenance est un outil simple et moderne destiné à faciliter la maintenance de Windows.  
Développé en Python dans le cadre d’un Travail de Fin d’Études (TFE), il regroupe plusieurs actions de diagnostic et de nettoyage dans une interface unique et accessible.

**Version actuelle : 0.1.1**

---

## 🖥️ Présentation du projet

L’objectif d’EasyMaintenance est de proposer une solution centralisée permettant d’effectuer rapidement plusieurs opérations de maintenance Windows, sans devoir taper manuellement des commandes système.

L’application utilise **CustomTkinter** pour offrir une interface moderne et intuitive, adaptée aux utilisateurs débutants comme avancés.

---

## 📦 Installation & utilisation (version compilée)

### 🔹 1. Télécharger la dernière version

Rendez-vous sur la page des Releases du projet et téléchargez `EasyMaintenance.exe` :

👉 **https://github.com/laserfuse/EasyMaintenance/releases/latest**

### 🔹 2. Lancer le logiciel

```text
EasyMaintenance.exe
```

Le logiciel peut demander les droits administrateur (UAC), car certaines actions de maintenance nécessitent ces autorisations.

---

## 🔧 Utilisation depuis le code source

Si vous souhaitez exécuter le projet depuis le code source :

### 1. Prérequis

- Python 3.10 ou plus récent  
- Git (optionnel, pour cloner le dépôt)

---

### 2. Cloner le dépôt ou télécharger le code

Via Git :

```bash
git clone https://github.com/laserfuse/EasyMaintenance.git
cd EasyMaintenance
```

Ou en téléchargeant le ZIP du code source depuis GitHub, puis en l’extrayant.

---

### 3. Installer les dépendances

Dans le dossier du projet, exécutez :

```bash
pip install -r requirements.txt
```

Les principales dépendances sont :

- requests
- customtkinter
- wmi
- psutil
- packaging

---

### 4. Lancer l’application

Depuis le dossier du projet, lancez :

```bash
python main.py
```

L’application peut demander les droits administrateur au démarrage.

## ✨ Fonctionnalités principales

### 🧩 Informations système

- Version de Windows  
- Quantité de RAM  
- Informations générales sur la machine  

---

## 💾 Gestion du stockage

Affichage des disques avec :

- Espace total  
- Espace utilisé  
- Espace libre  

---

## 🛠️ Maintenance Windows

Exécution automatisée de plusieurs commandes système :

- Nettoyage des fichiers temporaires  
- Vérification système avec `sfc /scannow`  
- Réparation de l’image Windows avec `DISM /Online /Cleanup-Image /RestoreHealth`  
- Vérification du disque avec `chkdsk /scan`  
- Réinitialisation du cache DNS  
- Réinitialisation réseau  
- Redémarrage du service Windows Update  
- Affichage de la sortie des commandes dans l’application, sans fenêtre CMD séparée  
- Exécution des commandes en arrière-plan pour garder l’interface réactive  

---

## 🤝 Contribution

Ce projet a été réalisé dans le cadre d’un Travail de Fin d’Études et continue d’évoluer.  
Toute contribution est la bienvenue :

- Suggestions d’amélioration  
- Corrections de bugs  
- Optimisations du code  
- Améliorations de l’interface  
- Documentation  

Vous pouvez :

- ouvrir une issue  
- proposer une pull request  

---

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

---

## 🎉 Remerciements

Merci d’utiliser EasyMaintenance.  
Le projet est encore jeune et amené à évoluer 
— vos retours et idées sont les bienvenus.