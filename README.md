# Deploy a Python (Flask) web app to Azure App Service 

This is the sample Flask application for testing chatgpt. Please use your key in the code for it to work.

If you need an free Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).


# Create Azure Web App for Python

Change these values based on your instance name and resource group 
Then run the command as follows:

RESOURCE_GROUP_NAME='my-rsg-1' \
APP_SERVICE_NAME='testforrobinpython'

az webapp create \
    --resource-group $RESOURCE_GROUP_NAME \
    --name $APP_SERVICE_NAME \
    --linux-fx-version "PYTHON|3.9.12" --sku B1

# Deploying the python code to Azure via AZ cli

Change these values based on your instance name and resource group 
Then run the command as follows:

RESOURCE_GROUP_NAME='my-rsg-1'
APP_SERVICE_NAME='testforrobinpython'

az webapp deploy \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --src-path <zip-file-path>

After deploy just open up the browser and refer to the full name of your website.
https://testforrobinpython.azurewebsites.net/


Testing the OpenAPI please use the following end point via POSTMAN or curl commands 
/openai/<question> with a GET call



# Deploying the python code to Azure via AZ download publish profile

On the overview page of the web app, use the Download Publish Profile to donwload the file
File has userid/password that can be used to push the zip file to the App Service


