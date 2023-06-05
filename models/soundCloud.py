import requests, xmltodict

class SoundCloudFeed:
	def __init__(self, userid):
		self.url = f"https://feeds.soundcloud.com/users/soundcloud:users:{userid}/sounds.rss"

		self.response = requests.get(self.url)

	def xml_as_dict(self):
		if self.response.status_code == 200:
			xml_data = self.response.content.decode("utf-8")
			data_dict = xmltodict.parse(xml_data)
			return data_dict
		return "Failed to obtain feed data. Error ", self.response.status_code

	def items(self):
		return self.xml_as_dict()["rss"]["channel"]["item"]

	def tracklist(self):
		return [SoundCloudTrack(item) for item in self.items()]

class SoundCloudTrack:
	def __init__(self, track):
		self.track = track
		self.trackid = self.track["guid"]["#text"].split("/")[-1]
		self.title = self.track["title"]
		self.description = self.track["description"]
		self.date = self.track["pubDate"]
		self.image = self.track["itunes:image"]["@href"]
		self.link = self.track["link"]
		self.author = self.track["itunes:author"]

	def as_dict(self):
		return {
			"trackid": self.trackid,
			"title": self.title,
			"description": self.description,
			"date": self.date,
			"image": self.image,
			"link": self.link,
			"author": self.author
		}