from trustscore import trust, graph


def build_trust_graph(
    model_path, n_user, ranges, identity_dist, behavior_dist, org_identity_trust, destination_dir, file_name
):
    trust_score_factory = trust.TrustScoreFactory(n_user=n_user)
    trust_score_factory.set_distribution_and_trust(
        ranges=ranges,
        identity_dist=identity_dist,
        behavior_dist=behavior_dist,
        org_identity_trust=org_identity_trust,
    )

    trust_score_df = trust_score_factory.generate_user_trust()

    trust_graph_factory = graph.TrustGraphFactory(model_path=model_path, destination_dir=destination_dir)
    trust_graph_factory.build_trust_graph(trust_score_df=trust_score_df, file_name=f"{file_name}.ttl")
