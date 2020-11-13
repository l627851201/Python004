from .animal import Anmial

class Cat(Anmial):
    """
    猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
    """

    def __init__(self, name, voice, isPet):
        super(self).__init__
        self.name = name
        self.voice = voice
        self.isPet = isPet

    def checkIsFierceness(self):
