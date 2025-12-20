import time
from engine.hypergraph import Hypergraph
from engine.rewrite_engine import RewriteEngine
from engine.observables import (
    worldline_interaction_graph,
    interaction_concentration,
    closure_density,
    hierarchical_closure
)

# -----------------------------
# Initialize universe
# -----------------------------
H = Hypergraph()
v1 = H.add_vertex()
v2 = H.add_vertex()
H.add_causal_relation(v1, v2)
H.add_hyperedge([v1, v2])

engine = RewriteEngine(H, seed=1)

# -----------------------------
# Diagnostics state
# -----------------------------
accepted = 0
rejected = 0
last_k = H.average_coordination()
last_L = H.max_chain_length()

start_time = time.time()

print(
    " time |   V   |  <k>  | Δ<k> |  L  | ΔL |    Φ    |    Ψ    |    Ω    | acc%"
)
print("-" * 86)

# -----------------------------
# Main evolution loop
# -----------------------------
for step in range(1, 20001):
    success = engine.step()
    if success:
        accepted += 1
    else:
        rejected += 1

    if engine.time % 100 == 0:
        inter = worldline_interaction_graph(H)

        k = H.average_coordination()
        L = H.max_chain_length()

        dk = k - last_k
        dL = L - last_L

        acc_ratio = accepted / max(accepted + rejected, 1)

        print(
            f"{engine.time:5d} | "
            f"{len(H.vertices):5d} | "
            f"{k:5.2f} | "
            f"{dk:+5.2f} | "
            f"{L:3d} | "
            f"{dL:+3d} | "
            f"{interaction_concentration(inter):7.4f} | "
            f"{closure_density(inter):7.4f} | "
            f"{hierarchical_closure(H, inter):7.4f} | "
            f"{acc_ratio:5.2%}"
        )

        last_k = k
        last_L = L

end_time = time.time()

print("\nRun complete.")
print(f"Total steps: {engine.time}")
print(f"Accepted: {accepted}, Rejected: {rejected}")
print(f"Acceptance ratio: {accepted / max(accepted + rejected,1):.3f}")
print(f"Wall time: {end_time - start_time:.2f} s")
