**Introduction:**

  The goal of this project is to create a vessel that can contain 16 to 20 ounces of fluid. Additionally, this vessel must be able to stand on a flat surface. The term vessel has many definitions, but the one this project focuses on is “a container (such as a cask, bottle, kettle, cup, or bowl) for holding something.” (Merriam-Webster Online) The creation of the vessel must utilize at least two functions -- neither of which can be linear. The thickness of the material used to construct the vessel is not taken into account.
  
**Design:**

  After playing around with many different functions on desmos (www.desmos.com) to get a rough idea of my final figure, I discovered and really liked the equations

![image](https://user-images.githubusercontent.com/50001718/131267124-63c9fe77-e7ff-494f-b05b-01d8ff0c95f7.png)
and ![image](https://user-images.githubusercontent.com/50001718/131267130-c2e4d2bd-2321-4454-b74d-3112b34e71b7.png)

  Even though desmos is 2D and so I could only view a “slab” of the 3D object, I wanted to use something similar to these functions. In the end, it would look like a smooth vase with a cool “base.” There is no traditional flat/solid base, but rather an inward semi-sphere type shape at the bottom of the vase. Essentially, the object looks like a manipulated parabola from the outside, but once picked up, with a really interesting (in my opinion) inward design from the bottom -- almost as if the water is “floating.” With this unique shape I discovered, it was time to program a 3D model. 

  However, before delving too deep, I figured these functions would not hold between 16 to 20 oz of fluid, which was required. (Calculations can be found in the process section of this write-up). So, after many manipulations and iterations, I found these equations to satisfy both the fluid requirement, while appearing visually pleasing.

 ![image](https://user-images.githubusercontent.com/50001718/131267138-36231e5e-0348-4df7-82c4-88095f19faaa.png)
 ![image](https://user-images.githubusercontent.com/50001718/131267142-475c9afc-2f6e-4412-bcaa-fa0525c16a82.png)

  As you may have noticed, I removed the ln(x) and replaced it with ln(5). This is due to the complications that arose with finding the inverse of (specifically) f(x). I had to find the inverse functions in order to calculate the volume, since I was rotating the “slab” about the y-axis. 

**Design (cont.):**

2D Graph:

Original Design:
![image](https://user-images.githubusercontent.com/50001718/131267177-e7d94624-eb3d-45c3-93c0-3f1b13c787fd.png)
![image](https://user-images.githubusercontent.com/50001718/131267178-2d38bde4-7a0c-4205-b3ee-3f70ce3d04d8.png)

●	https://www.desmos.com/calculator/nd9gjfcu5y 

●	Would not work because the object’s volume would be too small to hold the specified amount of fluid 

Final Design:

  ![image](https://user-images.githubusercontent.com/50001718/131267200-378e6578-063a-4bef-9500-9ce31701bac7.png)
  ![image](https://user-images.githubusercontent.com/50001718/131267204-c28282f8-028d-4557-a699-4284b3b3d08d.png)

●	https://www.desmos.com/calculator/i0afp2wl3k 

●	Will hold the specified amount of fluid 

●	Similar to original design

  ○ ![image](https://user-images.githubusercontent.com/50001718/131267436-c914993b-4f97-43d7-8450-3b321345a0ba.png)
 of f(x) was replaced with ![image](https://user-images.githubusercontent.com/50001718/131267438-f36d8b25-115f-4dd4-ae37-114d7f85b56c.png)
 due to complications with calculating an inverse function for finding the volume of the object (about the y-axis)

●	The point of intersection is (7.707, -10.395)

  ○	3D object will be created by rotating the area between x = 0 and x = 7.707 about the y-axis (note this is the area of g(x) to be rotated, not f(x); f(x) has an area between x = 1 and    x = 7.707 so that there will be a hole for the fluid to enter. 

**3D Graph:**

  The original and different iterations of my 3D design look too distorted (and out of graph bounds) to properly show considering their abnormal shapes. Nevertheless, since they are not as important as the final design, and would not have worked anyways because of size factors, the final design is the best work which is what will be shown below:

Final design:

 ![image](https://user-images.githubusercontent.com/50001718/131267223-5af1d9f6-57d4-4c78-9495-9ddbbb3ae0c1.png)

●	Side-view; orientation as if it was on a table. 

 ![image](https://user-images.githubusercontent.com/50001718/131267229-24a94bd1-ae4b-41f9-b6a6-bb7c5fa60314.png)

●	Top-view: you can see a hole where fluid can be put in the object through. 

 ![image](https://user-images.githubusercontent.com/50001718/131267232-cab36ca1-2d42-4369-a184-d81cb75b4162.png)

●	“Birds-eye view.” 

●	The fluid is stored in the empty space between the blue and the red. 

 ![image](https://user-images.githubusercontent.com/50001718/131267238-c84522b6-6c13-4012-8efa-759fdc8258bc.png)

●	Bottom view; “Empty space.” 

●	Looking at the object from the bottom, one can see that it goes inward in a very smooth fashion -- as if a semi-sphere can fit in there. 

**Process:** 
  
  While manipulating iterations, I had to adjust the functions accordingly so that the final object would hold between 16 - 20 ounces of fluid. Before I go further, I must clarify I am using centimeters. First I had to convert and figure out how much space (in centimeters) would hold 16 - 20 ounces. Using the conversion rate below that I found online (source in bibliography), I found that the minimum volume of the vessel can be about 473.178 cubic cm and the maximum volume can be about 591.47 cubic cm. Ideally, I want the volume to be somewhere between these two values, not too close to either one. 

![image](https://user-images.githubusercontent.com/50001718/131267252-3a74c20f-63b2-47e6-98a4-49e955b32f99.png)
![image](https://user-images.githubusercontent.com/50001718/131267254-da49d3ba-7c97-423b-969f-9802ebd0e0f0.png)
![image](https://user-images.githubusercontent.com/50001718/131267255-5a60d2f1-c235-48af-9964-e2597a178fea.png)

  In order to find the volume of my object, I had to utilize integrals. The equation to find the volume of a function rotated about the y-axis is as follows: 
  ![image](https://user-images.githubusercontent.com/50001718/131267271-2fedc558-4f2f-4a24-b6f9-46ef91af3ba1.png) (Equation from www.rit.edu (in bibliography))
    Where c and d are horizontal lines, or the “dimensions” (start to end) of the “slab” to the rotated. 
	
  The equations I want to use are f(x); however in order to find the volume of an object rotated about the y-axis, I needed f(y). So, I found the inverse of my functions:

Inverse of f(x): 
 ![image](https://user-images.githubusercontent.com/50001718/131267277-d41fb64a-60aa-4413-981a-5427e66b4725.png)

Inverse of g(x):
 ![image](https://user-images.githubusercontent.com/50001718/131267278-013998d4-285b-46e8-aca5-0a37365a34c5.png)

Finding the volume: 
 ![image](https://user-images.githubusercontent.com/50001718/131267281-cd818197-fb8e-4fa3-9afe-24a18e5e4e30.png)

  (Clarification: even though above I said the area I am rotating is between about x x = 0 and x = 7.707, the constraints of each integral are based off the y-axis (and of how much I want to rotate (e.g. fluid entrance hole)) since I am rotating about the y-axis and not the x-axis. Thinking about the area in terms of x as I mentioned above is easier to visualize/understand for an explanation; however, you must be careful when calculating the volume because you must use the corresponding constraints with the axis in which you intend to rotate the object about.) 
  
  Essentially, what I did here was subtract the volume of g(x) from the volume of f(x), so I could find the inner-volume of where the fluid will be located. It is the area between the red and the blue (referring to the 3D object diagrams above). The integral for f(x) (the inverse) was from (y = ) 3.31 to (y = ) -10.395 so that there would be a small hole on the top of the object where fluid could be put in. (If I was to use a value higher than 3.31, which I could of, then there would have been no entrance for the fluid.) The integral for g(x) (the inverse) was from (y = ) 0 to (y = ) -10.395 so there would be no opening and so that the object would be “closed” when the two functions “meet.” This volume is below the maximum and above the minimum, so it satisfies the requirement. Specifically, my object would hold 19.2 ounces of fluid. 
 ![image](https://user-images.githubusercontent.com/50001718/131267292-3097c2ef-fdf4-413c-a4d3-1f1bd22290f2.png)
![image](https://user-images.githubusercontent.com/50001718/131267293-0eb7bb06-c60e-403b-aee7-aa4ab1daa3f7.png)
![image](https://user-images.githubusercontent.com/50001718/131267296-d1f6422b-3024-44fa-8cea-facf41346192.png)

  Programming the 3D model was very difficult because I had to learn a new python library. After about 10 hours or so and lots of trial and error, I finally figured it out. It was very difficult because I was trying to do something that you could not do at the start -- I was trying to just 3D graph a function using a python library, which is not possible with the library I am using. Why not use another library? There are only a few for this specific ordeal, and the one I am using the is probably the best one of the few. So then, after sometime I decided to focus on plotting individual 3D points. I had the computer evaluate both functions and then scatter-plot the points on a 3D basis. I finally had my two graphs plotted. They looked like lines, which is what I wanted, because I graphed hundreds of plots. However, these lines were only just “slabs” of the entire shape. After some research, I figured out I needed to rotate these two functions about the y-axis to get my final shape.
  I found the 3D point rotation equations (source in bibliography):
 ![image](https://user-images.githubusercontent.com/50001718/131267308-1cd71ff0-f127-4a86-8a5d-77e6efc7f5ba.png)
![image](https://user-images.githubusercontent.com/50001718/131267310-1ddbafda-a18e-4172-8225-c304b909b73f.png)
![image](https://user-images.githubusercontent.com/50001718/131267312-1d1f4c7e-7693-4bb4-8d86-f051e631d983.png)

	Where d is the degrees of rotation. 

  I had the computer evaluate thousands of rotated points based on the rotation equations for each function, and then plot each of them for both functions in the 3D plane, so in the end I would have a 3D object. Although the object is not fully meshed together, I like how it came out since I can just barely see the inner, g(x) function. 

**Conclusion:** 

  Overall, I am satisfied with my end product because I have written the code and created something (a vessel) from essentially nothing. The coding of the 3D object took a while, but in the end was worth it because it is something I made on my own, rather than rendering it with geogebra or another application that was premade. I have reached the project’s goal of creating a vessel that can hold between 16 to 20 fluid ounces of fluid (19.2 ounces specifically). Going through many iterations was also a hassle, but I managed to discover a working combination of functions. If I had more time, I would incorporate more functions into my design/object; however, doing so would complicate the programming aspect -- which I would have needed more time to do. While going through (what are now) iterations and thinking I completed my project (write-up included), I realized I had calculated the volumes based on f(x), not f(y) while rotating about the y-axis; I had to essentially redo the whole project all over again. Nevertheless, I enjoyed this project because of the outcome of my hard-work. 

**Bibliography:**

https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
●	Learned the essentials of the python library I am using to create the 3D model

https://www.siggraph.org/education/materials/HyperGraph/modeling/mod_tran/3drota.htm
●	Learned how to rotate a 3D point about the y-axis

https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
●	Learned in detail how to plot specific 3D points

https://www.tutorialspoint.com/scipy/scipy_integrate.htm
●	Learned how to calculate integrals in python 

https://www.metric-conversions.org/volume/us-ounces-to-cubic-centimeters.htm
●	Found fl oz to cubic cm conversion rate

https://www.rit.edu/studentaffairs/asc/sites/rit.edu.studentaffairs.asc/files/docs/services/resources/handouts/C8_VolumesbyIntegration_BP_9_22_14.pdf
●	Calculating volume of a function 
