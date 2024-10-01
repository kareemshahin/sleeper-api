from src.base import BaseClient

class League(BaseClient):
    def __init__(self, league_id: str):
        super().__init__()

        self.league_id = league_id
        self.base_uri = f"league/{self.league_id}"

    def get_league(self):
        uri: str = "/"

        return self.get(uri)

    def rosters(self):
        uri: str = "/rosters"

        return self.get(uri)

    def users(self):
        uri: str = "/users"

        return self.get(uri)

    def matchups(self, week:int = 1):
        uri: str = f"/matchups/{week}"

        return self.get(uri)
