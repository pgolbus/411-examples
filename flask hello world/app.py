from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "Hello World"



if __name__ == "__main__":
    # to run me from the command line: <flask --app main run> or <python app.py>
    #                             
    app.run(host='0.0.0.0', port=5000, debug=True)