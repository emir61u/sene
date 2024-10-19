# Import
from flask import Flask, render_template,request, redirect
from ses import turkce



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get("button_discord")
    button_html = request.form.get("button_html")
    button_db = request.form.get("button_db")


    email = request.form.get("email")
    text = request.form.get("text")


    return render_template('index.html',button_python=button_python,
                                    button_discord = button_discord,
                                    button_html = button_html,
                                    button_db = button_db)


@app.route('/ses')
def sess():

    try:

        kayit = turkce()
    except:
        kayit= "bir hata oluştu" 
    return render_template('index.html', kayit=kayit)
@app.route("/ses")
def ses():

    try:
        kayit = "Merhaba"
        gibi = "iyi"
    except:
        gibi = "boşver be"
    return render_template('index.html', gibi=gibi,
                                        kayit=kayit)
    

    
    

                                    
    
    
    

    

if __name__ == "__main__":
    app.run(debug=True)
