from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    op = data.get('op')
    result = None
    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        result = a / b if b != 0 else 'Error: Division by zero'
    else:
        result = 'Invalid operation'
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
