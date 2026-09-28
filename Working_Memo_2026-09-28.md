# Working memo continuation: fibre localization and induced-path restrictions

Date: 2026-09-28. Repository: `jlhscu/Borel-poset-extend`, branch `main`.

Read together with `Working_Memo.md`, especially Sections 2, 8, and 17. The earlier memo and `main.tex` are preserved unchanged. This continuation records proved results, not a claimed solution of the unrestricted problem.

## Status

The unrestricted width-three and width-n FE + AS prescription problems remain unresolved in this continuation. The following results are proved here:

1. The chain-hull conclusion of Lemma 17.1 holds for **every Borel nondecreasing real-valued map**, without countable fibres. Consequently Theorem 17.2 extends to maps whose fibres have **locally countable incomparability graphs**. All finite Borel lists are allowed; AS is unnecessary. This includes uncountable chain fibres and does not require uniform comparisons between fibres.
2. At width three, FE + AS implies Borel prescribed extension whenever the incomparability graph is **induced-P5-free**. The prescribed chains may be arbitrary Borel sets, not just finite sets.
3. For every finite width n, **AS alone** suffices when the incomparability graph is **induced-P4-free**.
4. At width four, a verified nine-point induced-P5-free poset satisfies FE + AS but fails AD. A legitimate first puncturing chain destroys residual prescribed feasibility. The example extends to every n >= 4 and to locked (r,r+1) active templates for every r >= 1.

Here P_j denotes the path on j vertices. All path-freeness assertions concern **induced** subgraphs. No novelty claim relative to the entire literature, and no minimality claim for the finite examples, is made.

## 18. Borel chain hulls with arbitrary real-valued monotone maps

### 18.1. Countable bounds in arbitrary subchains

**Lemma 18.1.** Every nonempty chain in a finite-width Borel partial order has a countable cofinal subset and a countable coinitial subset. No definability assumption on the chain is necessary.

**Proof.** Borel Dilworth covers the order by finitely many Borel chains C_j. Harrington--Marker--Shelah prove that a Borel linear order embeds into lexicographically ordered 2^alpha for some countable ordinal alpha.

There is no strictly increasing sequence of length omega_1 in 2^alpha. Indeed, on a tail the first binary coordinate is constant. Recursively, after all earlier coordinates have stabilized, the next coordinate is monotone and eventually constant. At a limit stage take the supremum of the earlier stabilization indices. Since alpha is countable, their final supremum is still below omega_1, making the entire sequence constant on a tail. The decreasing case is identical.

Any subset of a linear order without an omega_1-increasing sequence has a countable cofinal subset: otherwise choose successively a point strictly above all previously chosen points at every countable stage. The order-dual argument gives a countable coinitial subset. Apply this to each nonempty intersection of the given chain with C_j, and take the finite unions of the resulting sets. QED.

The external input here is the theorem for **Borel linear orders**. It is not the false assertion that arbitrary chains in arbitrary Borel partial orders have countable cofinality.

### 18.2. Removing the countable-fibre hypothesis from the hull lemma

**Theorem 18.2 (fibre-local chain hull).** Let P be a finite-width Borel partial order on X, and let rho:X -> R be Borel and nondecreasing on P. For every P-chain M, whether definable or not, there is a Borel H containing M such that

    x,y in H and x incomparable_P y  =>  rho(x)=rho(y).

Neither maximality of M nor countability of the fibres is required.

**Proof.** If M is empty, take H empty. Otherwise put T=rho(M) and K=closure(T) in R. Choose a countable S contained in M such that rho(S) is dense in K. Define

    H_0 = {x : rho(x) in K and x is P-comparable with every s in S}.

This set is Borel and contains M. Let A be the set of the two endpoints of every bounded connected component of R minus K. There are only countably many such components, so A is countable.

Suppose x,y belong to H_0 and rho(x)<rho(y). If K meets the open interval (rho(x),rho(y)), choose s in S with rho(x)<rho(s)<rho(y). Comparability with s and monotonicity imply x<_P s<_P y. Consequently, if x,y are incomparable and have different rho-values, the open interval between these values misses K. Since both endpoints belong to K, this is a bounded component of R minus K; both values therefore belong to A.

