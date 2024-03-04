class Store:
    def __init__(self):
        self.store = []

    def get_store(self):
        return self.store.pop(0) if len(self.store) > 0 else None

    def add_store(self, data):
        self.store.append(data)
        return None


store = Store()
