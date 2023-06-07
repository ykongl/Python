import uuid


def get_UUID():
    return "".join(str(uuid.uuid4()).split("-"))


if __name__ == '__main__':
    print(get_UUID())
