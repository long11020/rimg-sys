from app import app, db
from flask import request, render_template, jsonify
from app.models import User, Admin


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login/', methods=['GET'])
def u_login():
    account = request.args.get("account")
    password = request.args.get("password")
    data = db.session.query(User).filter(User.u_account == account).first()
    result = data.to_dict()
    if password == result['u_password']:
        return jsonify({'status': 1, 'u_name': result['u_name'], 'id': result['u_id']})
    else:
        return jsonify({'status': 0})


@app.route('/alogin', methods=['GET'])
def a_login():
    account = request.args.get("account")
    password = request.args.get("password")
    data = db.session.query(Admin).filter(Admin.a_account == account).first()
    result = data.to_dict()
    if password == result['a_password']:
        return jsonify({'status': 1, 'u_name': result['a_name'], 'id': result['a_id']})
    else:
        return jsonify({'status': 0})


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/userReg', methods=['GET'])
def userReg():
    name = request.args.get("name")
    account = request.args.get("account")
    password = request.args.get("password")
    user = User(account,password,name)
    db.session.add(user)
    db.session.commit()
    app.logger.info(account+"用户注册")
    return jsonify({'status': 1})
