# READ THE GUIDELINES
<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║        ψ⟩  QUANTUM STATE DISCRIMINATION                              ║
║             using Bosonic Channels & Gaussian States                 ║
║                                                                      ║
║        ⟨ψ|ρ̂|ψ⟩  ·  Wigner Functions  ·  Helstrom Bound             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

[![Course](https://img.shields.io/badge/Course-Advanced%20Quantum%20Mechanics-blueviolet?style=flat-square)](.)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)](.)
[![License](https://img.shields.io/badge/License-Academic-lightgrey?style=flat-square)](.)
[![LaTeX](https://img.shields.io/badge/Written%20in-LaTeX-008080?style=flat-square&logo=latex)](.)
[![Python](https://img.shields.io/badge/Numerics-Python%203.10+-3776AB?style=flat-square&logo=python&logoColor=white)](.)

</div>

---

## 📐 Abstract

This paper investigates the problem of **quantum state discrimination** in the context of **bosonic channels** and **Gaussian states** — a setting of central importance in continuous-variable (CV) quantum information theory.

We analyze both the **unambiguous** and **minimum-error** discrimination paradigms, deriving error-probability bounds via the **Helstrom bound** and its Gaussian-state specializations. The role of bosonic channels — including thermal-loss, amplification, and additive-noise channels — is examined as a source of decoherence and as a physical constraint on measurement strategies.

Key results include:
- Closed-form expressions for the **Bhattacharyya bound** and **quantum Chernoff exponent** for displaced thermal states
- Phase-space analysis using **Wigner functions** and the **symplectic formalism**
- Numerical simulation of optimal POVM performance under thermal-loss channels

---

## 🌌 Background & Motivation

```
Phase Space (Wigner Representation)
                                          
    p  ↑                                 
       │    ╭────╮          ╭────╮       
       │   ╱  ρ₀  ╲        ╱  ρ₁  ╲     
       │  │   •    │       │   •    │    
       │   ╲      ╱        ╲      ╱     
       │    ╰────╯          ╰────╯       
       │         ←— Δα  —→              
       └────────────────────────→  q    
                                         
    Displaced coherent states |α₀⟩, |α₁⟩ 
    in the optical phase plane.          
```

**Quantum state discrimination** addresses the fundamental question:

> *Given a quantum system prepared in one of several possible states, what is the optimal measurement strategy to identify it?*

In the bosonic / CV setting, states live in infinite-dimensional Hilbert spaces and are most naturally described by their **Wigner quasi-probability distributions** over phase space. Gaussian states (coherent, squeezed, thermal) admit elegant analytic treatment via their first and second moments alone.

---

## 🧮 Core Formalism

### Helstrom Bound (Binary Case)

For two hypotheses with prior probabilities $\pi_0, \pi_1$ and states $\rho_0, \rho_1$:

$$P_e^* = \frac{1}{2}\left(1 - \|\pi_0 \rho_0 - \pi_1 \rho_1\|_1\right)$$

where $\|\cdot\|_1$ denotes the trace norm. This is the **minimum achievable error probability** over all POVMs $\{M_0, M_1\}$.

### Gaussian State Parameterization

A Gaussian state $\rho$ is fully characterized by:

$$\vec{r} = \langle \hat{\vec{x}} \rangle, \qquad \sigma_{ij} = \langle \{\Delta\hat{x}_i,\, \Delta\hat{x}_j\} \rangle$$

where $\hat{\vec{x}} = (\hat{q}, \hat{p})^T$ are the quadrature operators satisfying $[\hat{q}, \hat{p}] = 2i$ (in natural units).

### Bosonic Channel Action (Symplectic Map)

A bosonic Gaussian channel transforms moments as:

$$\vec{r} \;\mapsto\; T\,\vec{r} + \vec{d}, \qquad \sigma \;\mapsto\; T\,\sigma\, T^T + N$$

where $T$ is the channel's transfer matrix and $N \geq 0$ is the added-noise matrix satisfying $N + i(T J T^T - J) \geq 0$ (complete positivity).

| Channel | $T$ | $N$ |
|---|---|---|
| Thermal-loss ($\eta, \bar{n}$) | $\sqrt{\eta}\,\mathbb{I}$ | $(1-\eta)(2\bar{n}+1)\,\mathbb{I}$ |
| Amplification ($G$) | $\sqrt{G}\,\mathbb{I}$ | $(G-1)(2\bar{n}+1)\,\mathbb{I}$ |
| Additive noise ($\sigma_N^2$) | $\mathbb{I}$ | $\sigma_N^2\,\mathbb{I}$ |

### Quantum Chernoff Exponent

For $n$ copies, the error probability decays as:

$$P_e^{(n)} \;\asymp\; e^{-n \xi_{QCB}}, \qquad \xi_{QCB} = -\ln \min_{s \in [0,1]} Q_s(\rho_0, \rho_1)$$

$$Q_s(\rho_0, \rho_1) = \mathrm{Tr}\!\left[\rho_0^s\, \rho_1^{1-s}\right]$$

For two Gaussian states, $Q_s$ admits a closed-form expression in terms of their covariance matrices.

---

## 📁 Repository Structure

```
quantum-state-discrimination/
│
├── 📄 paper/
│   ├── main.tex                  # Main LaTeX source
│   ├── figures/                  # Generated plots (PDF/PNG)
│   └── refs.bib                  # BibTeX references
├── draft_points.tex
└── README.md
```

## 📚 References
**Si Hui Tan**(2010). *Quantum State Discrimination with Bosonic Channels and Gaussian States* MASSACHUSETTS INSTITUTE OF TECHNOLOGY


<div align="center">

```
⟨ψ| M† M |ψ⟩ ≥ P_e*     ∀ POVM {M, I−M}
```

*"The quantum world does not merely limit our knowledge — it defines what knowledge can mean."*

</div>
