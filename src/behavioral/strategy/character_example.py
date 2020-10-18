from __future__ import annotations
from abc import ABC, abstractmethod


class WeaponBehavior(ABC):

    @abstractmethod
    def use_weapon(self) -> None:
        pass


class SwordBehavior(WeaponBehavior):

    def use_weapon(self) -> None:
        print('Use a sword')


class KnifeBehavior(WeaponBehavior):

    def use_weapon(self) -> None:
        print('Use a knife')


class BowAndArrowBehavior(WeaponBehavior):

    def use_weapon(self) -> None:
        print('Use a bow and arrow')


class AxeBehavior(WeaponBehavior):

    def use_weapon(self) -> None:
        print('Use a axe')


class Character:

    _weapon_behavior: WeaponBehavior

    def __init__(self, weapon_behavior: WeaponBehavior) -> None:
        self._weapon_behavior = weapon_behavior

    @property
    def weapon_behavior(self) -> WeaponBehavior:
        return self._weapon_behavior

    @weapon_behavior.setter
    def weapon_behavior(self, weapon_behavior: WeaponBehavior) -> None:
        self._weapon_behavior = weapon_behavior

    @abstractmethod
    def fight(self) -> None:
        pass


class King(Character):

    def fight(self) -> None:
        print('Fight like a king')


class Knight(Character):

    def fight(self) -> None:
        print('Fight like a knight')


class Queen(Character):

    def fight(self) -> None:
        print('Fight like a queen')


class Troll(Character):

    def fight(self) -> None:
        print('Fight like a troll')


def main() -> None:
    axe = AxeBehavior()
    troll = Troll(axe)
    troll.fight()
    troll.weapon_behavior.use_weapon()

    bow_and_arrow = BowAndArrowBehavior()
    troll.weapon_behavior = bow_and_arrow
    troll.weapon_behavior.use_weapon()


if __name__ == '__main__':
    main()
