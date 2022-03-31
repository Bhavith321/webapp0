from flask import *
app = Flask(__name__)

@app.route('/')
def index():
   return redirect_url(url_for('home'))

@app.route('/home')
def home():
   return render_template('index.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/dashboard')
def dashboard():
   return render_template('dashboard.html')

if __name__ == '__main__':
   app.run()
