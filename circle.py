import math

class Circle:

	def __init__( self, xCoord, yCoord, radius ):
		self.x = xCoord
		self.y = yCoord
		self.radius = math.fabs( radius )
	
	def toString( self ):
		body = "x: " , self.x , \
			   "y: " , self.y , \
			   "radius: " , self.radius

		return body

circleTest  = [ Circle( 2,  0, -1 ), Circle( 1,  2,  1), Circle( 0,  3,  1 ), Circle( 0,  0,  1 ), Circle( -2,  1,  1 ), Circle( -2,  0,  1 ) ]

# A is an array of circleObjects

def boundCircles( A ):
	
	# initalize the box
	xmin = 100
	xmax = -100

	ymin = 100
	ymax = -100

	# x comparison
	for circle in A:

		# x comparison

		# lower comparison
		if ( circle.x - circle.radius ) < xmin:
			xmin = circle.x - circle.radius
			print ">" ,  xmin

		# upper comparison
		if ( circle.x  + circle.radius ) > xmax:
			xmax = circle.x + circle.radius
			print ">>>>",  xmax

		# y comparison 

		# lower comparison
		if ( circle.y - circle.radius ) < ymin:
			ymin = circle.y - circle.radius
			print "<" ,ymin

		# upper comparison
		if ( circle.y + circle.radius ) > ymax:
			ymax = circle.y + circle.radius

	# center point
	centerX = ( xmax + xmin ) / 2
	centerY = ( ymax + ymin ) / 2

	# get a radius
	xlength = xmax - centerX
	ylength = ymax - centerY

	# radius = math.sqrt( math.pow( xlength , 2 ) + math.pow( ylength, 2 ) )

	# making a circle of radius would work, but let's make it a little tighter
	# checks with all neighboring circles
	maxRad = 0

	for circle in A:

		xdist = centerX - circle.x
		ydist = centerY - circle.y

		rad = math.sqrt( math.pow( xdist, 2 ) + math.pow( ydist, 2 ) ) + circle.radius

		if rad > maxRad:
			maxRad = rad


	# have min radius and center point, lets return a circle of that size
	return Circle( centerX, centerY, maxRad )

print boundCircles( circleTest ).toString()