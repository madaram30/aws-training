The YAML template is completely automated, no manual action is required. 

Please follow below steps to complete the lambda-s3-events project. 
The project contains total 5 components.
  1. S3 - Two Bucekts. One for the Source and one for Destination
  2. Lambda function - this will run the program to create the images with the given pixel ranges.
  3. IAM Role - The role which to be assigned to Lambda. This gives lambda permissions to access S3 and CloudWatch
  4. SQS queue - This queue will bring the decoupling architecture to us. 

Step 1 - Pre-Req: 
  1. Before we create actual stack, you need to upload the .ZIP file available in the folder to your own S3 bucket.
  2. Create a bucket in S3.
  3. Download the .ZIP file from **lambda-s3-events/my-deployment-package/my-demployment-pacakge.zip** to your local.
  4. Upload the .ZIP file into your S3 bucket.
  5. Copy the template from the path **lambda-s3-events/cloudformation/s3-events-stack.yaml** to your local file editor and save it as **s3-events-sqs-lambda.yml**. 

Step 2 - CloudFormation Stack Creation: 
  1. Go to CloudFormation console and click on create stack (with new resources). 
  2. Click on "Choose Existing Template".
  3. Choose "upload a template file".
  4. Click on "Choose File" and then select the yaml file that you have created in the last step. Then, click Next. 
  5. You will be asked to provide stack name and the parameter values. Some parameters are having default values, some don't.
  6. Make sure you provide source bucket name and destination bucket name appending your account number.
  7. The source code bucket name and object key should be given correctly, otherwise the wrong code might get uploaded into lambda.
  8. After providing parameter values, click next and acknowledge the IAM resource creation, then Submit the stack creation. 

Step 4 - Test the project:
  1. Go to your source S3 bucket that is created in Step 1.
  2. Now upload a .jpg file into it.
  3. To observe the execution of the function, go to cloudwatch and choose "Log Groups" under logs.
  4. Click on the logs group -> /aws/lambda/<lambda-function-name>
  5. Once the function is executed successfully, you must be able to see the files in your target S3 bucket.
