from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

data=[Math, Gp, Physics, Chemistry, Biology, Econs]

def index():
  subject=None
  contact=None
  if request.method=='POST':
    subject=request.form["subject"]
    contact=request.form["contact"]
    for x in data:
      if x==subject:
        x.append(contact)
        break
  return render_template('index.html', subject=subject, contact=contact)




app.run(host='0.0.0.0', port=81)
