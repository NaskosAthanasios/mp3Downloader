from __future__ import unicode_literals
from flask import Flask, render_template, request, redirect
import youtube_dl

app = Flask(__name__)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=["POST", "GET"])
def download():
    url = request.form["url"]
    print("Someone just tried to download", url)
    # with youtube_dl.YoutubeDL() as ydl:
    #    url = ydl.extract_info(url, download=True)
    #    try:
    #        download_link = url["entries"][-1]["formats"][-1]["url"]
    #    except:
    #        download_link = url["formats"][-1]["url"]
    #    return redirect(download_link+"&dl=1")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return redirect('/')


if __name__ == '__main__':
    app.run()
