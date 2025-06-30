from flask import Flask, render_template, request
eco_app = Flask(__name__)

@eco_app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('success.html', name=name)
    return render_template('index.html')

if __name__ == '__main__':
    eco_app.run(host="0.0.0.0", port=8080, debug=True)