It remains to repair only the countably many endpoint fibres. For t in A put M_t=M intersect rho^{-1}({t}). If this is nonempty, Lemma 18.1 supplies a countable S_t contained in M_t that is both cofinal and coinitial in M_t. Put

    B_t = union{[a,b]_P : a,b in S_t and a<=_P b}.

If M_t is empty, put B_t empty. Each B_t is Borel, contains M_t, and lies in rho^{-1}({t}). Every member of B_t lies between two members of M_t. Define

    H = (H_0 minus rho^{-1}(A)) union
        union_{t in A}(H_0 intersect B_t).

This is a Borel superset of M. Take x,y in H with rho(x)<rho(y). If their open interval meets K, the earlier argument gives x<_P y. Otherwise both values belong to A. Choose b in M_{rho(x)} and a in M_{rho(y)} with x<=_P b and a<=_P y. Since a,b lie on M and rho(b)<rho(a), monotonicity forces b<_P a. Hence x<=_P b<_P a<=_P y. This proves the asserted localization of incomparability. QED.

The endpoint-fibre repair is essential. Merely choosing one representative at each isolated image value does not control an uncountable fibre. We instead use countable cofinal and coinitial subsets and their P-intervals. Only countably many fibres are repaired; no uniform selection from an uncountable family of arbitrary chains is used.

### 18.3. Full list-colouring theorem with uncountable fibres

Recall the previously proved input from Section 8 of the earlier memo:

**Locally countable input.** If the incomparability graph of a Borel partial order is locally countable, every finitely satisfiable assignment of Borel lists from a fixed finite palette has a Borel proper list colouring.

For clarity, its mechanism is as follows. The incomparability connectedness relation is a countable Borel equivalence relation. Distinct components are uniformly ordered by P: along an incomparability edge a point in another component cannot switch from lying below to lying above its endpoints, by transitivity. Thus P together with connectedness is a Borel total quasi-order whose equivalence classes are those components. This countable equivalence relation is smooth. Otherwise the Harrington--Kechris--Louveau dichotomy reduces E_0 to it, producing a Borel total order on the E_0 quotient. Such an order is impossible: its strict-order sections are E_0-invariant and have coin-flip measure zero or one; the function assigning their measures is itself E_0-invariant and almost everywhere constant. Fubini would make the product measure of the strict order zero or one, whereas symmetry and the nullity of E_0 force it to be one half. Smoothness gives Borel enumerations of components. On each enumerated component, solve the nonempty compact space of finite-palette colourings by recursively choosing the least extendable digit. Extendability is a countable conjunction of finite colouring tests and is Borel. This proves the input, including its list version.

**Theorem 18.3.** Let P be a finite-width Borel partial order and rho:X -> R a Borel nondecreasing map. Assume

    for every x, {y : rho(y)=rho(x) and x incomparable_P y}
    is countable.

Let L(x) be Borel lists contained in a fixed finite palette [n]. If every finite induced list-colouring problem for incomparability(P) is solvable, then there is a Borel proper L-colouring.

In particular every Borel n-chain prescription satisfying FE_n extends to a Borel n-chain partition. AS is not needed.

**Proof.** Compactness gives an abstract L-colouring d. Each D_i=d^{-1}({i}) is a P-chain. Apply Theorem 18.2 to obtain Borel H_i containing D_i, with incomparable pairs of H_i confined to individual rho-fibres. Define Borel restricted lists

    L'(x)=L(x) intersect {i : x in H_i}.

They retain d, so their entire system remains feasible.

Define a Borel partial order Q by

    x<=_Q y iff rho(x)<rho(y), or
                   [rho(x)=rho(y) and x<=_P y].

The relation is transitive and antisymmetric, contains P, and its incomparability graph is exactly

    {(x,y): rho(x)=rho(y) and x incomparable_P y}.

This graph is locally countable by hypothesis. The abstract d is still a proper L'-colouring for Q. Apply the locally countable input to obtain a Borel proper L'-colouring c of incomparability(Q).

