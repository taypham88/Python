import os
from flask import Flask
import time

app = Flask(__name__)

@app.route('/timer/')
def timer():
    return str(round(time.time()))
    # return str(time)

if __name__=="__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host ='0.0.0.0', port=port)