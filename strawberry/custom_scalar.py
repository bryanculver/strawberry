from typing import NewType

from graphql.type.scalars import GraphQLScalarType

from .type_converter import REGISTRY


def _process_scalar(cls, *, serialize, parse_value, parse_literal):
    name = cls.__name__

    custom_scalar_type = NewType(name, cls)

    REGISTRY[custom_scalar_type] = GraphQLScalarType(
        name=name,
        serialize=serialize,
        parse_value=parse_value,
        parse_literal=parse_literal,
    )

    return custom_scalar_type


def scalar(cls=None, *, serialize, parse_value, parse_literal=None):
    def wrap(cls):
        return _process_scalar(
            cls,
            serialize=serialize,
            parse_value=parse_value,
            parse_literal=parse_literal,
        )

    if cls is None:
        return wrap

    return wrap(cls)