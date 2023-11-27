import ast
import sys
from pylint.lint import Run

def parse_code(code):
    try:
        return ast.parse(code)
    except SyntaxError as e:
        raise SyntaxError(f"Syntax Error: {e}")

def run_pylint(code_filename):
    results = Run([code_filename], exit=False)
    return results.linter.stats

def analyze_code(code):
    try:
        parsed_code = parse_code(code)
    except SyntaxError as e:
        return {'error': str(e)}

    # write original code to a temporary file since pylint expects a file
    with open('temp_code.py', 'w') as temp_file:
        # remove trailing whitespace at the end of each line
        temp_file.write('\n'.join(line.rstrip() for line in code.split('\n')))

    # redirect stdout to a file
    with open('pylint_output.txt', 'w') as output_file:
        sys.stdout = output_file

        # run pylint on the temporary file
        pylint_output = run_pylint('temp_code.py')

        # reset stdout to the original value
        sys.stdout = sys.__stdout__

    # return the file name for reference
    return {'pylint_output_file': 'pylint_output.txt'}
