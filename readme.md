#Actualizar Sistema en Producción
1. git checkout produccion
2. git pull master
3. python manage.py makemigrations
4. python manage.py migrate
5. git add .
6. git commit -m ''
7. git push origin produccion

#Accesso a Servidor de Producción
IP: 190.128.217.106
PUERTO: 8012

#Servidor Amazon.
IP: 54.219.130.191
PUERTO: 8000

