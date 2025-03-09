Step 1: Launch an Amazon EC2 Instance
Log in to your AWS account.
![image](https://github.com/user-attachments/assets/98383267-c1b4-422a-9107-f11da86c492a)


Navigate to the EC2 dashboard. Choose "Mumbai" as the region. 
![image](https://github.com/user-attachments/assets/7190678e-788c-41c2-b414-1dc4ecbe626a)


Click “Launch Instance” to start the EC2 instance creation process.
Select an Amazon Machine Image (AMI) for your instance, such as “Amazon Linux 2.”
Choose an instance type - t2.micro.

![image](https://github.com/user-attachments/assets/378396e4-329a-48f7-bb5b-c8acfc3f078a)


Choose or create an SSH key pair to access your instance securely.

![image](https://github.com/user-attachments/assets/87c0900e-a63e-45a7-8b13-77141379d638)


Configure instance details like network settings, storage, and tags. Leave everything as default. Just make sure "Auto Assign Public IP" is enabled.

![image](https://github.com/user-attachments/assets/6a9c52a3-0754-4880-8687-6a1ab7edb33c)


Create or select an existing security group allowing inbound traffic on ports 22 (SSH), 80 (HTTP) and 443 (HTTPS).

![image](https://github.com/user-attachments/assets/f2cd2ff4-ce77-4d3a-832b-375ace327b39)


Review your instance settings and click “Launch.”

![image](https://github.com/user-attachments/assets/5294603a-1332-4d22-ab85-f35cfcafb3da)


Click “Launch Instances.”

![image](https://github.com/user-attachments/assets/846b7948-acb3-4c0f-9761-f6e4cea62798)


Step 2: Connect to Your EC2 Instance

Once your instance is running, select it in the EC2 dashboard.

![image](https://github.com/user-attachments/assets/3c72cc66-920d-43f6-9334-670c03887283)


Click “Connect” to view connection instructions.

Use an "EC2 Instance Connect" to connect to your instance. It will launch new tab in your web broswer with SSH login.

![image](https://github.com/user-attachments/assets/64b3123a-a438-4063-807d-0b0482a59c90)


Step 2: Update Your System
First, connect to your EC2 instance via SSH and update your system to ensure all packages are up to date:

sudo dnf update -y

![image](https://github.com/user-attachments/assets/a0a8f321-0a74-40c5-9c43-0ffa5d6f913d)


Step 3: Install Apache, PHP, and MariaDB
Install Apache web server, PHP, and its necessary modules, along with MariaDB, a community-developed fork of MySQL:

sudo dnf install -y httpd wget php-fpm php-mysqli php-json php php-devel

![image](https://github.com/user-attachments/assets/15aa2e51-dca9-4e97-9cb4-4f786ee7231b)


sudo dnf install -y mariadb105-server

![image](https://github.com/user-attachments/assets/b17e0892-384e-40fb-8d1e-d3e597efb5c6)


To check the MariaDB version:

dnf info mariadb105

![image](https://github.com/user-attachments/assets/310ecdb9-7bb8-4a05-9c3f-57ec1d3ebc6b)


Step 4: Start and Configure Apache
Start the Apache server and enable it to launch on boot:

sudo systemctl start httpd && sudo systemctl enable httpd

![image](https://github.com/user-attachments/assets/37d29802-ab5d-4474-9e23-c5accfd079ef)


Verify if Apache is enabled:

sudo systemctl is-enabled httpd

![image](https://github.com/user-attachments/assets/dcab7d66-b3d7-4806-8ef6-4083a97227c0)


Add your user (ec2-user) to the Apache group:

sudo usermod -a -G apache ec2-user


Step 5: Configure Permissions
Adjust the permissions for your web directory:

sudo chown -R ec2-user:apache /var/www
sudo chmod 2775 /var/www && find /var/www -type d -exec sudo chmod 2775 {} \;
find /var/www -type f -exec sudo chmod 0664 {} \;


Step 6: Install and Start MariaDB
Start MariaDB and secure your installation:

sudo systemctl start mariadb
sudo mysql_secure_installation
Secure the MySQL installation with the mysql_secure_installation command.
Type Y to remove the anonymous user accounts.
Type Y to disable the remote root login.
Type Y to remove the test database.
Type Y to reload the privilege tables and save your changes.

![image](https://github.com/user-attachments/assets/08610bd9-5ca6-4651-b2d4-0459b27eb6e7)


Step 7: Install WordPress
Download the latest WordPress package and extract it:

wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz

Start both Apache and MariaDB if not already running:

sudo systemctl start mariadb httpd

Step 8: Create a Database for WordPress


Access the MySQL shell as root:

mysql -u root -p


Then, create a new database and user for WordPress:

CREATE USER 'wordpress-user'@'localhost' IDENTIFIED BY 'your_strong_password';

Create your database. Give your database a descriptive, meaningful name, such as wordpress-db.

CREATE DATABASE `wordpress-db`;
Grant full privileges for your database to the WordPress user that you created earlier.

GRANT ALL PRIVILEGES ON `wordpress-db`.* TO "wordpress-user"@"localhost";
Flush the database privileges to pick up all of your changes.

FLUSH PRIVILEGES;
Exit the mysql client.

exit
Step 9: Configure WordPress
Copy the WordPress sample configuration file and edit it with your database details:

cp wordpress/wp-config-sample.php wordpress/wp-config.php
nano wordpress/wp-config.php
Update the database name, user, and password in the wp-config.php file.

define('DB_NAME', 'wordpress-db');

define(‘DB_USER’, ‘wordpress-user’);

define(‘DB_PASSWORD’, ‘your_strong_password’);

Step 10: Deploy WordPress
Copy the WordPress files to your web directory:

cp -r wordpress/* /var/www/html/
If you wish to install WordPress in a subdirectory, such as /blog, create the directory and copy the files:

mkdir /var/www/html/blog
cp -r wordpress/* /var/www/html/blog/
Step 11: Configure Apache
Before finalizing the installation, you may need to adjust the Apache configuration:

sudo nano /etc/httpd/conf/httpd.conf
Find the section that starts with <Directory “/var/www/html”>.

Change the AllowOverride None line in the above section to read AllowOverride All.

Step 12: Finalize the Installation
Restart Apache to apply the changes:

sudo systemctl restart httpd
Now, complete your WordPress installation by navigating to http://your-ec2-public-dns/ or http://your-ec2-public-dns/blog if you installed it in a subdirectory. Follow the on-screen instructions to finish the setup.





Congratulations! You have successfully installed WordPress on your Amazon EC2 instance using the 2023 Amazon Linux AMI.
