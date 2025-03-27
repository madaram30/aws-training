#This document helps you to create binds and volumes. 

Step1: Create the phpmyadmin container using below command.
docker run --name phpmyadmin -d -p 8081:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin

Step2: Run below command to go to home dir.
cd ~

Step3: create a directory named "mariadb_data"
mkdir mariadb_data


Step4: Below command creates a bind with directory "mariadb_data". Carefully look at the command to differentiate between the bind and volume. The bind can preserve the data only if the folder remains as it is. The container won't get same data if there is a change in the name of the folder or delete of it.
docker run \
 --name db \
 -e MYSQL_ROOT_PASSWORD=somewordpress \
 -e MYSQL_PASSWORD=wordpress \
 -e MYSQL_DATABASE=wordpress \
 -e MYSQL_USER=wordpress \
 -v "$(pwd)"/mariadb_data1:/var/lib/mysql \
 -d \
 mariadb:10.6.4-focal \
 --default-authentication-plugin=mysql_native_password

Step5: Stop and delete the container to create the volume.
docker stop db
docker rm db

Step6: Create the volume using below command. Note volume doesn't bind with any folder. It is an individual object created for docker itself. 
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

Step7: List the volumes created using below command:
docker volume ls

Step8: Access the application using below url and credentials.
https://localhost:8081 
username: root
password: wordpress

Step9: Upload some images into your wordpress websites. Once done stop and remove the container. 
docker stop db
docker rm db

Step10: Run the Step6 command and access your application using Step8. You must be able to see the images that you uploaded.

Step11: Cleanup everything.
docker stop db
docker rm db
docker stop phpmyadmin
docker rm phpmyadmin
docker volume rm mariadb_data