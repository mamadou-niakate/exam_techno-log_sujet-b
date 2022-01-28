from Jeu import Jeu
from CodeRayon import CodeRayon


def test_jeu():
    code_rayon = CodeRayon("FRA.12.42.2024")
    jeu = Jeu("console", "sport", 200, "cool description", code_rayon)
    assert jeu.is_jeu_valide() == False
