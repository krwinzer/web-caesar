from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""<!DOCTYPE html>
<html>
  <head>
    <style>
      form {{
        background-color: #eee;
        padding: 20px;
        margin: 0 auto;
        width: 540px;
        font: 16px sans-serif;
        border-radius: 10px;
      }}
      textarea {{
        margin: 10px 0;
        width: 540px;
        height: 120px;
      }}
    </style>
  </head>
  <body>
     <form action="" method="post">
        <input type="text" name="rot" value="0">Rotate by:<br>
        <textarea name="text" id="" cols="30" rows="10">{0}</textarea>
        <input type="submit" value="Submit">
     </form>
  </body>
</html>
"""

@app.route("/", methods=['POST'])
def crypt():
    rot = request.form["rot"]
    rot = int(rot)
    text = request.form["text"]

    return form.format(encrypt(text, rot))

@app.route("/")
def index():
    return form.format("")

app.run()
