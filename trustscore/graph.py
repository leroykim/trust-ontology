import pandas as pd
from rdflib import Graph, Namespace, URIRef

TRUST_IRI = "https://knacc.umbc.edu/dae-young/kim/ontologies/trust#"
TST = Namespace(TRUST_IRI)


class TrustGraphFactory:
    def __init__(self, model_path: str, destination_dir: str):
        self.model_path = model_path
        self.destination_dir = destination_dir

    def build_trust_graph(self, trust_score_df: pd.DataFrame, file_name: str):
        graph = Graph()
        self.__set_model(graph, self.model_path)
        self.__build_user_trust_graph(graph, trust_score_df)
        graph.serialize(destination=f"{self.destination_dir}/{file_name}.ttl", format="turtle")

    def __set_model(self, graph: Graph, model_path: str):
        graph.parse(model_path, format="n3")
        graph.bind("trust", TRUST_IRI)
        print(f"Model has {len(self.graph)} triples.")

    def __build_user_trust_graph(self, graph: Graph, user_trustscore_df: pd.DataFrame):
        organization = self.__organizationUri("x")
        graph.add((organization, TST.identityTrust, row["organization_trust"]))
        for index, row in user_trustscore_df.iterrows():
            user = self.__userUri(index)
            graph.add((user, TST.identityTrust, row["identity_trust"]))
            graph.add((user, TST.behaviorTrust, row["behavior_trust"]))
            graph.add((user, TST.isAffiliatedWith, organization))
            graph.add((organization, TST.hasEmployed, user))

    def __userUri(id):
        return URIRef(f"{TST}user_{id}")

    def __organizationUri(id):
        return URIRef(f"{TST}org_{id}")
