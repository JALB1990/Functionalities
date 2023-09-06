#!/bin/bash
echo "Nombre del script: $0"

echo "Número de argumentos: $#"

if [ $# -ge 1 ]; then
  echo "Primer y segundo argumento: $1 $2"
fi

if [ $# -gt 2 ]; then
  echo "Argumentos a partir del tercero:"
  shift 2  # Descartar los primeros dos argumentos
  for arg in "$@"; do
    echo "$arg"
  done
fi

exit 0
