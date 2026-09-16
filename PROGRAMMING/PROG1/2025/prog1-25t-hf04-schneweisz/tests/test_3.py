import random

import hf3_fogadas as hf3


def test_calc_profit():
    for _ in range(10):
        racer_count = random.randint(3, 15)
        order = [chr(ord("A") + i) for i in range(racer_count)]
        random.shuffle(order)
        bet_count = random.randrange(1, racer_count)
        selected = random.sample(range(racer_count), bet_count)
        bets = {order[i]: random.randint(50, 100) for i in selected}
        wagers = list(bets.values())
        bets_before = bets.copy()
        order_before = order.copy()
        result = hf3.calc_profit(bets, order)
        assert bets == bets_before, "A bets dict megváltozott!"
        assert order == order_before, "A befutók listája megváltozott!"
        assert isinstance(
            result, int
        ), f"Az eredménynek egész számnak kell lennie: {result}"
        assert result == sum(
            wagers[selected.index(i)] * (3 - i) for i in range(3) if i in selected
        ) - sum(wagers), f"Az eredmény hibás: {bets}, {order} -> {result}"
