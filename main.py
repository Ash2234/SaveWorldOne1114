from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

Math=[]
Gp=[]
Physics=[]
Chemistry=[]
Biology=[]
Econs=[]
data=[Math, Gp, Physics, Chemistry, Biology, Econs]

def index():
  subject=None
  if request.method=='POST':
    subject=request.form["subject"]
    contact=request.form["contact"]
  return render_template('index.html', subject=subject, contact=contact)




app.run(host='0.0.0.0', port=81)
