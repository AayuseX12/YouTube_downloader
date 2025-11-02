from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route("/ytdownload", methods=["GET"])
def ytdownload():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Please provide a YouTube URL"}), 400

    ydl_opts = {"format": "best"}  # you can change format if you want
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        # Returning title + direct download URL
        video_info = {
            "title": info.get("title"),
            "url": info.get("url")
        }
        return jsonify(video_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
