import pandas as pd
from rdflib import Graph


def build_user_trust_graph(user_trustscore_df: pd.DataFrame):
    graph = Graph()
    for index, row in user_trustscore_df.iterrows():
        graph.add((f"User_{index}", "hasIdentityTrust", row["identity_trust"]))
        graph.add((f"User_{index}", "hasBehaviorTrust", row["behavior_trust"]))
    return graph


def build_org_trust_graph(org_trustscore_df: pd.DataFrame):
    graph = Graph()
    for index, row in org_trustscore_df.iterrows():
        graph.add((f"Org_{index}", "hasIdentityTrust", row["identity_trust"]))
    return graph
