#Versión 1.0 (para probar) 17:07 24/01
#
#
# Hacer las tablas de multiplicar del 1 al 10
for i in range(1, 11):
    # Range(m, n) porque la función va desde m hasta n-1
    print("Tabla del " + str(i)+"\n-----------")
    for j in range(1, 11):
        resultado = i*j
        print(str(j) + " por " + str(i) + " es " + str(resultado))
    print("\n")
