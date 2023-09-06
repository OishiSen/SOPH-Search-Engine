from flask import Flask, render_template, request
from SOPSearchEngine import SOPSearchEngine

app = Flask(__name__)
engine = SOPSearchEngine()

@app.route('/', methods=['GET', 'POST'])
def index():
    combined_results = []
    query = ""

    if request.method == 'POST':
        query = request.form['query']
        combined_results = engine.search(query)
    print(combined_results)

    return render_template('index.html', combined_results=combined_results, query=query)

if __name__ == "__main__":
    app.run(debug=True)
