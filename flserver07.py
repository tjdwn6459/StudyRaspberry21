#index.html 로딩 서버 
from flask import Flask, render_template, request
import MySQLdb as mysql


#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')
def index():

    db = mysql.connect('localhost', 'root', '12345', 'test', charset='uft8')
    cur = db.cursor(mysql.cursors.DictCursor)
    cur.execute('SELECT * FROM student')
    result = []
    while True:
        student = cur.fetchone()
        if not student: break

        result.append(student)

    cur.close()
    db.close()

  
     
     
    return render_template('mysqldata.html', row=result)

  
if __name__=='__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)