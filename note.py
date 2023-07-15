import datetime


class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        note = cls(data['id'], data['title'], data['body'])
        note.created_at = data['created_at']
        note.updated_at = data['updated_at']
        return note
