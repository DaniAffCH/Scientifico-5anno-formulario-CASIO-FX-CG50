### FORMULARIO - potenze di x ###
print("D k = 0\nD x = 1\nD x^a = ax^(a-1)\nD sqrt(x) = 1/(2*sqrt(x)) con x > 0")

### FORMULARIO - funzioni logaritmiche ed esponenziali ###
print("D a^x = a^x * ln(a) con a > 0\ne^x = e^x\nD log[a](x) = 1/x * log[a](e)\nD ln(x) = 1/x")

### FORMULARIO - funzioni goniometriche ###
print("D sin(x) = cos(x)\nD cos(x) = -sin(x)\nD tan(x) = 1/(cos^2(x)) = 1 + tan^2(x)\n D cot(x) = - 1/(sin^2(x)) = -(1 + cot^2(x))")

### FORMULARIO - inverse delle funzioni goniometriche ###
print("D arctan(x) = 1/(1 + x^2 \nD arccot(x) = -1/(1 + x^2)\nD arcsin(x) = 1/(sqrt(1 - x^2))\n D arccos(x) = -1/(sqrt(1 - x^2))")

### FORMULARIO - regole di derivazione ###
print("D[k * f(x)] = k * f'(x)\nD[f(x) + g(x) = f'(x) + g'(x)\nD[f(x) * g(x)] = f'(x) * g(x) + f(x) * g'(x)\nD 1/f(x) = - f'(x) / f''(x)\nD f(x)/g(x) = [f'(x)*g(x) - f(x)*g'(x)] / [g^2(x)\nD[f(g(x))] = f'(g(x)) * g'(x)\nD[f(x)]^[g(x)] = [f(x)]^[g(x)] * [g'(x)*ln_f(x) + [g(x)*f'(x)] / f(x) ]\nD[f^-1(y)] = 1 / f'(x)")

### EQ. RETTA TANGENTE A f nel punto (xo; f(xo)) ###
print("EQ. RETTA TANGENTE A f nel punto (xo; f(xo))\ny - f(xo) = D[xo] * (x - xo)")

### DERIVATA ' QUANDO NON ESISTE ###
print("DERIVATA PRIMA - punto stazionario: x = c  se f'(c) = 0\n- no derivabile:\n- punto angoloso: se lim[x -> Xo-] != lim[x -> Xo+]\n- flesso a tan verticale: se (lim[x -> Xo-] e lim[x -> Xo+]) danno entrambi + o - infinito\n- cuspide: se lim[x -> Xo-] = + infinito e lim[x -> Xo+] = - infinito o viceversa")

### DERIVATA '' QUANDO NON ESISTE ###
print("DERIVATA SECONDA:\n- si annulla quando cambia la concavità (∩) o convessità (U)")