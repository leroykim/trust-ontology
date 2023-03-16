from trustscore import trust, graph

"""
DATA LABEL INFORMATION
+--------+---------------------+---------------------+-----------------------------+
|        | USER_IDENTITY_TRUST | USER_BEHAVIOR_TRUST | ORGANIZATION_IDENTITY_TRUST |
+--------+---------------------+---------------------+-----------------------------+
| UHH_OH |         HIGH        |         HIGH        |             HIGH            |
+--------+---------------------+---------------------+-----------------------------+
| UHH_OL |         HIGH        |         HIGH        |             LOW             |
+--------+---------------------+---------------------+-----------------------------+
| UHL_OH |         HIGH        |         LOW         |             HIGH            |
+--------+---------------------+---------------------+-----------------------------+
| UHL_OL |         HIGH        |         LOW         |             LOW             |
+--------+---------------------+---------------------+-----------------------------+
| ULH_OH |         LOW         |         HIGH        |             HIGH            |
+--------+---------------------+---------------------+-----------------------------+
| ULH_OL |         LOW         |         HIGH        |             LOW             |
+--------+---------------------+---------------------+-----------------------------+
| ULL_OL |         LOW         |         LOW         |             HIGH            |
+--------+---------------------+---------------------+-----------------------------+
| ULL_OL |         LOW         |         LOW         |             LOW             |
+--------+---------------------+---------------------+-----------------------------+
"""

N_USER = 1000
RANGES = [(0, 0.5), (0.5, 1)]
IDENTITY_DIST_HIGH = [0.3, 0.7]
IDENTITY_DIST_LOW = [0.7, 0.3]
BEHAVIOR_DIST_HIGH = [0.3, 0.7]
BEHAVIOR_DIST_LOW = [0.7, 0.3]
ORG_IDENTITY_HIGH = 0.9
ORG_IDENTITY_LOW = 0.3

trust_score_factory = trust.TrustScoreFactory(n_user=1000)
trust_score_factory.set_distribution_and_trust(
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_HIGH,
    behavior_dist=BEHAVIOR_DIST_HIGH,
    org_identity_trust=ORG_IDENTITY_HIGH,
)

trust_score_df = trust_score_factory.generate_user_trust()
trust_score_df.to_csv("result/trustscore.csv", index=False)

trust_graph_factory = graph.TrustGraphFactory(model_path="ontology/trust_ontology.ttl", destination_dir="result")
trust_graph_factory.build_trust_graph(trust_score_df=trust_score_df, file_name="trust_UHH_OH.ttl")
