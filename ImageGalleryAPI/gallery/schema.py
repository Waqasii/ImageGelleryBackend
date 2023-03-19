import graphene
from gallery.queries.query import Query
from gallery.mutations.mutation import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
