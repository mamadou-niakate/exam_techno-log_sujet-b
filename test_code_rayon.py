from CodeRayon import CodeRayon


def test_code_rayon():
    code_rayon = CodeRayon("FRA.12.42.2021")

    assert code_rayon.is_code_rayon_valide()
