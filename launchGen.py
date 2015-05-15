import json
import urllib2
import math

METRES_PER_INCH = 0.0254
LAUNCH_ANGLE = input('Enter the Launch Angle in Degrees: ')
LAUNCH_HEIGHT = input('Enter your Launch Height in Inches: ')
INCREMENT = input('Enter a Distance Increment in Inches: ')
FIELD_SIZE = 140.5
GOAL_X = 4.0941
GOAL_Y = 139.9059

i = 0
l = ''

for length in xrange(0, 195, INCREMENT):
	y = length + GOAL_Y
	data = json.load(urllib2.urlopen('http://vex.us.nallen.me/exec/extras/nbn_shooting?x=' + str(GOAL_X*METRES_PER_INCH) + '&y=' + str(y*METRES_PER_INCH) + '&z='+ str(LAUNCH_HEIGHT * METRES_PER_INCH) +'&angle='+ str(LAUNCH_ANGLE)))
	basic = '	{' + str(round(data['incident'],2)) + ',' + str(round(data['speed'],2)) + ',' + str(length) + '}'

	if data['speed'] == -1:
		i = i+1
	else:
		l = l + basic + ',\n'

print 'float fiedlPOSLaunch[' + str(round(195/INCREMENT) - i + 1) + '] [3] = {'
print l[:-2]
print '};'
