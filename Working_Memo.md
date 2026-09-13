# Working Memo: Borel chain prescriptions

## Research round: 2026-09-07

Repository: `jlhscu/Borel-poset-extend`, branch `main`.
Baseline inspected: commit `b5b264a3b7ca3b3cc958826182b1c746d8ae4b8b`;
`main.tex` blob `df8cbe4457f5265553fc99bc77216e5b2c3d4105`.
At this baseline the repository contained only `main.tex`, with no existing
memo or research notes. This memo records results established in this round;
it does not claim that the main prescription problem has been solved.

### Status (updated through the 2026-09-08 continuation)

| Question | Conclusion established in this round |
| --- | --- |
| Width three, arbitrary Borel chains, FE + AS | Still unresolved |
| Arbitrary finite width, arbitrary Borel chains, FE + AS | Still unresolved |
| One prescribed Borel chain, with finite coherence | Positive at every finite width; chain PU is proved below |
| Finite chain prescriptions satisfying AS + AD | Positive at every finite width, with no additional PU assumption |
| Does FE + AS imply AD for chains? | No; seven points suffice at width three, and seven is minimal |
| Do locked active templates imply AD? | No, for every width n >= 3 and every saturation parameter r >= 1 |
| Are AS transition permutations confined to an order-two subgroup? | No; arbitrary permutations occur, and a connected sequence of overlapping witnesses generates S3 |
| Are there positive special cases for arbitrary Borel prescriptions? | Yes: realistic finite-width orders, and orders with locally countable incomparability graphs; AS is unnecessary in both cases |
| Is relative augmentation recognizable by a fixed finite arity? | No, even in locked active templates for every n >= 3 and r >= 1; Section 11 |
| Is exact feasibility of a finite permutation state Borel? | Not in general: it can be complete coanalytic, already for parameterized width-three locked templates; Section 12 |
| Can complete states nevertheless be selected Borelly? | Yes along any given Borel sequence of countably many markers, preserving all finite extension constraints; this alone does not colour unmarked points; Section 13 |
| A further positive class beyond the two earlier special cases? | Yes: uniform substitution over a realistic quotient, with locally countable incomparability inside each fibre; arbitrary finite Borel lists are allowed; Section 14 |

“Positive” in the last row means that FE suffices. The local-countability result
also allows arbitrary Borel lists from a fixed finite palette.

## 1. Source audit and corrections to retain

The finite locked-template and active-block arguments, the finite-width
saturation theorem, the two-colour invariant-separation argument, and the
explicit height-three antichain construction were read in full. The main
manuscript is not edited in this round.

Two specific formulation errors should be corrected in a later manuscript edit.

1. Theorem C in the introduction omits PU, although the precise theorem
   `thm:many` assumes PU and its proof explicitly uses it. The unrestricted
   graph statement in the introduction is false as written: take the disjoint
   union of the irrational-rotation graph and one edge {e0,e1}, and prescribe
   E0={e0}, E1={e1}. AS, FE_2, and AD hold, but there is no Borel 2-colouring.
   Section 2 below proves PU for incomparability graphs of finite-width Borel
   orders; this repairs the chain application, not the unrestricted graph claim.
2. The final four-point example describes two disjoint chains a0<a1 and b0<b1,
   with every cross pair incomparable, but calls {a0,b1} and {a1,b0} chains.
   They are antichains. A correct mixed-pattern chain example instead has the
   lower antichain {a0,b0}, the upper antichain {a1,b1}, and all four
   lower-to-upper comparisons. Its two crossed prescribed chains do satisfy
   FE and AS. Sections 4 and 5 give stronger, fully checked examples.

Do not use the incorrect four-point example or the unqualified Theorem C as
proved inputs.

## 2. Proved: puncturing with one prescribed Borel chain

Let P be a Borel partial order on X of width m >= 1, and put G = incomparability(P).
Define the finite forced-inequality graph G* by

\[
x\,G^*\,y
\iff
\text{some finite }F\supseteq\{x,y\}\text{ has no proper }m\text{-colouring with }c(x)=c(y).
\]

The graph G* is analytic: finite sets can be coded by finite tuples, and for a
fixed tuple the condition quantifies over only finitely many colour assignments.
Also G is contained in G*, and G* is irreflexive by finite Dilworth.

