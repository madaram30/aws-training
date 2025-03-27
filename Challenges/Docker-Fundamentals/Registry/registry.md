#Registry Challenge#

Step1: singup in hub.docker.com with your email address.

Step2: Login into your account, Click on your profile, Click on the settings and create a personal token. 

Step3: Open a terminal and Login into your docker hub account. 
docker login --username=<your-user-name>

Step4: Build any of the image using 2048 folder. 

docker build .

Step5: List the images
docker images

Step6: Tag the docker image with your username
docker tag <image-id> <user-name>/2048:latest

Step7: push the image to docker hub registry
docker push  sairamsunkaranam1/2048:latest