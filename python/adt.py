from enum import Enum
from typing import Any, Generic, Optional, TypeVar, Union

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T, left: 'Tree[T]', right: 'Tree[T]') -> None:
        self.value = value
        self.left = left
        self.right = right


Tree = Optional[Node[T]]
