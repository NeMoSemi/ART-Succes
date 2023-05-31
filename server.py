from flask import render_template, Flask

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = 'never-gonna-give-you-up'


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")