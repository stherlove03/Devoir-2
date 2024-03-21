Part 3 - Django, Database, Git & GitHub 
Approche "Database First" dans Django :
1.	Utilisez MySQL pour créer une base de données nommée « ecole » avec les champs « etudiants » ayant ces propriétés : id, prénom, nom, pays, adresse, téléphone.
2.	Créez un projet Django « écoles » puis une application appelée « école ».
3.	Créez un modèle Django et à l'intérieur un fichier « index.html ».
4.	Connectez votre base de données à votre projet.
5.	Créez un modèle pour interagir avec la base de données.
6.	Ensuite, affichez les informations du champ « étudiants » sur votre page principale (index.html).
7.	Dans le navigateur, lorsque vous tapez : http://127.0.0.1:8000/, vous devriez voir s'afficher toutes les informations de vos étudiants.
8.	Fournissez une capture d'écran de votre résultat.
9.	Fournissez le lien de votre projet Django sur GitHub.
10.	Fournissez un fichier Readme.md, qui explique comment vous avez procédé pour construire cette application.

Au lieu d'utiliser MySQL, j'ai plutôt utiliser PostgreSQL. Dans ce dernier, j'ai créé la base de donnéesn ommée « ecole » avec les champs « etudiants » ayant ces propriétés : id, prénom, nom, pays, adresse, téléphone. J'ai rempli la table avec des données. 
J'ai créé le projet django "ecoles" en utilisant le terminal Windows Powershell. Au lieu d'utiliser la commande django-admin startproject "nomprojet" , j'ai utilisé à la place python -m django startproject "nomprojet", pour un problème dont je ne connais pas,
la première ligne de commande ne voulait pas créer le projet django.

