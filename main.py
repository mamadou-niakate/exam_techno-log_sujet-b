from Jeu import Jeu
from CodeRayon import  CodeRayon

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    code_rayon = CodeRayon("FRA.12.42.2021")
    jeu = Jeu("console", "sport", 200, "cool description", code_rayon)

    print(jeu.is_jeu_valide())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
