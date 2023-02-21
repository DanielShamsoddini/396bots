# 396bots
Assignment 7

This is a program for Assignment 7 for Northwestern University's CS396: Artificial Life

It is heavily based on the ludobots MOOC on https://www.reddit.com/r/ludobots/ created by Professor Josh Bongard and uses the PyBullet engine and pyrosim additional code
PyBullet: https://pybullet.org/wordpress/
Pyrosim: https://github.com/jbongard/pyrosim


This program runs and generates a random creature in a 3D morphospace in the PyBullet engine.

It does this by following the diagram drawn out below
		

<img width="996" alt="a7 photo" src="https://user-images.githubusercontent.com/23564433/220255009-096bab20-a135-4bbb-a26d-ad78dd6e6122.png">

Morphospace Description:

This leads to a wide potential variety of shapes, and makes it so that blocks can have anywhere from 1 to 4 connected blocks. However, some shapes are still not possible as these vestigial blocks are not capable of randomly linking to more blocks, meaning that a centipede or spiral like shape can be expected a lot of the time.
Its neurons are also connected in a semi random way, as while each block either has motor/possible sensor neurons, the synapse connections for these are decided randomly, meaning that for example a vestigial sensor can potentially be linked to a core block motor or vice versa. Movement as of right now is still using the standard pyrosim single joint axis for each joint, but given the potentially large # of blocks it was my opinion that the robot should still be able to have substantial freedom of movement thanks to the vestigial blocks.

To run this program clone this repository and run runsnakemake.py
