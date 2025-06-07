import math
import random
from typing import List, Tuple, Callable

# ------------Définitions------------
# Une K est une paire (input_list, expected_output)
KType = Tuple[List[float], float]

# Quelques Black-box fonctions
black_box = {
    # Liste des fonctions mathématique
    "product": lambda x: math.prod(x),
    "sum": lambda x: sum(x),
    "sum_squares_minus_prod": lambda x: sum(i**2 for i in x) - math.prod(x),
    "complex_mix": lambda x: abs(sum([math.cos(math.pi * xi) + 1j * math.sin(math.pi * xi) for xi in x]))**2 - math.prod([math.sin(xi) for xi in x]),
}

# Générateur de données
def generate_k(bb: Callable, n: int = 5, size_range = (1, 4), val_range = (-5, 5)) -> List[KType]:
    print('\n--- GENERATION DES EXEMPLES K ---')
    print(f"Fonction black-box utilisée: {bb.__name__ if hasattr(bb, '__name__') else 'lambda'}")
    print(f"Génération de {n} exemples avec {size_range[0]} à {size_range[1]} valeurs entre {val_range[0]} et {val_range[1]}")
    
    Ks = []
    for i in range(n):
        size = random.randint(*size_range)
        xs = [random.uniform(*val_range) for _ in range(size)]
        r = bb(xs)
        Ks.append((xs, r))
        print(f"K{i+1}: Inputs = {[round(x, 2) for x in xs]}, Output = {round(r, 4)}")
    return Ks

# Simulation de Black-Box candidate
def candidate_functions() -> List[Callable[[List[float]], float]]:
    print('\n--- GENERATION DES FONCTIONS CANDIDATES ---')
    candidates = [
        ("Somme", lambda x: sum(x)),
        ("Produit", lambda x: math.prod(x)),
        ("Somme des carrés", lambda x: sum([i**2 for i in x])),
        ("Somme carrés - produit", lambda x: sum([i**2 for i in x]) - math.prod(x)),
        ("Somme des valeurs absolues", lambda x: sum([abs(i) for i in x])),
        ("Somme des cubes", lambda x: sum([i**3 for i in x])),
        ("Tous zéros?", lambda x: 1 if all(v == 0 for v in x) else 0)
    ]
    
    print(f"{len(candidates)} fonctions candidates générées:")
    for i, (name, _) in enumerate(candidates):
        print(f"{i}: {name}")
    
    # On retourne seulement les fonctions (sans les noms)
    return [func for _, func in candidates]

# Evalutaion
def evaluate(func: Callable, Ks: List[KType], tolerance=1e-3) -> float:
    correct = 0
    for inputs, expected in Ks:
        try:
            res = func(inputs)
            if abs(res - expected) <= tolerance:
                correct += 1
        except Exception as e:
            continue
    return correct / len(Ks)

# ---- PIPELINE DE TEST ----
def run_blackbox_test():
    print("\n=== DEBUT DU TEST BLACK-BOX ===")
    
    print("\n--- PHASE: SELECTION DE LA BLACK-BOX ---")
    true_bb_name = random.choice(list(black_box.keys()))
    true_bb = black_box[true_bb_name]
    print(f"Black-box sélectionnée: '{true_bb_name}'")

    print("\n--- PHASE: GENERATION DE K ---")
    Ks = generate_k(true_bb, n=10)
    print(f"\n{len(Ks)} exemples K générés")

    print("\n--- PHASE: TEST DES FONCTIONS CANDIDATES ---")
    candidates = candidate_functions()
    scores = []
    for i, f in enumerate(candidates):
        acc = evaluate(f, Ks)
        scores.append((i, acc))
        print(f"Candidate {i}: {round(acc*100, 2)}% de correspondance")

    best = max(scores, key=lambda x: x[1])
    print(f"\n--- RESULTATS FINAUX ---")
    print(f"Meilleur candidat: Fonction {best[0]} avec {round(best[1]*100, 2)}% de précision")
    print("=== FIN DU TEST ===")

if __name__ == '__main__':
    run_blackbox_test()