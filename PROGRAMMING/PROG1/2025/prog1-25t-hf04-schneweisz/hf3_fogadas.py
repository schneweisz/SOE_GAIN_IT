"""
Implementáld az alábbi függvényt!
"""


def calc_profit(bets: dict[str, int], results: list[str]) -> int:
    """Kiszámolja a fogadásokkal elért profitot.

    Az 1. helyezett eltalálásáért a tét 3-szorosa, a 2. helyezett eltalálásáért a tét 2-szerese jár,
    a 3. helyezett eltalálásáért a tét visszajár, a többi helyezésért pedig nem jár semmi.

    Args:
        bets (dict[str, int]): Fogadások, kulcs=versenyző, érték=tét
        results (list[str]): Versenyzők helyezési sorrendben

    Returns:
        int: Profit = nyeremények - tétek összege

    >>> calc_profit({"A": 100, "B": 200, "C": 50}, ["A", "D", "B", "C"])
    150

    A fenti példában a nyeremény 3*100 + 1*200 = 500, a tétek összege 100 + 200 + 50 = 350,
    a profit 500 - 350 = 150.
    """
  
    top3 = results[:3]
    payouts = {
        0: 3,
        1: 2,
        2: 1,
    }

    total_payout = 0
    total_bet = sum(bets.values())

    for idx, contestant in enumerate(top3):
        if contestant in bets:
            total_payout += bets[contestant] * payouts[idx]

    return total_payout - total_bet
