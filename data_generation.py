from trustscore import generation

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

MODEL_PATH = "trust-ontology/ontology/trust_ontology.ttl"
N_USER = 1000
RANGES = [(0, 0.5), (0.5, 1)]
IDENTITY_DIST_HIGH = [0.3, 0.7]
IDENTITY_DIST_LOW = [0.7, 0.3]
BEHAVIOR_DIST_HIGH = [0.3, 0.7]
BEHAVIOR_DIST_LOW = [0.7, 0.3]
ORG_IDENTITY_HIGH = 0.9
ORG_IDENTITY_LOW = 0.3

# UHH_OH
generation.build_trust_graph(
    model_path=MODEL_PATH,
    n_user=N_USER,
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_HIGH,
    behavior_dist=BEHAVIOR_DIST_HIGH,
    org_identity_trust=ORG_IDENTITY_HIGH,
    destination_dir="result",
    file_name="UHH_OH",
)

# UHH_OL
generation.build_trust_graph(
    model_path=MODEL_PATH,
    n_user=N_USER,
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_HIGH,
    behavior_dist=BEHAVIOR_DIST_HIGH,
    org_identity_trust=ORG_IDENTITY_LOW,
    destination_dir="result",
    file_name="UHH_OL",
)

# UHL_OH
generation.build_trust_graph(
    model_path=MODEL_PATH,
    n_user=N_USER,
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_HIGH,
    behavior_dist=BEHAVIOR_DIST_LOW,
    org_identity_trust=ORG_IDENTITY_HIGH,
    destination_dir="result",
    file_name="UHL_OH",
)

# UHL_OL
generation.build_trust_graph(
    model_path=MODEL_PATH,
    n_user=N_USER,
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_HIGH,
    behavior_dist=BEHAVIOR_DIST_LOW,
    org_identity_trust=ORG_IDENTITY_LOW,
    destination_dir="result",
    file_name="UHL_OL",
)

# ULH_OH
generation.build_trust_graph(
    model_path=MODEL_PATH,
    n_user=N_USER,
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_LOW,
    behavior_dist=BEHAVIOR_DIST_HIGH,
    org_identity_trust=ORG_IDENTITY_HIGH,
    destination_dir="result",
    file_name="ULH_OH",
)

# ULH_OL
generation.build_trust_graph(
    model_path=MODEL_PATH,
    n_user=N_USER,
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_LOW,
    behavior_dist=BEHAVIOR_DIST_HIGH,
    org_identity_trust=ORG_IDENTITY_LOW,
    destination_dir="result",
    file_name="ULH_OL",
)

# ULL_OH
generation.build_trust_graph(
    model_path=MODEL_PATH,
    n_user=N_USER,
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_LOW,
    behavior_dist=BEHAVIOR_DIST_LOW,
    org_identity_trust=ORG_IDENTITY_HIGH,
    destination_dir="result",
    file_name="ULL_OH",
)

# ULL_OL
generation.build_trust_graph(
    model_path=MODEL_PATH,
    n_user=N_USER,
    ranges=RANGES,
    identity_dist=IDENTITY_DIST_LOW,
    behavior_dist=BEHAVIOR_DIST_LOW,
    org_identity_trust=ORG_IDENTITY_LOW,
    destination_dir="result",
    file_name="ULL_OL",
)
