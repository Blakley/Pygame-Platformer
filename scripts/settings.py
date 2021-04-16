# -- setup game window configuration variables --
w = 1000; # screen width
h = 900; # screen height

# -- game variables -- 
tile_size = 50


# -- world tile data --

# 18 x 20, test stage data
data = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
	[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2], 
	[2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2], 
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

# image tile locations
imgT = [
	'../assets/Tiles/bg_1.png',						# 0
	'../assets/Tiles/sun.png',						# 1
	'../assets/Tiles/bg_2.png',						# 2
	'../assets/Tiles/grass.png',					# 3
	'../assets/Tiles/grassCenter.png',				# 4
	'../assets/Tiles/grassCenter_rounded.png',		# 5
	'../assets/Tiles/grassCliffLeft.png',			# 6
	'../assets/Tiles/grassCliffLeftAlt.png',		# 7
	'../assets/Tiles/grassCliffRight.png',			# 8
	'../assets/Tiles/grassCliffRightAlt.png',		# 9
	'../assets/Tiles/grassHalf.png',				# 10
	'../assets/Tiles/grassHalfLeft.png',			# 11
	'../assets/Tiles/grassHalfMid.png',				# 12
	'../assets/Tiles/grassHalfRight.png',			# 13
	'../assets/Tiles/grassHillLeft.png',			# 14
	'../assets/Tiles/grassHillLeft2.png',			# 15
	'../assets/Tiles/grassHillRight.png',			# 16
	'../assets/Tiles/grassHillRight2.png',			# 17
	'../assets/Tiles/grassLeft.png',				# 18
	'../assets/Tiles/grassMid.png',					# 19
	'../assets/Tiles/grassRight.png',				# 20
	'../assets/Tiles/bridge.png',					# 21
	'../assets/Tiles/bridgeLogs.png'				# 22
]

# image items locations
imgI = [
	'../assets/.png',
	'../assets/.png',
	'../assets/.png',
	'../assets/.png',
	'../assets/.png'
]


# image player locations, test player
imgP = [
	'../assets/Player/guy1.png',
	'../assets/Player/guy2.png',
	'../assets/Player/guy3.png',
	'../assets/Player/guy4.png'
]

