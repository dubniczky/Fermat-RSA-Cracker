#!/bin/bash

BITS=2048
DAYS=2048
KEY_FILE="gen.key"
CRT_FILE="gen.crt"

# Generates a certificate using openvpn
echo -e "\n\n\n\n\n\n\n" \
    | openssl req \
        -x509 \
        -sha256 \
        -nodes \
        -days $DAYS \
        -newkey rsa:$BITS \
        -keyout $KEY_FILE \
        -out $KEY_FILE
