from typing import List
from dataclasses import dataclass


@dataclass
class HanoiTower:
    disk_values: List[int]
    name: str = ''

    @property
    def is_empty(self) -> bool:
        return len(self.disk_values) == 0

    @property
    def current_disk_value(self) -> int:
        return self.disk_values[-1] if not self.is_empty else 0

    def can_receive_value(self, value: int) -> bool:
        if self.is_empty:
            return True

        return value < self.current_disk_value

    def add_value(self, value: int) -> None:
        assert self.can_receive_value(value)

        self.disk_values.append(value)

    def remove_current_value(self) -> None:
        self.disk_values.pop()


@dataclass
class Disk:
    value: int
    tower: HanoiTower
    was_mooved: bool = False

    @property
    def is_current_value(self) -> bool:
        """Checks if its value is the upper value of the tower"""
        return self.value == self.tower.current_disk_value

    def can_go_to_tower(self, new_tower: HanoiTower) -> bool:
        return new_tower.can_receive_value(self.value) and not self.tower.name == new_tower.name

    def move(self, new_tower: HanoiTower) -> None:
        if not self.is_current_value or not self.can_go_to_tower(new_tower):
            return

        print(f"Mooving disk {self.value} from {self.tower.name} tower to {new_tower.name} tower")

        self.was_mooved = True
        self.tower.remove_current_value()
        new_tower.add_value(self.value)
        self.tower = new_tower


class HanoiTowerOrchestrator:
    """Solves the Hanoi Tower problem given a number of disks:

    problem: https://www.mathsisfun.com/games/towerofhanoi.html

    usage:
    >>> hanoi = HanoiTowerOrchestrator(number_of_disks=3)
    >>> hanoi.run()
    """

    def __init__(self, number_of_disks: int) -> None:
        # creates a decreasing list of disk sizes
        # so we can pop() and append() to the minor values
        self.values = list(range(number_of_disks,0,-1))

        self.origin_tower = HanoiTower(name='origin', disk_values=[])
        self.auxiliar_tower = HanoiTower(name='auxiliar', disk_values=[])
        self.destination_tower = HanoiTower(name='destination', disk_values=[])

        self.disks = []

        self._build_initial_values()

    def run(self) -> None:
        towers = [self.origin_tower, self.destination_tower, self.auxiliar_tower]

        last_mooved_value = 0

        while not self.is_tower_solved:
            for disk in self.disks:
                for tower in towers:
                    if not disk.value == last_mooved_value:
                        disk.move(tower)

                    if disk.was_mooved:
                        last_mooved_value = disk.value
                        disk.was_mooved = False

    @property
    def is_tower_solved(self) -> bool:
        """All disks must be in the destination tower"""
        return set(self.destination_tower.disk_values) == set(self.values)

    def _build_initial_values(self) -> None:
        """All disks must start at the origin tower"""
        for value in self.values:
            self.disks.append(Disk(value=value, tower=self.origin_tower))
            self.origin_tower.add_value(value)
