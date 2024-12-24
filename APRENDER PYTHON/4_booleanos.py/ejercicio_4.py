es_mayor: bool = True
es_par: bool = False

resultado_and: bool = es_mayor and es_par
resultado_or: bool = es_mayor or es_par
resultado_not: bool = not es_par

print(f"El resultado de 'es_mayor and es_par' es: {resultado_and}")
print(f"El resultado de 'es_mayor or es_par' es: {resultado_or}")
print(f"El resultado de 'not es_par' es: {resultado_not}")
