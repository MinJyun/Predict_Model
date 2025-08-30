from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# 載入模型
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        user_input = float(request.form['input_value'])
        prediction = model.predict([[user_input]])[0]
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
