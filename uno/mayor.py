def mayor_v1(numero1:int, numero2:int)->int:
    """
        Compara 2 numeros enteros y regresa el numero
        mayor
        Parameters:
            numero1 (int): Numero1 a comparar
            numero2 (int): Numero2 a comparar
        Returns:
            mayor (int) : Valor mayor
    """
    if numero1 > numero2:
        return numero1
    if numero1 < numero2:
        return numero2
    else:
        return None

def test_mayor_v1()->None:
    """
        Test method mayor_v1()
    """
    assert mayor_v1(1, 2) == 2
    assert mayor_v1(2, 1) == 2
    assert mayor_v1(2, 2) is None
    assert mayor_v1(-2, -1) == -1
    assert mayor_v1(-1, -2) == -1
    assert mayor_v1(-1, -1) is None
