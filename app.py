from flask import Flask
app = Flask(_name_)

@app.rout("/")
def hello():
    return "Hello, World! Running inside Docker!"
if__name_":
    app.run(host="0.0.0.0",port=5000)
