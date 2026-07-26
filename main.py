
class Bookshelf:
    def __init__(self):
        self.soni = 0

    def kitob_qosh(self):
        self.soni += 1
        print("1 ta kitob qo'shildi.")

    def korsat(self):
        print("Javondagi kitoblar soni 'agar siz javon.kitob_qosh dan copy qlb qoshsaiz kitob soni oshadi':", self.soni)


javon = Bookshelf()

javon.kitob_qosh()
javon.kitob_qosh()
javon.korsat()