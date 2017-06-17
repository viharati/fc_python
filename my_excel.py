class Excel():
	excel_file = ''
	def save_to_excel(self, list_data):
		for data in list_data:
			string = "Save " + str(data) + " into " + self.excel_file
			print(string)