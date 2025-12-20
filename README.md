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
---

---
#How to Run a Toy Universe
## Requirements
- Python ≥ 3.10
- No external dependencies required (pure Python)
## Basic Run
Run the following command:
python3 run_diagnostics.py
This evolves a toy universe and prints diagnostics every N steps:
- average coordination ⟨k⟩
- causal depth (time)
- interaction concentration
- closure density
- hierarchical stability

---

---
## Diagnostics Explained
| Quantity | Meaning |
|---------|--------|
| ⟨k⟩ | Average coordination (dimension control) |
| L | Max causal chain length (emergent time) |
| Φ | Interaction concentration (hub suppression) |
| Ψ | Closure density (redundancy) |
| Ω | Hierarchical closure (RG stability) |

----

----
## Stable Spacetime-Like Behavior
Stable spacetime-like behavior is empirically associated with:
- ⟨k⟩ ≈ 7.5–8.5
- Φ small
- Ω non-zero across scales
## Current Research Focus
- Preventing metric collapse under coarse-graining
- Implementing logarithmic information metrics
- Enforcing holographic bounds dynamically
- Identifying Lorentz-invariant fixed points
- Exploring quantum probability emergence
Negative results are considered valuable — they identify missing axioms.

---

---
## Who Can Contribute?
You don’t need to be an expert in quantum gravity.
We welcome:
- physicists (theory, GR, QFT, QG)
- mathematicians (graph theory, category theory)
- programmers (simulation, optimization, visualization)
- curious thinkers
If you can:
- question assumptions
- test ideas
- improve code clarity
You can contribute meaningfully.

---

---
## Status
🚧 Active Research
This is not a finished theory.
It is a controlled exploration of what minimal rules can generate a universe.

## Philosophy
> “The universe may not be described by computation — it may be computation.”
HCSN treats this not as a metaphor, but as a testable hypothesis.
---
