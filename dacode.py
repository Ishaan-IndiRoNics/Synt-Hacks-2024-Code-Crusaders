from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

name = ""
q = 0
c = 0
p = [0, 0]
s = [0, 0]
messages = ["You a noob", ""]
test = [["x multipled by 6 gives 66", "11", 0], ["Evaluate the following x+28/4=50", "172", 0], ["Find square root of 2704.", "52", 0], ["What are the openings in our noses?", "nostrils", 1], ["How many teeth do adults have?", "32", 1], ["If we were to fall and get cut what part of blood will help it get better?", "platelets", 1]]
assesment = []

@app.route('/')
def start():
    global name, q, c, p, s
    name = ""
    q = 0
    c = 0
    p = [0, 0]
    s = [0, 0]
    return render_template("login.html")

@app.route('/teststarts', methods=['POST', 'GET'])
def ts():
    global name
    name = request.form['name']
    return redirect(url_for('t'))
  
@app.route('/test')
def t():
    global q
    if q <= 5:
        q = q + 1
        return render_template("test.html", question=test[q-1][0])
    else:
        return redirect(url_for('success'))

@app.route('/check', methods=['POST', 'GET'])
def check():
    ans = request.form['ans']
    if ans.lower() == test[q-1][1]:
        s[test[q-1][2]] = s[test[q-1][2]] + 1
    return redirect(url_for('t'))

@app.route('/success')
def success():
    return render_template("success.html", s0=s[0], s1=s[1])

@app.route('/home')
def home():
    return render_template("home.html", s0=s[0], s1=s[1])

@app.route('/assessstarts')
def assessstarts():
    global q
    q = 0
    for i in range(10):
        assessment[i][4] = 0
    return redirect(url_for('a'))

@app.route('/assessment')
def a():
    global q, c
    if q == 0:
        for i in range(10):
            if assessment[i][3] == s[0] and assessment[i][4] == 0:
                assessment[i][4] = 1
                c = i
                return render_template("assessment.html", question=assessment[i][0])
        q = 1
    if q == 1:
        for i in range(10, 15):
            if assessment[i][3] == s[1] and assessment[i][4] == 0:
                assessment[i][4] = 1
                c = i
                return render_template("assessment.html", question=assessment[i][0])
    return redirect(url_for('home'))

@app.route('/assesscheck', methods=['POST', 'GET'])
def assesscheck():
    global s
    ans = request.form['ans']
    if ans.lower() == assessment[c][1]:
        s[assessment[c][2]] = s[assessment[c][2]] + 1
    else:
        s[assessment[c][2]] = s[assessment[c][2]] - 1
    return redirect(url_for('a'))

if __name__ == '__main__':
    app.run(debug=True)

