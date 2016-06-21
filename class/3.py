class HousePark:
	lastname = "Park"
	def __init__(self, name):
		self.fullname = self.lastname + name

	def travel(self, where):
		print("%s, Go to %s." % (self.fullname, where))

	def love(self, other):
		print('%s, %s fall in love' % (self.fullname, other.fullname))

	def fight(self, other):
		print("%s, %s are fight" % (self.fullname, other.fullname))

	def __add__(self, other):
		print('%s, %s are married' % (self.fullname, other.fullname))

	def __sub__(self, other):
		print('%s, %s are divoice' % (self.fullname, other.fullname))


pey = HousePark("Jimmy")
# pey.setname("Jimmy")
pey.travel("Busan")
# print(pey.fullname)


class HouseKim(HousePark):
	lastname = "Kim"
	def travel(self, where, *day):
		if day:
			pass
		else:
			day = 1
		print("%s, Go to %s and %ddays" % (self.fullname, where, day))


juliet = HouseKim("juliet")	
juliet.travel("Dokdo")
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet