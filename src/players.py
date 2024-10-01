from src.base import BaseClient

class Players(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_uri = 'players'

    def trending(self, sport='nfl', type='add', lookback_hours='24', limit='25'):
        uri: str = f"/{sport}/trending/{type}"
        params = { lookback_hours: lookback_hours, limit: limit }

        return self.get(uri,params)

    def all(self, sport='nfl'):
        uri: str = f"/{sport}"

        return self.get(uri)


