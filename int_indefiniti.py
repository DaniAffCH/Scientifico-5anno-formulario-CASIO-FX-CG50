### FORMULARIO - proprietà linearità integrali ###
print("integrale(f(x)+g(x))=integrale(f(x))+integrale(g(x))\nintegrale(k*f(x))=k*integrale(f(x))")

### FORMULARIO - metodo sostituzione ###
print("integrale(f(x)dx)=integrale(f(g(t))*g'(t)dt) con x=g(t) e dx=g'(t)dt")

### FORMULARIO - metodo per parti ###
print("integrale(f(x)g'(x)dx)=f(x)*g(x)-integrale(f'(x)*g(x)dx)")

### FORMULARIO - integrali immediati ###
print("integrale(x^a dx)=(x^(a+1))/(a+1) con a=!1\nintegrale(1/x dx)=ln(|x|)\nintegrale(e^x dx)=e^x\nintegrale(a^x dx)=a^x/ln(a)\nintegrale(sin(x) dx)=-cos(x)\nintegrale(cos(x) dx)=sin(x)\nintegrale(1/cos^2(x) dx)=tan(x)\nintegrale(1/sin^2(x) dx)=-cot(x)\nintegrale(1/sqrt(1-x^2) dx)=arcsin(x)\nintegrale(1/(1+x^2) dx)=arctan(x)")

### FORMULARIO - integrali con funzioni composte ###
print("integrale((f(x)^a)*f'(x) dx)=(f(x)^(a+1))/(a+1) con a=!1\nintegrale(f'(x)/f(x) dx)=ln(|f(x)|)\nintegrale(f'(x)*e^f(x) dx)=e^f(x)\nintegrale(f'(x)*a^f(x) dx)=a^f(x)/ln(a)\nintegrale(f'(x)*sin(f(x)) dx)=-cos(f(x))\nintegrale(f'(x)*cos(f(x)) dx)=sin(f(x))\nintegrale(f'(x)/cos^2(f(x)) dx)=tan(f(x))\nintegrale(f'(x)/sin^2(f(x)) dx)=-cot(f(x))\nintegrale(f'(x)/sqrt(1-f(x)^2) dx)=arcsin(f(x))\nintegrale(f'(x)/(1+f(x)^2) dx)=arctan(f(x))")

### FORMULARIO - integrazione funzioni fratte###
print("grado num< ed è la derivata del den\nintegrale(f'(x)/f(x) dx)=ln(|f(x)|)\ngrado num< con den di primo grado\nintegrale(1/(ax+b) dx)=1/a*ln(|ax+b|)")

### FORMULARIO - integrazione funzioni fratte due##
print("grado num< con denominatore di secondo grado\n delta>0 cerco A e B\n(px+q)/(ax^2+bx+c)=A/(a(x-x[1]))+B/(x-x[2])\ndelta=0 cerco A e B\n(px+q)/(ax^2+bx+c)=A/(a(x-x[1]))+B/(x-x[1])^2\ndelta<0 con p=0\nintegrale(1/(ax^2+bx+c) dx) trasformato in integrale(f'(x)/(k^2+f(x)^2) dx)=1/k*arctan(f(x)/k)\ndelta<0 con p=!0\n(px+q)/(ax^2+bx+c) trasformato in r*integrale((2ax+b)/(ax^2+bx+c) dx)+s*integrale(1/(ax^2+bx+c) dx)")
