#!/bin/bash

set -e

logger "Arrancando instalacion y configuracion de MongoDB"
USO="Uso : install.sh [opciones]
Ejemplo:
install.sh -f config.ini
Opciones:
usuario : nombre del usuario 
password : contraseña
puerto : numero de puerto, si se omite se colocará 27017
"
function ayuda() {
echo "${USO}"
 if [[ ${1} ]]
  then
   echo ${1}
 fi
}

# Gestionar los argumentos
if [ -f "config.ini" ]; then
    source config.ini
else
    echo "El archivo config.ini no existe."
    exit 1
fi

# Comprobamos que los parámetros requeridos estén definidos
if [ -z "${user}" ]; then
    echo "El usuario no ha sido especificado en el archivo config.ini"
    exit 1
fi

if [ -z "${password}" ]; then
    echo "La contraseña no ha sido especificada en el archivo config.ini ."
    exit 1
fi

if [ -z "${port}" ]; then
    port=27017
fi

sudo apt-get -q -y update \
&& apt-get -q install -y curl

# Obtén la clave de MongoDB
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | 
   sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
   --dearmor

# Obtener la versión de Ubuntu
ubuntu_version=$(lsb_release -cs)

# Agregar el repositorio según la versión de Ubuntu detectada
if [[ "$ubuntu_version" == "xenial" ]]; then
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
elif [[ "$ubuntu_version" == "bionic" ]]; then
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
elif [[ "$ubuntu_version" == "jammy" ]]; then
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
else
    echo "La versión actual de Ubuntu no es compatible con MongoDB 6.0."
    exit 1
fi

if [[ -z "$(mongo --version 2> /dev/null | grep '6.0')" ]]
 then

# Instalar paquetes comunes, servidor, shell, balanceador de shards y herramientas
apt-get -q -y update \
&& apt-get -q install -y \
mongodb-org \
mongodb-org-server \
mongodb-org-shell \
mongodb-org-mongos \
mongodb-org-tools \
&& rm -rf /var/lib/apt/lists/* \
&& pkill -u mongodb || true \
&& pkill -f mongod || true \
&& rm -rf /var/lib/mongodb
fi

# Crear las carpetas de logs y datos con sus permisos
[[ -d "/datos/bd" ]] || mkdir -p -m 755 "/datos/bd"
[[ -d "/datos/log" ]] || mkdir -p -m 755 "/datos/log"

# Establecer el dueño y el grupo de las carpetas db y log
chown mongodb /datos/log /datos/bd
chgrp mongodb /datos/log /datos/bd

# Crear el archivo de configuración de mongodb con el puerto solicitado
mv /etc/mongod.conf /etc/mongod.conf.orig
(
cat <<MONGOD_CONF
# /etc/mongod.conf

systemLog:
  destination: file
  path: /datos/log/mongod.log
  logAppend: true
storage:

  dbPath: /datos/bd
  engine: wiredTiger
  journal:
    enabled: true
net:
  port: ${port}
security:
  authorization: disabled

MONGOD_CONF
) > /etc/mongod.conf

# Reiniciar el servicio de mongod para aplicar la nueva configuracion
systemctl restart mongod 


# Función para comprobar si MongoDB ha arrancado correctamente
function wait_for_mongodb() {
    local retries=10
    local wait_time=5sed -i "s/authorization: enabled/authorization: disabled/" /home/vboxuser/mongod.conf
    local count=0

    while [ ${count} -lt ${retries} ]; do
        sleep ${wait_time}
        if mongosh --quiet --eval "db.runCommand({ ping: 1 }).ok === 1" admin; then
            echo "MongoDB ha arrancado correctamente."
            return 0
        fi
        ((count++))
    done

    echo "No se pudo comprobar que MongoDB ha arrancado correctamente."
    return 1
}

# Esperar a que MongoDB arranque
if ! wait_for_mongodb; then
    exit 1
fi

# Crear usuario con la password proporcionada como parametro
mongosh admin << 'CREACION_DE_USUARIO'
db.createUser({
user: "${user}",
pwd: "${password}",
roles:[{
role: "root",
db: "admin"
},{
role: "restore",
db: "admin"
}] })
CREACION_DE_USUARIO

logger "El usuario ${user} ha sido creado con exito!"

exit 0