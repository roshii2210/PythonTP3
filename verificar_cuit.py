import re

def VerificarCuit(cuil):

    return re.match(r'\d{2}-\d{8}-\d{1}', cuil)

