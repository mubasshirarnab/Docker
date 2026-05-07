# This is a simple Flask application that will show "Hello, World!", Port and Container id.  

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is Port: ' + os.getenv('PORT') + ' and Container ID: ' + os.getenv('HOSTNAME')  
 
if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=3000)

