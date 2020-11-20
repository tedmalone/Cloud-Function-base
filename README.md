# Cloud-Function-base
Python example for testing cloud functions

This is the base code which I will use to test several different cloud-hosted functions. I highly recommend that
you make sure this code runs in VS Code (or your preferred IDE) before trying to run on a cloud platform.

You can follow these steps to match the test setup. I am running on Windows 10, so you may have to tweak these instructions slightly.
1. Install VS Code - https://code.visualstudio.com/Download
2. Install Python environment - https://www.python.org/downloads/
3. Run VS Code and install Python extensions - https://marketplace.visualstudio.com/items?itemName=ms-python.python
4. In VS Code, open the folder where you downloaded this sample code (File->Open Folder)
4. In VS Code, open a terminal (Terminal->New Terminal)
5. In the terminal window, type the following commands:
    PS C:\demo> python -m venv .venv
    PS C:\demo> .venv/Scripts/activate.ps1
    (.venv) PS C:\demo> pip install -r requirements.txt
6. If VS Code has not created a .vscode directory yet, select the CloudTest.py file and Run->Start Debuggging and select the blue "Run and Debug" box.
7. Open the file .vscode/launch.json file and add the required environment variables after the console entry:
            "console": "integratedTerminal",
            "env": {
                "EMAIL_ME": "sender@gmail.com",
                "EMAIL_YOU": "recipient@anydomain.com",
                "EMAIL_PWD": "xxxx xxxx xxxx xxxx"
            }
Note: Don't forget to add the comma after the "console" line. 

Because I have 2-factor authentication on my Google account, I created a unique app password here - https://myaccount.google.com/security
Under "Signing into Google", choose App Passwords. In the left pull-down menu, choose "Other (Custom Name)"
Enter a name like "Python" and click Generate. Copy the password and enter it (with spaces) into your launch.json file.

At this point, you should be able to select the Python file in VS Code and Run->Run Without Debuggging. The program
should run in the terminal and exit quietly. Check your recipient email and see if you received the proper output.
If you don't see the email, check your spam folder. You can also look in the Sent folder on the outgoing Gmail account
to verify that the mail was sent properly.
