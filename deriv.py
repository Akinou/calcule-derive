
def u(x):
    """Définition de la fonction u"""
    return x ** 2

def v(x):
    """Définition de la fonction v"""
    return 3 * x

def produit(u, v):
    """Définition du produit u*v"""
    return u * v

def quotient(u, v):
    """Définition du quotient u/v"""
    return u / v

def derivee_produit(u, v, x):
    """Calcule la dérivée du produit u*v en x"""
    return u(x) * v.deriv()(x) + v(x) * u.deriv()(x)

def derivee_quotient(u, v, x):
    """Calcule la dérivée du quotient u/v en x"""
    return (v(x) * u.deriv()(x) - u(x) * v.deriv()(x)) / v(x) ** 2

# Exemple d'utilisation :
x = 2
f = lambda x: produit(u, v)(x) / quotient(u, v)(x)
derivee_f = f.deriv()(x)

print(f"La dérivée de la fonction f(x) = u(x)*v(x) / (u(x)/v(x)) en x = {x} est {derivee_f}")
