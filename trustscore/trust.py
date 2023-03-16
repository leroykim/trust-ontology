import random
import time
import pandas as pd


class TrustScoreFactory:
    def __init__(self, n_user: int):
        self.n_user = n_user
        self.__ranges = None
        self.__identity_dist = None
        self.__behavior_dist = None
        self.__org_identity_trust = None

    def set_distribution_and_trust(
        self,
        ranges: list[tuple[float, float]],
        identity_dist: list[float],
        behavior_dist: list[float],
        org_identity_trust: float,
    ):
        print(
            f"Length of ranges: {len(ranges)} identity_dist: {len(identity_dist)} behavior_dist: {len(behavior_dist)}"
        )
        if len(identity_dist) != len(ranges):
            raise ValueError("The length of identity_dist must be the same as the length of ranges.")
        elif len(behavior_dist) != len(ranges):
            raise ValueError("The length of behavior_dist must be the same as the length of ranges.")
        elif len(identity_dist) != len(behavior_dist):
            raise ValueError("The length of identity_dist must be the same as the length of behavior_dist.")

        self.__ranges = ranges
        self.__identity_dist = identity_dist
        self.__behavior_dist = behavior_dist
        self.__org_identity_trust = org_identity_trust

    def generate_user_trust(self):
        trust_score_df = self.__generate_user_trustscore()
        trust_score_df["organization_trust"] = self.__org_identity_trust
        return trust_score_df

    def __generate_user_trustscore(self):
        user_id = range(0, self.n_user)
        identity_weights = [int(x * self.n_user) for x in self.__identity_dist]
        behavior_weights = [int(x * self.n_user) for x in self.__behavior_dist]
        identity_trust = self.__generate_random_float(self.__ranges, identity_weights)
        behavior_trust = self.__generate_random_float(self.__ranges, behavior_weights)
        data = {"user": user_id, "identity_trust": identity_trust, "behavior_trust": behavior_trust}
        print(
            f"Number of rows of user_id: {len(user_id)} identity_trust: {len(identity_trust)} behavior_trust: {len(behavior_trust)}"
        )
        return pd.DataFrame.from_dict(data)

    def __generate_random_float(self, ranges: list, weights: list):
        result = []
        i = 0
        while i < len(ranges):
            for n in range(weights[i]):
                random.seed(time.time())
                result.append(round(random.uniform(ranges[i][0], ranges[i][1]), 3))
            i += 1
        return result
