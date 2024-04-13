from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    
    
    
    return "Running as intended"
    

@app.route("/map")
def map():
    
    



if __name__ == "__main__":
    
    app.run()


    