import os
from trustscore import trust, graph

N_USER = 1000
RANGES = [(0, 0.3), (0.3, 0.6), (0.6, 1)]
IDENTITY_DIST_HIGH = [0.1, 0.3, 0.6]
IDENTITY_DIST_MEDIUM = [0.2, 0.6, 0.2]
IDENTITY_DIST_LOW = [0.6, 0.3, 0.1]
BEHAVIOR_DIST_HIGH = [0.1, 0.3, 0.6]
BEHAVIOR_DIST_MEDIUM = [0.2, 0.6, 0.2]
BEHAVIOR_DIST_LOW = [0.6, 0.3, 0.1]


if not os.path.exists("./data"):
    os.makedirs("./data")

"""
USER DATA INFORMATION
+------+-----------------------+-----------------------+
|      | IDENTITY_DISTRIBUTION | BEHAVIOR_DISTRIBUTION |
+------+-----------------------+-----------------------+
| IHBH |          HIGH         |          HIGH         |
+------+-----------------------+-----------------------+
| IHBM |          HIGH         |         MEDIUM        |
+------+-----------------------+-----------------------+
| IHBL |          HIGH         |          LOW          |
+------+-----------------------+-----------------------+
| IMBH |         MEDIUM        |          HIGH         |
+------+-----------------------+-----------------------+
| IMBM |         MEDIUM        |         MEDIUM        |
+------+-----------------------+-----------------------+
| IMBL |         MEDIUM        |          LOW          |
+------+-----------------------+-----------------------+
| ILBH |          LOW          |          HIGH         |
+------+-----------------------+-----------------------+
| ILBM |          LOW          |         MEDIUM        |
+------+-----------------------+-----------------------+
| ILBL |          LOW          |          LOW          |
+------+-----------------------+-----------------------+
"""

# Dataframes
df_ihbh = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_HIGH, BEHAVIOR_DIST_HIGH)
df_ihbm = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_HIGH, BEHAVIOR_DIST_MEDIUM)
df_ihbl = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_HIGH, BEHAVIOR_DIST_LOW)
df_imbh = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_MEDIUM, BEHAVIOR_DIST_HIGH)
df_imbm = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_MEDIUM, BEHAVIOR_DIST_MEDIUM)
df_imbl = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_MEDIUM, BEHAVIOR_DIST_LOW)
df_ilbh = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_LOW, BEHAVIOR_DIST_HIGH)
df_ilbm = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_LOW, BEHAVIOR_DIST_MEDIUM)
df_ilbl = trust.generate_user_trustscore(N_USER, RANGES, IDENTITY_DIST_LOW, BEHAVIOR_DIST_LOW)

# Serializtion to CSV
df_ihbh.to_csv("./data/user_trust_ihbh.csv", index=False)
df_ihbm.to_csv("./data/user_trust_ihbm.csv", index=False)
df_ihbl.to_csv("./data/user_trust_ihbl.csv", index=False)
df_imbh.to_csv("./data/user_trust_imbh.csv", index=False)
df_imbm.to_csv("./data/user_trust_imbm.csv", index=False)
df_imbl.to_csv("./data/user_trust_imbl.csv", index=False)
df_ilbh.to_csv("./data/user_trust_ilbh.csv", index=False)
df_ilbm.to_csv("./data/user_trust_ilbm.csv", index=False)
df_ilbl.to_csv("./data/user_trust_ilbl.csv", index=False)

"""
ORGANIZATION DATA INFORMATION
+----+-----------------------+
|    | IDENTITY_DISTRIBUTION |
+----+-----------------------+
| IH |          HIGH         |
+----+-----------------------+
| IM |         MEDIUM        |
+----+-----------------------+
| IL |          LOW          |
+----+-----------------------+
"""

# Dataframes
df_ih = trust.generate_org_trustscore(N_USER, RANGES, IDENTITY_DIST_HIGH)
df_im = trust.generate_org_trustscore(N_USER, RANGES, IDENTITY_DIST_MEDIUM)
df_il = trust.generate_org_trustscore(N_USER, RANGES, IDENTITY_DIST_LOW)

# Serializtion to CSV
df_ih.to_csv("./data/org_trust_ih.csv", index=False)
df_im.to_csv("./data/org_trust_im.csv", index=False)
df_il.to_csv("./data/org_trust_il.csv", index=False)
