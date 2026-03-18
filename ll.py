from __future__ import annotations
from typing import Optional, Dict


class Node:
    def __init__(self, data: Dict[str, str]):
        self.data: Dict[str, str] = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def __repr__(self) -> str:
        return f"DATA: {self.data}"


class LinkedList:
    def __init__(self) -> None:
        self.start: Optional[Node] = None

    def __repr__(self) -> str:
        nodes = ["START"]

        for node in self:
            nodes.append(node.data["name"])

        nodes.append("NIL")

        return "\n" + " --> ".join(nodes)

    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next

    def traverse(self) -> None:
        for node in self:
            print(node)

    def insert_at_beginning(self, element: Node) -> None:
        if self.start is not None:
            self.start.prev = element

        element.next = self.start
        self.start = element

    def insert_at_end(self, element: Node) -> None:
        if self.start is None:
            self.start = element
            return

        current = self.start

        while current.next is not None:
            current = current.next

        current.next = element
        element.prev = current