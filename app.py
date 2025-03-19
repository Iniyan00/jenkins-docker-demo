from flask import Flask
app = Flask(_name_)

@app.route("/")
def hello():
    return "Hello, World! Running inside Docker!"
if __name_ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
