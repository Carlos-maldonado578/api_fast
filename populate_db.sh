#!/bin/bash

# Iterar sobre los ítems del archivo JSON y enviar cada uno en una solicitud POST
jq -c '.[]' data.json | while read item; do
    echo "Enviando ítem: $item"
    curl -X POST "http://127.0.0.1:8000/items/" \
        -H "Content-Type: application/json" \
        -d "$item"
    echo -e "\n"
done
