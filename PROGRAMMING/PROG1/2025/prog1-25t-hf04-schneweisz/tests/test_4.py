import json
import os
import random
from copy import deepcopy

from pytest import fail

import hf4_friends as hf2

people = [
    "Alice",
    "Bob",
    "Carol",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Judy",
    "Karl",
    "Lily",
    "Mallory",
    "Nancy",
    "Oscar",
    "Peggy",
    "Quinn",
    "Robert",
    "Steve",
    "Trudy",
    "Ursula",
    "Victor",
    "Wendy",
    "Xavier",
    "Yvonne",
    "Zach",
]


def test_add_friendship() -> None:
    for _ in range(5):
        hf2.friend_network.clear()
        count = random.randint(1, 50)
        for _ in range(count):
            a, b = random.choices(people, k=2)
            before = deepcopy(hf2.friend_network)
            hf2.add_friendship(a, b)
            if a != b:
                assert b in hf2.friend_network[a], "Friendship not added"
                assert a in hf2.friend_network[b], "Friendship not symmetric"
                for p1, friends in before.items():
                    for p2 in friends:
                        assert p2 in hf2.friend_network[p1], "Friendship lost"
                        assert p1 in hf2.friend_network[p2], "Friendship lost"
                for p1, friends in hf2.friend_network.items():
                    for p2 in friends:
                        if {p1, p2} != {a, b}:
                            assert p2 in before[p1], "Extra friendship added"
                            assert p1 in before[p2], "Extra friendship added"
            else:
                assert hf2.friend_network == before, "Error when name1 == name2"


def test_are_friends() -> None:
    for _ in range(5):
        hf2.friend_network.clear()
        count = random.randint(1, 50)
        pairs: set[tuple[str, str]] = set()
        for _ in range(count):
            a, b = random.choices(people, k=2)
            hf2.add_friendship(a, b)
            before = deepcopy(hf2.friend_network)
            if a != b:
                pairs.add((a, b))
                pairs.add((b, a))
                assert hf2.are_friends(a, b), "Friendship not found"
                assert hf2.are_friends(b, a), "Friendship not symmetric"
            else:
                assert not hf2.are_friends(a, a), "False friendship found"
            for _ in people:
                a, b = random.choices(people, k=2)
                if (a, b) not in pairs:
                    assert not hf2.are_friends(a, b), "False friendship found"
                    assert not hf2.are_friends(b, a), "False friendship found"
            for p in pairs:
                assert hf2.are_friends(*p), "Friendship not found"
            assert hf2.friend_network == before, "Network was changed by are_friends"


def test_common_friends() -> None:
    for _ in range(15):
        hf2.friend_network = {}
        count = random.randint(1, 50)
        for _ in range(count):
            a, b = random.choices(people, k=2)
            hf2.add_friendship(a, b)
        a, b = random.choices(people, k=2)
        before = deepcopy(hf2.friend_network)
        result = hf2.common_friends(a, b)
        assert hf2.friend_network == before, "Network was changed by common_friends"
        for p in people:
            if p in result:
                assert p in hf2.friend_network[a], "Wrong common friend"
                assert p in hf2.friend_network[b], "Wrong common friend"
            else:
                assert p not in hf2.friend_network.get(
                    a, []
                ) or p not in hf2.friend_network.get(b, []), "Common friend not found"


def test_most_popular() -> None:
    for _ in range(15):
        hf2.friend_network = {}
        count = random.randint(1, 50)
        for _ in range(count):
            a, b = random.choices(people, k=2)
            hf2.add_friendship(a, b)
        before = deepcopy(hf2.friend_network)
        result = hf2.most_popular()
        assert hf2.friend_network == before, "Network changed"
        assert result in people, "Most popular person not found"
        for p in people:
            assert len(hf2.friend_network.get(p, [])) <= len(
                hf2.friend_network[result]
            ), "Not the most popular person was found"


def test_export() -> None:
    for _ in range(5):
        hf2.friend_network = {}
        count = random.randint(1, 50)
        for _ in range(count):
            a, b = random.choices(people, k=2)
            hf2.add_friendship(a, b)
        before = deepcopy(hf2.friend_network)
        hf2.export_network("test.json")
        assert hf2.friend_network == before, "Network changed"
        with open("test.json") as f:
            data = json.load(f)
            for p1, friends in data.items():
                assert p1 in before, "Unknown person in JSON"
                for p2 in friends:
                    assert p2 in before[p1], "Unknown friend in JSON"
            for p1, friends in before.items():
                for p2 in friends:
                    if p1 in data.get(p2, []):
                        assert p2 not in data.get(
                            p1, []
                        ), "Symmetric friendship in JSON"
                    elif p2 in data.get(p1, []):
                        assert p1 not in data.get(
                            p2, []
                        ), "Symmetric friendship in JSON"
                    else:
                        fail("Friendship not in JSON")
        os.remove("test.json")


def test_import_export() -> None:
    for _ in range(5):
        hf2.friend_network = {}
        count = random.randint(1, 50)
        for _ in range(count):
            a, b = random.choices(people, k=2)
            hf2.add_friendship(a, b)
        before = deepcopy(hf2.friend_network)
        hf2.export_network("test.json")
        hf2.friend_network = {}
        hf2.import_network("test.json")
        for p in before:
            assert p in hf2.friend_network, "Person not imported"
            for f in before[p]:
                assert f in hf2.friend_network[p], "Friend not imported"
        os.remove("test.json")