If c(x)=c(y)=i and rho(x) differs from rho(y), membership in H_i makes x,y P-comparable by Theorem 18.2. If the rho-values are equal, Q-comparability is precisely P-comparability. Thus c is a proper colouring for P as well, and it respects the original lists L. QED.

This strictly relaxes the countable-to-one assumption in Theorem 17.2. It also subsumes the earlier uniform-substitution theorem of Section 14: compose that quotient map with its realistic real coordinate. The proof does not require distinct fibres to have uniform comparisons in the original order P, and it does not require rho(X) to be Borel.

**Corollary 18.4.** If every rho-fibre is a P-chain, every maximal P-chain is Borel, and the conclusion of Theorem 18.3 holds for arbitrary finite Borel lists.

**Proof.** In Theorem 18.2, equal-value pairs in H are now comparable too. Thus H is a Borel chain containing M; when M is maximal, H=M. Empty within-fibre incomparability also satisfies Theorem 18.3 directly. QED.

### 18.4. The map hypothesis is not automatic

For n>=2 take

    X=R x [n] x R,

with (t,i,u)<_P(s,j,v) if t<s, or if t=s, i=j, and u<v. This is the ordinal sum, over t in R, of n mutually incomparable copies of R. It is Borel and has width n.

There is no nondecreasing real-valued rho with locally countable within-fibre incomparability. For each t, rho must be nonconstant on the block {t} x [n] x R: if it were constant, each point would have uncountably many incomparable neighbours in that rho-fibre. Choose two values u_t<v_t in the image of that block. For t<s, monotonicity on the ordinal sum gives v_t<=u_s. Thus (u_t,v_t), for t in R, would be uncountably many pairwise disjoint nonempty real intervals, impossible by choosing a rational in each.

This example is not a counterexample to prescribed extension. Its incomparability graph is P4-free, and Theorem 20.2 below handles it. It shows that Theorem 18.3 cannot be declared a solution of the unrestricted problem by silently assuming the existence of rho.

## 19. A complete width-three theorem excluding induced P5

### 19.1. Two saturated colours in a bipartite P5-free graph

**Lemma 19.1.** Let G be a bipartite induced-P5-free graph. Let A_0,A_1 be disjoint independent sets, and suppose every point of A_i has a neighbour in A_{1-i}. Then this prescribed two-colouring extends abstractly to all of G. In particular it satisfies FE_2.

**Proof.** First, in a connected bipartite P5-free graph, neighbourhoods of vertices in the same bipartition side are linearly ordered by inclusion. Every shortest path is induced, so the diameter is at most three. Two distinct vertices u,v in the same side therefore have a common neighbour z. If their neighbourhoods were incomparable, choose a adjacent to u but not v and b adjacent to v but not u. Then

    a-u-z-v-b

is an induced P5: a,z,b lie on one bipartition side, u,v on the other, and the two possible cross chords were excluded. This is a contradiction.

Consequently such a component has no induced 2K_2. Let D be a component of G meeting A=A_0 union A_1. The graph induced on D intersect A has no isolated vertices, by the hypothesis. It is connected: two different components would each contain an edge, and their four endpoints would induce a 2K_2. Thus the prescribed proper two-colouring of D intersect A agrees, up to one flip, with either bipartition of D. Choose that flip. Components disjoint from A may be coloured arbitrarily. This gives an abstract extension. QED.

No descriptive selection of components is claimed in this lemma. In the Borel application the already proved two-colour extension theorem provides Borelness.

### 19.2. The width-three result

**Theorem 19.2.** Let P be a Borel partial order of width at most three whose incomparability graph is induced-P5-free. Every prescription by three Borel chains satisfying FE_3 and AS extends to a Borel partition into three chains.

**Proof.** If all prescribed sets are empty, use Borel Dilworth. Otherwise AS implies that all three are nonempty and the width is exactly three.

FE_3 implies that E_0 is finitely 3-coherent as a single seed. By the single-seed puncturing theorem proved in Section 2 of the earlier memo, there is a Borel chain C_0 containing E_0 and meeting every three-antichain. This input follows from Carroy--Miller--Vidnyanszky, Propositions 12 and 16: for G=incomparability(P), finite coherence makes E_0 independent in G*, ordinary Borel Dilworth colours G*, Proposition 12 gives the independent-extension property for maximum antichains, and Proposition 16 gives the required Borel puncturing superset.

