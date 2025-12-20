# engine/rewrite_engine.py

import random
import math
import copy

from engine.observables import hierarchical_closure
from engine.rules import edge_creation_rule, vertex_fusion_rule
from engine.observables import adjacency_overlap
from engine.observables import (
    worldline_interaction_graph,
    interaction_concentration,
    closure_density
)


class RewriteEngine:
    """
    Time + space emergence via inertia biases.
    """

    def __init__(
        self,
        hypergraph,
        p_create=0.6,
        seed=None,
        gamma_time=0.1,
        gamma_space=0.1,
        gamma_ext=0.05,
        gamma_closure=0.05,
        gamma_hier=0.06
    ):
        self.H = hypergraph
        self.p_create = p_create
        self.gamma_time = gamma_time
        self.gamma_space = gamma_space
        self.gamma_ext = gamma_ext
        self.gamma_closure = gamma_closure
        self.gamma_hier = gamma_hier
        self.time = 0

        if seed is not None:
            random.seed(seed)

    def step(self):
        # --- Snapshot BEFORE rewrite ---
        H_before = copy.copy(self.H)

        # Time structure before
        L_before = self.H.max_chain_length()

        # Extensivity before
        inter_before = worldline_interaction_graph(self.H)
        phi_before = interaction_concentration(inter_before)

        # Apply Closure
        psi_before = closure_density(inter_before)

        # Apply Hierarchical Closure
        omega_before = hierarchical_closure(self.H, inter_before)

        # --- Apply rewrite rule ---
        if random.random() < self.p_create:
            success = edge_creation_rule(self.H)
        else:
            success = vertex_fusion_rule(self.H)

        if not success:
            self.time += 1
            return False

        # --- Measure AFTER rewrite ---
        L_after = self.H.max_chain_length()
        delta_L = L_after - L_before

        inter_after = worldline_interaction_graph(self.H)
        phi_after = interaction_concentration(inter_after)
        delta_phi = phi_after - phi_before

        psi_after = closure_density(inter_after)
        delta_psi = psi_after - psi_before

        omega_after = hierarchical_closure(self.H, inter_after)
        delta_omega = omega_after - omega_before

        # --- Acceptance probability ---
        accept_prob = 1.0

        # Time inertia: penalize loss of causal depth
        if delta_L < 0:
            accept_prob *= math.exp(self.gamma_time * delta_L)

        # Spatial locality inertia (if you already had it)
        # NOTE: leave this part unchanged if it already exists
        # accept_prob *= spatial_factor

        # Extensivity axiom: suppress hub growth
        if delta_phi > 0:
            accept_prob *= math.exp(-self.gamma_ext * delta_phi)

        # Closure axiom: REWARD loops (redundancy)
        if delta_psi > 0:
            accept_prob *= math.exp(self.gamma_closure * delta_psi)

        # Hierarchical Closure Acceptance Rule
        if delta_omega > 0:
            accept_prob *= math.exp(self.gamma_hier * delta_omega)

        # --- Accept or reject ---
        if random.random() > accept_prob:
           # Reject rewrite (do nothing, state already mutated minimally)
           self.time += 1
           return False

        self.time += 1
        return True

    def run(self, steps):
        for _ in range(steps):
            self.step()
