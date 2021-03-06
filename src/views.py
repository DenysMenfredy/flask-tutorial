from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html', name='Denys')


@views.route('/profile')
def profile():
    args = request.args
    name = args.get('name')
    return render_template('profile.html', name=name)


@views.route('/json')
def get_json():
    return jsonify({'name': 'Denys', 'age': 22})

@views.route('/data')
def get_data():
    data = request.json
    print(data)
    return jsonify(data)

@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))

