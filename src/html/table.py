from flask import Flask
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)
CORS(app)

open = "open"
close = "close"
tableData = [
    
    [open,open,close],
    [close,open,close],
    [open,close,close]
    
]


@app.route("/")
def table():
            

    return render_template('parking_page.html', trial = tableData)



if __name__ == "__main__":''
    
app.run(debug = True)
    