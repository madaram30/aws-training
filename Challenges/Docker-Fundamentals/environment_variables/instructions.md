#This document help you to pass the environment variables to the existing images. We will create a php based frontend and mariadb backend. Later, we will try connecting from one host to another. 

Step1: Create the phpmyadmin container using below command. Note that We are passing "PMA_ARBITRARY" environment variable to the container.
docker run --name phpmyadmin -d -p 8081:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin

Step2: Pull the mariadb image 
docker pull mariadb:10.6.4-focal

Step3: Use the below command to insepct the image and look for environment variables in it. 
docker inspect mariadb:10.6.4-focal 

Step4: Create the mariadb container using below command. Note the environment variables that we are passing to the conatiner. 
docker run --name db -e MYSQL_ROOT_PASSWORD=somewordpress -e MYSQL_PASSWORD=wordpress -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wordpress -d mariadb:10.6.4-focal --default-authentication-plugin=mysql_native_password

Step5: List the running containers and insepct the mariadb container using below commands. You must locate the environment variables that we passed in the previous command and note the mariadb IP address of the mariadb. The IP address will be used in next command.
docker ps
docker inspect <container-id>

Step6: Access your application using DB ip:
open http://localhost:8081 to access phpmyadmin enter DB_IP for server

enter root for username
enter somewordpress for password

Step7: Come back to terminal and try to login into the container using below command:
docker exec -it db bash

Step8: Run below commands to know about the file systems attached to the container. 
df -k

Step9: Exit out of the container using "exit" command and remove both the images:

docker stop db
docker rm db

docker stop phpmyadmin
docker rm phpmyadmin


###Challenge####
There is a Dockerfile kept in this folder which is using an environment variable. Build the image using the Dockerfile and run the container using the image. You must pass the environment variable that is used in the Dockerfile while running the container. 

