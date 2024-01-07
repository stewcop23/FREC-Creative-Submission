# FREC Creative Submission!

Tasked with creating a creative work that describes the impact that O-Week has had on us.

I decided to go with an implementation of chaos theory, something that goes by many names, but most notably 'The Logistic Map'.


## The Logistic Map

This equation was first used to model the populations of a species under varying growth rates, and has since been shown to appear in many other areas of mathmatics such as the mandelbrot set, or liquid convection

The funamental equation used to calculate this is an "example of how complex, chaotic behaviour can arise from very simple nonlinear dynamical equations", and is given by:

[EQN]

Where:
x_n is the current population (a rational number greater than 0, but less than 1)(i.e.: 0.1, 0.736483, 0.999999, etc.)
The parameter r here refers to the growth rate of the population. r > 4 will create x_n+1's that lie outside of our desired range for x_n, so only values of 0<r<4 are considered
x_n+1 is the population of the next generation

if this equation is plotted with r ans the x axis and x_n plotted as the y axis, as this equation is iterated, the logistic map will be formed


## Python Implementation


### First Implementation 

A simple implentation of this was rather easy to construct. All it required was looping through every x value in the image to be generated, iterating the logistic function several times (skipping the first few iterations to allow the patterns to converge), then changing that calculated pixel from 0 to 1.


### "Anti-Aliased" Implementation

