@app.route("/login")
def login():
  username = request.values.get('username')
  password = request.values.get('password')
  
  db = pymysql.connect("localhost")
cursor = db.cursor()
