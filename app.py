from flask import Flask, render_template, request
import message


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/badges')
def badges():
    return render_template('badges.html')


@app.route('/sub', methods = ['POST'])
def sub():
    if request.method == 'POST':
        names = request.form['names']
        email = request.form['email']
        mobile = request.form['mobile']
        reason = request.form['reason']
        news = request.form['message']
        message.email_alert(news,reason, 'nrainer001@gmail.com' , names, email, mobile)
        return render_template('home.html' )

if __name__ == '__main__':
    app.run(debug=True)