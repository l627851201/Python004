from abc import ABCMeta, abstractmethod

class Anmial(metaclass=ABCMeta):
    """
    动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
    """

    def __init__(self, type, body, character, isFierceness):
        self.type = type
        self.body = body
        self.character = character
        self.isFierceness = isFierceness

    @abstractmethod
    def checkIsFierceness(self):
        pass

