from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route("/api/v1/similarity", methods=['GET','POST'])
def computeSimilarity():
    f = request.files['file']
    f.save(f.filename)
    data = {
        'similarity': '97.335%'
    }
    return jsonify(
        code=0,
        data=data
    )

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)