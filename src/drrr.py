from requests import Session

class Drrr:
    def __init__(self, language: str = "en-US") -> None:
        self.api = "https://drrr.com"
        self.language = language
        self.auth_token = None
        self.client_token = None
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-N975F Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.120 Mobile Safari/537.36"
        }
        self._fetch_tokens()

    def _post(self, endpoint: str, data: dict = None) -> dict:
        return self.session.post(
            f"{self.api}{endpoint}", data=data).json()

    def _get(self, endpoint: str) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}").json()

    def _room_post(self, data: dict) -> dict:
        return self._post("/room?ajax=1&api=json", data)

    def _fetch_tokens(self) -> None:
        response = self._get("?api=json")
        self.auth_token = response["token"]
        self.client_token = response["authorization"]
        self.session.headers["Cookie"] = f"drrr-session-1={self.client_token}"

    def login(
            self,
            nickname: str,
            icon: str = "kuromu-2x") -> dict:
        data = {
            "name": nickname,
            "icon": icon,
            "token": self.auth_token,
            "login": "ENTER",
            "language": self.language
        }
        return self._post("?api=json", data)

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
        return self._post("/create_room?api=json", data)

    def join_room(self, room_id: str) -> dict:
        return self._get(f"/room?id={room_id}&api=json")

    def leave_room(self) -> dict:
        return self._room_post({"leave": "leave"})

    def transfer_host(self, user_id: str) -> dict:
        return self._room_post({"new_host": user_id})

    def ban_user(self, user_id: str) -> dict:
        return self._room_post({"ban": user_id})

    def kick_user(self, user_id: str) -> dict:
        return self._room_post({"kick": user_id})

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
        return self._room_post(data)

    def edit_room(
            self,
            title: str = None,
            description: str = None) -> dict:
        data = {}
        if title:
            data["room_name"] = title
        if description:
            data["room_description"] = description
        return self._room_post(data)

    def play_music_in_room(self, name: str, url: str) -> dict:
        data = {
            "music": "music",
            "name": name,
            "url": url
        }
        return self._room_post(data)

    def get_room_info(self) -> dict:
        return self._get("/json.php?fast=1")

    def get_current_session(self) -> dict:
        return self._get("/profile?api=json")

    def get_lounge(self) -> dict:
        return self._get("/lounge?api=json")
