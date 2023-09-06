#!/bin/bash

var="$1"

if [ -f "$1" ];
then
        echo "Esto es un archivo llamado: $1, de tipo:" && file -b $var

elif [ -d "$1" ];
then
        echo "Esto es un directorio: $1"

        ls -l $1

else
        echo "No es un archivo ni es un directorio"

fi
