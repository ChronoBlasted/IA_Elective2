# 🎮 Générateur de Description de Jeu Vidéo 🎮

Ce projet utilise un modèle de langage pré-entraîné de Hugging Face (`GPT-2` version française) pour générer des descriptions de jeux vidéo fictifs. En entrant une idée de jeu vidéo, l'application génère une description créative basée sur l'idée fournie par l'utilisateur.

## 🌐 Lien vers l'application

Vous pouvez accéder à l'application hébergée en ligne à l'adresse suivante :  
[https://alexisgelinprojetiagen.streamlit.app/](https://alexisgelinprojetiagen.streamlit.app/)

## 🚀 Fonctionnalités

- **Génération automatique de descriptions de jeu vidéo** : Entrez une idée de jeu et laissez l'IA générer une description complète et créative.
- **Paramètres ajustables** :
  - **Longueur maximale de la description** : Contrôlez la longueur de la description générée.
  - **Créativité** : Ajustez la température pour rendre le texte plus ou moins créatif.
  - **Réflexion/Choix** : Ajustez le nombre de faisceaux (beam search) pour améliorer la qualité du texte généré.

## 💡 Idée du Projet

L'application permet à l'utilisateur de décrire brièvement une idée de jeu vidéo, puis le modèle générera une description originale et imaginative pour ce jeu, en se basant sur les paramètres définis par l'utilisateur.

## 🛠️ Technologies

- **Streamlit** : Pour la création de l'interface utilisateur interactive.
- **Transformers** : Pour l'utilisation du modèle pré-entraîné de Hugging Face (`GPT-2` en français).
- **PyTorch** : Utilisé pour l'exécution du modèle de langage.

## 🔧 Prérequis

Avant de pouvoir exécuter l'application localement, vous devez installer les bibliothèques suivantes :

1. **Transformers** : Pour charger et utiliser le modèle GPT-2.
2. **Torch** : La bibliothèque nécessaire pour exécuter les modèles pré-entraînés de Hugging Face.
3. **Streamlit** : Pour créer l'interface web de l'application.

## 🖥️ Exécution de l'application

1. Clonez ou téléchargez le projet sur votre machine locale.
2. Accédez au répertoire contenant le script Python de votre application.
3. Lancez l'application avec la commande suivante : 
streamlit run votre_script.py


## 🎨 Interface Utilisateur

- **Saisie de l'idée de jeu** : Vous pouvez entrer une idée de jeu dans une zone de texte.

### Paramètres ajustables :

- **Longueur maximale de la description** : Vous pouvez définir la longueur de la description générée.
- **Température** : Ajustez la "créativité" du texte généré. (Plus la température est élevée, plus le texte sera créatif.)
- **Nombre de faisceaux** : Ajustez le nombre de faisceaux pour améliorer la qualité du texte généré. (Plus élevé = meilleure qualité, mais plus lent.)

### Bouton "Générer" :

Appuyez sur le bouton "Générer" pour obtenir une description basée sur l'idée de jeu que vous avez fournie.

## 📄 Exemple

### Entrée de l'utilisateur :
Idée de jeu : "Un jeu de rôle d'aventure dans un monde futuriste."

### Sortie générée par l'IA :
Description : "Dans ce jeu de rôle futuriste, les joueurs explorent des mondes lointains à la recherche de nouvelles technologies pour sauver l'humanité. À travers des batailles stratégiques et des choix de dialogue, les joueurs devront décider du destin de la planète."

## 🛠️ Contribuer

Si vous souhaitez contribuer à ce projet, voici quelques façons de le faire :

- Proposez de nouvelles idées de fonctionnalités.
- Améliorez la génération de texte ou la qualité du modèle.
- Corrigez les bugs ou améliorez la documentation.
