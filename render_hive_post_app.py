import os
from beem import Steem
from flask import Flask, request

app = Flask(__name__)

steem = Steem(keys=[os.getenv("POSTING_KEY")])

@app.route('/hive', methods=['POST'])
def hive_post():
    data = request.json
    title = data.get('title', 'Untitled')
    body = data.get('body', 'No content provided.')

    try:
        steem.post(
            title=title,
            body=body,
            author=os.getenv("HIVE_USERNAME"),
            tags=["ai", "n8n"]
        )
        return {"status": "success", "message": "Hive post submitted."}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
