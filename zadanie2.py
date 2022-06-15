class Doctor():
    def __init__(self, name, pat, sick):
        self.name = name
        self.pat = pat
        self.sick = sick
    def info(self):
        print('Doctor', self.name, ',', self.pat)
    def difference(self):
        print(self.pat - self.sick)
    def say_clever_phrases():
        a = ["The puppet is dead, However, "
             "if he wasn't completely dead"
             " it would be a sure sign that he was still alive."
              "The puppet is still alive."
             "However, if he were not alive"
             " it would be a sure sign that he was actually dead."]
        s = choice(a)
        print(s)

    def treat_patients(self, nameP):
        if len(nameP) % 2 == self.pat % 2:
            print('True')
            self.pat += 1
        else:
            print('False')