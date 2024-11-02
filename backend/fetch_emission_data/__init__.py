import azure.functions as func
from .app import app

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context) # Convert to a WSGI-compatible request (azure handles it)