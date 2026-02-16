import requests

class Drrr:
	def __init__(self, language: str = "en-US") -> None:
		self.api = "https://drrr.com"
		self.auth_token = None
		self.client_token = None
		self.tokens = self.get_tokens()
		self.session = requests.Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-N975F Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.120 Mobile Safari/537.36",
			"Cookie": f"drrr-session-1={self.client_token}"
		}
		self.language = language
	
	def login(
			self,
			nickname: str,
			icon: str = "kuromu-2x",
			language: str = "en-US") -> dict:
		data = {
			"name": nickname,
			"icon": icon,
			"token": self.auth_token,
			"login": "ENTER",
			"language": self.language
		}
		return self.session.post(
			f"{self.api}?api=json", data=data).json()
	
	def create_room(
			self,
			name: str,
			description: str,
			users_limit: int = 5,
			music: bool = False,
			adult: bool = False,
			conceal: bool = False) -> dict:
		data = {
			"name": name,
			"description": description,
			"limit": users_limit,
			"language": self.language,
			"submit": "Create Room"
		}
		if music:
			data["music"] = music
		if adult:
			data["adult"] = adult
		if conceal:
			data["conceal"] = conceal
		return self.session.post(
			f"{self.api}/create_room?api=json", data=data).json()
	
	def join_room(self, room_id: str) -> dict:
		return self.session.get(
			f"{self.api}/room?id={room_id}&api=json").json()
	
	def leave_room(self, room_id: str) -> dict:
		data = {
			"leave": "leave"
		}
		return self.session.post(
			f"{self.api}/room?ajax=1&api=json", data=data).json()
	
	def transfer_host(self, user_id: str) -> dict:
		data = {
			"new_host": user_id
		}
		return self.session.post(
			f"{self.api}/room?ajax=1&api=json", data=data).json()
	
	def ban_user(self, user_id: str) -> dict:
		data = {
			"ban": user_id
		}
		return self.session.post(
			f"{self.api}/room?ajax=1&api=json", data=data).json()
	
	def kick_user(self, user_id: str) -> dict:
		data = {
			"kick": user_id
		}
		return self.session.post(
			f"{self.api}/room?ajax=1&api=json", data=data).json()
	
	def send_message(
			self,
			message: str,
			url: str = "",
			to: str = "") -> dict:
		data = {
			"message": message,
			"url": url,
			"to": to
		}
		return self.session.post(
			f"{self.api}/room?ajax=1&api=json", data=data).json()
	
	def edit_room(
			self,
			title: str = None,
			description: str = None) -> dict:
		data = {}
		if title:
			data["room_name"] = title
		if description:
			data["room_description"] = description
		return self.session.post(
			f"{self.api}/room?ajax=1&api=json", data=data).json()
	
	def play_music_in_room(
			self,
			name: str,
			url: str) -> dict:
		data = {
			"music": "music",
			"name": name,
			"url": url
		}
		return self.session.post(
			f"{self.api}/room?ajax=1&api=json", data=data).json()
	
	def get_room_info(self) -> dict:
		return self.session.get(
			f"{self.api}/json.php?fast=1").json()
	
	def get_current_session(self) -> dict:
		return self.session.get(
			f"{self.api}/profile?api=json").json()
	
	def get_lounge(self) -> dict:
		return self.session.get(
			f"{self.api}/lounge?api=json").json()
	
	def get_tokens(self) -> dict:
		response = self.session.get(f"{self.api}?api=json").json()
		self.auth_token = response["token"]
		self.client_token = response["authorization"]
		return self.auth_token, self.client_token
