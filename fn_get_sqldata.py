import azure.functions as func
import logging
import os
import pyodbc

getsqldata_blueprint = func.Blueprint()

# Create a function which will fetch and return data from sql database using env variable for connection string
@getsqldata_blueprint.route(route="get_sqldata") 
def get_sqldata(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        # Get the connection string from the environment variable
        conn_str = os.environ["sqldb_connection"]
    
        # Create a connection to the database
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM dbo.Persons")

        # Fetch the data
        row = cursor.fetchone()
        logging.info(row)

        # Close the connection
        conn.close()

        return func.HttpResponse(f"Data fetched successfully: {row}")
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {e}", status_code=500)