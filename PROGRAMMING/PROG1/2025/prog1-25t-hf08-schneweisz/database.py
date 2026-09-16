import json


def read_usages(year: int, month: int) -> list[dict]:
    with open(f"{year}-{month:02d}.json") as f:
        stats = json.load(f)
    return stats


def usage_by_weekday(stats: list[dict]) -> tuple[int, ...]:
    amounts = [0] * 7
    counts = [0] * 7
    for day in stats:
        amounts[day["weekday"]] += sum(day["usage"].values())
        counts[day["weekday"]] += 1
    return tuple(round(amounts[i] / counts[i]) for i in range(7))


def usage_by_app(stats: list[dict]) -> dict[str, int]:
    amounts: dict[str, int] = {}
    for day in stats:
        for app, amount in day["usage"].items():
            amounts[app] = amounts.get(app, 0) + amount
    return amounts


def usage_by_category(stats: list[dict]) -> dict[str, int]:
    amounts = usage_by_app(stats)
    with open("apps.json") as f:
        categories = json.load(f)
    category_sums = {c: 0 for c in categories}
    for c, apps in categories.items():
        for app in apps:
            category_sums[c] += amounts.get(app, 0)
    return category_sums


def get_category(app: str) -> str:
    with open("apps.json") as f:
        categories = json.load(f)
    for cat, apps in categories.items():
        if app in apps:
            return cat
    raise ValueError(f"App '{app}' not found.")
