# Bash Jail 1 

> ssh ssh level1@ringzer0team.com -p 1016

after login we're served by a bash script 



```bash

Flag is located at /home/level1/flag.txt

while :
do
	echo "Your input:"
	read input
	output=`$input`
done
 
 
Your input:

```
-----------------------------

bash accessable from /bin/bash , but we can't get stdout, every command using stdout returns nothing
> level1@lxc17-bash-jail:~$ cat /home/level1/flag.txt

(nothing)

<strong>but</strong> when we put unrecognized command in the bash script
> dasdasdsad

return

> /home/level1/prompt.sh: line 24: dasdasdsad: command not found

so stderr is accessable, we just need to redirect the stdout to stderr

> cat /home/level1/flag.txt 1>&2

Flag :

> FLAG-U96l4k6m72a051GgE5EN0rA85499172K