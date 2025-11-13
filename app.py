from flask import Flask, render_template,request

app = Flask(__name__)

app_name = "Flask App"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/app')
def home():
    return f"welcome {app_name}"

@app.route('/data')
def data():
    user = {"name" : "aril", "age" :20, "city" : "Makassar"}
    return render_template('data.html', user=user)

@app.route("/aplikasi", methods=["GET","POST"])
def aplikasi():
    er = None
    if request.method == "POST":
        try:
            likes = int(request.form["likes"])
            comments = int(request.form["comments"])
            share = int(request.form["shares"])
            followers = int(request.form["followers"])

            if followers == 0:
                return "jumlah followers tidak boleh 0!"
            
            er = ((likes + comments + share) / followers) * 100

        except ValueError:
            return "input tidak valid ! masukkan angka yang benar"
        
    return render_template("aplikasi.html", er=round(er, 2)if er is not None else None)

if __name__ == "__main__":
    app.run(debug=True)
            

app.run(debug=True)