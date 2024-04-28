def user_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }


def users_entity(entity) -> list:
    return [user_entity(item) for item in entity]


def serialize_dict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serialize_list(entity) -> list:
    return [serialize_dict(a) for a in entity]
