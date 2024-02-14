from marshmallow import Schema, fields

class NS:
    @staticmethod
    def create(name, description):
        return {
            'metadata': {
                'annotations': {},
                'description': description,
                'disable': False,
                'labels': {},
                'name': name,
                'namespace': ''
            }
        }
    
    @staticmethod
    def delete(name):

    

class NS:
    def __init__(self, name, description):
        self.name = name
        self.descriotion = description

    def __repr__(self):
        return "<NS(name={self.name!r})>".format(self=self)

NSSchema = Schema.from_dict(
    {
        'metadata': {
            'annotations': {},
            'description': fields.Str(),
            'disable': False,
            'labels': {},
            'name': fields.Str(),
            'namespace': ''
        }
    }
)

ns = NS(name="this_ns", description="placeholder")
schema = NSSchema()
result = schema.dump(ns)
result