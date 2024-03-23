# How to Access SQL Database Using Private Endpoint from Azure Function

## 1. Create SQL Database
- Navigate to **Create a resource**.
- Search and select **SQL Database**, then click **Create**.
- Choose a resource group, provide a database name, and select or create a new SQL server.
- Review the settings and click **Create**.

## 2. Create Virtual Network and Subnets
- Go to **Create a resource**.
- Search for **Virtual Network** and click **Create**.
- Enter a name for the Virtual Network.
- Optionally, select **Azure Bastion** if needed.
- Add two subnets:
  - `sql-subnet` with the range `10.0.0.0/24`
  - `fn-subnet` with the range `10.0.1.0/24`
- **Note**: The `sql-subnet` is for the private endpoint of the SQL database, and the `fn-subnet` is for VNet integration to restrict outbound network traffic. They must be distinct to avoid conflicts.

## 3. Create Private Endpoint for Azure SQL Database
- Select the Azure SQL Database resource.
- Go to **Networking** > **Private access** and click **Create private endpoint**.
- Choose the `sql-subnet` within your Virtual Network.
- Review and create the endpoint.

## 4. Create Azure Function and Link with Endpoint
- **Note**: VNet integration is only available with the Premium plan.
- Create an Azure function with the Premium plan.
- In the Azure portal, navigate to your Azure Function.
- Go to **Networking** and select **VNet Integration**.
- Click to **Add VNet Integration**.
- Select the `fn-subnet` from your existing Virtual Network.

## 5. Verify the Access
- In the Azure portal, select the Private endpoint.
- Navigate to the **Private DNS zone** and copy the URL (usually `privatelink.database.windows.net`).
- Modify the connection string in your application to use the new URL instead of the SQL server name.
- Ensure that **Public network access** to the SQL server is disabled.
- Test the Azure function to confirm it can retrieve data from the SQL database.

# How to use this code.
## 1. Make sure you have added local.setting.json with below content
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "sqldb_connection": "<connection string>"
  }
}
```

## 2. deploy azure function using below command on terminal.
func azure functionapp publish "`<function_app_name>`"

