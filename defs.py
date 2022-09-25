class Music:
    def __init__(self, name: str, album: str, artist: str = ""):
        self.name = name
        self.album = album
        self.artist = artist
        self.name = f"{self.artist} - {self.name}" if self.artist else self.name
