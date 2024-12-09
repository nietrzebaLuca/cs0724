Rete Configurata
network		192.168.50.0/24
kali 		192.168.50.100
metasploit	192.168.50.101

una volta instaurata la connessione bilateerale si procede con:
0 - start burpsuite and start intercepting
1 - through bs browser login into http://192.168.50.1/dvwa/login.php
	on bs intercepting window we can see usarname and password clearly
2 - setting dvwa security level on LOW
3 - shell.php file upload on dvwa
4 - running script and connecting
5 - http requests and shell cmd line request

- - dvwa security set on medium
6 - uploaded shell.php.jpg script why jp? because dvwa without it recognize the php script
7 - http requets and cmd line request