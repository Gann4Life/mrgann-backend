from flask import Blueprint, render_template, url_for
from models.deviantArt import DeviantArtGallery
from models.soundCloud import SoundCloudFeed

site = Blueprint("site", __name__, template_folder="templates", static_folder="static", static_url_path="/static")

@site.route("/")
def index():
	return render_template("index.html", showBackButton=False)

@site.route("/deviantart/<username>/<int:gallery>")
def view_gallery(username, gallery):
	gallery = DeviantArtGallery(username, gallery)
	return render_template("gallery.html", items=gallery.get_deviant_items(), author=username, showBackButton=True)

@site.route("/soundcloud/<int:userid>")
def view_music(userid):
	feed = SoundCloudFeed(userid)
	return render_template("music.html", items=feed.tracklist(), showBackButton=True)