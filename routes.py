from flask import Flask, render_template, request, session, url_for, redirect
from models import db, user ,blogModel
from forms import  LoginForm, blogForm
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/demo'
db.init_app(app)
app.secret_key = "development-key"


@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    print("method is"+request.method)
    if request.method=='POST':
        loginid = form.loginid.data
        password = form.password.data

        loginuser = user.query.filter_by(loginid=loginid,password=password).first()

        if loginuser is not None:
            session['loginid']=form.loginid.data
            print("value is"+session['loginid'])
            return redirect(url_for('blog'))
        else:
            return redirect(url_for('login'))
    elif request.method=='GET':
        return render_template('login.html',form=form)

@app.route("/blog",methods=['GET','POST'])
def blog():
    if not 'loginid' in session:
        return redirect(url_for('login'))
    print("value is blog   " + session['loginid'])
    form = blogForm()
    if request.method=="POST":
        newblog = blogModel(form.title.data,form.blog.data,session['loginid'])
        db.session.add(newblog)
        db.session.commit()
        return "success"
    return render_template('addThought.html',form=form)

if __name__=="__main__":
    app.run(debug=True)
