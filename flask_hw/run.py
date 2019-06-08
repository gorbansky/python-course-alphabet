import db

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html', page='main')


@app.route('/fruits')
def fruits_page():
    return render_template('fruits.html', values=db.get_fruits(), page='fruits')


@app.route('/fruits', methods=['POST'])
def fruit_setup():
    input_value = request.form.get('definition')
    input_action = request.form.get('action')
    if input_action == 'add':
        db.add_fruit(input_value)
    elif input_action == 'remove':
        db.remove_fruit(input_value)
    else:
        return fruits_page()
    return fruits_page()


@app.route('/vegetables')
def vegetables_page():
    return render_template('vegetables.html', values=db.get_vegetables(), page='vegetables')


@app.route('/vegetables', methods=['POST'])
def vegetable_setup():
    input_value = request.form.get('definition')
    input_action = request.form.get('action')
    if input_action == 'add':
        db.add_vegetable(input_value)
    elif input_action == 'remove':
        db.remove_vegetable(input_value)
    else:
        return vegetables_page()
    return vegetables_page()


@app.route('/come_back_home')
def come_back_home():
    return redirect(url_for("home_page"))


@app.route('/blablabla')
def test_404_page():
    return render_template("404.html")


@app.errorhandler(404)
def error_404_page(error):
    return render_template("404.html", error=error)


if __name__ == '__main__':
    app.run(debug=True)
