
from flask import Flask, request
from beem import Steem

app = Flask(__name__)

# Initialize with your Posting Key

# 修正前（ダメ）
# steem = Steem(keys=["PASTE_YOUR_POSTING_KEY_HERE"])

# ✅ 修正後（環境変数から取得）
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
            author="PASTE_YOUR_HIVE_USERNAME_HERE",
            tags=["ai", "n8n"]
        )
        return {"status": "success", "message": "Hive post submitted."}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
