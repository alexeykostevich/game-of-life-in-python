from abc import ABCMeta, abstractproperty, abstractmethod
from typing import Generic, Iterable, TypeVar, Tuple


T = TypeVar('T')


class World(Generic[T]):
    """Represents a world for 'The Game of Life'."""
    __metaclass__ = ABCMeta

    @abstractproperty
    def width(self) -> int:
        """Returns world width."""
        pass

    @abstractproperty
    def height(self) -> int:
        """Returns world height."""
        pass

    @abstractmethod
    def get_positions(self) -> Tuple[int, int]:
        """Returns a new iterator that can iterate over world positions."""
        pass

    @abstractmethod
    def get_neighbours_of(self, x: int, y: int) -> Iterable[T]:
        """Returns a new iterator that can iterate over neighbours around the specified position."""
        pass

    @abstractmethod
    def __getitem__(self, position: Tuple[int, int]) -> T:
        """Returns a value for the specified position using self[x, y]."""
        pass

    @abstractmethod
    def __setitem__(self, position: Tuple[int, int], value: T):
        """Sets the value for the specified position using self[x, y]."""
        pass
