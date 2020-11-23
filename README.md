# Cloud-Function-base
Python example for testing Azure functions

This branch contains the modifications necessary to push to an Azure function. This version assumes 
you are using VS Code to push to Azure. I highly recommend that you make sure this code runs in VS Code 
(or your preferred IDE) before trying to run on Azure.

First: Follow all instructions in the base branch to ensure CloudTest.py runs properly. If it does, it should send you an email
that contains a table that has been scraped from a Yahoo finance page. Then, follow the next steps to publish CloudTest as an Azure function:
1. In VS Code, open the folder where you downloaded the sample code (File->Open Folder)
2. If you do not have an Azure account, sign-up for a free trial here: https://azure.microsoft.com/en-in/free/ 
3. While you can create new Azure functions directly in VS Code, I find it more intuitive to use the web portal. https://portal.azure.com/
4. In the Azure Portal, choose "Create a Resource" and type "Function App" into the search bar
5. Choose Function App from the results and select Create
6. Your Subscription should already be selected. Below the Resource Group choose "Create New". This will make it easier to delete
   the various components of the demo later because you can delete a whole resource group.
7. Give your Function app a name, Select "Code" and a Python runtime stack (I chose 3.8). Choose any region you want and select Next
8. Create a new Storage Account to associate with your function. It has to be stored somewhere, right? Choose Plan Type Consumption(Serverless)
9. You can now select Review + Create at the bottom of the screen to create your function.
10. In VS Code, select the icon for Extensions on the left and install the Azure Tools pack
11. Once installed, there should be a new icon in the left of VS Code for Azure. Select this and login to your Azure account
12. Once logged in, there will be several options associated with your Azure account. Expand the arrow for Functions and then
    expand the arrow for your subscription. You should see the name of the function you just created in the web portal
13. Right click on your function and choose Deploy to Function App... VS Code will now offer to create a new Function app
    in your existing project folder. Choose "Yes" to create a new project.
14. Choose Python, Timer Trigger and set the rules for your timer. I used "0 0 22 * * 1-5" which tells the timer to run every
    weekday at 10pm UST (5pm EST). Azure cron entries are slightly different than some. The first entry is seconds, and they
    do not offer a day-of-month option. {second} {minute} {hour} {day} {month} {day-of-week}. You can always change these
    values later, as they are stored in the file "function.json"
15. The Azure plugin to VS Code will now do what it needs in order to support automated publishing. This includes a folder for
    your function and a few Azure specific files - function.json, host.json, readme.md and sample.dat. There is also a
    .funcignore file which you can use to exclude local files in the project directory from being published to your function
16. The Python file that gets run by the function is titled __init__.py. To keep this example simple, we're just going to copy/paste
    our sample function into __init__.py:
    - Copy all of the import settings from CloudTest.py to the top of __init__.py
    - Copy the function cloudtest() just below the import settings and above main()
    - At the end of main(), add a single line cloudtest() that is indented to match the logging.info print statement stating
    that the function just ran.
17. Before we publish our function, we need to set the environment variables on Azure. We don't want to expose our usernames and
    password, so we're going to recreate the same local environment variables in our function. You can do this in the web portal
    under the Configuration tab for your function, but you can also do it right from inside VS Code:
    - Select the Azure icon in the left of VS Code, and expand the arrows for Functions, Your Subscription, and your Function.
    - Right click on "Application Settings" and choose "Add New Setting..."
    - Replicate the 3 environment variables from the base demo - EMAIL_ME, EMAIL_YOU and EMAIL_PWD
18. Now, we're ready to publish our function. Because each VS Code project folder is associated with a single function, publishing
    is quite easy. In the Azure->Functions menu, right-click on your function and choose "Deploy to Function App..."
19. If you don't want to wait 24 hours to see if your function runs, you can increase the frequency in function.json:
    - "schedule": "0 0 * * * *" will have it run every day, every hour, at the top of the hour
20. If you are still having problems with your function running properly, you can view the logs on portal.azure.com or you
    can follow these instructions to debug a function locally - https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python

