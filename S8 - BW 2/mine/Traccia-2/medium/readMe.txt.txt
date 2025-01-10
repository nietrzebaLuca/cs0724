PRE BUILD WEEK 2

0 - configurazione di rete dispositivi attaccante e target:	Attaccante 192.168.13.100, Target 192.168.13.150
	configurazione security DVWA a LOW

1 - si procede con il test SQL Injection sulla DVWA. Con la sintassi: "1' SELECT UNION user, password FROM users#" si ottiene
	la lista degli utenti con le rispettive password in formato hash.
	Di mio interesse è l'utente pablo picasso. Con il tool hash-identifier verifico il tipo di crittografia.
2 - con john the ripper procedo alla decrittazione della password: "john --show --format=raw-md5 	/direcroty/file/contenente/hash".

	user: pablo	password: letmein	hash: 0d107d09f5bbe40cade3de5c71e9e9b7 