import tarantool

connection = tarantool.connect("localhost", 3301)

space_user = connection.space('user')

space_story = connection.space('story')


class User:
	def __init__(self, user_id,):
		self.user = space_user.select(user_id)
		if not self.user:
			self.user = space_user.insert((user_id, True, 0, [], 0))
		self.user_id = user_id

	def save(self):
		space_user.replace(self.user[0])   