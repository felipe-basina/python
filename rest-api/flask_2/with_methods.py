from flask import render_template, request, jsonify, flash, Flask

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():  
    return render_template("index_2.html")

@app.route("/add/<int:first>/<int:second>", methods=["POST"])
@app.route("/add", methods=["POST"])
def add(first='',second=''):
    if first == '':
        first = int(request.form["first"])
    if second == '':
        second = int(request.form.get("second"))
    result = first + second
    return render_template("index_2.html",result=result)

@app.route("/send_data", methods=["GET","POST"])
def send_data():  
    data={"Eric Schles":"eric.schles@syncano.com",
          "job":"developer evangelist",
          "mission":"end slavery",
          "training for":"the olympics",
          "hobbies":["guitar","rock climbing"],
          "friends":"everyone"
          }
    return jsonify(data)
    
app.run(debug=True)