from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
  subject=None
  contact=None
  pp=""
  if request.method=='POST':
    subject=request.form["subject"]
    contact=request.form["contact"]
  if subject=="Math":
    with open("Math.txt", "r") as file:
      pp=file.read()
    with open("Math.txt", "a") as file:
      file.write(contact+"\n")

      
  if subject=="Biology":
    with open("Biology.txt", "r") as file:
      pp=file.read()
    with open("Biology.txt", "a") as file:
      file.write(contact+"\n")

      
  if subject=="Chemistry":
    with open("Chemistry".txt, "r") as file:
      pp=file.read()
    with open("Chemistry.txt", "a") as file:
        file.write(contact+"\n")

      
  if subject=="Econs":
    with open("Econs.txt", "r") as file:
      pp=file.read()
    with open("Econs.txt", "a") as file:
        file.write(contact+"\n")

      
  if subject=="Gp":
    with open("Gp.txt", "r") as file:
      pp=file.read()
    with open("Gp.txt", "a") as file:
        file.write(contact+"\n")

      
  if subject=="Physics":
    with open("Physics.txt", "r") as file:
      pp=file.read()
    with open("Physics.txt", "a") as file:
        file.write(contact+"\n")

      
    
  return render_template('index.html', subject=subject, contact=contact, pp=pp)




app.run(debug=True, host='0.0.0.0', port=81)
