from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people: int):
        for room in self.rooms:
            if room_number == room.number:
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room_number == room.number:
                return room.free_room()

    def status(self):
        total_guests = sum([room.guests for room in self.rooms])
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        return f"Hotel {self.name} has {total_guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
