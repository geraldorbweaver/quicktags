class Card:
	def __init__(self,name,tags = None):
		self.name = name
		if tags is None:
			self.tags = []
		else:
			self.tags = tags

	def from_csvrow(row):
		retVal = Card(row[0])
		for tag in row[1:]:
			retVal.add_tag(tag)
		return retVal

	def add_tag(self, tag):
		self.tags.append(tag)

	def __str__(self):
		builder = []
		builder.append(self.name)
		builder.append(': ')
		for tag in self.tags:
			builder.append(tag)
			builder.append(',')
		return ''.join(builder[:-1])