#!/bin/bash

var="$1"
path=$HOME/fotos

echo "la ruta es: $path"

if [ -d "$path" ];
then
        #echo "entra al if normal"
        #Obtenemos la extension del archivo
        extension=$(echo $var | rev | cut -d'.' -f1 | rev)

        if [ $extension = jpg ];
        then
                cp $var ~/fotos/.
                echo "El archivo se Movio al directorio: $path"
        else
                echo "El archivo no tiene extencion .JPG"

        fi

fi

if [ ! -d "$path" ];
then
        #echo "entra al if negado"
        #echo "Creamos el Directorio"
        mkdir ~/fotos

        #Obtenemos la extension del archivo
        extension=$(echo $var | rev | cut -d'.' -f1 | rev)

        if [ $extension = "jpg" ];
        then
                cp $var ~/fotos/.
                echo "El archivo se Movio al directorio: $path"
        else
                echo "El archivo no tiene extencion .JPG"

        fi
fi
