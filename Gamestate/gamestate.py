from utils.named_list import NamedList
from .room_data import Rooms as rm


class Gamestate(NamedList):
    def __init__(self, player=None):
        names = ['player', 'room', 'history']
        vals = [player, rm.CC, []]
        super(Gamestate, self).__init__(title="Gamestate", names=names, values=vals)

    # Updates history by adding previous room and changes current room
    def new_room(self, room):
        history = self.get('history')
        self.update('history', history.append(self.get('room')))
        self.update('room', room)
