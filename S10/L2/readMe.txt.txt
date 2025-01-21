ESERCITAZIONE S10 L2

Oggetto: Gestione Permessi di Lettura, Scrittura ed Esecuzione Linux

(vedere lo screenshot)

1 - Creare una directory /SHARED nel percorso /home/kali/Documents/ con il comando 'mkdir'.
2 - Verificare con 'ls -l' le autorizzazioni.
3 - Con 'sudo chmod -R 744' applico restrizioni:
	7 = rwx - lettura scrittura ed esecuzione per il proprietario.
	4 = r-- - solo lettura per il gruppo.
	4 = r-- - solo lettura per tutti gli altri utenti.
4 - Verificare con 'ls -l' le autorizzazioni modificate.
5 - Scrivere un file con comando 'echo "text" > file.txt', non è permesso per via delle restrizioni. Riprovo anche con 'sudo' ma nulla.
6 - Elevo i privilegi del mio utente (divento root), allora accedo alla cartella, riesco a scrivere un file e a leggerlo.
7 - Verifico la autorizzazioni del file creato.

