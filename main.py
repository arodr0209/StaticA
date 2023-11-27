from flask import Flask, render_template, request
from analyzers.code_analyzer import analyze_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']

    # perform code analysis and save the results to a file
    analysis_result = analyze_code(code)

    # read the content of the file
    pylint_output_content = ''
    with open('pylint_output.txt', 'r') as file:
        pylint_output_content = file.read()

    # add the content to the analysis_result dictionary
    analysis_result['pylint_output_content'] = pylint_output_content

    # pass the analysis_result to the template
    return render_template('result.html', code=code, analysis_result=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
