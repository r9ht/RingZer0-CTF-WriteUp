# 	Who I am?

find information about the website , i'm using <strong>dnsrecon</strong>

> dnsrecon -d ringzer0team.com -t std

 Output : 
 
 [*] Performing General Enumeration of Domain:
[-] DNSSEC is not configured for ringzer0team.com
[*] 	 SOA ns17.domaincontrol.com 216.69.185.9
[*] 	 NS ns18.domaincontrol.com 208.109.255.9
[*] 	 NS ns18.domaincontrol.com 2607:f208:302::9
[*] 	 NS ns17.domaincontrol.com 216.69.185.9
[*] 	 NS ns17.domaincontrol.com 2607:f208:206::9
[*] 	 MX mailstore1.secureserver.net 68.178.213.243
[*] 	 MX mailstore1.secureserver.net 68.178.213.244
[*] 	 MX mailstore1.secureserver.net 72.167.238.32
[*] 	 MX smtp.secureserver.net 72.167.238.29
[*] 	 MX smtp.secureserver.net 68.178.213.203
[*] 	 MX smtp.secureserver.net 68.178.213.37
[*] 	 A ringzer0team.com 24.37.41.154
[*] 	 TXT ringzer0team.com FLAG-305l9RR202HG695t6Y8ZU77xyq
[*] 	 TXT ringzer0team.com uid=0(root) gid=0(root) groups=0(root)
[*] Enumerating SRV Records
[-] No SRV Records Found for ringzer0team.com

Flag :
> FLAG-305l9RR202HG695t6Y8ZU77xyq