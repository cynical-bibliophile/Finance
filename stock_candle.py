class StockCandle:
	def __init__(self, ticker, date, open, low, high, close):
		self.ticker = ticker
		self.date = date
		self.open = open
		self.low = low
		self.high = high
		self.close = close

	def __str__(self):
		ret = "StockCandle {\n"
		ret += "\tTicker: " + self.ticker + "\n"
		ret += "\tDate: " + self.date.__str__() + "\n"
		ret += "\tOpen: " + str(self.open) + "\n"
		ret += "\tLow: " + str(self.low) + "\n"
		ret += "\tHigh: " + str(self.high) + "\n"
		ret += "\tClose: " + str(self.close) + "\n"
		ret += "}\n"
		return ret