AS ensures C_0 is disjoint from E_1 union E_2. Indeed, every point of either set has a prescribed E_0-neighbour in the incomparability graph. Let Y=X minus C_0. This is Borel and has width at most two. The induced graph on Y is still P5-free. Moreover every point of E_1 has a neighbour in E_2 and conversely: restrict any AS witness to these two colours. These points all remain in Y.

Borel Dilworth makes incomparability(P|Y) Borel two-colourable. Lemma 19.1 gives FE_2 for E_1,E_2 on Y. The established Borel two-colour prescription theorem now gives Borel chains C_1,C_2 partitioning Y and extending E_1,E_2. Together with C_0 they form the desired partition. QED.

The proof permits **any** Borel first puncturing chain through E_0; in this class residual coherence is automatic. It neither assumes AD nor tries to derive the false unrestricted implication FE + AS => AD.

**Stronger formulation.** Full AS can be replaced by the two conditions that every point of E_1 union E_2 has an incomparability neighbour in E_0, and that each E_1-point has an E_2-neighbour and conversely. Full FE_3 can be replaced by finite 3-coherence of E_0 alone. The same proof applies when P has width three.

**Corollary 19.3.** At width three, in the P5-free class, finite prescriptions satisfying FE + AS satisfy the manuscript's AD condition. The t=0 case is FE; for t=1 every eligible finite Z is bipartite and inherits the neighbour condition of Lemma 19.1; for t=2 the graph is independent.

**Corollary 19.4.** In any genuine width-three Borel counterexample to FE + AS extension, the complement of **every** Borel first puncturing chain through E_0 contains an induced P5.

**Proof.** If one such complement were P5-free, the second half of Theorem 19.2 would finish the extension. QED.

## 20. AS alone for all finite widths in the P4-free class

### 20.1. Finite lemma

**Lemma 20.1.** Let H be a finite induced-P4-free graph with clique number at most k. Every prescription by k independent sets satisfying AS_k extends to a proper k-colouring. FE is unnecessary.

**Proof.** Use the classical finite cograph decomposition: every P4-free graph with at least two vertices is disconnected or its complement is disconnected. In the latter case H is a complete join of the graphs on the complement-components. The same decomposition proves chi(H)=omega(H), by induction using maximum for disjoint unions and sum for complete joins.

Induct on the number of vertices for the prescribed assertion. If there are no prescribed points, use the unprescribed colouring just noted.

If H is disconnected, each component containing a prescribed point inherits AS_k, since each witnessing clique lies in that component. Apply induction there. Components without prescribed points use ordinary k-colourings.

Otherwise write H as the complete join of nonempty smaller graphs H_j. Each nonempty prescribed colour class is contained in a single H_j, by independence. Let J_j be the set of its assigned colour labels and let k_j=|J_j|. One full AS clique gives omega(H_j)>=k_j. Since

    sum_j omega(H_j)=omega(H)<=k=sum_j k_j,

all these inequalities are equalities; in particular every k_j is positive. Restricting AS witnesses to J_j gives AS_{k_j} inside H_j. Apply induction in each H_j with its own labels, then combine the disjoint palettes across the complete join. QED.

The finite cograph decomposition is standard; see Corneil--Lerchs--Stewart Burlingham (1981), or the definition/equivalence in Oxley--Singh (2023). It is not asserted here as a Borel decomposition theorem for an uncountable graph.

### 20.2. Borel theorem

**Theorem 20.2.** For every finite n, if P is a Borel partial order of width at most n and its incomparability graph is induced-P4-free, every prescription by n Borel chains satisfying AS extends to a Borel n-chain partition. FE need not be assumed.

**Proof.** For any finite F, adjoin one AS witness for every prescribed point already in F. The enlarged set is still finite, and every newly adjoined prescribed point lies in the very witness that introduced it. Therefore the induced finite prescription satisfies AS. Lemma 20.1 gives a colouring extending it, and restriction to F proves FE.

