import random
import time
import pandas as pd


def generate_user_trustscore(
    n_user: int, ranges: list[tuple[float, float]], identity_dist: list[float], behavior_dist: list[float]
):
    user_id = range(0, n_user)
    identity_weights = [int(x * n_user) for x in identity_dist]
    behavior_weights = [int(x * n_user) for x in behavior_dist]
    identity_trust = generate_random_float(ranges, identity_weights)
    behavior_trust = generate_random_float(ranges, behavior_weights)
    data = data = {"user": user_id, "identity_trust": identity_trust, "behavior_trust": behavior_trust}
    return pd.DataFrame.from_dict(data)


def generate_org_trustscore(n_org: int, ranges: list[tuple[float, float]], distributions: list[float]):
    org_id = range(0, n_org)
    weights = [int(x * n_org) for x in distributions]
    identity_trust = generate_random_float(ranges, weights)
    data = data = {"org": org_id, "identity_trust": identity_trust}
    return pd.DataFrame.from_dict(data)


def generate_random_float(ranges: list, weights: list):
    result = []
    i = 0
    while i < len(ranges):
        for n in range(weights[i]):
            random.seed(time.time())
            result.append(round(random.uniform(ranges[i][0], ranges[i][1]), 3))
        i += 1
    return result
