import time
import webbrowser
from flask import Flask, request, render_template, jsonify
import callable

HOST = "localhost"
PORT = 8080

# surclass flask to popen browser
class MyFlask(Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        webbrowser.open('http://{}:{}'.format(host, port), autoraise=True)
        super().run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

app = MyFlask(__name__)

#main page
@app.route('/', methods=['GET','POST'])
def index():
    # handle ajax requests
    if request.method == 'POST':
        data = request.json
        if "function_name" not in data:
            raise ValueError('No function_name specified')
        if "kwargs" not in data:
            data["kwargs"] = dict()

        # execute asked function with kwargs
        func = eval("callable.{}".format(data["function_name"]))
        result = func(**data["kwargs"])

        # return data
        resp = jsonify(result)
        resp.status_code = 200
        return resp

    # render page on get requests
    return render_template(
        'index.html',
        css="/static/style.css?q="+str(time.time()),
        jsPython="/static/pythonCom.js?q="+str(time.time()),
        js="/static/script.js?q="+str(time.time())
    )

@app.route('/quit', methods=['GET'])
def quit():
    # kill server
    shutdown_server()
    return ''

#launch server on http port
app.run(host=HOST, port=PORT)