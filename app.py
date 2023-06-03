from modules.deviantArt import DeviantArtGallery
from modules.soundCloud import SoundCloudFeed
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", showBackButton=False)

@app.route("/view/deviantart/<username>/<int:gallery>")
def view_gallery(username, gallery):
	gallery = DeviantArtGallery(username, gallery)
	return render_template("gallery.html", items=gallery.get_deviant_items(), author=username, showBackButton=True)

@app.route("/api/deviantart/<username>/<int:gallery>")
def user_gallery(username, gallery):
	gallery = DeviantArtGallery(username, gallery)
	return jsonify(gallery.get_gallery_items())

@app.route("/view/soundcloud/<int:userid>")
def view_music(userid):
	feed = SoundCloudFeed(userid)
	return render_template("music.html", items=feed.tracklist(), showBackButton=True)

@app.route("/api/soundcloud/<int:userid>")
def user_music(userid):
	feed = SoundCloudFeed(userid)
	return jsonify(feed.items())

@app.route("/console")
def console():
	return "fuck you"

if __name__ == '__main__':
	app.run()
