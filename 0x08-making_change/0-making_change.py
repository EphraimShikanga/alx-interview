#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """Function that makes change from given coins"""
    if total is 0 or total < 0:
        return 0
    if coins == [] or coins is None:
        return -1
    remainder = total
    coins_count = 0
    coin_id = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remainder > 0:
        if remainder - sorted_coins[coin_id] >= 0:
            remainder -= sorted_coins[coin_id]
            coins_count += 1
        else:
            coin_id += 1
    return coins_count
