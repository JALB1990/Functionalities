#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Error: Se requieren exactamente dos parámetros."
  echo "Uso: $0 archivo_origen archivo_destino"
  exit 1
fi


archivo_origen=$1
archivo_destino=$2


if [ ! -f "$archivo_origen" ]; then
  echo "Error: El archivo de origen '$archivo_origen' no existe."
  exit 1
fi


cp "$archivo_origen" "$archivo_destino"


if [ $? -eq 0 ]; then
  echo "El archivo se copió correctamente."
else
  echo "Error al copiar el archivo."
fi

exit 0
