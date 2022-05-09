# __Classes
Explication du contenu des différents fichiers du répertoire **__classes** de l'application FollowIt!

## Acces.class.php
Classe **Acces** représent un compte utilisateur (un accès à l'application)
#### Attributs :
| Nom            | Descripton								|
|----------------|------------------------------------------|
|code_acces      | Identifiant de l'utilisateur				|
|role			 | Role de l'utilisateur					|
|nom             | Nom de l'utilisateur						|
|prenom          | Prénom de l'utilisateur					|
|usine           | Usine de ratachement de l'utilisateur	|
|mail            | Adresse eMail de l'utilisateur			|
|date_accord     | Date à laquelle le compte a été créé 	|

#### Constructeur
le constructeur prend en paramètre un tableau associatif ou les clés sont les noms des attributs et l'objet **Acces** et les valeurs sont les données qu'on veut attribuer à l'objet.
*Exemple de construction d'un objet* ***Acces*** :
```
\$a = new Acces(array("code_acces"=>"TyJDupont1",
			"role"=>"lecteur"
			"nom"=>"Jean",
			"prenom"=>"Dupont",
			"usine"=>3));
```
Seules les valeurs *usine*, *code_acces* et *role* sont réelement importantes. Les autres sont uniquement là à titre informatif.
#### Getters and setters
La classe dispose de getters pour tous ses attributs mais d'aucun setters.
#### Méthodes dynamiques
##### getSecteurs()
Cette méthode  renvoie les informations sur le secteur de la machine sous la forme d'un objet (stdClass) avec deux attributs (id_secteur et nom_secteur) ou *False* si aucun secteur correspondant n'est trouvé.
Elle fait un appel à la base de données locale avec la requête SQL suivante :

##### modify(\$nom,\$prenom,\$role,\$mail)
Cette méthode modifie dans la base de données les colonnes *nom*, *prenom*, *role*, *mail* pour l'**Acces** sur lequel cette fonction a été appelée en les remplacant par les valeurs données en paramètre.
Ces quatre propriétés sont les seules qui peuvent être changées chez un **Acces**.

##### insert()
Cette méthode insère dans la base de données l'objet **Acces** sur lequel cette fonction a été appelée.

##### canBeModifyBy(\$session)
Cette méthode vérifie si l'**Acces** sur lequel elle est appelée peut être modifiée par l'utilisateur avec le *code_acces* fourni en paramètre.
Elle vérifie le rôle et l'usine de l'**Acces** et de l'utilisateur et renvoie *true* si l'utilisateur a le droit de modifier et *false* dans le cas contraire.

#### Méthodes statiques
##### getSecteurById(\$id_sect)
Cette méthode prend en paramètre un numéro de secteur est renvoie :
- *False* Si aucun secteur ne correspond à ce numéro.
- Les informations associées au secteur si le numéro de secteur est valide.

##### getAllSecteurs()
Cette méthode renvoie tous les secteurs contenus dans la base de données locale.

##### addSecteur(\$numSect, \$nom_sect = "")
Cette méthode ajoute un secteur dans la base de données locale

##### renameSect(\$num_sect, \$nom_sect)

##### deleteSect(\$num_sect)

##### getById(\$code_acces)
Cette méthode prend en parametre un code d'accès et renvoie :
- *False* si le code d'accès passé en parametre n'est pas valide
- les informations associées à ce compte sous la forme d'un objet **Acces** si le code d'accès est valide.

##### getAll()
Cette méthode ne prend aucun parametre et renvoie la liste de tous les comptes créés sous la forme d'un tableau d'objets **Acces**.

##### getUsersOfUsine(\$usine)
Cette méthode prend en paramètre un numéro d'*usine* et renvoie la liste de tout les **Acces** correspondant a des utilisateurs d'une usine (qui ne sont pas des super administrateurs).

##### delete(\$code_acces)
Supprime l'**Acces** ayant le *code_acces* passé en paramètre.

## Machine.class.php
Classe **Machine** représent une machine créée par un utilisateur
Cet objet implémente l'interface **JSONSerializable**.
#### Attributs :
| Nom        | Descripton                                       |
|------------|--------------------------------------------------|
|id		 	 | Identifiant de la machine						|
|code_acces	 | Code de l'utilisateur ayany créé cette machine	|
|usine		 | Usine dans laquelle se situe la machine			|
|sect		 | Secteur de la machine							|
|ssect		 | Sous secteur de la machine						|
|nomac		 | Numéro de la machine			 					|
|nom		 | Nom donné par l'utilisateur à cette machine 		|

#### Constructeur
le constructeur prend en paramètre un tableau associatif ou les clés sont les noms des attributs et l'objet **Machine** et les valeurs sont les données qu'on veut attribuer à l'objet.
*Exemple de construction d'un objet* ***Machine*** :
```
\$m = new Machine(array("code_acces"=>"RTJDupont1",
			"usine"=>"3",
			"sect"=>"2",
			"ssect"=>"1",
			"nomac"=>"14",
			"nom"=>"Onduleuse 14 Toury"));
```
#### Getters and setters
La classe dispose de getters pour tous ses attributs mais d'aucun setters.
#### Méthodes dynamiques
##### jsonSerialize()
Cette méthode renvoie un tableau représentant l'objet, permettant ainsi de le transformer en JSON.
Elle est obligatoire pour que l'objet **Machine** puisse implémenter l'interface **JSONSerializable**

##### insert()
Cette méthode insère ne base de données l'objet **Machine**.
L'attribut *Id* de l'objet devient alors l'Id attribué par le SGBD

##### rename()
Cette méthode met à jour le nom de la machine dans la base de données

##### delete()
Cette méthode supprime cet objet de la base de données

##### canBeModifyBy(\$session)
Cette méthode vérifie si la **Machine** sur laquelle elle est appelée peut être modifiée par l'utilisateur avec le *session* fourni en paramètre.
Elle vérifie le rôle et l'usine de l'**Acces** et de l'utilisateur et renvoie *true* si l'utilisateur a le droit de modifier et *false* dans le cas contraire.

#### Méthodes statiques
##### getById(\$id)
Cette méthode prend en parametre un id de machine et renvoie :
- *False* si l'id ne correspond à aucune machine
- les informations associées à cette machine sous la forme d'un objet **Machine** si le code d'accès est valide.

##### getByCodeMachine(\$code_acces, \$usine, \$sect, \$ssect, \$nomac)
Cette méthode prend en parametre un code d'acces et les informations d'une machine (usine, secteur, sous secteur et numéro de machine et renvoie
- *False* si les informations ne correspondent à aucune machine
- les informations associées à cette machine sous la forme d'un objet **Machine** si les informations sont valides.

##### getAllByUsine(\$usine)
Cette méthode recherche toutes les **Machines** faisant partie d'une même *usine* donnée en paramétre.
Elle retourne
- *False* si aucune machine n'est trouvée.
- Une liste d'objets de type **Machine** représentant les informations trouvés dans la base de données.

##### getAllBySecteur(\$sect)
Cette méthode recherche toutes les **Machines** faisant partie d'un même secteur (*sect*) donné en paramétre.
Elle retourne
- *False* si aucune machine n'est trouvée.
- Une liste d'objets de type **Machine** représentant les informations trouvés dans la base de données.

##### getAll()
Cette méthode ne prend aucun parametre et renvoie la liste de toutes les machines créées sous la forme d'un tableau d'objets **Machine**.

## Event.class.php
Classe **Event** représent un évenement apparaissant sur une machine dans la base de données AS400.
Cet objet implémente l'interface **JSONSerializable**.
#### Attributs :
| Nom        | Descripton					|
|------------|------------------------------|
|USINE		 | Code usine de la machine		|
|SECT		 | Secteur de la machine		|
|SSECT		 | Sous secteur de la machine	|
|NOMAC		 | Numéro de la machine			|
|FACONF		 | Numéro d'OF					|
|FASEQ		 | Numéro de séquence			|
|FAEVCO		 | Code d'évenement			 	|
|FAEVTY		 | Type d'opération			 	|
|PPHDEB		 | Heure de début d'évenement	|
|PPEQUI		 | Numéro d'équipe				|
|PPJJ		 | Jour					 		|
|PPMM		 | Mois					 		|
|PPAA		 | Année				 		|

#### Constructeur
Cette classe ne contient aucun constructeur.
Elle sert uniquement à récupérer et mapper les données de l'AS400.
#### Getters and setters
La classe dispose de getters pour tous ses attributs mais d'aucun setters.

#### Méthodes dynamiques
##### jsonSerialize()
Cette méthode renvoie un tableau représentant l'objet, permettant ainsi de le transformer en JSON.
Elle est obligatoire pour que l'objet **Event** puisse implémenter l'interface **JSONSerializable**

#### Méthodes statiques
##### getAll()
Cette méthode ne prend aucun paramètre et renvoie la liste de tous les évènements en cours sous la forme d'un tableau d'objets **Event**.

##### getAllByUsine(\$usine)
Cette méthode prend en paramètre un numéro d'usine et renvoie  la liste des évènements en cours sur les machines de l'usine sous la forme d'un tableau d'objets **Event**.

## NoWsEvent.class.php
Classe **NoWsEvent** représente l'enregistrement dans la base de données locale d'un évènement apparaissant sur une machine dans la base de données AS400.
Elle sert notamment à permettre à l'application de continuer de fonctionner presque normalement si la websocket n'est pas accessible.
#### Attributs :
| Nom        | Descripton					|
|------------|------------------------------|
|usine		 | Code usine de la machine		|
|sect		 | Secteur de la machine		|
|ssect		 | Sous secteur de la machine	|
|nomac		 | Numéro de la machine			|
|faconf		 | Numéro d'OF					|
|faseq		 | Numéro de séquence			|
|faevco		 | Code d'évenement			 	|
|faevty		 | Type d'opération			 	|
|pphdeb		 | Heure de début d'évenement	|
|ppequi		 | Numéro d'équipe				|
|ppjj		 | Jour					 		|
|ppmm		 | Mois					 		|
|ppaa		 | Année				 		|

#### Constructeur
Cette classe ne contient aucun constructeur.
Elle sert uniquement à récupérer et mapper les données de la base de données locale.

#### Méthodes statiques
##### updateLocalState(\$idMach, \$event)
Créé une nouvelle entrée dans la table local_state à partir de l'identifiant d'une machine et d'un objet **Event**.

##### getAllByUsine_noWs(\$usine)
Récupère l'état enregistré localement de toutes les machines d'une usine donnée retournant
- *false* si aucun état n'est enregistré localement
- Une liste de **NoWsEvent** contenant les états enregistrés de toutes les machines d'une usine donnée.

##### getAll()
Récupère l'état enregistré de toutes les machines suivies et renvoie une liste de **NoWsEvent**.

##### clear()
Supprime tous les états précédemment enregistrés.

## Historique.class.php
Classe **Historique** représente l'historique des états des machines enregistré dans la base de données locale.
#### Attributs :
| Nom        | Descripton							|
|------------|--------------------------------------|
|id_hist	 | Identifiant de l'historique			|
|id_machine	 | Identifiant de la machine associé	|
|usine	  	 | Code d'usine de la machine			|
|sect	  	 | Secteur de la machine				|
|ssect	  	 | Sous secteur de la machine			|
|nomac	  	 | Numéro de la machine					|
|faconf	  	 | Numéro d'OF							|
|faseq	  	 | Numéro de séquence					|
|faevco	  	 | Code d'évènement						|
|faevty	  	 | Type d'opération						|
|ppequi	  	 | HNuméro d'équipe						|
|date_debut	 | Date et heure de début de l'opération|
|duree	  	 | Durée totale de l'opération			|

#### Constructeur
Cette classe ne contient aucun constructeur.
Elle sert uniquement à récupérer et mapper les données de la base de données locale.

#### Méthodes statiques
##### getHistoriqueByMachine(\$id_machine)
Cherche dans la base de données l'historique d'une machine et retourne
- *false* si l'identifiant est incorrect.
- Une liste contenant les éléments **Historique** trouvés.

##### getNonFinishedOperation()
Cherche dans la base de données tous les **Historiques** correspondant a des événements pas encore terminés et retourne une liste contenant les éléments **Historique** trouvés.

##### updateHistorique(\$eventsList)
Met a jour l'historique de la base de données locale en se servant d'une liste d'**Event** donnée en paramètre.

##### getIndexHistorique(\$listeHisto, \$usine, \$sect, \$ssect, \$nomac)
Méthode qui prend une liste d'objets **Historique** ainsi qu'une usine, un secteur, un sous-secteur et un numéro de machine et retourne
- *false* si il n'existe aucune machine dans la liste avec cette usine, secteur, sous secteur et numéro de machine.
- *int* l'index de la machine avec ces propriétés sinon.

##### isInSameState(\$event, \$eventHistorique)
Méthode qui prend un **Event** et un **Historique** puis les compare et renvoie *true* si ils décrivent la même opération *false* dans le cas contraire.

##### cloturerHistoEvent(\$historiqueEvent)
Méthode qui prend en paramètre un **Historique**, elle marque l'évènement qu'il décrit comme terminer en inscrivant sa durée dans la base de données locale.

##### createHistoEvent(\$event)
Méthode qui prend en paramètre un **Event**, elle créée dans la base de données local un **Historique** avec des propriétés similaires a celles de l'**Event** et le marque comme non terminé avec une (durée égale a *NULL*).

## Autoloader.php
Autoloader basique en PHP
#### Attributs
| Nom            | Descripton                                                   |
|----------------|--------------------------------------------------------------|
|FOLDER		 | Répertoire ou aller chercher les fichiers de classes		|
#### Constructeur
Le constructeur prenant en parametre un répertoire et crée un spl_autoload_register sur ce repertoire.
