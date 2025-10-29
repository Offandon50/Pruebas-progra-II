import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from cuenta import Cuenta

# Test 1
def test_saldo_inicial_cero():
    c = Cuenta()
    assert c.saldo == 0

""" PRUEBA FALLADA:
======================================= test session starts ========================================
[...]
===================================== short test summary info ====================================== 
ERROR tests/test_cuenta_pytest.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
========================================= 1 error in 0.37s =========================================
"""

# Test 2
def test_ingreso_suma_al_saldo():
    c = Cuenta()
    c.ingresar(100)
    assert c.saldo == 100
    c.ingresar(50)
    assert c.saldo == 150

""" PRUEBA FALLADA:
======================================= test session starts ========================================
[...] """ """
===================================== short test summary info ====================================== 
FAILED tests/test_cuenta_pytest.py::test_ingreso_suma_al_saldo - AttributeError: 'Cuenta' object has no attribute 'ingresar'
=================================== 1 failed, 1 passed in 0.30s ====================================

PRUEBA ACERTADA:
======================================= test session starts ========================================
[...]                                                                           

tests/test_cuenta_pytest.py::test_saldo_inicial_cero PASSED                                   [ 50%] 
tests/test_cuenta_pytest.py::test_ingreso_suma_al_saldo PASSED                                [100%] 

======================================== 2 passed in 0.08s ========================================= 
"""
# Test 3
def test_retirada_resta_del_saldo():
    c = Cuenta()
    c.ingresar(200)
    c.retirar(70)
    assert c.saldo == 130

""" PRUEBA FALLADA:
[...]
========================== short test summary info =========================== 
FAILED tests/test_cuenta_pytest.py::test_retirada_resta_del_saldo - AttributeError: 'Cuenta' object has no attribute 'retirar'
======================== 1 failed, 2 passed in 0.35s =========================

PRUEBA ACERTADA:
[...]

tests/test_cuenta_pytest.py::test_saldo_inicial_cero PASSED             [ 33%] 
tests/test_cuenta_pytest.py::test_ingreso_suma_al_saldo PASSED          [ 66%] 
tests/test_cuenta_pytest.py::test_retirada_resta_del_saldo PASSED       [100%]

============================= 3 passed in 0.11s ==============================
"""

class Cuenta:
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo
    
    def ingresar(self, cuantia):
        self._saldo += cuantia
    
    def retirar(self, cuantia):
        if self._saldo < cuantia:
            raise ValueError("Fondos insuficientes")
        else:
            self._saldo -= cuantia