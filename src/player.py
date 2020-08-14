# Write a class to hold player information, e.g. what room they are in
# currently.
from src.room import Room


class Player:
    def __init__(self, current_room, items):
        self.current_room: Room = current_room
        # self.items = items
