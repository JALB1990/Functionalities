#!/bin/bash

fecha=$(date +"%Y%m%d")

for archivo in *.jpg; do
    nombre=$(basename "$archivo" .jpg)

    nuevo_nombre="${fecha}-${nombre}.jpg"

    mv "$archivo" "$nuevo_nombre"
done
