### FORMULARIO - proprietà integrali def###
print("se a<b<c\nintegrale[a][c](f(x) dx)=integrale[a][b](f(x) dx)+integrale[b][c](f(x) dx)\nintegrale[a][b](f(x)+g(x) dx)=integrale[a][b](f(x) dx)+integrale[a][b](g(x) dx)\nintegrale[a][b](k*f(x))=k*integrale[a][b](f(x))\nse f(x)<=g(x)\nintegrale[a][b](f(x) dx)<=integrale[a][b](g(x) dx)\n|integrale[a][b](f(x) dx)|=integrale[a][b](|f(x)| dx)\nintegrale[a][b](k dx)=k*(b-a)")

### FORMULARIO - calcolo aree integrali def###
print("integrale[a][b](f(x) dx)=F(b)[a][b]=F(b)-F(a)\nper calcolare l'area compresa tra una curva e l'asse y si porta nella forma x=f(y)\nintegrale[a][b](f(y) dy)")

### FORMULARIO - calcolo volumi integrali def###
print("rotazione intorno all'asse x\nV=pi*integrale[a][b](f(x)^2 dx)\nrotazione intorno all'asse y\nV=pi*integrale[a][b](f(y)^2 dy)\ngusci cilindrici\nV=2pi*integrale[a][b](x*f(x) dx)")

### FORMULARIO - calcolo integrali impropri###
print("integrale[a][b](f(x) dx)=lim[z to b^-]integrale[a][z](f(x) dx)\nintegrale[a][b](f(x) dx)=lim[z to a^+]integrale[z][b](f(x) dx)\nintegrale[a][inf](f(x) dx)=lim[z to inf]integrale[a][z](f(x) dx)")

### FORMULARIO - integrali in fisica###
print("la velocità e l'integrale della posizione\nl'accelerazione è l'integrale della velocità\nil lavoro è l'integrale della forza\nla quantità di carica è l'integrale dell'intensità")