More generally, let I be any nonempty subset of the labels, and let W contain every E_i for i in I, avoid the other prescribed sets, and have width at most |I|. Restricting original AS witnesses to I gives AS_{|I|} on W. The same finite enlargement argument proves the full FE condition for these remaining labelled sets, even when they are infinite.

Now remove one Borel chain at a time. At a stage with m labels, the preceding paragraph makes the chosen seed finitely m-coherent. Apply the single-seed puncturing theorem. AS prevents the removed chain from meeting other remaining prescribed sets; the width drops to m-1 and AS restricts to the remaining labels. Repeat until no points remain. Every step is Borel and retains all required labels. If all original prescribed sets were empty, ordinary Borel Dilworth suffices instead. QED.

This avoids the finiteness restriction in the manuscript's AD definition: the finite enlargement argument proves the needed coherence directly for arbitrary Borel prescribed chains.

## 21. A P5-free width-four obstruction to tail preservation

This is a counterexample to AD and to arbitrary first-chain deletion, **not** a counterexample to Borel extension. Being finite and satisfying FE, it has a prescribed extension.

### 21.1. The nine-point order

Let

    X={s,t,a,b,c,d,e,f,x}.

Take the reflexive transitive closure of the strict generating comparisons

    a<b, a<d, e<b, e<f,
    c<d, c<x, s<x, x<f, x<t.

There are no other generators. The transitive closure adds precisely

    c<f, c<t, s<f, s<t.

This relation is acyclic: {s,a,c,e} is the lower level, {x} the middle level, and {t,b,d,f} the upper level. Prescribe

    E_0={s,t}, E_1={a,b}, E_2={c,d}, E_3={e,f}.

The two four-antichains

    {s,a,c,e},  {t,b,d,f}

witness AS for all eight prescribed points. The partition

    {s,x,t}, {a,b}, {c,d}, {e,f}

is a prescribed four-chain partition. Hence FE_4 holds and the width is exactly four.

However put

    Z=X minus E_0={a,b,c,d,e,f,x}.

Its width is three, witnessed above by restriction of the four-antichains and bounded above by the chain partition

    {a,d}, {c,x,f}, {e,b}.

The point x cannot join any remaining prescribed class: it is incomparable with a in E_1, d in E_2, and e in E_3. Thus the tail prescription E_1,E_2,E_3 on Z has no extension. This is exactly failure of AD at t=1.

Moreover the chain C_0=E_0 itself punctures every four-antichain, since its complement has width three. It contains the first seed, avoids the other anchors, and lowers the width, but still destroys residual FE.

### 21.2. Proof that the incomparability graph is P5-free

Write N(v) for incomparability neighbours in the nine-point graph. The vertices a,b,d,e have degree six and therefore only two non-neighbours; they cannot be endpoints of an induced P5, whose endpoints have three non-neighbours among the other four vertices.

The three non-neighbours of s are x,f,t. If s were an endpoint of an induced P5, these three points would all be on that path, together with its unique neighbour v there. But x has no neighbours among s,f,t, so it is either isolated on these five points or is a second leaf sharing v with s. Neither is a P5. The identical argument for t uses its three non-neighbours s,c,x. Thus s,t cannot be endpoints either.

The endpoints must therefore be chosen from c,f,x. Their neighbourhoods are

    N(c)={s,a,b,e},
    N(f)={t,a,b,d},
    N(x)={a,b,d,e}.

For endpoints c,f, their common neighbours a,b cannot be on an induced path between them. The middle vertex must be x. To be adjacent to x, the neighbour of c must then be e and that of f must be d. The only candidate path is c-e-x-d-f, but e-d is a chord.

For endpoints c,x, their respective path-neighbours must be s,d. The middle vertex must be f or t, neither of which is adjacent to s. For endpoints f,x, their respective neighbours must be t,e; the middle vertex must be c or s, neither adjacent to t. Every case is impossible. The graph is induced-P5-free. QED.

The accompanying standard-library script `research/verify_p5_counterexample.py` independently verifies all 126 five-vertex subsets, the exact widths, AS, FE_4, puncturing, and failure of residual extension. The seven-point residual has exactly six unprescribed three-colourings and no prescribed one. The proof above does not rely on unexplained computational enumeration.

