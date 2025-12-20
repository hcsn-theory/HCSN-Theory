# 🌀 HCSN Theory: Holographic Computational Spin-Networks

**A computational approach to emergent spacetime, gravity, and quantum mechanics.**

---

## 📖 Overview
**HCSN (Holographic Computational Spin-Network)** is a theoretical and computational framework proposing that the universe is not fundamentally geometric. Instead, spacetime, gravity, and quantum mechanics emerge from a **discrete computational hypergraph** governed by simple rewrite rules and information-theoretic principles.



### This repository contains:
* **Formal Axioms:** The foundational logic of HCSN.
* **Toy-Universe Simulations:** Python implementations of hypergraph evolution.
* **Diagnostic Tools:** Metrics to test the emergence of time, space, dimensionality, and metric structure.

The long-term goal is to identify the minimal rule set capable of producing a universe consistent with Lorentz invariance, 4D spacetime, holography, and the Born rule.

---

## 🔬 Core Principles (Axioms)

| Axiom | Name | Description |
| :--- | :--- | :--- |
| **1** | **Discreteness** | Reality consists of discrete events (vertices); no fundamental continuum. |
| **2** | **Causality** | Events are partially ordered by a causal relation. |
| **3** | **Minimal Dynamics** | Evolution via local rewrite rules: **Edge Creation** and **Vertex Fusion**. |
| **4** | **Holography** | Information content scales with the boundary, not the volume. |
| **5** | **Geometricity** | Stable geometry emerges only if $\langle k \rangle \approx 8$ (Dimensional attractor). |
| **6** | **Persistence** | Hierarchical stability and error correction via redundant causal loops. |

---

## 📂 Repository Structure

```text
HCSN-Theory/
├── engine/                # Core simulation engine
│   ├── hypergraph.py      # Vertices, hyperedges, causality
│   ├── rules.py           # Rewrite rules
│   ├── rewrite_engine.py  # Acceptance dynamics
│   └── observables.py     # Physical diagnostics
├── experiments/           # Reproducible experiments
│   ├── exp_phase_diagram.py
│   ├── exp_critical_scan.py
│   └── exp_worldline_interactions.py
├── notebooks/             # Visualization & exploration
├── figures/               # Generated plots
├── theory/                # Conceptual documentation
│   └── hcsn_summary.md
└── README.md
