from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [song for song in songs]

    def add_song(self, song: Song):
        if not song.single:
            if not self.published:
                if song not in self.songs:
                    self.songs.append(song)
                    return f"Song {song.name} has been added to the album {self.name}."
                else:
                    return "Song is already in the album."
            else:
                return "Cannot add songs. Album is published."
        else:
            return f"Cannot add {song.name}. It's a single"

    def remove_song(self, song_name: str):
        for song in self.songs:
            if song.name == song_name:
                if not self.published:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
                else:
                    return "Cannot remove songs. Album is published."
        return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = [f'Album {self.name}']
        for song in self.songs:
            result.append(song.get_info())
        return "\n".join(result)


