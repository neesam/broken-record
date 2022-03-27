import re
from ..config.mysqlconnection import connectToMySQL
from datetime import datetime
import math

class Message:
    db = 'rym'

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.sender = data['sender']
        self.receiver_id = data['receiver_id']
        self.receiver = data['receiver']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod

    def get_user_messages(cls, data):

        query = 'SELECT users.username as sender, users2.username as receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users2.id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        messages = []

        for message in results:
            messages.append(cls(message))
        return messages

    @classmethod

    def get_my_messages_too(cls, data):

        query = 'SELECT users.username as sender, users2.username as receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users.id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        messages = []

        for message in results:
            messages.append(cls(message))
        return messages

    @classmethod
    
    def time_span(self):

        now = datetime.now()

        delta = now - self.created_at

        print(delta.days)

        print(delta.total_seconds())

        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
                return f"{math.floor(math.floor(delta.total_seconds() / 60) /60)} hours ago"
        elif delta.total_seconds() >= 60:
                return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    @classmethod
    def save(cls,data):

        query = "INSERT INTO messages (content,sender_id,receiver_id, created_at, updated_at) VALUES (%(content)s,%(sender_id)s,%(receiver_id)s, NOW(), NOW());"

        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)

        return results

    @classmethod
    def destroy(cls,data):

        query = "DELETE FROM messages WHERE messages.id = %(id)s;"

        return connectToMySQL(cls.db).query_db(query,data)