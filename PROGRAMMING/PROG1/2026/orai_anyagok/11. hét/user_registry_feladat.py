
def is_adult(user):
    age = user["age"]
    assert isinstance(age, int)
    return age >= 18


def build_user_summary(
    user
):
    username = user["username"]
    role = user["role"]
    assert isinstance(username, str)
    assert role in {"student", "teacher", "admin"}

    category = f"{role}-adult" if is_adult(user) else f"{role}-minor"
    can_edit_courses = role in {"teacher", "admin"}
    return {
        "username": username,
        "category": category,
        "can_edit_courses": can_edit_courses,
    }


def count_active_users_by_role(
    users
):
    counts: dict[str, int] = {"student": 0, "teacher": 0, "admin": 0}
    for user in users:
        active = user["active"]
        role = user["role"]
        assert isinstance(active, bool)
        assert role in counts

        if active:
            counts[role] += 1
    return counts


def run_demo() -> None:
    users: list[dict[str, str | int | bool]] = [
        {"username": "anna", "age": 17, "role": "student", "active": True},
        {"username": "mark", "age": 34, "role": "teacher", "active": True},
        {"username": "julia", "age": 29, "role": "admin", "active": False},
    ]
    print("Summary:", build_user_summary(users[0]))
    print("Active counts:", count_active_users_by_role(users))


if __name__ == "__main__":
    run_demo()
