from flask import Flask
from calcalc.CalCalc import calculate

app = Flask(__name__)

@app.route("/")
def hello():
    show_result = calculate('2+2', return_int = True)
    print("\ncalculate('2+2', return_int = True: ", show_result)
    return "Running python/flask inside Docker (from Bloom). \n Value: " + str(show_result)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
