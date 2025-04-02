## Below Steps help you in creating the ECS Cluster for WrodPress ##

# Step 1: Create an ECS Cluster

1.1 Sign in to AWS Management Console: Go to AWS Management Console, sign in with your AWS account, and search for ECS (Elastic Container Service).
1.2 Navigate to ECS Console:
    In the AWS Management Console, type “ECS” in the search bar.
1.3 Click on ECS under the "Services" section.
1.4 Create ECS Cluster:
    On the ECS dashboard, click on Clusters on the left side.
    Click the Create Cluster button.
1.5 Enter a name for your cluster (e.g., my-ecs-cluster).
1.6 Click Create to create your cluster.


# Step 2: Create ECS Task Definition with Two Containers
2.1 Navigate to Task Definitions:
    On the ECS dashboard, click Task Definitions from the left menu.
2.2 Click the Create new Task Definition button.
    Select Launch Type:
    Choose Fargate as the launch type.
    Click Next Step.
2.3 Configure Task Definition:
    Enter a Task Definition Name wordpress-definition.
    Set Network Mode to awsvpc.
    Leave Task Execution Role as ecsTaskExecutionRole.
2.4 Add Container Definitions:
    Click on Add Container to add the first container:
    Container Name: wordpress
    Image: Enter your container image URL - docker.io/wordpress:latest
    Memory Limits: Set Soft Limit to 512MB and Hard Limit to 1GB (You can adjust based on your container's needs).
    Port Mappings: Map the container port to a host port - 80.
    Environment Variables: Add environment variables
        - WORDPRESS_DB_HOST=127.0.0.1
        - WORDPRESS_DB_USER=wordpress
        - WORDPRESS_DB_PASSWORD=wordpress
        - WORDPRESS_DB_NAME=wordpress
2.5 After adding the first container, click on Add Container again to add the second container:
    Container Name: mariadb
    Image: docker.io/mariadb:10.6.4-focal
    Memory Limits: Set Soft Limit to 256MB and Hard Limit to 512MB.
    Port Mappings: 3306
    Environment Variables: 
        - MYSQL_ROOT_PASSWORD=somewordpress
        - MYSQL_DATABASE=wordpress
        - MYSQL_USER=wordpress
        - MYSQL_PASSWORD=wordpress
2.6 Review and Create Task Definition:
    Review all settings.
    Click Create to save the task definition.

# Step 3: Create Load Balancer (Application Load Balancer)
3.1 Navigate to EC2 Console:
    Go to EC2 in the AWS Console (search for EC2).
    Create Load Balancer:
    On the left menu, click Load Balancers.
    Click Create Load Balancer.
3.2 Choose Application Load Balancer.
    Set Name for the Load Balancer - wordpress-loadbalancer.
    Select Scheme as internet-facing.
    Choose IP Address Type as ipv4.
    For Listeners, ensure you have an HTTP listener (port 80).
3.3 Click Next: Configure Security Settings.
    Configure Security Groups:
    Select an existing security group or create a new one that allows inbound traffic on port 80 (HTTP).
3.4 Click Next: Configure Routing.
    Configure Target Group:
    For Target Group, create a new target group. You can name it wordpress-group.
    Set the Target type to IP.
    Set Protocol to HTTP and port to 80.
    Choose Health checks for the target group, configure as needed, and click Next: Register Targets.
    Finish Load Balancer Creation:
    Skip the Register Targets step for now, as the ECS service will register them automatically.
    Click Create.

# Step 4: Create ECS Service and Attach Load Balancer
4.1 Navigate to ECS Cluster:
    Go back to the ECS dashboard.
    Click on Clusters, then select the cluster (my-ecs-cluster) you created.
    Create ECS Service:
    Click the Create button under the Services tab.
4.2 Choose Fargate as the launch type.
    Select your Task Definition - wordpress-definition.
    Set the Service Name - wordpress-service.
    Set Number of Tasks to 2 (or adjust according to your needs).
    Click Next Step.
4.3 Configure Network:
    Choose VPC and Subnets for your service. Ensure you select subnets that allow internet access.
    Ensure Auto-assign Public IP is enabled (if needed).
    Click Next Step.
4.4 Configure Load Balancer:
    Under Load balancing, select Application Load Balancer.
    Choose the Load Balancer - wordpress-loadbalancer created earlier.
    Select the Target Group - wordpress-group.
    Choose Container Name - wordpress and Container Port - 80.
    Click Next Step.
4.5 Set Auto Scaling (Optional):
    You can configure auto-scaling if needed.
    Click Next Step.
4.6 Review and Create Service:
    Review the configuration.
    Click Create Service.
Step 5: Verify the Setup
5.1 Verify ECS Service:
    Once the ECS service is created, it will automatically register tasks and target containers in the target group of the load balancer.
    You can verify the tasks running in the Tasks tab under your ECS cluster.
5.2 Access the Load Balancer:
    In the Load Balancers section of the EC2 dashboard, find your load balancer wordpress-loadbalancer.
    Copy the DNS name of the load balancer.
    Paste it in the browser to verify the application is accessible via the load balancer.
    Check Target Group Health:
    In the Target Groups section under EC2, verify that the targets (containers) are healthy.