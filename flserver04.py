#index.html 로딩 서버 
from flask import Flask, render_template

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')
def index():
    #백엔그에서 데이터를 프론트엔드로 전달 
    return render_template('login.html')

    @app.route('/post', methods=['POST'])
    def post():
        userid = request.form.get('userid')
        password = request.form.get('password')
        msg = "{0} / {1}".format(userid, password)

        return msg


if __name__=='__main__':
    app.run(host='127.0.0.1', port=8080)