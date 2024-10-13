import pytest
from molinoindustrial import MolinoIndustrial

@pytest.fixture
def molino():
    return MolinoIndustrial()

def test_encender_molino(molino):
    molino.encender()
    assert molino.esta_encendido() == True, "El molino debería estar encendido después de llamar a encender()"

def test_apagar_molino(molino):
    molino.encender()
    molino.apagar()
    assert molino.esta_encendido() == False, "El molino debería estar apagado después de llamar a apagar()"

def test_moler_molino_encendido(molino):
    molino.encender()
    resultado = molino.moler()
    assert resultado == "Molino está moliendo", "El molino debería moler cuando está encendido"
    assert molino.produccion == 1, "La producción debería incrementarse cuando el molino está moliendo"

def test_moler_molino_apagado(molino):
    resultado = molino.moler()
    assert resultado == "Molino apagado, no puede moler", "El molino no debería moler cuando está apagado"
    assert molino.produccion == 0, "La producción no debería incrementarse cuando el molino está apagado"

