# Django, Database, Git & GitHub
Approche "Database First" dans Django :
1.	J'ai utilisé **PostgreSQL** à la place de MySQL pour créer une base de données nommée « ecole » avec les champs « etudiants » ayant ces propriétés : id, prénom, nom, pays, adresse, téléphone.
2.	J'ai rempli la base de donnée avec les informations de 11 étudiants.
3.	J'ai créé un projet Django « écoles » puis un environnement virtuel "env" et une application appelée « école » 
4.	J'ai créé un modèle Django et à l'intérieur un fichier « index.html » dans lequel j'ai utilisé du bootstrap pour le navbar et le tableau.
5.	J'ai connecté ma base de données "école" au projet.
6.	J'ai créé un modèle pour interagir avec la base de données.
7.	Ensuite, j'ai affiché les informations du champ « étudiants » sur ma page principale (index.html).
8.	Dans le navigateur, lorsque je tape : http://127.0.0.1:8000/, après avoir exécuté cette commande: python manage.py runserver, les informations des 11 étudiants se sont affichées.

![Screenshot (288)](https://github.com/stherlove03/Devoir-2/assets/89224789/ae08b668-ab59-452b-bceb-e3652619352d)

# Création d'un utilisateur SuperAdmin :
1.	J'ai créé une nouvelle branche Git appelée « superadmin ».
2.	J'ai créé un utilisateur super administrateur dans cette branche.
3.	J'ai accédé au tableau de bord super administrateur et ajouté cinq nouveaux étudiants dans la base de données (via le tableau de bord administrateur).
4.	Ensuite, j'ai affiché les informations du champ « étudiants » sur la page principale (index.html).
5.	Dans le navigateur, lorsque je tape: http://127.0.0.1:8000/, les informations des 11 étudiants se sont affichées. ainsi que les 5 nouveaux étudiants que j'ai ajoutés.

  
La photo ci-dessous montre le tableau qui s'affiche avec les informations des étudiants.
![Screenshot (290)](https://github.com/stherlove03/Devoir-2/assets/89224789/5eb5a6e0-a91b-440a-ba7f-cf91ce35019a)

La photo ci-dessous montre l'interface administrateur dans laquelle figure les informations des étudiants.
![Screenshot (291)](https://github.com/stherlove03/Devoir-2/assets/89224789/3931df0a-99ab-4d22-925d-ae8582a7c362)


