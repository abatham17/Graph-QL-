import graphene
from GraphQLapp.schema import Query as expq

class Query(expq):
    pass

schema=graphene.Schema(query=Query)
