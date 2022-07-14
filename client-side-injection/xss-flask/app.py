from flask import Flask, render_template, request, make_response
import db

app = Flask(__name__)
app.config['TITLE'] = 'Comments or somethn'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    query = request.args.get('q')
    return render_template('index.html', comments=db.get_comments(query), query=query)

@app.route('/csp', methods=['GET', 'POST'])
def csp():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    query = request.args.get('q')
    res = make_response(render_template('index.html', comments=db.get_comments(query), query=query))
    res.headers.set('Content-Security-Policy', "script-src 'none'")
    return res

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)