from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/next')
def next():
 return render_template('next.html')

app.run(host='0.0.0.0' , port=5000)
