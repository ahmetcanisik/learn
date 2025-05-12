#!/usr/bin/env python3
import uuid


class P:
    def __init__(self, id: str = None):
        if id is None:
            raise ValueError("Missing id")
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if new_id == self._id:
            raise ValueError("id's same!")
        self._id = new_id

    def __str__(self):
        return str(self._id)


def gen_id():
    return str(uuid.uuid4())


def main():
    pid = P(gen_id())
    print(pid)

    pid.id = gen_id()
    print(pid.id)


if __name__ == "__main__":
    main()
