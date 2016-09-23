class AngkaTerbilang():
	"""
	kelas ini digunakan untuk mengubah dari angka ke kalimat terbilang

	@contoh: 60 -> enam puluh
			59 -> lima puluh sembilan

	@pembatasan: hanya untuk angka 1 - 60
	"""
	def __init__(self, angka):
		# angka puluhan
		self.puluhan = self.getPuluhan(angka)
		# angka satuan
		self.satuan = self.getSatuan(angka)

	def bacaAngka(self):
		# angka terbilang
		angka_terbilang = ['', 'satu ', 'dua ', 'tiga ', 'empat ', 'lima ', 'enam ', 'tujuh ', 'delapan ', 'sembilan ', 'se']
		sambungan = ['', 'belas ', 'puluh ']
		index_sambungan = 2

		if self.puluhan < 1:
			index_sambungan = 0
		elif self.puluhan == 1:
			if self.satuan == 0:
				index_sambungan = 2
				self.puluhan = 10
			else:
				index_sambungan = 1

				if self.satuan == 1:
					self.puluhan = 10
				else:
					self.puluhan = self.satuan
				self.satuan = 0

		result = angka_terbilang[self.puluhan] + sambungan[index_sambungan] + angka_terbilang[self.satuan]

		return result


	def getPuluhan(self, angka):
		if angka < 10:
			return 0

		return int(str(angka)[0])

	def getSatuan(self, angka):
		if angka < 10:
			return angka

		return int(str(angka)[1])
		