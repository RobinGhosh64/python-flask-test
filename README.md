# Deploy a Python (Flask) web app to Azure App Service - Sample Application

This is the sample Flask application for testing chatgpt. Please use your key in the code for it to work.

If you need an free Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).


Create Azure Web App for Python

# Change these values to the ones that you want to use 
# Then run the commands as follows:

RESOURCE_GROUP_NAME='my-rsg-1'
APP_SERVICE_NAME='testforrobinpython'

az webapp deploy \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --src-path <zip-file-path>



Deploying the python code to Azure via AZ cli

# Change these values to the ones that you want to use 
# Then run the commands as follows:

RESOURCE_GROUP_NAME='my-rsg-1'
APP_SERVICE_NAME='testforrobinpython'

az webapp deploy \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --src-path <zip-file-path>
