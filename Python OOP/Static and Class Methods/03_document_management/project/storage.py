from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if not self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if not self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for category in self.categories:
            if category_id == category.id:
                category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic_id == topic.id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document_id == document.id:
                document.file_name = new_file_name

    def delete_category(self, category_id):
        for category in self.categories:
            if category_id == category.id:
                self.categories.remove(category)

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic_id == topic.id:
                self.topics.remove(topic)

    def delete_document(self, document_id):
        for document in self.documents:
            if document_id == document.id:
                self.documents.remove(document)

    def get_document(self, document_id):
        return next((d for d in self.documents if d.id == document_id))

    def __repr__(self):
        result = []
        for doc in self.documents:
            result.append(doc.__repr__())

        return "\n".join(result)