from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'TOPSECRET' # set a secret key for security purposes


@app.route('/')          
def initialCount():
    if 'integer' in session:
        session['integer'] +=1
        print('count it!')
        print(session['integer'])
    else:
        print("not counting")
        session['integer'] = 1

    return render_template('index.html')

@app.route('/plus')
def plusNumber():

    session['integer'] +=1
    print('count it 2x!')
    print(session['integer'])
    return redirect('/')


@app.route('/destroy_session')
def Destroy():
    session.pop('integer')		# clears a specific key
    session.clear()		# clears all keys
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True, port=5005)