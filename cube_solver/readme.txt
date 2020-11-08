
If you want to run the solver of Rubik's cube, just run
## python solver.py ##
There are 3 steps for using this software.
1. Show 6 faces to the camera and the screen will display what it recognizes. Users have to make sure that every face is recognized correctly.

2. When candidate permutation is found, users need to rotate this cube slowly in front of the camera. After getting the rotation direction, you can view a list number in the screen. Until the largest number is 3 more than the second largest one, the optical flow prediction will stop.

3. After getting the permutation of the cube, just follow the solutions step by step. And type 'n' for the next step. (Red arrow means 90 degrees and black arrow means 180 degrees.)

If you want to stop this software, just type 'x'.