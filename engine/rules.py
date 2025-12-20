# engine/rules.py

import random


def edge_creation_rule(H):
    """
    Edge creation:
    •—•  →  •—•—•
    Includes causal thickening.
    """

    if not H.hyperedges:
        return False

    edge = random.choice(list(H.hyperedges.values()))
    new_vertex = H.add_vertex()

    # connect causally to vertices in the chosen edge
    for v in edge.vertices:
        H.add_causal_relation(v, new_vertex)

    # causal thickening: inherit some causal past
    for v in edge.vertices:
        for u in H.causal_past(v):
            if random.random() < 0.3:
                H.add_causal_relation(u, new_vertex)

    # create new hyperedge with extension
    H.add_hyperedge(list(edge.vertices) + [new_vertex])

    return True


def vertex_fusion_rule(H):
    """
    Vertex fusion:
    •—•—• → •═•
    Only allowed if hypergraph remains non-degenerate.
    """

    if len(H.vertices) < 3 or len(H.hyperedges) < 1:
        return False

    edge = random.choice(list(H.hyperedges.values()))

    if len(edge.vertices) < 3:
        return False

    v_keep = edge.vertices[0]
    v_remove = edge.vertices[1]

    # Check if removing v_remove would destroy all hyperedges
    remaining_edges = [
        e for e in H.hyperedges.values()
        if v_remove not in e.vertices
    ]

    if not remaining_edges:
        return False

    # Redirect causal relations
    for u in list(H.vertices.values()):
        if v_remove.id in H.causal_order[u.id]:
            H.causal_order[u.id].add(v_keep.id)
            H.causal_order[u.id].discard(v_remove.id)

    # Remove vertex
    del H.vertices[v_remove.id]
    del H.causal_order[v_remove.id]

    # Remove edges containing removed vertex
    for eid in list(H.hyperedges.keys()):
        if v_remove in H.hyperedges[eid].vertices:
            del H.hyperedges[eid]

    return True
