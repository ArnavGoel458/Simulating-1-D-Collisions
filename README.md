# Simulating-1-D-Collisions
This python script predicts the time, location and the balls which collide.  
n- point objects are located in a gravity free one dimensional universe where for an i ∈ {0,1,2......n-1}, the i'th objext has a mass m<sub>i</sub> and at time t=0 
all the particles are located at position x<sub>i</sub> ∈ R and has velocity v<sub>i</sub> ∈ R.    

Objects are numbered from left to right i.e x<sub>0</sub><x<sub>1</sub>.........<x<sub>n-1</sub>. All these object undergo several collision over time and move away from each other.
All collisions are assumed to be elastic. A collision always occurs between the i<sup>th</sup> and i+1<sup>th</sup> object.  
This script returns a list of tuples (t, i, x) representing a collision happening at time t between objects i and i + 1 at location x.    

The script takes five arguments:  
1. M: a list of positive floats, where M[i] is the mass of the i’th object,  
2. x: a sorted list of floats, where x[i] is the initial position of the i’th object,  
3. v: a list of floats, where v[i] is the initial velocity of the i’th object,  
4. m: a non-negative integer,
5. T: a non-negative float,  

The list of collisions returned are in chronological order that ends as soon as the first m collisions happen or time reaches T (whichever earlier).
