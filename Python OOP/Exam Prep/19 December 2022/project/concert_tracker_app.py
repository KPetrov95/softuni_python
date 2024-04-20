from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: [Band] = []
        self.musicians: [Musician] = []
        self.concerts: [Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        already_musician = next((m for m in self.musicians if m.name == name), None)
        if already_musician:
            raise Exception(f"{name} is already a musician!")
        musician = self._create_musician(self.MUSICIAN_TYPES[musician_type], name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        already_band = self._find_band(name)
        if already_band:
            raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        already_concert = next((c for c in self.concerts if c.place == place), None)
        if already_concert:
            raise Exception(f"{place} is already registered for {already_concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_musician(musician_name)
        band = self._find_band(band_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician = self._find_musician(musician_name)
        band = self._find_band(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        if musician not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._find_band(band_name)
        concert = next(c for c in self.concerts if c.place == concert_place)
        guitarists = [s for s in band.members if isinstance(s, Guitarist)]
        drummers = [s for s in band.members if isinstance(s, Drummer)]
        singers = [s for s in band.members if isinstance(s, Singer)]
        if not (guitarists and singers and drummers):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        guitarist_qualified = True
        for guitarist in guitarists:
            if concert.genre == 'Rock':
                if 'play rock' not in guitarist.skills:
                    guitarist_qualified = False
            elif concert.genre == 'Metal':
                if 'play metal' not in guitarist.skills:
                    guitarist_qualified = False
            else:
                if 'play jazz' not in guitarist.skills:
                    guitarist_qualified = False

        singers_qualified = True
        for singer in singers:
            if concert.genre == 'Rock':
                if 'sing high pitch notes' not in singer.skills:
                    singers_qualified = False
            elif concert.genre == 'Metal':
                if 'sing low pitch notes' not in singer.skills:
                    singers_qualified = False
            else:
                if 'sing low pitch notes' not in singer.skills or 'sing high pitch notes' not in singer.skills:

                    singers_qualified = False
        drummers_qualified = True
        for drummer in drummers:
            if concert.genre == 'Rock':
                if 'play the drums with drumsticks' not in drummer.skills:
                    drummers_qualified = False
            elif concert.genre == 'Metal':
                if 'play the drums with drumsticks' not in drummer.skills:
                    drummers_qualified = False
            else:
                if 'play the drums with drum brushes' not in drummer.skills:
                    drummers_qualified = False

        if not guitarist_qualified or not drummers_qualified or not singers_qualified:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

#HELPER_METHODS

    @staticmethod
    def _create_musician(_type, name, age):
        return _type(name, age)

    def _find_musician(self, param):
        musician = [m for m in self.musicians if m.name == param]
        if musician:
            return musician[0]

    def _find_band(self, _name):
        band = [b for b in self.bands if b.name == _name]
        if band:
            return band[0]
