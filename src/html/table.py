from flask import Flask
from flask_cors import CORS, cross_origin
from flask import render_template

app = Flask(__name__)
CORS(app)

@app.route("/")
def table():
    
    tableData = ""
    
    for x in range(0, 4):
        #print <tr>
        row = "<tr>" 
        
        
        for y in range (0, 21):
            
            row += "<td>open</td>"
        
    
        row += "</tr>"
        tableData += row
            

    return render_template('parking_page.html', tableData)



if __name__ == "__main__":''
    
app.run()


    