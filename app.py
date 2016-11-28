from flask import Flask
from calcalc.CalCalc import calculate

app = Flask(__name__)

@app.route("/")
def hello():
    show_int = calculate('2+2', return_int = True)
    show_float = calculate('2+2', return_float = True)
    print("\ncalculate('2+2', return_int = True: ", show_int)
    return "<h3>Running python/flask inside Docker (from Bloom).</h3><p>Value of 'calculate('2+2', return_int = True)': <strong>" + str(show_int) + "</strong></p><p>Value of 'calculate('2+2', return_float = True)': <strong>" + str(show_float) + "</strong></p>"


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
