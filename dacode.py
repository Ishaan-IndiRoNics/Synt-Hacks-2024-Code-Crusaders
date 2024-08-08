from flask import Flask, redirect, url_for, request

app = Flask(__name__)

op = 0
n1 = 0
n2 = 0


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


@app.route('/')
def start():
    return """
    
#user input operator to database
    
<html>
   <body style="backgroungcolor:blue" topmargin=50 leftmargin=100>      
      <form action = "http://localhost:5000/r1" method = "post">
<p>Type operation (1/2/3/4):</p>
<p><input type = "number" name = "n" /></p>
<p><input type = "Submit" value = "submit" /></p>
      </form>      
   </body>
</html>
"""


@app.route('/num1')
def num1():
    return """

#user input first no. to database
    
<html>

   <body>      
      <form action = "http://localhost:5000/r2" method = "post">
<p>Type number 1:</p>
<p><input type = "number" name = "n" /></p>
<p><input type = "Submit" value = "submit" /></p>
      </form>      
   </body>

</html>
"""


@app.route('/num2')
def num2():
    return """

#user input second no. to database
    
<html>
   <body>      
      <form action = "http://localhost:5000/r3" method = "post">
<p>Type number 2:</p>
<p><input type = "number" name = "n" /></p>
<p><input type = "Submit" value = "submit" /></p>
      </form>      
   </body>
</html>
"""


@app.route('/r1', methods=['POST', 'GET'])
def r1():
    global op
    op = request.form['n']
    return redirect(url_for('num1'))


@app.route('/r2', methods=['POST', 'GET'])
def r2():
    global n1
    n1 = request.form['n']
    return redirect(url_for('num2'))


@app.route('/r3', methods=['POST', 'GET'])
def r3():
    global n2
    n2 = request.form['n']
    return redirect(url_for('success'))

#output

@app.route('/success')
def success():
    num1 = int(n1)
    num2 = int(n2)
    if op == '1':
        return f"{num1} + {num2} = {add(num1, num2)}"

    elif op == '2':
        return f"{num1} - {num2} = {subtract(num1, num2)}"

    elif op == '3':
        return f"{num1} * {num2} = {multiply(num1, num2)}"

    elif op == '4':
        return f"{num1} / {num2} = {divide(num1, num2)}"


if __name__ == '__main__':
    app.run()
