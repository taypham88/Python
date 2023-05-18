import os
from flask import Flask
app = Flask(__name__)

@app.route('/hello/')
@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/hello/<name>/')
def hello_name(name):
    return "hello, {}".format(name)

@app.route('/goodbye/<times>/<name>/')
def goodbye_name(name,times):
    try:
        return(f"Goodbye {name}!")*int(times)
    except:
        return(f"Goodbye {name}!")

if __name__=="__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)

