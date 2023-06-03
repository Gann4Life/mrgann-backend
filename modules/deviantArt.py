import requests, xmltodict
class DeviantArtGallery:
	def __init__(self, username, gallery):
		self.username = username
		self.gallery = gallery
		self.response = requests.get(self.get_url())
	def get_url(self):
		return f"https://backend.deviantart.com/rss.xml?q=gallery:{self.username}/{self.gallery}"

	def get_request_status(self):
		return self.response.status_code

	def get_request_dict(self):
		if self.response.status_code == 200:
			xml_data = self.response.content.decode("utf-8")
			data_dict = xmltodict.parse(xml_data)
			return data_dict
		return "Failed to obtain gallery data. Error ", self.response.status_code

	def get_gallery_items(self):
		return self.get_request_dict()["rss"]["channel"]["item"]

	def get_deviant_items(self):
		return [Deviant(item) for item in self.get_gallery_items()]

class Deviant:
	def __init__(self, item):
		self.item = item
		self.title = self.item["title"]
		self.description = self.item["description"]
		self.date = self.item["pubDate"]
		self.image = self.item["media:content"]["@url"]
		self.height = self.item["media:content"]["@height"]
		self.width = self.item["media:content"]["@width"]
		self.link = self.item["link"]
		# self.author = self.item["media:credit"][0]["#text"]
