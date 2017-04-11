#File Recovery 

The private.pem file identified as RSA private key and could be use for decrypting the flag (flag.enc) using openssl command

Decrypt : openssl rsautl -decrypt -inkey priv* -in flag.enc -out flag

Flag    : flag(FLAG-vOAM5ZcReMNzJqOfxLauakHx)
