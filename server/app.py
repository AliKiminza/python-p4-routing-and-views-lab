#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views.</h1>'

@app.route("/print/<string:param>")
def print_string(param):
    print (param)
    return f'Printed String:{param}'

@app.route("/count/<int:param>")
def count (param):
    counting = '\n'.join(map(str,range(param +1)))
    return f'Counting Range:{counting}'

@app.route("/math/<int:num1><operation><int:num2>")
def math(num1,operation,num2):
    result=None
    if operation == '+' :
        result = num1 + num2
    elif operation == '-' :
        result = num1 - num2
    elif operation == '*' :
        result = num1 * num2
    elif operation == 'div' :
        result = num1/num2  
    elif operation == '%' :
        result = num1%num2         

    if result is not None:
        return f'Result:{result}'    
    else :
        return f'invalid operation'
    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