### 21.3. All n>=4 and locked active templates

For n>4, adjoin n-4 two-element chains, each incomparable with the entire old order and with every other new chain. Prescribe each new chain as an additional colour class. The width becomes n, the preceding prescribed partition extends, and AS follows by adding one point from each new chain to each old four-antichain. Both points of each new chain are covered by choosing its appropriate endpoint in the lower or upper witnessing antichain.

The incomparability graph remains P5-free. Every newly added vertex is nonadjacent only to its own chain-mate, whereas every vertex of a P5 has at least two non-neighbours on that path. An induced P5 cannot use a new vertex, and none existed before. After deleting E_0, the width is n-1, while x still cannot join any remaining prescribed colour. Thus AD fails for all n>=4 in this class.

For arbitrary r>=1, prepend r-1 n-antichain layers by ordinal sum and place the point with label i in E_i. Each prescribed block now has size r+1. The r-1 new layers together with the two old extended witnessing antichains yield r+1 disjoint n-antichains. Thus alpha_r=rn and alpha_{r+1}=(r+1)n. On the set S of all prescribed points the E_i form a simultaneously saturated partition, and adding the sole outside point x to colour 0 preserves both norms. Hence this is a locked active template in the manuscript's sense.

P5-freeness is unchanged because ordinal sum makes the incomparability graph a disjoint union with the new complete graphs. Deleting the whole enlarged E_0 still leaves width n-1 and still prevents x from joining any remaining prescribed class. The tail obstruction therefore persists for every n>=4 and every r>=1.

## 22. What remains and what not to infer

- Theorems 18.3, 19.2, and 20.2 are complete positive theorems under their stated hypotheses.
- Theorem 18.2 removes the **countability of fibres** from the earlier hull lemma. The remaining hypothesis in the full colouring theorem is **local countability of within-fibre incomparability**, not cardinality of the fibre.
- The example in Section 18.4 proves that a suitable real map does not exist for every finite-width Borel order. It is not a negative solution of the original prescription problem.
- The nine-point example proves that the P5-free width-three tail argument cannot simply be iterated to width four. It does not refute Borel extension at width four.
- For the unrestricted width-three problem, a successful first-chain construction must either preserve all residual labelled path constraints or arrange a residual class in which such constraints automatically agree. Excluding induced P5 gives one fully proved instance, not a replacement assumption for the original question.
- For the general real-fibre approach, the construction localizes same-colour conflicts to fibres. Arbitrary uncountable-fibre instances still require a method of simultaneous Borel selection respecting the restricted lists. Such a method is not proved here. No assertion about it is used in the complete theorems above.

The main manuscript and original working memo are unchanged; the new theorems and their limitations are isolated in this continuation for further review.

## Verified external inputs

- R. Carroy, B. D. Miller, Z. Vidnyanszky, *On the existence of small antichains for definable quasi-orders*, Journal of Mathematical Logic 21 (2021), no. 2, 2150005. Theorem 1 and Propositions 12 and 16 were checked in the authors' PDF: https://glimmeffros.github.io/publications/dilworth.pdf . Proposition 16 explicitly permits a Borel independent seed.
- L. Harrington, D. Marker, S. Shelah, *Borel orderings*, Transactions of the AMS 310 (1988), 293-302. The Borel-linear-order embedding into lexicographic 2^alpha for countable alpha is the input to Lemma 18.1. Author archive: https://shelah.logic.at/papers/215/ .
- D. G. Corneil, H. Lerchs, L. Stewart Burlingham, *Complement reducible graphs*, Discrete Applied Mathematics 3 (1981), 163-174; and J. Oxley, J. Singh, *Generalizing Cographs to 2-Cographs*, Electronic Journal of Combinatorics 30 (2023), no. 1, P1.1, for the finite P4-free/cograph decomposition. The latter equivalence is stated explicitly at https://www.combinatorics.org/ojs/index.php/eljc/article/view/v30i1p1 .
- The single-seed and locally countable list-colouring inputs are also proved, with their hypotheses, in Sections 2 and 8 of `Working_Memo.md`. They are previous project results, not new claims from this continuation.
