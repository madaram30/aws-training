Step1: Save the compose.yaml in your local
Step2: Run the below command:

docker compose up -d

This will make the container up and running in your local. 

Make sure the containers are running using below command:
docker ps 

Step3: Once the containers are up, use below URL to acces the application. 
http://localhost:8081

Step4: Once the application check is completed, you can bring it down using below command:

docker compose down

Step5: Though the docker compose is down, the volumes still persists after the container run time. Run below command to list the volumes:
docker volume ls

Step6: Remove the volumes using volume names returned from above command:
docker volume rm <VOLNAME>