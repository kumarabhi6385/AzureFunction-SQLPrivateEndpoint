import azure.functions as func
import logging
from fn_get_sqldata import getsqldata_blueprint

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
app.register_functions(getsqldata_blueprint)
