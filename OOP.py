

class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!" + self.name + " is eating " +food)
	def description(self):
		print(self.name + " is " + str(self.age) +" years old and loves the color "+self.favorite_color)
	def make_sound(self,num):
		print((self.sound + " ")*num)

a= Animal("Skrra", " Big Shaq", "44", "Green")

"""a.eat("Sauce")
a.description()"""

class Person(object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eat_breakfast(self, breakfast):
		print(self.name + " is eating "+breakfast )

j=Person("Nick Crompton",22,"England","Male I think" )
"""j.eat_breakfast("tea")"""
"""print(j.city)"""
class Song(object):
	def __init__(self, lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self):
		print(self.lyrics)
		b=0
		for i in range(len(self.lyrics)):
			print(self.lyrics[b])
			b+=1
flower_song = Song(["Roses are red", "Violets are blue", "I wrote this poem, just for you."])
the_fall_of_jake_paul= Song(["YAA YEET", "Little brother try to roast me? (nope)", "Little brother standin on his own two feet? (NOT FOR LONGG!)", "I'm a dog, you're a puppy call you Kong! (Woof)", "Lets break down this garbage that you call a song"])
the_fall_of_jake_paul.sing_me_a_song()



