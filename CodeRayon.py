class CodeRayon:
    def __init__(self, code_rayon):
        self.code_rayon = code_rayon

    def is_code_rayon_valide(self):
        code_rayon_list = self.code_rayon.split('.')
        if len(code_rayon_list) < 4 or len(code_rayon_list) > 4:
            return False
        else:
            letters = code_rayon_list[0]
            numEntreprise = code_rayon_list[1]
            numArticle = code_rayon_list[2]
            annee = code_rayon_list[3]
            if not letters.isalpha() or (len(letters) < 3 or len(letters) > 3):
                return False
            if not numEntreprise.isnumeric() or (len(numEntreprise) < 2 or len(numEntreprise) > 2):
                return False
            if not numArticle.isnumeric() or (len(numArticle) < 2 or len(numArticle) > 2):
                return False
            if not annee.isnumeric() or int(annee) > 2022:
                return False
        return True
