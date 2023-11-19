

class Player:
    def __init__(self, hp, name, st, dex, const, intelligence, wis, char, ac):

        self._name = name
        self._hp = hp
        self._str = st
        self._dex = dex
        self._const = const
        self._int = intelligence
        self._wis = wis
        self._ac = ac
        self._unc = False
        self._info = ""
        self._init = 0
        self._group = 0

    def take_damage(self, amount):
        if amount >= self._hp:
            self._hp = 0
            self._unc = True
            return

        self._hp -= amount

    def set_name(self, name):
        self._name = name

    def set_hp(self, hp):
        self._hp = hp

    def set_str(self, st):
        self._st = st

    def set_dex(self, dex):
        self._dex = dex

    def set_const(self, const):
        self._const = const

    def set_int(self, inte):
        self._int = inte

    def set_wis(self, wis):
        self._wis = wis

    def set_ac(self, ac):
        self._ac = ac

    def set_unc(self, unc):
        self._unc = unc

    def add_info(self, info):
        self._info += info
        self._info += "\n"

    def set_group(self, group):
        self._group = group

    def set_init(self, init):
        self._init = init

    def get_group(self):
        return group


