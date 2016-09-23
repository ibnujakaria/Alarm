from datetime import datetime

from cores.AngkaTerbilang import AngkaTerbilang


class MenampilkanWaktu():

	def getStringOfWaktu(self):

		self.waktu_sekarang = datetime.now()
		# angka = int(input('masukkan angka -> '))
		# print(AngkaTerbilang(angka).bacaAngka())
		jam_terbilang = AngkaTerbilang(self.waktu_sekarang.hour).bacaAngka()
		menit_terbilang = AngkaTerbilang(self.waktu_sekarang.minute).bacaAngka()

		sambungan = 'lebih '

		if menit_terbilang == '':
			sambungan = 'tepat '
		
		elif menit_terbilang == 'lima belas ':
			menit_terbilang = 'seperempat'


		return jam_terbilang + sambungan + menit_terbilang

	def periksaSiangMalam(self):
		if self.waktu_sekarang.hour < 12:
			waktu = 'pagi'
		elif self.waktu_sekarang.hour < 15:
			waktu = 'siang'
		elif self.waktu_sekarang.hour < 18:
			waktu = 'sore'
		else:
			waktu = 'malam'

		return waktu

	def getWaktuBiasa(self):
		self.waktu_sekarang = datetime.now()

		jam = str(self.waktu_sekarang.hour)
		menit = str(self.waktu_sekarang.minute)
		detik = str(self.waktu_sekarang.second)

		if len(jam) < 2:
			jam = "0" + jam
		if len(menit) < 2:
			menit = "0" + menit
		if len(detik) < 2:
			detik = "0" + detik

		return jam + ":" + menit + ":" + detik

	def getHour(self):
		return self.waktu_sekarang.hour

	def getMinute(self):
		return self.waktu_sekarang.minute