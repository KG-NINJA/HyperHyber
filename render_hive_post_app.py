
from flask import Flask, request
from beem import Steem

app = Flask(__name__)

# Initialize with your Posting Key
steem = Steem(keys=["PASTE_YOUR_POSTING_KEY_HERE"])

@app.route('/hive', methods=['POST'])
def hive_post():
    data = request.json
    title = data.get('title', 'Untitled')
    body = data.get('body', 'No content provided.')

    try:
        steem.post(
            title=title,
            body=body,
            author="PASTE_YOUR_HIVE_USERNAME_HERE",
            tags=["ai", "n8n"]
        )
        return {"status": "success", "message": "Hive post submitted."}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
