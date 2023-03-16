import pandas as pd
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import XSD

TRUST_IRI = "https://knacc.umbc.edu/dae-young/kim/ontologies/trust#"
TRUST = Namespace(TRUST_IRI)


class TrustGraphFactory:
    def __init__(self, model_path: str, destination_dir: str):
        self.model_path = model_path
        self.destination_dir = destination_dir

    def build_trust_graph(self, trust_score_df: pd.DataFrame, file_name: str):
        graph = Graph()
        self.__set_model(graph, self.model_path)
        self.__build_user_trust_graph(graph, trust_score_df)
        graph.serialize(destination=f"{self.destination_dir}/{file_name}", format="turtle")

    def __set_model(self, graph: Graph, model_path: str):
        graph.parse(model_path, format="n3")
        graph.bind("trust", TRUST_IRI)
        print(f"Model has {len(graph)} triples.")

    def __build_user_trust_graph(self, graph: Graph, user_trustscore_df: pd.DataFrame):
        organization = self.__organizationUri("x")
        graph.add(
            (organization, TRUST.identityTrust, self.__floatLiteral(user_trustscore_df["organization_trust"].iloc[0]))
        )
        for index, row in user_trustscore_df.iterrows():
            user = self.__userUri(index)
            graph.add((user, TRUST.identityTrust, self.__floatLiteral(row["identity_trust"])))
            graph.add((user, TRUST.behaviorTrust, self.__floatLiteral(row["behavior_trust"])))
            graph.add((user, TRUST.isAffiliatedWith, organization))
            graph.add((organization, TRUST.hasEmployed, user))

    def __userUri(self, id):
        return URIRef(f"{TRUST}user_{id}")

    def __organizationUri(self, id):
        return URIRef(f"{TRUST}org_{id}")

    def __floatLiteral(self, value):
        return Literal(value, datatype=XSD.float)
