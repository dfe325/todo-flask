from models import ToDoModel

class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        result = self.model.create(params["Title"], params["Description"])
        return result

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def list(self):
        response = self.model.list_items()
        return response