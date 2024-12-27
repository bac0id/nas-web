from flask import Flask, render_template
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    result = subprocess.run(['df', '-h'], capture_output=True, text=True)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', df_output=result.stdout, current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
