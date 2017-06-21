class News():
	news = []

	def get_news(self, keyword):
		print("find news")
		for i in range(10):
			string = " "+ str(i) + " news. " + keyword
			self.news.append(string)
		print("finished")
		return self.news