The exact external inputs are [Carroy--Miller--Vidnyanszky,
*On the existence of small antichains for definable quasi-orders*](https://glimmeffros.github.io/publications/dilworth.pdf):

- Proposition 12: if A is an m-element P-antichain and Y is G*-independent,
  some a in A has Y union {a} G*-independent.
- Proposition 16: for an analytic, countably Borel-colourable graph H and an
  analytic family of finite sets, if every H-independent set can be extended
  by a point of each member of that family, then every Borel H-independent
  set has a Borel H-independent extension puncturing the family.

These are already proved results in that paper, not new hypotheses.

**Theorem 2.1 (chain PU).** Suppose B is a Borel P-chain and is finitely
m-coherent: every finite F subset X has a partition into at most m chains
with F intersection B contained in one part. Then there is a Borel P-chain
C containing B that meets every m-element P-antichain. Consequently there is
a Borel m-chain partition having B in its first part.

**Proof.** Coherence implies that B is G*-independent: a finite witness for
b G* b' with b,b' in B would contradict coherence on that witness.

Take a Borel m-colouring c of G by Borel Dilworth. This same c colours G*:
if c(x)=c(y), its restriction to every finite set containing x,y witnesses
that x and y are not G*-adjacent. Thus the countable-colourability hypothesis
of Proposition 16 is verified without any extra assumption on G*.

Let F_m be the Borel family of m-element P-antichains, viewed as a family
of finite subsets of X. Proposition 12 verifies the point-extension
hypothesis of Proposition 16 for H=G* and F=F_m. Apply Proposition 16 to B.
It gives a Borel G*-independent C containing B and puncturing F_m. Since
G is contained in G*, C is a P-chain. The Borel induced order on X minus C
has width at most m-1. Borel Dilworth partitions it into m-1 Borel chains
(allowing empty parts). Together with C these prove the assertion. QED.

All hypotheses of the two cited propositions have thus been checked.
Theorem 2.1 applies to every Borel induced suborder, exactly as required by
the manuscript's formulation of PU. AS is not used.

**Corollary 2.2 (pair criterion for a single prescribed chain).** For a
Borel subset B of a width-m Borel order, the following are equivalent:

1. B is contained in one part of a Borel m-chain partition.
2. B is finitely m-coherent.
3. Every pair b,b' in B can be put in one part of some abstract m-chain
   partition, where the partition may depend on the pair.

Indeed, 1 implies 2 and 3. Condition 3 makes B G*-independent, so the proof
of Theorem 2.1 applies directly and gives 1. For m=1 the conclusion is
immediate; singleton and empty seeds present no exception. This is a
verified consequence of the cited machinery, not a claim of bibliographic
priority for a new general theorem.

**Corollary 2.3 (finite AS + AD chain prescriptions).** In a finite-width
Borel partial order, the manuscript's finite chain prescriptions satisfying
AS and AD extend to a Borel partition into the prescribed number of chains.

**Proof.** Use Theorem 2.1 at every puncturing step in `thm:many`. Its
induction verifies coherence from AD, preserves the remaining anchors by
AS, and reduces the width by one. The induction is therefore now
unconditional for the chain application. QED.

The AD definition in the manuscript requires a finite set Z containing
the entire tail prescription. It is intended for finite E_i. Do not apply
that wording to infinite E_i, for which it can become vacuous. An infinite
version must explicitly require finite extension for the remaining
prescription in each relevant Borel residual order.

## 3. Proved: the AS witnesses form a Borel distributive lattice

Let E_0,...,E_{n-1} be disjoint Borel chains, and let

\[
\mathcal W=\{(e_i)_{i<n}\in\prod_{i<n}E_i:
             \{e_i:i<n\}\text{ is an antichain}\}.
\]

Give the product its coordinatewise order. For a,b in W set

\[
(a\wedge b)_i=\min_{\le_P}(a_i,b_i),\qquad
(a\vee b)_i=\max_{\le_P}(a_i,b_i).
\]

**Proposition 3.1.** W is closed under these operations, which are Borel.
It is therefore a distributive sublattice of the product of the chain
orders. AS says exactly that every coordinate projection of W onto E_i
is onto.

**Proof.** Put u=a meet b. If u_i <= u_j for distinct i,j, choose whichever
tuple supplied u_i, say u_i=a_i. Since u_j <= a_j, transitivity gives
a_i <= a_j, contradicting that a is an antichain. Thus u is an antichain.
For v=a join b, if v_i <= v_j and v_j=a_j, then a_i <= v_i <= a_j,
again a contradiction. Borelness follows from the Borel order on each
E_i, and the distributive identities are coordinatewise identities in
linear orders. The assertion about AS is its definition. QED.

**Corollary 3.2 (finite sorting).** For any finite list of AS witnesses
A^1,...,A^q there are witnesses B^1 <= ... <= B^q with exactly the same
coordinate multisets. In particular their unions of points agree.

**Proof.** Run any finite sorting network, replacing a comparison by
(a,b) -> (a meet b,a join b). Each coordinate undergoes ordinary sorting;
Proposition 3.1 keeps every output tuple in W. QED.

Consequently any finite collection of prescribed points has AS witnesses
covering it that are monotone simultaneously along all E_i. For a finite
prescription this gives a finite monotone witness cover of the whole
prescription. FE is not needed for this fact. It does not imply AD: the
counterexample below already has two monotone witnessing antichains.

## 4. Exact permutation information and counterexamples to a subgroup bound

Fix a Borel n-chain partition C_0,...,C_{n-1}. For A=(a_i) in W define
pi_A(i)=j when a_i is in C_j. This is a permutation, and A -> pi_A is Borel.

If A and B share their coordinate points at indices J, the transition
rho_{A,B}=pi_B composed with pi_A inverse fixes pi_A(J) pointwise.
For a pair of witnesses this is the only constraint on their permutations.

**Exact two-witness realization.** Given pi,sigma in S_n that agree on J,
take a common prescribed point e_i for i in J. For each i outside J take
two points a_i<b_i; make all lower a-points less than all upper b-points,
and make all e-points incomparable with one another and with both layers.
Set E_i={e_i} on J and E_i={a_i,b_i} otherwise. Use the lower and upper
layers, together with the common points, as the two witnesses. Their
width is n. Define the base colour of a_i to be pi(i), that of b_i to be
sigma(i), and that of e_i to be their common value. Each base colour
class is a chain. Thus the desired permutations are realized, with FE
and AS. Extra coincident permutation values need not correspond to
extra shared points. QED.

More generally, in the ordinal sum of q n-element antichains, prescribe
E_i to contain the i-th point of each layer. A base chain partition can
assign any independently specified permutation pi_t to layer t. Hence
arbitrary finite words of transition permutations are realizable. Already
two three-element layers, six points in total, realize a 3-cycle.

**A connected sequence of overlapping witnesses generating S3.** Take
seven points a,b,c,d,e,f,g and the transitive closure of

\[
a<f,\ a<g,\ b<d,\ b<e,\ c<d,\ c<e,\ e<f,\ e<g.
\]

The prescribed and base partitions are respectively

\[
E_0=\{a,f\},\quad E_1=\{b,d\},\quad E_2=\{c,e,g\},
\]

\[
C_0=\{a,g\},\quad C_1=\{b,e,f\},\quad C_2=\{c,d\}.
\]

Both are chain partitions. All strict edges go from the bottom layer
{a,b,c} to {d,e} or {f,g}, or from e to {f,g}; their closure is acyclic.
The triples

\[
A=(a,b,c),\quad B=(a,d,e),\quad D=(f,d,g)
\]

are antichains, cover all seven prescribed points, and have permutations

\[
\pi_A=(0,1,2),\quad\pi_B=(0,2,1),\quad\pi_D=(1,2,0).
\]

Thus width=3 and FE + AS hold. A and B share a; B and D share d. The
successive transitions are (1 2) and (0 1), which generate S3. In fact
A <= B <= D in the lattice of Section 3. Even monotone, overlapping
witnesses therefore do not give a fixed order-two subgroup.

**Cocycle qualification.** The literal transitions defined from pi_A
already satisfy

\[
\rho_{B,D}\rho_{A,B}=\rho_{A,D}
\]

and are a Borel coboundary on the witness space, without FE. Their
products around closed paths are identity. The example proves freedom
of transitions, not nontrivial holonomy of this tautological cocycle.
Neither that tautological triviality nor the realization of S3 solves
the problem of assigning colours to points outside the prescription.

## 5. A smallest width-three counterexample to FE + AS => AD

Take lower points a0,a1,a2, upper points b0,b1,b2, and x. Declare

\[
a_i<b_j\quad(i,j<3),\qquad
a_0<x,\ a_1<x,\ x<b_0,\ x<b_2,
\]

and no other strict comparisons. This relation is already transitive:
the only two-step paths through x yield listed lower-to-upper comparisons.
It is antisymmetric, and all sets and relations are finite, hence Borel.
Prescribe E_i={a_i,b_i}.

The chains

\[
\{a_0,x,b_0\},\quad\{a_1,b_1\},\quad\{a_2,b_2\}
\]

partition the order and extend the prescription, proving FE_3 and the
upper bound on width. Both A={a0,a1,a2} and B={b0,b1,b2} are antichains,
so width=3; these two antichains witness AS for all six prescribed points.

For the tail {1,2}, take

\[
Z=\{a_1,a_2,x,b_1,b_2\}=E_1\cup E_2\cup\{x\}.
\]

It has width two, as witnessed by the chain partition

\[
\{a_1,x,b_2\}\sqcup\{a_2,b_1\}
\]

and the antichain {a1,a2}. However, x is incomparable with b1 in E1 and
with a2 in E2, so no prescribed two-chain partition of Z exists. This
is precisely failure of AD at t=1.

**Proposition 5.1 (minimality).** Seven is the minimum total number of
points in a width-three poset with three nonempty prescribed chains
satisfying FE_3 + AS but failing AD.

**Proof.** Only the two-colour tail can fail: t=0 is FE_3 and a
width-one one-colour tail is automatic. Let Q=E1 union E2. AS implies
that the incomparability graph on Q has no isolated vertices. If this
graph is connected, its prescribed proper 2-colouring agrees, up to a
single flip, with the restriction of any proper 2-colouring of any
width-two Z containing Q. Dilworth therefore gives a prescribed
extension on every such Z. Thus failure requires this graph to be
disconnected, with at least two nontrivial components, so |Q| >= 4.
There must also be a point of Z outside Q, and E0 is nonempty.

If the total order had at most six points, equality would hold in
all these bounds: Q has four points, E0={e}, and there is just one
additional point x. The graph on Q is exactly two disjoint edges.
Different incomparability components are uniformly ordered (the
elementary proof is in Section 8), so Q is an ordinal sum of two
two-element antichains A={a1,a2}, B={b1,b2}. Relabel so that
E_j={a_j,b_j} for j=1,2. AS and E0={e} imply e is incomparable with
every point of Q.

Because Z=Q union {x} has no prescribed two-chain partition, any
prescribed three-chain partition supplied by FE_3 must put x with e.
Thus e<x or x<e. If e<x, no point of Q can lie above x, as that would
be comparable with e. Since Z has width two, some b_j is comparable
with x; hence a_j<b_j<x, so x can be added to E_j, a contradiction.
If x<e, the dual argument using A puts x below some a_j<b_j and gives
the same contradiction. No example with six points exists. QED.

### 5.2. The obstruction is already a locked active template

In the seven-point example set r=1, U=A, V=A union B, and S=V. Then

\[
\alpha_1(X)=3,\qquad\alpha_2(X)=6.
\]

The first equality is the width computation. The second follows from
the two disjoint three-antichains A,B and the bound alpha_2 <= 2 width.
The template E0,E1,E2 on S has norms 3 and 6. Each block has one point
in U and two in V, so all three blocks are active. The only possible
outside point is x, and adding it to E0 leaves both norms unchanged.
The template is therefore locked in exactly the manuscript's sense.
Nevertheless AD fails as above.

This refutes the claim that the active-block structure in the
saturation proof automatically supplies AD. The example itself has
a prescribed extension; it is not a Borel counterexample.

### 5.3. Every finite width n >= 3 and every r >= 1

For n >= 3 use lower and upper n-antichains A={a_i:i<n} and
B={b_i:i<n}, put all a_i<b_j, and keep exactly
a0<x, a1<x, x<b0, x<b2 as the comparisons involving x.
Prescribe E_i={a_i,b_i}. Assigning x to E0 proves width=n and FE_n;
the two layers prove AS. The tail set

\[
Z=\bigcup_{1\le i<n}E_i\cup\{x\}
\]

has width n-1: use chains {a1,x,b2}, {a2,b1}, and {a_i,b_i} for
3 <= i < n. Yet x fits none of the prescribed tail chains: it is
incomparable with b1, with a2, and with all points of E_i for i>=3.
Thus AD fails for every n>=3.

For an arbitrary r>=1 prepend, by ordinal sum, r-1 further n-element
antichain layers. Add their i-th points to E_i. Let S be the union of
all r+1 prescribed layers; let U consist of r of those layers and V=S.
Then alpha_r=nr and alpha_(r+1)=n(r+1), attained by these layers.
Every E_i has r points in U and r+1 in V, and assigning the sole outside
point x to E0 preserves both norms. This is a locked active template.
Removing E0 leaves the same unsatisfiable tail restriction on the old
points, and a width-(n-1) residual order. AD still fails.

Thus the obstruction survives all finite n>=3 and all saturation
parameters; it is not an artefact of small r.

## 6. A direct failure of the anchored forced-inequality adaptation

One might try replacing G* in the CMV proof by the relation H of
inequalities forced by all prescribed colourings. The crucial
transitivity statement for P minus G* does not survive this replacement.

Take two three-element antichains A={a0,a1,a2} and B={b0,b1,b2}, put a
single point y above every a_i and below every b_i, and prescribe
E_i={a_i,b_i}. This has width three, FE_3, and AS. The point y may
receive any of the three colours. Accordingly,

\[
a_0<y<b_1,\qquad \neg(a_0 H y),\qquad\neg(y H b_1),\qquad a_0 H b_1.
\]

So P minus H is not transitive, already on seven points. The
unprescribed transitivity statement is CMV Proposition 7. Its
prescribed analogue is false even under AS. Do not invoke it when
trying to strengthen Section 2 to simultaneous prescriptions.

## 7. Positive special case: realistic orders

**Proposition 7.1.** Suppose P has finite width and admits a Borel
injection r:X -> R with x<_P y implying r(x)<r(y). Every Borel chain
prescription satisfying FE_n extends to a Borel n-chain partition.
AS is not required.

**Proof.** Compactness supplies an abstract prescribed partition D_i.
Extend each D_i to a maximal P-chain M_i. These maximal chains are
Borel by [Bosek--Grytczuk--Lonc, Lemma 3 and Theorem 1](https://arxiv.org/pdf/2004.02162),
applied to the Borel image r(X). Their Lemma 3 is stated for arbitrary
subsets of R, so the image need not be all of R. Define

\[
M'_i=M_i\setminus\bigcup_{j\ne i}E_j,\qquad
C_i=M'_i\setminus\bigcup_{j<i}M'_j.
\]

The M'_i are Borel chains covering X: an unprescribed point keeps all
its memberships, and a prescribed point in E_i keeps its membership
in M'_i. Also each E_i is excluded from every other M'_j. The C_i
therefore give the required Borel partition. QED.

This proof uses maximal-chain regularity, a stronger property than
unprescribed Borel Dilworth. That property fails in general: on
R x {0,1}, ordered strictly by the real coordinate, a maximal chain
may choose an arbitrary non-Borel one-point section of the two-point
fibres. Thus this particular proof cannot be transferred to all
finite-width orders by simply assuming maximal chains are Borel.

## 8. Positive special case: locally countable incomparability

**Proposition 8.1.** If the incomparability graph G of a Borel partial
order is locally countable, its connectedness relation E_G is smooth.
Consequently any Borel prescription satisfying FE_n has a Borel
n-chain extension. The same conclusion holds for any Borel lists
L(x) subset {0,...,n-1} for which every finite induced problem is
solvable. No AS assumption is needed.

**Proof of smoothness.** First, two distinct incomparability
components are uniformly ordered. If x<y and x is incomparable with
x', then y<x' would imply x<x', a contradiction; since x' and y are
in different components they are comparable, so x'<y. Propagate
along finite paths in each component. Transitivity then linearly
orders the distinct components.

Local countability makes E_G a countable Borel equivalence relation:
each finite-path relation has countable sections and is Borel by
Lusin--Novikov, and E_G is their countable union. The relation

\[
R=\le_P\ \cup\ E_G
\]

is consequently a Borel total quasi-order whose associated
equivalence relation is exactly E_G.

For completeness, the equivalence relation of any Borel total
quasi-order is smooth. If not, the [Harrington--Kechris--Louveau
dichotomy](https://authors.library.caltech.edu/records/cvb33-qt212)
gives a Borel reduction of E0 to that equivalence relation. Pull back
the quasi-order to a Borel total quasi-order S on 2^omega whose
equivalence relation is E0. For fair-coin measure mu, every section
S_x is E0-invariant, so mu(S_x) is 0 or 1. The Borel map
x -> mu(S_x) is itself E0-invariant, and hence is almost surely
constant. Fubini gives (mu x mu)(S) in {0,1}. But S union S^{-1} is
the whole square and S intersection S^{-1}=E0 has product measure
zero. Symmetry gives (mu x mu)(S)=1/2, a contradiction. QED.

**Proof of the extension assertion.** A smooth countable Borel
equivalence relation has a Borel transversal. For each representative
t, choose a Borel enumeration (f_k(t)) of its component using
Lusin--Novikov; repetitions are permitted and finite components can
be padded with t. Consider all s in n^omega satisfying

- equal coordinates whenever f_k(t)=f_l(t);
- unequal colours whenever f_k(t) G f_l(t);
- s(k) in L(f_k(t)) for all k.

These conditions define a nonempty compact set K_t of assignments,
with Borel dependence on t. Nonemptiness follows from finite
solvability and compactness, including the equality constraints.
There is a direct Borel choice: a finite word u has an extension in
K_t iff, for every q>=|u|, there is a finite assignment on the first
q coordinates extending u and satisfying the corresponding finite
constraints. This is a countable conjunction of finite Borel tests.
Choose the least extendable next digit recursively. The resulting
s_t is Borel in t. Colour x by s_t(k), where t is its representative
and k is the least index with f_k(t)=x. Equality constraints ensure
well-definedness. All edges lie within components, so the result is
a Borel proper list colouring. Prescriptions correspond to singleton
lists on E_i and the full palette elsewhere. QED.

Therefore any negative example to the main problem must have an
uncountable incomparability neighbourhood somewhere. A locally
countable irrational-orbit construction cannot be the entire
incomparability graph of the sought Borel order.

## 9. What remains, and which routes have actually been eliminated

The width-three problem for arbitrary Borel prescribed chains is
unresolved in this round. No Borel counterexample satisfying all
eight required checks has been produced. The same is true for
general finite n>=3. The finite examples in this memo have explicit
prescribed extensions and must never be described as counterexamples
to the main Borel theorem.

The strongest verified positive mechanism is chain PU from Section 2.
Its exact limitation can be seen in the seven-point example: the
chain {a0,b0} contains E0 and meets every maximum antichain, because
its complement Z has width two. Nevertheless the remaining
prescription fails FE_2. Puncturing maximum antichains alone does
not preserve the required finite-extension invariant.

For the finite active templates, every parameter n>=3 and r>=1 can
exhibit this defect. The following proposed shortcuts are now ruled out:

1. FE + AS automatically implies AD for chains.
2. Locked active blocks automatically imply AD.
3. Sorting AS witnesses forces their permutations into a fixed
   order-two subgroup.
4. The literal witness-permutation coboundary by itself supplies the
   prescribed chain partition.
5. The anchored forced-inequality relation retains CMV Proposition 7.
6. Every maximal chain in every finite-width Borel order is Borel.

Items 1, 2, 3, 5, and 6 have explicit counterexamples above. Item 4
is a logical insufficiency: the coboundary is already defined before
one assigns a colour to any unprescribed point.

A simultaneous extension must choose its puncturing chain so that
the remaining prescription still has finite extension. Equivalently,
in addition to maximum antichains it must hit every finite set on
which the remaining prescribed (n-1)-colour problem is unsatisfiable.
FE supplies such a chain abstractly; the Borel choice with this full
family has not been established. This is an explanation of the
remaining difficulty, not a newly assumed lemma or a claimed solution.

## 10. Verification and repository record

Finite checks enumerated all subsets and proper prescribed
colourings of the displayed seven-point examples. They verified:
transitivity and antisymmetry; exact widths 3 and 2; AS witnesses;
the unique prescribed colour of x; all six generated permutations;
alpha_1=3 and alpha_2=6; the locked-template norm conditions; and
closure under meet and join of the actual finite witness sets.
The minimality claim in Proposition 5.1 is proved mathematically
above; it is not inferred from an exhaustive search over all posets.

Only `Working_Memo.md` is added to the repository in this round.
`main.tex` remains the inspected baseline, including the two issues
documented in Section 1. All statements marked as proved have proofs
here or an explicit application of a known theorem with its
hypotheses checked. Conditional directions are identified as such.

## 11. Continuation: unbounded minimal obstructions to adding one chain

The continuation following the user's request to keep working establishes
a stronger obstruction than failure of AD. Even after restricting to
points individually eligible for colour 0, pairwise feasibility does not
imply simultaneous feasibility. In fact there is no bound on the arity
of the minimal obstructions, already at width three with six prescribed
points.

### 11.1. Statement

**Theorem 11.1 (unbounded relative obstruction size).** For every m>=2
there is a finite width-three partial order P_m, three prescribed
two-element chains E0,E1,E2 satisfying FE_3 and AS, and an m-element
chain Y, disjoint from the prescription, such that:

1. for every proper subset T of Y there is a prescribed three-chain
   partition D0,D1,D2 with T contained in D0;
2. no prescribed three-chain partition has Y contained in D0.

Moreover, E0,E1,E2 are precisely the active blocks of a locked
(1,2)-saturated template. The chain E0 union Y is a maximal chain
meeting every maximum antichain, and is the first part of an
unprescribed optimal chain partition, but its deletion destroys
finite extension for the other two prescribed chains.

Consequently, for any fixed k, testing all subsets of size at most k
of a proposed augmentation does not suffice; take m>k. The theorem
concerns extension relative to the other prescribed chains. It does
not contradict the unprescribed single-chain pair criterion in
Corollary 2.2.

### 11.2. The explicit order

The point set consists of m+2 layers, each with three points:

\[
A=\{a_0,a_1,a_2\},\quad
L_i=\{p_i,q_i,x_i\}\ (1\le i\le m),\quad
B=\{b_0,b_1,b_2\}.
\]

Order the layers as A,L1,...,Lm,B. Declare s<t whenever s lies in an
earlier layer than t, with exactly the following exceptions:

\[
a_1\perp p_1,\qquad
q_i\perp p_{i+1}\ (1\le i<m),\qquad
q_m\perp b_1.
\tag{11.1}
\]

Points in the same layer are incomparable. Equivalently, the
incomparability graph consists of the layer triangles and the m+1
edges in (11.1), with no other edges.

This is a partial order. Every exception concerns consecutive
layers. If s<t<u, the layers of s and u differ by at least two, so
s<u is included. Thus transitivity holds directly. Antisymmetry
follows from increasing layer indices. The order is finite and
therefore Borel.

Set

\[
E_c=\{a_c,b_c\}\quad(c<3),\qquad
Y=\{x_1,\ldots,x_m\}.
\]

Each E_c is a chain, since A and B are nonconsecutive layers. The
set Y is a chain because no exceptional pair involves any x_i.

### 11.3. Every proper subset has an explicit extension

For any chosen j in {1,...,m}, colour a_c and b_c by c and colour
the inner layers as follows:

| Layer index | d(p_i) | d(q_i) | d(x_i) |
| --- | --- | --- | --- |
| i<j | 2 | 1 | 0 |
| i=j | 2 | 0 | 1 |
| i>j | 1 | 2 | 0 |

Each layer receives all three colours. The first exceptional edge
has colours 1 and 2. Before layer j, a bridge q_i--p_(i+1) has
colours 1 and 2. The bridge immediately after j, if present, has
colours 0 and 1. Subsequent bridges have colours 2 and 1. The last
exceptional edge has colours 0 and 1 when j=m, and 2 and 1 when j<m.
Thus every exceptional edge is properly coloured, and these are
all the remaining incomparabilities. The colour classes are chains.

This gives a prescribed partition with every x_i except x_j in
colour 0. Given T properly contained in Y, choose x_j outside T.
The same partition witnesses T subset D0. It also proves FE_3
and the upper bound width(P_m)<=3. Since every layer is a
three-element antichain, width(P_m)=3. A and B witness AS for all
six prescribed points.

### 11.4. Why the full chain cannot be assigned colour 0

Suppose a prescribed partition gives every x_i colour 0. Then p_i
and q_i have colours 1 and 2 in some order. Since a1 has colour 1
and is incomparable with p1, we must have

\[
d(p_1)=2,\qquad d(q_1)=1.
\]

Inductively, q_i of colour 1 and the exceptional edge q_i--p_(i+1)
force p_(i+1) to have colour 2 and q_(i+1) to have colour 1. Hence
q_m has colour 1. But b1 also has prescribed colour 1 and is
incomparable with q_m, a contradiction. This proves Theorem 11.1.

The argument is the forced two-colouring of the odd path

\[
a_1,p_1,q_1,p_2,q_2,\ldots,p_m,q_m,b_1,
\]

whose endpoints have the same prescribed colour. Declaring all
x_i to have colour 0 removes colour 0 from every internal vertex
of this path. Leaving even one x_j unrestricted permits the
explicit repair in the table above.

### 11.5. Consequences for proposed compatibility graphs

Let U0 consist of those points that can receive colour 0 in at
least one prescribed extension. On U0 define Gamma0 by saying that
two distinct points are adjacent if no prescribed extension gives
both of them colour 0.

For m>=3, all points of Y belong to U0, and Gamma0 restricted to Y
has no edges, because every pair is a proper subset of Y. Yet Y
cannot receive colour 0 simultaneously. Therefore the feasible
augmentations of E0, while preserving E1 and E2, are not the
independent sets of Gamma0. They cannot be the independent sets of
any graph on the same candidate points: every pair in Y is feasible
but Y is not. The same reasoning with m>k rules out an exact
description by forbidden subsets of uniformly bounded size k.

This rules out the specific proposal to reuse a pairwise
forced-inequality graph as a complete description of relative
coherence. It does not rule out encodings with additional state
variables, nor methods that retain arbitrary finite constraints.

Even colour-specific pair conflicts need not coincide with the
ordinary G*: take m=2. Both x1 and x2 individually can have colour 0,
but they cannot both have colour 0. They can, however, both have
colour 1 in a prescribed partition: colour every inner layer
(p_i,q_i,x_i) by (0,2,1), and keep both boundary colourings (0,1,2).
Thus x1 and x2 are Gamma0-adjacent but are not G*-adjacent.

For m>=3, the stronger obstruction is genuinely of higher arity,
even after all such colour-specific pair conflicts have been
included. The restricted-order transitivity question is not used
as an assumption in any argument here.

### 11.6. The bad chain is already maximal and G*-independent

Let C0=E0 union Y. It is a chain. It is maximal: every point outside
C0 shares its layer with a point of C0, and those two points are
incomparable.

There is an unprescribed three-chain partition having exactly C0
as its colour-0 class. Colour all inner layers by (2,1,0), the lower
boundary by (0,1,2), and the upper boundary by (0,2,1). The
exceptional edges all receive different colours. This also shows
that C0 is G*-independent for the ordinary finite forced-inequality
graph, and therefore is maximal G*-independent as well.

Every three-element antichain is one of the displayed layers.
Indeed, points in nonconsecutive layers are comparable, and
between any two consecutive layers there is only one exceptional
pair, which cannot belong to a triangle spanning those layers.
Thus C0 meets every maximum antichain.

Deleting C0 leaves the odd path obstruction above, with its two
endpoints still in E1, so the remaining prescribed two-chain
problem has no solution. Requiring the PU output to be maximal,
even maximal G*-independent, therefore does not fix the problem.

### 11.7. Locked active templates and all n,r

For r=1, set U=A, V=A union B, and S=V. Width three gives
alpha_1=3 and alpha_2<=6, while A and B attain alpha_2=6.
The three two-element blocks E_c have template norms 3 and 6 and
are all active. Fix any one of the prescribed partitions from
Section 11.3. Restricting it to S union F, for any finite F outside
S, preserves both norms, because each colour class retains its
two prescribed endpoints. Hence the template is locked in the
exact sense of the manuscript.

The construction extends to every n>=3 and r>=1. First prepend
r-1 additional three-element antichain layers by ordinal sum,
and prescribe their c-th points to E_c for c<3. Then take the
disjoint union with n-3 chains H_c, 3<=c<n, each of length r+1;
make every point of every H_c incomparable with the entire
three-width construction and with every other H_d. Prescribe
E_c=H_c for c>=3.

The width is 3+(n-3)=n. The displayed three-chain partition,
together with the H_c, gives FE_n. Each prescribed base layer,
augmented by one point from every H_c, witnesses AS for its
points; choosing any specified point of H_c in such a witness
also verifies AS on the added chains.

All prescribed blocks now have r+1 points. Let V=S be their union,
and choose U by taking r of the r+1 prescribed base layers and
r points of each H_c. These give r and r+1 disjoint n-antichains,
respectively, so alpha_r=nr and alpha_(r+1)=n(r+1). Every block
is active, and the fixed prescribed partition proves locking
over every outside finite set.

On the original gadget, colours c>=3 are unavailable because
every original point is incomparable with every prescribed point
of H_c. The argument of Sections 11.3--11.4 therefore still proves
that every proper subset of Y, and not Y itself, can be added to
the first prescribed chain. This is an unbounded obstruction
family inside locked active templates for all n>=3 and r>=1.

### 11.8. Verification and updated research status

The search that led to this construction first found a
fifteen-point example through exact permutation states on five
three-element layers. The final construction above is simpler and
has a proof for every m; its validity does not depend on that
search. Direct finite checks for m=1,...,8 verified transitivity,
AS, the displayed prescribed partitions, the nonexistence of an
all-zero assignment on Y, exact width, the locked norms, the list
of maximum antichains, and maximality of C0. No claim that 3m+6
is the smallest possible number of vertices is made.

The main Borel prescription problem remains unresolved at width
three and for general finite n>=3. These finite orders have
explicit Borel prescribed extensions; they are counterexamples
to compatibility and puncturing shortcuts, not to the main
theorem sought by the project.

What has now been ruled out is stronger than merely deriving AD:
neither pairwise tests nor any fixed finite-arity replacement can
recognize all coherent additions to one prescribed chain. A
remaining positive approach must preserve the entire finite
prescribed-extension condition, potentially through finite
colouring states. No new selection lemma is assumed here.

Only this memo is updated in the continuation. The main manuscript
remains unchanged.

## 12. Continuation: exact finite-state feasibility can be complete coanalytic

Research continuation: 2026-09-08, following repository commit
5da11b7bbf37e52ab4db3a5060e1779a77442ab0.

The finite-state approach must distinguish the exact set of possible states
from the existence of a Borel selection among possible states. This section
gives a sharp obstruction to the first; Section 13 proves a selection result
that survives it.

### 12.1. General upper bound from compactness

Consider a Borel family of graphs or partial orders indexed by a standard
Borel parameter space T. Write X_t for the fibre at t. Fix a finite palette
n and Borel lists L(t,x) contained in n, and assume every finite induced
list-colouring problem in every fibre is solvable. Prescriptions are the
special case of singleton lists on the prescribed sets.

Formally, the family has a Borel total space contained in T x Z for a
standard Borel space Z, and its relations and lists are Borel on that
space. Constraints in this parameterized assertion do not couple
different fibres.

Let b_0(t),...,b_(k-1)(t) be Borel marked points in X_t. For a word
s in n^k, let V_s be the set of parameters t for which some abstract
list-colouring of the entire X_t has c(b_j(t))=s(j) for j<k.
Repeated markers must have equal assigned colours.

**Proposition 12.1.** V_s is coanalytic.

**Proof.** By compactness in n^(X_t), failure of this extension condition
is witnessed by finitely many vertices and constraints. Equivalently,
some finite F containing the marked points has no list-colouring respecting
the word s. For a fixed finite tuple, existence or nonexistence of such a
colouring is a finite Boolean combination of Borel predicates, since the
palette is finite. Existentially quantifying over the finite tuple makes
T minus V_s analytic. This includes conflicts between repeated markers.
QED.

The quantification is over all finite witnesses in X_t, not merely over
finitely many marked points. In general it cannot be replaced by a Borel
test, as the next construction shows.

### 12.2. A uniform width-three construction

Let T be the space of trees on N, with its usual standard Borel structure.
For t in T let Y_t be a tagged copy of the branch set [t], ordered by the
lexicographic order on N^N. Thus Y_t is a chain, possibly empty. The set of
pairs (t,z) with z a branch through t is closed.

In addition to Y_t put nine named points in the fibre:

- A_t={a_0,a_1,a_2};
- B_t={b_0,b_1,b_2};
- D_t={d_0,d_1,d_2}.

Each of these three sets is an antichain. Declare all comparisons
A_t < B_t < D_t, where comparisons between whole sets mean every pair
in the indicated direction. For every y in Y_t also declare

\[
a_1<y,\qquad y<b_0,\qquad y<b_2,\qquad y<d_i\quad(i<3).
\]

Apart from the order inside Y_t, these are all strict comparisons.
In particular y is incomparable with a_0,a_2,b_1.
Prescribe E_i(t)={a_i,d_i}.

The relation is transitive: the only extra two-step comparisons through
Y_t are a_1<b_0,b_2,d_i, already included, and those through B_t yield
the listed comparisons to D_t. It is antisymmetric because all strict
comparisons respect the displayed levels, with a strict linear order
inside the Y_t level. It is Borel uniformly in t.

There is a fixed Borel prescribed partition, valid whether or not Y_t
is empty:

\[
C_0(t)=\{a_0,b_1,d_0\},\quad
C_1(t)=\{a_1,b_0,d_1\}\cup Y_t,\quad
C_2(t)=\{a_2,b_2,d_2\}.
\]

These are chains. A_t witnesses width at least three, so the exact width
is three. The partition verifies FE_3 and abstract and Borel extension.
A_t and D_t verify AS for every prescribed point.

This is also an actual locked active template in each fibre:
take U=A_t and V=S=A_t union D_t. Each prescribed chain has two points,
the norms are alpha_1=3 and alpha_2=6, and restriction of the displayed
partition to S union F keeps both norms for every finite outside F.
The two disjoint three-antichains A_t,D_t verify the second norm directly.

### 12.3. Exact state computation

A colouring on B_t is a permutation sigma in S3, with sigma(i)=c(b_i).
Let S(t) be the set of permutations that extend the prescribed colouring.
Then

\[
S(t)=
\begin{cases}
S_3, & [t]=\varnothing,\\
\{\sigma\in S_3:\sigma(1)\ne1\}, & [t]\ne\varnothing.
\end{cases}
\]

Indeed, every y in Y_t is incomparable with a_0 and a_2, so its colour
must be 1. Its incomparability with b_1 excludes sigma(1)=1 whenever
Y_t is nonempty. Conversely, if sigma(1) differs from 1, assign colour
1 to all of Y_t. The unique colour-1 point in B_t is then b_0 or b_2,
both above Y_t, and this gives a prescribed chain partition. If Y_t
is empty, any permutation on B_t works because all A_t-to-B_t and
B_t-to-D_t comparisons are present.

Consequently

\[
\{t:\operatorname{id}\in S(t)\}
=\{t:[t]=\varnothing\}=\mathrm{WF}.
\]

This is complete coanalytic. The standard completeness fact and its proof
are in [B. D. Miller, An introduction to classical descriptive set theory,
Proposition 1.4.28](https://glimmeffros.github.io/seminars/descriptive.pdf):
ill-founded trees are complete analytic, hence their complement WF is
complete coanalytic. Proposition 12.1 is therefore sharp.

In particular, choosing the lexicographically least feasible permutation,
with the identity first, gives a non-Borel map: the inverse image of the
identity is exactly WF. A Borel choice nevertheless exists here, for
example the constant permutation (1,0,2) used in the displayed partition.

To view the construction as one Borel poset with Borel prescribed chains,
fix a Borel linear order on T and take the ordinal sum of the fibres:
every point in an earlier fibre is below every point in a later fibre.
The global width is three, each union E_i=union_t E_i(t) is a Borel
chain, and the displayed partition is globally Borel. State feasibility
at B_t is unchanged since choices in different fibres are independent.
Thus the example satisfies the main problem's hypotheses, but it is
not a counterexample to its conclusion.

### 12.4. All widths and all locked parameters

For n>=3 and r>=1, in each fibre prepend r-1 three-antichain layers
to the base order and add their i-th points to E_i for i<3. Disjointly
add n-3 chains H_i of length r+1, each incomparable with the whole base
and with every other H_j, and prescribe E_i=H_i for i>=3.

The width is n, witnessed by any displayed three-antichain together
with one point from each H_i. The displayed partition extends, so FE_n
holds. The r+1 prescribed three-antichain layers, augmented by arbitrary
points of the H_i, verify AS for all prescribed points.

All E_i have r+1 points. Their union V=S and the subset U consisting
of r prescribed base layers and r points from each H_i give norms
alpha_r=nr and alpha_(r+1)=n(r+1). Every block is active and restriction
of the explicit colouring verifies locking for every finite outside set.
The additional colours are unavailable on the base because of its
incomparability with the prescribed H_i. Therefore the same exact S3
state computation remains valid.

The locking assertion here is fibrewise, for finite prescribed blocks.
After forming the global ordinal sum, the E_i are infinite; no finite
global template containing these entire unions is asserted.

Direct finite checks replaced Y_t by chains of lengths 0,...,5 and
exhaustively computed all boundary permutations, obtaining exactly six
states when empty and four when nonempty. Transitivity, exact width,
AS, the explicit colouring, and locked norms were also checked.
The lifted cases n=5,r=3 with zero and two witnesses passed the same
checks. These finite computations support the order calculation;
the descriptive complexity claim follows from the proof above.

## 13. Proved: Borel coherent selection along countably many marked points

The non-Borel viability relation in Section 12 does not prevent choosing
a viable state. The needed distinction can be proved using analytic
separation; it does not require a new unproved uniformization hypothesis.

### 13.1. Finite coanalytic covers have Borel refinements

**Lemma 13.1.** If V_0,...,V_(q-1) are coanalytic subsets of a standard
Borel space T and their union is T, there is a Borel function h:T->q
such that t belongs to V_(h(t)).

**Proof.** Put A_i=T minus V_i. These are analytic and have empty
intersection. They have Borel supersets B_i with empty intersection.
For completeness, this finite version follows by induction from
Lusin separation. Separate intersection_(i<q-1) A_i from A_(q-1)
by a Borel set C. On T minus C apply the induction hypothesis to
the first q-1 analytic sets. If their resulting hulls there are B'_i,
use B_i=C union B'_i for i<q-1 and B_(q-1)=T minus C. The base
q=1 has A_0 empty. Now let h(t) be the least i with t outside B_i.
It is Borel and t is outside A_i, as required. QED.

The separation inputs are classical; see Theorems 1.4.14 and 1.4.21
of [Miller's notes](https://glimmeffros.github.io/seminars/descriptive.pdf).
This proof selects from a Borel refinement. It does not claim that
the lexicographically least genuinely viable state is Borel.

### 13.2. Countably many markers, with full finite extension preserved

Retain the parameterized setup of Section 12.1, and suppose now that
we are given Borel markers b_j(t) in X_t for every j in N.

**Theorem 13.2.** There is a Borel map s:T->n^N such that, for every t,
some abstract list-colouring c_t of the entire X_t satisfies
c_t(b_j(t))=s(t)(j) for every j. No Borel dependence of the unmarked
part of c_t is claimed.

**Proof.** A finite marker word is called viable if it extends to an
abstract colouring of the entire fibre. Its viability set is coanalytic
by Proposition 12.1. Start with the empty viable word.

Suppose Borel s_k:T->n^k has been chosen and is viable at every t.
For each i<n, the set of t for which s_k(t) followed by i is viable
is coanalytic: partition T into the finitely many Borel sets where
s_k has a specified value and use Proposition 12.1 on each.
These n sets cover T. An abstract colouring witnessing viability
of s_k supplies at least one allowable next colour.

Apply Lemma 13.1 to choose a Borel next digit, and obtain s_(k+1).
Iterating gives the Borel sequence s(t).

For fixed t, the space K_t of all abstract list-colourings of X_t is
a nonempty closed subset of the compact product n^(X_t). The sets
of colourings in K_t agreeing with s(t) on the first k markers are
nonempty nested closed sets. Compactness gives a colouring in their
intersection. It agrees on every marker, including repeated markers.
QED.

This argument preserves the entire finite extension condition at every
step. It does not project feasibility to individual colours independently
or impose any fixed arity bound. Finite blocks of marked points, including
antichains carrying permutation states, can be treated as successive
groups of coordinates.

### 13.3. A positive extension criterion from a determining sequence

**Corollary 13.3.** In the setup of Theorem 13.2, assume that any two
abstract prescribed list-colourings of each X_t agreeing on all b_j(t)
agree everywhere in X_t. Then there is a Borel prescribed list-colouring
of the entire Borel family.

**Proof.** The theorem chooses marker values admitting an extension;
the extra hypothesis makes this extension unique in each fibre.
For i<n let Bad_i be the set of (t,x) for which these marker values,
the original lists, and the extra demand c(x)=i have no extension.

Bad_i is analytic. Compactness witnesses membership by finitely many
vertices and finitely many of the assigned markers. Their indices range
over a countable set, and their chosen colours depend Borelly on t,
so the finite obstruction condition is again a projection of a Borel
relation.

By existence and uniqueness, the colour-i class is
intersection_(j!=i) Bad_j. It is analytic. The n such classes are
disjoint and cover the family, so the complement of each is also
analytic; therefore each class is Borel. For n=1 the colouring is
constant. QED.

This is a proved sufficient criterion, not a claim that a determining
sequence exists for every finite-width Borel order. In fact, for n>=2,
even an ordinal sum over an uncountable index set of n-antichains has no
countable determining subset for all its unprescribed colourings:
one can change the permutation on an untouched layer. Such an order
still has easy Borel colourings.

The marker hypothesis is also not automatic from compactness. A compact
space of abstract colourings on an uncountable vertex set need not be
metrizable or determined by countably many vertex evaluations. The
theorem does not provide a Borel enumeration of uncountable fibres
or of nonsmooth countable equivalence classes.

### 13.4. A finite permutation criterion without a smooth quotient

The same separation argument yields a directly usable special case.

**Proposition 13.4.** Let G be a Borel graph with a fixed Borel
n-colouring c. Suppose every proper n-colouring on each connected
component is a permutation of c on that component. Then every Borel
precolouring satisfying FE_n extends to a Borel n-colouring.

**Proof.** Let E be connectedness; it is an analytic equivalence
relation, with no Borelness or smoothness assumption. For each
permutation pi in S_n, let A_pi be the set of x whose component
contains a prescribed point e whose required colour differs from
pi(c(e)). Each A_pi is analytic and E-invariant.

Compactness gives an abstract prescribed colouring. Its restriction
to any component is pi composed with c for some pi, by hypothesis.
Thus the intersection of all A_pi is empty.

Disjoint analytic E-invariant sets can be separated by an E-invariant
Borel set. To see this, start with a Borel separator D_0. Its
E-saturation is analytic and still avoids the second invariant set.
Enclose that saturation in another Borel separator D_1 and repeat.
The union of the D_k is Borel, invariant, and separates the sets.
Apply the induction in Lemma 13.1 using such invariant separators.
It gives invariant Borel hulls B_pi of A_pi with empty intersection.

Choose the least pi with x outside B_pi. This choice is Borel and
constant on each component. The colouring x -> pi_x(c(x)) is proper
and has every required colour. QED.

For orders, Borel Dilworth supplies c whenever the palette is the
finite width. This proposition extends the component-permutation
argument beyond two colours when its explicit rigidity hypothesis
holds. The unrestricted width-three problem does not have that
hypothesis: the finite examples in Sections 4 and 11 already allow
different permutations in the same connected component.

## 14. Proved: extension over a realistic quotient with countable local incomparability

The earlier realistic and locally countable cases can be combined
in a way that handles orders satisfying neither global hypothesis.

**Theorem 14.1.** Let P be a finite-width Borel partial order on X.
Suppose there are a Borel surjection q:X->T, a Borel subset T of R,
and a realistic finite-width Borel partial order Q on T such that:

1. For points in different fibres, comparisons are determined entirely
   by Q:
   x<_P y if and only if q(x)<_Q q(y), whenever q(x)!=q(y).
2. Inside each fibre q^(-1)({t}), every point has only countably
   many incomparable neighbours.

For any Borel lists L(x) contained in a fixed finite palette n,
finite solvability implies a Borel list-colouring of
incomparability(P). In particular FE_n suffices for prescribed
Borel chains, with no AS assumption.

**Proof.** Take an abstract list-colouring d by compactness, and let
D_i be its colour-i chain. Its image T_i=q(D_i) is a Q-chain:
any two distinct image points have comparable representatives in D_i,
so condition 1 makes the image points Q-comparable.

Extend T_i to a maximal Q-chain M_i. All M_i are Borel by maximal-chain
regularity for realistic finite-width orders, as in Section 7.
The sets T_i and D_i need not be definable; no projection regularity
for them is assumed. Define the Borel restricted lists

\[
L'(x)=L(x)\cap\{i<n:q(x)\in M_i\}.
\]

They contain d(x), so all their finite constraints remain solvable.

Now replace comparisons between distinct fibres by the ordinary real
order of their parameters. In other words, define a Borel partial
order P' by keeping P inside each fibre and declaring every point
of fibre t below every point of fibre u whenever t<u in R.
This is an ordinal sum of the fibre orders. It is transitive and
antisymmetric; its incomparability graph is locally countable by
condition 2. Each fibre has finite width bounded by that of P.

The map d is an abstract L'-colouring of incomparability(P'), since
only extra comparabilities were added. Apply Proposition 8.1 to P'
and L'. It supplies a Borel proper list-colouring c.

Finally, two distinct points with c(x)=c(y)=i are P-comparable.
If they lie in the same fibre, this follows from the definition of
P'. If they lie in different fibres, their parameters both belong
to the Q-chain M_i, so condition 1 again gives P-comparability.
Also c respects L' and hence L. QED.

No uniform choice of maximal chains across parameters is required:
only the finitely many chains M_i of the single quotient Q are
chosen. Uniform colouring inside fibres is supplied by applying
the already proved locally countable theorem once to the whole P'.

**Corollary 14.2.** In particular the theorem applies when each fibre
is an arbitrary Borel chain. Fibres need not be countable and their
linear orders need not embed in the reals.

This positive class is not contained in either earlier global
special case. For example, take three mutually incomparable chains,
each of order type R x {0,1} in lexicographic order. Collapse the
two-point fibres onto a quotient consisting of three incomparable
copies of R, encoded in three disjoint real intervals. This quotient
is realistic and the fibre incomparability graphs are empty.

The full order has width three and uncountable incomparability
neighbourhoods. It is not realistic: in any one of its chains, an
order-preserving injection into R would assign disjoint nonempty
real intervals to the uncountably many pairs (t,0)<(t,1), requiring
uncountably many distinct rationals. Theorem 14.1 nevertheless
gives prescribed and list extensions.

The quotient condition is essential to this proof. Without uniform
comparisons between distinct fibres, membership of q(x),q(y) in a
quotient chain would not imply that x,y are P-comparable. No claim
that every finite-width Borel order admits such a quotient is made.

## 15. Status after the 2026-09-08 continuation

The main FE + AS implication remains unresolved at width three
and for all finite widths n>=3.

What is proved in this continuation is:

- Exact feasibility of a complete finite boundary permutation can be
  complete coanalytic, even in a Borel family of finite prescribed
  locked active templates, for all n>=3 and r>=1.
- Finite coanalytic viability sets still admit Borel refinements.
  Countably many given Borel markers can therefore be assigned
  colours Borelly while retaining the entire finite extension
  condition. A determining sequence gives a full Borel extension.
- Componentwise permutation rigidity gives another positive
  prescribed-extension criterion, without requiring smooth
  connectedness.
- Uniform substitution over a realistic quotient, with locally
  countable fibre incomparability, gives a further full positive
  theorem for arbitrary finite Borel lists, without AS.

The viable-state route is therefore not defeated by non-Borel
state membership itself. Its remaining task is to organize enough
states, or enough uniformly manageable residual pieces, to colour
the whole uncountable order while maintaining compatibility.
Countable marker selection by itself does not do this; the
component-rigidity and quotient hypotheses have not been derived
from FE + AS.

Only this memo is updated. The main manuscript is unchanged.


## 16. Reading the simplified proof: anchored overflow, forced closure, and the bulk-addition obstruction

Research continuation: 2026-09-13. Source supplied by the user:
Jialiang He, "Proof of Borel Dilworth Theorem", six-page PDF
(simplifyboreldilworth .pdf). The entire text was read and the final
induction page was also checked visually. This section follows its
specific proof mechanism rather than substituting an unrelated method.

The requested full multi-anchor extension theorem is not proved here.
Two parts of the mechanism do extend, with proofs below. The direct
bulk-addition step has a verified finite counterexample.

### 16.1. The precise scope of the original Q construction

The PDF's Q is the unprescribed refinement
x <=_Q y iff x <=_P y and every finite problem admits an optimal
partition putting x,y together. Its incomparability graph is G*.

Propositions 0.2 and 0.3 supply a width-k partial order and the safe-point
property for maximum Q-antichains. For one finitely coherent Borel seed
B, the same puncturing argument can begin at B rather than at the empty
set. Its result is exactly the single-seed extension theorem already
recorded in Section 2; this is not a new claim of progress.

To finish that argument without a regularity issue, puncture the maximum
Q-antichains and then apply the width induction to the Borel induced
P-order on the complement. Its width is at most k-1. The resulting full
optimal P-partition automatically consists of Q-chains, since restriction
of this partition witnesses pair compatibility on every finite set.

This also repairs two details in the PDF's Proposition 0.6 as written:
the punctured family should be the maximum Q-antichains if the subsequent
width bound is asserted for Q; and Q is not known to be Borel merely
from its definition, so a Borel-order induction should be applied to the
residual P-order. Alternatively one can explicitly use the wider
definability class of the Carroy--Miller--Vidnyanszky theorem.
Neither issue affects the finite arguments in Propositions 0.2--0.3.

For several prescribed colours, the correct analogue of safety must
preserve all labels and all finite extension constraints. Being merely
a Q-chain does not express that condition.

There is also a useful valid consequence of AS. If the one-seed
construction starts at E_0, its output C_0 cannot meet any E_i for
i!=0: an AS witness for e in E_i contains a point of E_0 incomparable
with e. Thus AS guarantees avoidance of the other prescribed sets.
It does not guarantee FE for their residual prescription. Section
16.4 exhibits a legitimate puncturing Q-chain with precisely that
residual failure.

### 16.2. Elementary Borel hull lemma for all finite constraints

**Lemma 16.1.** Let Z be a standard Borel space and let R_m be an analytic
subset of Z^m for every m>=1. If A is analytic and
R_m intersect A^m is empty for every m, then A has a Borel superset B
with R_m intersect B^m empty for every m.

**Proof.** Fix m. Starting with R_m disjoint from A^m, enlarge the
coordinates one at a time. Suppose B_1,...,B_(j-1) have already been
chosen Borel, contain A, and

R_m intersect (B_1 x ... x B_(j-1) x A x ... x A) is empty.

The projection onto coordinate j of
R_m intersect (B_1 x ... x B_(j-1) x Z x A x ... x A)
is analytic and disjoint from A. By analytic separation choose a Borel
B_j containing A and disjoint from that projection. After all m steps,
R_m avoids the product of the B_j. Hence it avoids B(m)^m where
B(m)=intersection_(1<=j<=m) B_j. Finally set B=intersection_m B(m).
QED.

Apply this with Z=X x n. A point (x,i) represents the requirement that
x receive colour i. For a Borel graph G and a Borel initial prescription
p, let R_m consist of the m-tuples of such requirements which cannot
be extended to any abstract proper n-colouring extending p.
These relations are analytic: compactness reduces failure to a finite
vertex witness, and the finite colouring tests are Borel.

**Corollary 16.2 (simultaneous anchored Borel hull).** Suppose analytic
sets A_i, i<n, contain the initial prescribed colour classes, and
every finite problem admits a proper n-colouring respecting all A_i.
There are Borel supersets B_i of A_i with the same finite-extension
property. In particular the B_i are pairwise disjoint independent sets.

**Proof.** The tagged union A=union_i (A_i x {i}) avoids every R_m.
Apply Lemma 16.1 and take the colour sections of the resulting Borel
set. A repeated vertex assigned distinct colours is a forbidden
two-tuple, and an edge assigned the same colour is also forbidden.
Thus the sections are disjoint independent sets. Avoidance of all
R_m says that all their finite assignments extend relative to p;
compactness then gives simultaneous finite coherence, indeed an
abstract full extension. QED.

For incomparability graphs the B_i are chains. This proves the exact
multi-anchor version of the PDF's overflow step, including preservation
of FE. It does not assume any bounded arity for the forbidden relations.

### 16.3. A Borel extension closed under all forced colours

For a coherent Borel partial colouring p, let K(p) be the nonempty
compact space of all abstract proper n-colourings extending p.
Say x is forced to colour i over p if every c in K(p) has c(x)=i.

**Theorem 16.3.** Any coherent Borel partial n-colouring p of a Borel
graph has a coherent Borel partial extension p_infty such that every
point outside its domain has at least two possible colours among
the abstract full extensions of p_infty.

**Proof.** For each i, the set Bad_i(p) of x for which p together with
x=i has no extension is analytic, by the finite-obstruction argument.
The set of points forced to colour i is

F_i(p)=intersection_(j!=i) Bad_j(p).

It is analytic. For n=1 it is all X. All the assignments x=i for
x in F_i(p) hold simultaneously in every member of K(p). Therefore
adjoining all of them to p preserves finite coherence. By Corollary
16.2, this analytic partial extension has a coherent Borel extension.

Starting from p_0=p, repeat this operation to obtain increasing coherent
Borel partial colourings p_m, with every point forced over p_m assigned
in p_(m+1). Their union p_infty is Borel and coherent: every finite
set of assigned requirements already appears at one stage.

Suppose x outside its domain had just one possible colour i. For every
j!=i, failure of p_infty together with x=j has a finite witness. Only
finitely many assigned points of p_infty occur in the finitely many
witnesses, so all those requirements already belong to some p_m.
Thus every j!=i is already impossible over p_m, whereas K(p_m) is
nonempty. The point x is forced to colour i over p_m and is assigned
at stage m+1, a contradiction. QED.

This is a genuine anchored expansion theorem for partial colourings,
but it does not assert that the expanded domain is all X.

**Corollary 16.4.** If G already has a Borel proper 2-colouring, every
coherent Borel precolouring extends to a Borel proper 2-colouring.

**Proof.** Apply Theorem 16.3 with n=2. No edge joins the coloured
domain to its complement: such an edge would exclude the coloured
endpoint's colour and force the other colour at its uncoloured endpoint.
Use the original Borel 2-colouring on the complement and glue it to
p_infty. There are no cross edges, so the result is proper. QED.

For width-two Borel orders, unprescribed Borel Dilworth supplies the
initial Borel 2-colouring. This is another complete proof of the
width-two anchored theorem along an overflow-and-iteration route.

At width three, the identical conclusion is weaker: an uncoloured
point can still have two possible colours and have neighbours in the
coloured domain. Gluing an arbitrary residual Borel 3-colouring is
therefore not justified.

### 16.4. Why the PDF's bulk-addition line does not preserve all anchors

The PDF repeatedly uses the implication

each point of H is safe over C, and H lies in one Q-chain
=> C union H is a Q-chain.

For the original binary chain property this is correct. The analogous
implication for simultaneous anchored finite coherence is false.

Use the m=2 instance from Section 11. Its twelve points are four
three-antichain layers, in increasing order:

A={a_0,a_1,a_2}, L_1={p_1,q_1,x_1},
L_2={p_2,q_2,x_2}, B={b_0,b_1,b_2}.

Every earlier-layer point is below every later-layer point except

a_1 incomparable with p_1,
q_1 incomparable with p_2,
q_2 incomparable with b_1.

Prescribe E_i={a_i,b_i}. This is a transitive width-three order,
satisfies FE and AS, and is a locked active template with all three
blocks of size two, as proved in Section 11.

Both x_1 and x_2 can individually be added to colour 0 while keeping
every E_i. Explicit prescribed colourings of the two inner layers are:

| Additional requirement | (p_1,q_1,x_1) | (p_2,q_2,x_2) |
| --- | --- | --- |
| x_1 has colour 0 | (2,1,0) | (2,0,1) |
| x_2 has colour 0 | (2,0,1) | (1,2,0) |

In both rows a_i and b_i have colour i. Thus each candidate is safe
over the full original prescription, in the correct anchored sense.

Moreover E_0 union {x_1,x_2} is itself a Q-chain for the PDF's original
unprescribed Q. To verify this without computing Q, colour A by
(0,1,2), both inner layers by (2,1,0), and B by (0,2,1).
This is a proper optimal colouring with E_0,x_1,x_2 all in colour 0.
Its finite restrictions witness every required Q-comparability.

However x_1 and x_2 cannot both be assigned colour 0 while retaining
E_1 and E_2. If they were, a_1=1 would force p_1=2 and q_1=1;
then q_1 incomparable with p_2 forces p_2=2 and q_2=1;
finally q_2 incomparable with b_1=1 is a contradiction.

Consequently the bulk union may cease to have FE before any Borel
hull is taken. Corollary 16.2 cannot repair an incoherent input.

In fact the example already satisfies the all-safe condition sought
by the first phase of the PDF's iteration. Here is a finite certificate
that Q=P. In the following five unprescribed colourings each row lists
the colours in A,L_1,L_2,B, in their displayed point order:

| A | L_1 | L_2 | B |
| --- | --- | --- | --- |
| 012 | 012 | 012 | 021 |
| 012 | 021 | 120 | 210 |
| 012 | 201 | 210 | 102 |
| 012 | 210 | 201 | 120 |
| 012 | 012 | 201 | 012 |

Every row is proper, and every comparable pair of distinct vertices
has equal colours in at least one row. Thus every P-comparison is a
Q-comparison, proving Q=P. All three-antichains are the four layers:
an interlayer incomparability is one of the three isolated bridge
edges and cannot be part of a triangle crossing layers. Hence the
maximum Q-antichains missed by E_0 are exactly L_1 and L_2.

The two prescribed colourings displayed earlier make x_1,q_2 and
q_1,x_2, respectively, safe for colour 0. The additional prescribed
colouring L_1=012,L_2=021 makes p_1,p_2 safe for colour 0.
Therefore every point of every unhit maximum Q-antichain is individually
safe over the full prescription.

Choose the background Q-colouring with A=012,L_1=L_2=210,B=021.
Its colour-0 class is E_0 union {x_1,x_2}. The second-phase bulk
addition, applied to this class, adds both candidates and destroys FE.
Thus the failed inference occurs even after the advertised all-safe
condition has already been achieved.

Moreover C_0=E_0 union {x_1,x_2} meets every maximum Q-antichain,
because it meets all four layers. It is a valid output of the
unprescribed one-seed puncturing theorem, contains E_0, and avoids
E_1 union E_2. Its complement has width two, but its prescribed
E_1,E_2 extension fails on the odd path
a_1,p_1,q_1,p_2,q_2,b_1 with equally pinned endpoints.
Thus every part of the proposed first-chain step can succeed while
the labelled induction on the complement still fails.

An exhaustive check found 10 prescribed colourings and 384 unprescribed
proper 3-colourings, and verified the two tables and all comparable-pair
certificates. The explicit certificates above also give a finite proof
independent of relying on an unexplained search result.

The Section 11 family gives the same failure at every prescribed
arity threshold, so increasing a fixed bound on simultaneous checks
does not resolve this step.

### 16.5. A labelled version of splicing that is valid

There is a useful way to preserve labels when splicing: splice at a
whole maximum antichain, instead of at a single point.

**Lemma 16.5 (maximum-antichain amalgamation).** Let P have width n
and A={a_i:i<n} be an n-antichain. Define

L={x: x<=a_i for some i}, U={x: a_i<=x for some i}.

Then L union U=X and L intersect U=A. If proper n-colourings of L
and U agree on A, their union is a proper n-colouring of X.
It preserves all prescriptions respected by the two colourings.

**Proof.** A is a maximal antichain, so every point is comparable
with some a_i, giving the union assertion. If a_i<=x<=a_j,
the antichain property and antisymmetry force i=j and x=a_i,
giving the intersection assertion.

Relabel the common colouring of A as a_i=i. If x in L has colour i,
it is comparable with a_i. The possibility a_i<x is excluded by
x<=a_j for some j, which would give a_i<a_j. Hence x<=a_i.
Dually any colour-i point y in U satisfies a_i<=y. Thus all
cross pairs of colour i satisfy x<=a_i<=y. The glued colour
classes are chains and all prescribed labels remain intact. QED.

If P is Borel and A is finite, L and U are Borel. Therefore the
lemma also glues Borel colourings whenever they have already been
constructed on the two sides with matching boundary states.

This is an actual label-preserving consequence of the splicing idea.
It does not produce the two required Borel side colourings from their
abstract existence, so it is not presented as a solution of the
multi-anchor theorem.

### 16.6. Exact conclusion of the requested adaptation

The supplied proof rigorously supports the one-seed theorem, a full
simultaneous anchored Borel hull lemma, a Borel forced-colour closure,
and maximum-antichain amalgamation. The forced-colour closure completes
the anchored theorem at width two.

For width three and general n>=3, the bulk-addition step that would
continue the same iteration is false even in finite locked active
templates. The main FE + AS extension theorem remains unresolved.
No conclusion that the supplied proof is useless is drawn; the valid
parts and the precise failed inference are separated above so that
further adaptations do not silently discard the remaining anchors.

The main manuscript and the user's PDF are unchanged.
