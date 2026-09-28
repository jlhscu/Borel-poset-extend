"""Finite certificates for the P5-free chain-prescription research note.

Uses only the Python standard library. Run with Python 3.10 or newer.
These checks audit the finite examples; the Borel theorems are proved
mathematically in the accompanying note, not inferred from this script.
"""
from itertools import combinations, product
from typing import Iterable

VERTICES = ("s", "t", "a", "b", "c", "d", "e", "f", "x")
GENERATORS = (
    ("a", "b"), ("a", "d"), ("e", "b"), ("e", "f"),
    ("c", "d"), ("c", "x"), ("s", "x"),
    ("x", "f"), ("x", "t"),
)
PRESCRIPTION = (("s", "t"), ("a", "b"), ("c", "d"), ("e", "f"))


def transitive_closure(vertices: tuple[str, ...],
                       generators: Iterable[tuple[str, str]]) -> set[tuple[str, str]]:
    relation = set(generators)
    for z in vertices:
        relation.update((x, y) for x in vertices for y in vertices
                        if (x, z) in relation and (z, y) in relation)
    assert all((x, x) not in relation for x in vertices), "Strict cycle"
    assert all((x, z) in relation
               for x, y in relation for y2, z in relation if y == y2)
    return relation


def verify() -> None:
    relation = transitive_closure(VERTICES, GENERATORS)

    def comparable(x: str, y: str) -> bool:
        return x == y or (x, y) in relation or (y, x) in relation

    def adjacent(x: str, y: str) -> bool:
        return x != y and not comparable(x, y)

    def is_chain(points: Iterable[str]) -> bool:
        return all(comparable(x, y) for x, y in combinations(points, 2))

    def is_antichain(points: Iterable[str]) -> bool:
        return all(adjacent(x, y) for x, y in combinations(points, 2))

    def width(points: tuple[str, ...]) -> int:
        return max((len(q) for k in range(len(points) + 1)
                    for q in combinations(points, k) if is_antichain(q)), default=0)

    def induced_p5(points: tuple[str, ...]) -> list[tuple[str, ...]]:
        failures = []
        for q in combinations(points, 5):
            neighbours = {x: {y for y in q if adjacent(x, y)} for x in q}
            if sorted(map(len, neighbours.values())) != [1, 1, 2, 2, 2]:
                continue
            seen, pending = {q[0]}, [q[0]]
            while pending:
                for y in neighbours[pending.pop()] - seen:
                    seen.add(y)
                    pending.append(y)
            if len(seen) == 5:
                failures.append(q)
        return failures

    lower, upper = ("s", "a", "c", "e"), ("t", "b", "d", "f")
    assert is_antichain(lower) and is_antichain(upper)
    assert all(is_chain(E) for E in PRESCRIPTION)
    assert len(set().union(*map(set, PRESCRIPTION))) == 8
    for E in PRESCRIPTION:
        for p in E:
            witnesses = [q for q in (lower, upper)
                         if p in q and all(len(set(q) & set(F)) == 1
                                          for F in PRESCRIPTION)]
            assert witnesses, ("Missing AS witness", p)

    partition = (("s", "x", "t"), ("a", "b"), ("c", "d"), ("e", "f"))
    assert all(is_chain(C) for C in partition)
    assert sorted(p for C in partition for p in C) == sorted(VERTICES)
    assert all(set(E) <= set(C) for E, C in zip(PRESCRIPTION, partition))
    assert width(VERTICES) == 4
    assert not induced_p5(VERTICES)

    residual = tuple(p for p in VERTICES if p not in {"s", "t"})
    assert width(residual) == 3
    residual_partition = (("a", "d"), ("c", "x", "f"), ("e", "b"))
    assert all(is_chain(C) for C in residual_partition)
    assert sorted(p for C in residual_partition for p in C) == sorted(residual)
    assert not induced_p5(residual)
    assert all(not is_chain((*E, "x")) for E in PRESCRIPTION[1:])
    assert all(set(q) & {"s", "t"} for q in combinations(VERTICES, 4)
               if is_antichain(q)), "The bad puncturing chain misses a maximum antichain"

    # Exhaust all three-colour assignments on the residual graph.
    count, extends, coherent_seeds = 0, 0, [False, False, False]
    for colours in product(range(3), repeat=len(residual)):
        d = dict(zip(residual, colours))
        if any(d[x] == d[y] and adjacent(x, y)
               for x, y in combinations(residual, 2)):
            continue
        count += 1
        extends += all(d[p] == i for i, E in enumerate(PRESCRIPTION[1:]) for p in E)
        for i, E in enumerate(PRESCRIPTION[1:]):
            coherent_seeds[i] |= len({d[p] for p in E}) == 1
    assert count == 6 and extends == 0 and not any(coherent_seeds)

    print("PASS: strict partial order, exact widths 4 and 3, AS, and FE_4.")
    print("PASS: all 126 five-vertex subsets of the nine-point graph are P5-free.")
    print("PASS: all 21 five-vertex subsets of the seven-point residual are P5-free.")
    print("PASS: the chain {s,t} punctures every maximum four-antichain.")
    print("PASS: the residual has six unprescribed 3-colourings, no prescribed one.")
    print("No minimality claim is inferred from these checks.")


if __name__ == "__main__":
    verify()
