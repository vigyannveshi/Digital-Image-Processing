# **Digital Image Processing** 

<img src="featured_img\featured_img_1.png"><img src="featured_img\featured_img_2.png">
## Acknowledgements

---

**_Special Thanks to:_**

- **_God_**, all the things I will and have learnt initiate and terminate from whom, who supports me in all my endeavours.
- **_Rafael C. Gonzalez | Richard E.Wood_**, for the most amazing textbook on Digital Imaging Processing, that I have refered to, most of the programs written are based on concepts learnt from the book (3rd Edition). It is the standard reference for the Digital Image Processing course offered in my college. 
- **_Prof. Purti Savardekar, Goa Engineering College_**, my teacher in the course of Digital Image Processing. For her initiative to write programs for the concepts taught in the class. Motivating me to visualize them to achieve better understanding. 
- **_My parents, and well-wishers_**, for their active support.

## Disclaimer

---
The repository is created to share the concepts that I have been fortunate to learn in the Digital Image Processing course. I hope it  helps DIP enthusiasts in their journey. All programs have been written in python. The experiments are implementations of concepts. Most of the concepts have been tried to be implemented from scratch to understand the underlying nitti-grittis and have been combined into classes for better code organization and access. Rest of them have been inherited from existing image processing libraries in python to avoid reinventing the wheel unnecessarily. Images used in the experiments are taken from reference:https://www.imageprocessingplace.com/DIP-3E/dip3e_book_images_downloads.htm
and are used only for study purposes.
Tracking about updates in the experiments, can be done by checking out the featured images in the README, which depicts the **input_output** folder.


## Making the Best possible use of the repository:

---
Download the repository as a zip file, and extract it in a folder on your local system. All the experiments exist in their respective topic folder named as per the topic-wise alphabet **{A,B,C...,}**, the images used are in separate folders **{CH01,CH02,CH03..., extra_images}**, the classes created for special functionalities are stored in separate folder **important_classes**  which are combined for easy access using the python file **diptoolbox**. You will be able to run the experiments directly using their corresponding python files, the final output will be saved in the **input_output** folder. You are encouraged to tweak the values and observe the change, and if you find something new or something strange please do share it at: mailtovigyannveshi@gmail.com


## Experiments Done:
---
| Experiment No. | Title                                                                                       |
|----------------|---------------------------------------------------------------------------------------------|
|**A.** | **Digital Image Fundementals**  | 
|   |   |
| 1.             | Introduction to Digital Image Processing                                                    |
| 2.             | Bit Plane Slicing                                                                           |
| 3.             | Image Resolution                                                                            |
| 4.             | Image Interpolation :                                                                       |
|                | a) Nearest Neighbourhood, Bilinear, Bicubic interpolations and their comparison             |
|                | b) Resizing QR codes using Nearest Neighbourhood interpolation                              |
| 5.             | Arithmetic Operations in Digital Image Processing                                           |
|                | a) Addition (Averaging) of noisy images for noise reduction                                 |
|                | b) Image Subtraction for Enhancing Differences                                              |
|                | c) Image Subtraction for Angiography                                                        |
|                | d) Image Multiplication for Shading Correction                                              |
|                | e) Image Multiplication for 'Region of Interest' (ROI) operations                           |
| 6.             | Point and Neighbourhood Operations in Digital Image Processing                              |
|                | a) Intensity Transformation to obtain the negative of an 8-bit image using Point Processing |
|                |  b) Local Blurring using Neighbourhood Processing
| 7.             | Geometric Spatial Transformation in Digital Image Processing                                |
|   |   |
|**B.** | **Intensity Transformations and Spatial  Filtering**  |  
|   |   |
| 1. | Intensity Transformations in Digital Image Processing |
|    | a) Contrast Stretching                                |
|    | b) Thresholding                                       |
|    | c) Intensity level Slicing                            |
|    | d) Image negative                                     |
|    | e) Logarithmic and Antilogarithmic Transformations    |
|    | f) Power-Law (Gamma Transformations)                  |
|    | g) Bit-plane slicing                                  |
|   |   |
|| *..Some expts yet to be added*|
|   |   |
|**C.** | **Image Restoration and Reconstruction**  | 
|   |   |
| 1. | Image Noise Analysis in Digital Image Processing |
| 2. | Noise removal using various mean filters|
| 3. | Handling salt and pepper noise using Contraharmonic mean filters |
| 4. | Handling Salt & Pepper, Gaussian and Uniform noise 
|    |a) Using 3*3 Order Statistic filters|
|    |b) Using 3*3  Max, Min, Midpoint filters 
| 5. | Handling combination of additive Uniform noise with Salt & Pepper noise |
| 6. | Handling Salt & Pepper Noise with probabilities Ps>0.2, Pp>0.2 using Adaptive Median Filter |
| 7. | Handling Additive Gaussian noise with high variance using Adaptive Local Noise Reduction Filter |
| 8. | Visualizing the Atmospheric Turbulence Degradation function on an image in the spatial as well as the frequency domain |
| 9. | Visualizing the Motion Blur Degradation in an image in the spatial as well as the frequency domain|
| 10.| Direct Inverse and Weiner Filtering |
|   |   |
|**D.** | **Filtering in the Frequency Domain**  | 