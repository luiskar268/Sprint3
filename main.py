from flask import Flask
import os
app = Flask(__name__)

app.run( host='127.0.0.1', port =443, ssl_context=('micertificado.pem', 'llaveprivada.pem') )
from app import rutas