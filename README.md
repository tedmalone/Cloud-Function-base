# Cloud-Function - AWS
Python example for testing AWS Lambda

This branch contains the modifications necessary to push to an AWS Lambday function. This version assumes you are using 
VS Code to push to AWS.

First: Follow all instructions in the base branch to ensure CloudTest.py runs properly. If it does, it should send you an email that contains a table that has been scraped from a Yahoo finance page. Then, follow the next steps to publish CloudTest as an AWS Lambda serverless function:

The AWS and SAM client line interfaces (CLI) can run local if you have Docker installed. However, this demo is only designed to 
run on AWS Lambda. The CLI will package everything up and deploy the container onto AWS for you.

You can follow these steps to match the test setup. I am running on Windows 10, so you may have to tweak these instructions slightly.
1. In VS Code, open the folder where you downloaded the sample code (File->Open Folder)
2. If you do not have an AWS account, sign-up for a free trial here: https://aws.amazon.com/free
3. In VS Code, select the icon for Extensions on the left and install the AWS Toolkit pack
4. Once installed, there should be a new icon in the left of VS Code for AWS. Select this and connect to AWS using the
same credentials you use to login to the AWS Console
5. Right click on Lambda and choose "Create new SAM Application. Choose Python 3.8 as your runtime.
6. Select "AWS SAM Hello World" to create a new function in your current directory
7. Give your Function app a name, I chose "Cloud Function - AWS"
8. This will create a new hello_world folder with a bunch of new files and directories.
9. While you can certainly play around with the Hello World function, our goal is to deploy our web scraper onto lambda
   You should have a cloud_function folder in your directory now. For AWS, we are going to modify "app.py" in order
   to run our function. For Lambda, the main function called is lambda_handler(). We also need to specify our Python
   requirements in requirements.txt Lambda will use this to install the required packages.
10. Add the cloud function to the top of app.py, along with the required import statements. Since the lambda default
    function is already set to run on demand vs. the crontab we used with Azure, we'll go ahead and return the
    text to the calling web function as well as sending the same email used in the default function.
11. Use SAM to publish to Lambda. Open a Terminal in VS Code and cd into Cloud Function - AWS
    > cd "Cloud Function - AWS"
    > aws configure
    Note: If you still need to create app specific credentials, you can do that here - https://console.aws.amazon.com/iam 
    Make sure you keep track of your Key and Secret in case you need it to authenticate your function later
    > sam validate
    > sam build
    > sam deploy --guided
12. Now that the function is deployed to Lamba, we need to set the environment variables for our function. 
    We don't want to expose our usernames and password, so we're going to recreate the same local environment variables in our function. 
    While you can set the variables in the web console, I found it better to use the CLI to do this. That is because Lambda
    resets the environment variables every time you deploy a new version of the function. Here is the easiest way I found to do it:
    a. In VS Code, choose AWS in the left nav and expand the Lambda pull-down to see your function
    b. Right click on your function and choose "Copy Name". My deployed Lambda function was named "sam-app-CloudFunction-1B44HXPW2HY9X"
    c. In the terminal, issue the following AWS command:
        aws lambda update-function-configuration --function-name sam-app-CloudFunction-1B44HXPW2HY9X --environment "Variables={EMAIL_YOU=recipient@yahoo.com,EMAIL_PWD=wwww xxxx yyyy zzzz,EMAIL_ME=sender@gmail.com}"
    d. You can verify this worked by issuing the following command:
        aws lambda get-function-configuration --function-name sam-app-CloudFunction-1B44HXPW2HY9X
13. In order to test your function, we now need to locate it's endpoint. To do this, go to https://console.aws.amazon.com/lambda/home and
    select your function. You should see a purple graphic labeled "API Gateway". Select this and scroll down to the API Gateway.
    Below your gateway, expand the Details arrow and you should see an entry that looks like this:
    API endpoint: https://35x38i9t3a.execute-api.us-east-1.amazonaws.com/Prod/cloudtest Select this endpoint to open it in a browser.
    This should execute your function and return the python payload to the browser. If everything worked, behind the scenes you should
    have just sent yourself an email similar to the one that was sent manually when we first ran the cloud function
14. If you want to view your logs, you can issue this command:
    sam logs --name sam-app-CloudFunction-1B44HXPW2HY9X


For more information and how to debug your functions locally, check out this documentation: 
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html