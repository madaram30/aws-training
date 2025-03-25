docker run --name phpmyadmin -d -p 8081:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin

docker pull mariadb:10.6.4-focal

docker inspect mariadb:10.6.4-focal

docker run --name db -e MYSQL_ROOT_PASSWORD=somewordpress -e MYSQL_PASSWORD=wordpress -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wordpress -d mariadb:10.6.4-focal --default-authentication-plugin=mysql_native_password

docker inspect <container-id>

open http://localhost:8081 to access phpmyadmin enter DB_IP for server

enter root for username
enter somewordpress for password

docker exec -it db bash

df -k

docker stop db
docker rm db

docker stop phpmyadmin
docker rm phpmyadmin

