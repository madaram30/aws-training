docker run --name phpmyadmin -d -p 8081:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin

cd ~

mkdir mariadb_data

docker run \
 --name db \
 -e MYSQL_ROOT_PASSWORD=somewordpress \
 -e MYSQL_PASSWORD=wordpress \
 -e MYSQL_DATABASE=wordpress \
 -e MYSQL_USER=wordpress \
 -v "$(pwd)"/mariadb_data:/var/lib/mysql \
 -d \
 mariadb:10.6.4-focal \
 --default-authentication-plugin=mysql_native_password

docker stop db
docker rm db

docker run \
 --name db \
 -e MYSQL_ROOT_PASSWORD=somewordpress \
 -e MYSQL_PASSWORD=wordpress \
 -e MYSQL_DATABASE=wordpress \
 -e MYSQL_USER=wordpress \
 -v mariadb_data:/var/lib/mysql \
 -d \
 mariadb:10.6.4-focal \
 --default-authentication-plugin=mysql_native_password

docker volume ls

https://localhost:8081 
    root
    wordpress

docker stop db
docker rm db
docker stop phpmyadmin
docker rm phpmyadmin
docker volume rm mariadb_data