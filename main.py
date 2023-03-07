from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  numbers=[1, 2, 3, 4, 5]
  with open('text.txt', 'r') as file:
    intro=file.read()
  data=None
  if request.method == 'POST':
    data=request.form['data']
    data=data.upper() #whatever you want to do here
    with open('data.txt', 'a') as file:
      file.write(data + "\n")
    return render_template('index.html', data=data, intro=intro, nums=numbers)


app.run(host='0.0.0.0', port=81)
