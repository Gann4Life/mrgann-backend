from flask import Blueprint, jsonify
from models.deviantArt import DeviantArtGallery
from models.soundCloud import SoundCloudFeed

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/deviantart/<username>/<int:gallery>")
def user_gallery(username, gallery):
	gallery = DeviantArtGallery(username, gallery)
	return jsonify(gallery.get_gallery_items())

@api.route("/soundcloud/<int:userid>")
def user_music(userid):
	feed = SoundCloudFeed(userid)
	return jsonify(feed.items())