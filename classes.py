from queue import Empty

class choice:
    last = False
    prompt = ""
    questions = []
    def __init__(self, txt = "", q = [], last = False):
        self.questions = q
        self.prompt = txt
        self.last = last

class question:
    txt = ""
    nextChoice = 0
    req = 0
    def __init__(self, txt = "", nc = -1, req = 0):
        self.txt = txt
        self.nextChoice = nc
        self.req = req