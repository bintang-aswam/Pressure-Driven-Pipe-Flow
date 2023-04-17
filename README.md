## In Partial Fulfillment of Final Project on High Performance Python Lab Course (term 2 2022)
### cae study: Hagen-Poiseuille Flow

Team's name: $Lyubits^{*}$ Flow

Team's member: 

1). Albina Lyubitskaya

2). Bintang A.S.W.A.M


**GENERAL DESCRIPTION:**

**Hagen-Poiseuille Flow** can be understood as an ideal approximation to **axisymmetrical flow inside a pipe** (a.k.a internal flow) due to the presence of **pressure-driven**. It only occurs at **SMALL Reynolds Number**(defined as the ratio between **inertial force** over **viscous force**) regime (a.k.a **incompressible viscous flow**).  

To conduct numerical modeling on this flow, we are planned to mathematically and physically idealize the Continuity Equation and Two-Dimensional Navier Stokes Equation (Momentum Equation) such that the final governing equation leads to One-Dimensional Incompressible-Viscous Navier Stokes (under certain circumstances related physical assumptions) as follows:

Two-Dimensional NS-equation: 
- Continuity Equation: $∇ ⋅ u = 0$ (incompressibility)

- Momentum Equation: $\frac{∂u}{∂t} + (u ⋅ ∇) u = − 1/ρ ∇p + \nu ∇²u + g$ 

where: 

$u$:  velocity profile (dimension: $LT^{-1}$) 
 
$p$:  pressure field (dimension: $ML^{-1}T^{-2}$) 

$g$:  gravity (dimension: $LT^{-2}$)

$ν$:  kinematic viscosity (dimension: $L^{2}T^{-1}$)

$ρ$:  density (dimension: $ML^{-3}$)

$t$:  time (dimension: $T$)

$∇$:  Nabla operator or known as gradient (mathematical operations to define the convection and diffusion terms) (dimension: $L^{-1}$)

$∇^{2}$: Laplace Operator (mathematically defined as $∇.(∇(⋯))$ or divergence of gradient of any continuous-differentiable function. (dimension: $L^{-2}$)


In particular, the physical assumptions to describe Hagen-Poiseuille Flow (in the interest of analytical derivation on velocity profile) given as follows: 
1). steady-state incompressible flow 

2). the [swirling flow](https://www.keyence.com/Images/flowknowledge_trouble_02_02_1470930.gif) can be ignored 

3). fully developed-based drifting flow will be physically considered 

Notice that fully developed flow occurs when the viscous effects due to the presence of the shear stress between the fluid particles against pipe wall, which generates a fully-developed velocity profile.

### **Environment**
`tqdm == 4.64.1`
`numpy == 1.21.6`
`cupy == 11.0.0`
`numba == 0.56.4`
`matplotlib == 3.2.2`

how to install:
`pip install -r requirements.txt`
