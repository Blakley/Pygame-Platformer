# -- setup game window configuration variables --
w = 1000; # screen width
h = 900; # screen height

# -- game variables -- 
tile_size = 100


# -- world tile data --

# 9 x 10
data = [
	[1,1,1,1,1,1,1,1,1,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1]
]

# image tile locations
imgT = [
	'../assets/Tiles/bg_1.png',
	'../assets/Tiles/sun.png',
	'../assets/Tiles/bg_2.png',
	'../assets/Tiles/grass.png',
	'../assets/Tiles/grassCenter.png',
	'../assets/Tiles/grassCenter_rounded.png',
	'../assets/Tiles/grassCliffLeft.png',
	'../assets/Tiles/grassCliffLeftAlt.png',
	'../assets/Tiles/grassCliffRight.png',
	'../assets/Tiles/grassCliffRightAlt.png',
	'../assets/Tiles/grassHalf.png',
	'../assets/Tiles/grassHalfLeft.png',
	'../assets/Tiles/grassHalfMid.png',
	'../assets/Tiles/grassHalfRight.png',
	'../assets/Tiles/grassHillLeft.png',
	'../assets/Tiles/grassHillLeft2.png',
	'../assets/Tiles/grassHillRight.png',
	'../assets/Tiles/grassHillRight2.png',
	'../assets/Tiles/grassLeft.png',
	'../assets/Tiles/grassMid.png',
	'../assets/Tiles/grassRight.png',
	'../assets/Tiles/bridge.png',
	'../assets/Tiles/bridgeLogs.png'
]

# image items locations
imgI = [
	'../assets/.png',
	'../assets/.png',
	'../assets/.png',
	'../assets/.png',
	'../assets/.png'
]

# image player locations
imgP = [
	'../assets/.png',
	'../assets/.png',
	'../assets/.png',
	'../assets/.png',
	'../assets/.png'
]