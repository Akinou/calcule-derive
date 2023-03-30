def f(x):
    """Définition de la fonction à dériver"""
    return x ** 2

def derivee(f, x, h=1e-6):
    """Calcule la dérivée de la fonction f en x à l'aide de la méthode de différenciation numérique"""
    return (f(x + h) - f(x - h)) / (2 * h)

# Exemple d'utilisation :
x = 2
derivee_f = derivee(f, x)

print(f"La dérivée de la fonction f(x) = x^2 en x = {x} est {derivee_f}")
