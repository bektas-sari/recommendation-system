import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# CSV dosyasını yükle
data = pd.read_csv('data/recommendations.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    category = request.args.get('category', 'movies')  # Varsayılan olarak 'movies'
    recommendations = data[data['category'] == category][['title', 'author', 'description']].values.tolist()
    return render_template('recommend.html', category=category.capitalize(), recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
