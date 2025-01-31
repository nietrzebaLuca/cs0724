ESERCITAZIONE S11 L5

analisi pacchetti http & https

Eseguo l'esercizio su VM CyberOps Workstation

si confrontano i risultati dei dump tcp in ascolto sulle connessioni tra workstation e i siti di logging.

1 - si apre in entrambi i casi un terminale, con il comando: sudo tcpdump -i enp0s3 -s 0 -w "file_salvataggio_dump".pcap.
	Si esegue un tcpdump con privilegi elevati sull'interfaccia enp0s3 e poi viene salvato su un file .pcap per una successiva analisi.
	Apro:
	- http: pagina www.altoromutual.com ed accedo
	- https: pagina www.netacad.com

2 - analisi con wireshark si analizzano i file di cattura:
	- http: si cerca il pacchetto con info il "POST" che detiene nel HTML form le informazioni di login ricercate.
	- https: si cerca il pacchetto con le info "Application Data" per cercare di ottenere le informazioni nel Secure Sockets Layer. E per ogni pacchetto di questo tipo si nota che i dati di login sono criptati.

Conclusione: il protocollo HTTPS, rispetto al protocollo HTTP, si ritiene sicuro per il fatto di crittografare le informazioni sensibili.


