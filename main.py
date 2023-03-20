from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
  subject=None
  contact=None
  if request.method=='POST':
    subject=request.form["subject"]
    contact=request.form["contact"]
  return render_template('index.html', subject=subject, contact=contact)




app.run(host='0.0.0.0', port=81)
