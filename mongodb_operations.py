from pymongo import MongoClient
from datetime import datetime

class MongoDBOperations:
    def __init__(self, connection_string="mongodb://localhost:27017/"):
        self.client = MongoClient(connection_string)
        self.db = self.client['sample_database']
        self.collection = self.db['sample_collection']
    
    def insert_single_document(self, document):
        """Insert a single document into collection"""
        result = self.collection.insert_one(document)
        return result.inserted_id
    
    def insert_multiple_documents(self, documents):
        """Insert multiple documents into collection"""
        result = self.collection.insert_many(documents)
        return result.inserted_ids
    
    def find_all_documents(self):
        """Find all documents in collection"""
        return list(self.collection.find())
    
    def find_by_field(self, field, value):
        """Find documents by field value"""
        return list(self.collection.find({field: value}))
    
    def update_single_document(self, filter_query, update_data):
        """Update first document matching filter"""
        result = self.collection.update_one(filter_query, {"$set": update_data})
        return result.modified_count
    
    def update_multiple_documents(self, filter_query, update_data):
        """Update all documents matching filter"""
        result = self.collection.update_many(filter_query, {"$set": update_data})
        return result.modified_count
    
    def delete_single_document(self, filter_query):
        """Delete first document matching filter"""
        result = self.collection.delete_one(filter_query)
        return result.deleted_count
    
    def delete_multiple_documents(self, filter_query):
        """Delete all documents matching filter"""
        result = self.collection.delete_many(filter_query)
        return result.deleted_count
    
    def find_with_projection(self, filter_query, projection):
        """Find documents with specific fields"""
        return list(self.collection.find(filter_query, projection))
    
    def sort_documents(self, sort_field, direction=1):
        """Sort documents by field"""
        return list(self.collection.find().sort(sort_field, direction))
    
    def limit_results(self, limit):
        """Limit number of results"""
        return list(self.collection.find().limit(limit))
    
    def skip_documents(self, skip):
        """Skip documents in query"""
        return list(self.collection.find().skip(skip))
    
    def create_index(self, field):
        """Create index on field"""
        return self.collection.create_index(field)
    
    def drop_index(self, field):
        """Drop index from field"""
        return self.collection.drop_index(field)
    
    def aggregate_group(self, group_field, aggregate_field, operation):
        """Group documents and perform aggregation"""
        pipeline = [
            {"$group": {
                "_id": f"${group_field}",
                "result": {f"${operation}": f"${aggregate_field}"}
            }}
        ]
        return list(self.collection.aggregate(pipeline))
    
    def aggregate_match_project(self, match_query, project_fields):
        """Filter and reshape documents in aggregation"""
        pipeline = [
            {"$match": match_query},
            {"$project": project_fields}
        ]
        return list(self.collection.aggregate(pipeline))
    
    def collection_exists(self):
        """Check if collection exists"""
        return self.collection.name in self.db.list_collection_names()
    
    def count_documents(self, filter_query=None):
        """Count documents matching filter"""
        if filter_query:
            return self.collection.count_documents(filter_query)
        return self.collection.count_documents({})
    
    def paginate_results(self, page, per_page, filter_query=None):
        """Implement pagination"""
        skip = (page - 1) * per_page
        if filter_query:
            return list(self.collection.find(filter_query).skip(skip).limit(per_page))
        return list(self.collection.find().skip(skip).limit(per_page))

def main():
    # Example usage
    mongo_ops = MongoDBOperations()
    
    # Insert single document
    doc = {"name": "John", "age": 30, "city": "New York"}
    print("Inserted document ID:", mongo_ops.insert_single_document(doc))
    
    # Insert multiple documents
    docs = [
        {"name": "Alice", "age": 25, "city": "London"},
        {"name": "Bob", "age": 35, "city": "Paris"}
    ]
    print("Inserted document IDs:", mongo_ops.insert_multiple_documents(docs))
    
    # Find all documents
    print("\nAll documents:", mongo_ops.find_all_documents())
    
    # Find by field
    print("\nDocuments with name 'John':", mongo_ops.find_by_field("name", "John"))
    
    # Update document
    print("\nUpdated documents:", mongo_ops.update_single_document(
        {"name": "John"}, {"age": 31}))
    
    # Delete document
    print("\nDeleted documents:", mongo_ops.delete_single_document({"name": "Bob"}))
    
    # Create index
    print("\nCreated index:", mongo_ops.create_index("name"))
    
    # Count documents
    print("\nTotal documents:", mongo_ops.count_documents())
    
    # Paginate results
    print("\nFirst page of results:", mongo_ops.paginate_results(1, 2))

if __name__ == "__main__":
    main() 