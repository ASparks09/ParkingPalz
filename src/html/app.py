from flask import Flask, request

app = Flask(__name__)

@app.route('/action_page', methods=['POST'])
def store_info():
    email = request.form.get('Email')
    sid = request.form.get('SID')
    
    # Here you can store the data in a file or a database
    with open('student_info.txt', 'a') as f:
        f.write(f'Email: {email}, SID: {sid}\n')

    return 'Information stored successfully', 200

if __name__ == '__main__':
    app.run(debug=True)