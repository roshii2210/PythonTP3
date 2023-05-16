from verificar_cuit import VerificarCuit

cuil = "30-56225215-7"

if VerificarCuit(cuil):
    print(f"CUIT/CUIL: {cuil}, \033[92m (valido) \033[0m")
else:
    print(f"CUIT/CUIL: {cuil}, \033[91m (no valido) \033[0m")