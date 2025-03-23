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
  4. Click on "Choose File" and then select the yaml file that you have created in the last step.
  5. Now, i

Step 2 - Create the Lambda function:
  1. Go to Lambda Service and click create function.
  2. Choose "Author From Scratch"
  3. Provide a function name
  4. Choose run time as "Python 3.9"
  5. In the permission section, expand the option "Change default Execution Role"
  6. Select "Use an existing role" and choose the role that was created in step 1.
  7. Click on Create Function

Step 3 - Configure the Lambda function:
  1. Once the Lambda function is created, click on the function name to configure it.
  2. Please download the ZIP file "my-deplpyment-package.zip" into your local.
  3. Go to the "Code" section to upload the ZIP file that was downloaded.
  4. Once the above step is completed successfully, go to "Configuration" section/
  5. Under "General Configuration", Click on "edit" and change the time out to "1 Min, 0 Sec".
  6. Go to "Envrionment Varialbes", Click on "Edit" to add a variable.
  7. Add the key as "processed_bucket" and value as the your target S3 bucket name that you created in Step 1.
  8. Click on the Trigger and Select the source as S3 service. Choose the source bucket created in Step 1.
  9. Click on the checkbox "I Acknowledge..." and click on "Add" to add the trigger. 

Step 4 - Test the project:
  1. Go to your source S3 bucket that is created in Step 1.
  2. Now upload a .jpg file into it.
  3. To observe the execution of the function, go to cloudwatch and choose "Log Groups" under logs.
  4. Click on the logs group -> /aws/lambda/<lambda-function-name>
  5. Once the function is executed successfully, you must be able to see the files in your target S3 bucket.


Errors:
  1. If you can't see the logs in the CloudWatch, please check the IAM role that is created. Make sure you replaced <lambda-function-name> with the correct name.
