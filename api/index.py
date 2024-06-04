from flask import Flask, render_template,request, session,jsonify,Response, stream_with_context
import time

app = Flask(__name__)


@app.route('/real_time_number')
def real_time_number():
    def generate():
        for i in range(100):
            yield '{"number": %s}' % i
            time.sleep(1)

    return Response(stream_with_context(generate()), mimetype='application/json')


@app.route('/hello')
def home():
    return jsonify({"message": "Hello, World"})

@app.route('/data', methods = ["GET","POST"])   # GET 和 POST 都可以
def get_data():
    name = request.args.get("name")
    age = request.args.get("age")
    return jsonify({"name": name,"age":age})

@app.route('/hello1')
def hello():
    return 'Hello, world'


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/html')
def html():
   return render_template('test.html')

@app.route('/')
def list_html():
   return render_template('list.html')   