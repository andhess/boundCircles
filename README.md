# About
This is a simple program I was asked to write in an interview with Square.

The function boundCircles takes in an array of circle objects and will return a circle that encapsulates all of them.

A Circle object has the following properties:
* x coordinate
* y coordinate
* radius

This was completed in under an hour.  I built 2 versions. The first runs in O(n) time, the second will find a tigther circle but needs to interate through the list another time.

My approach was to create a bounding box that would contain everything.  From there, I could get a decent center point, and calculate the radius.  The 2nd method goes one step further and attempts to find a slightly tighter radius.