# Road-Lane-Detection
in this project, i used Python and OpenCV to find lane lines in the road images.

#The following techniques are used:

Color Selection Canny Edge Detection Region of Interest Selection Hough Transform Line Detection

#Test Images

In this image show plane road line. Road lane not detected

![road](https://github.com/user-attachments/assets/abd0a212-4743-40ac-960e-8ee6bafe735e)



Road lane detection image using web camera Road lane detection

![Uploading road2.jpeg…]()


Gaussian Smoothing (Gaussian Blur) When there is an edge (i.e. a line), the pixel intensity changes rapidly (i.e. from 0 to 255) which we want to detect. But before doing so, we should make the edges smoother. As you can see, the above images have many rough edges which causes many noisy edges to be detected.

I use cv2.GaussianBlur to smooth out edges.

Gaussian Filter OpenCV Theory cv2.GaussianBlur OpenCV API Reference

#Conclusion

The project was successful in that the video images clearly show the lane lines are detected properly and lines are very smoothly handled.

It only detects the straight lane lines. It is an advanced topic to handle curved lanes (or the curvature of lanes). We'll need to use perspective transformation and also poly fitting lane lines rather than fitting to straight lines.

Having said that, the lanes near the car are mostly straight in the images. The curvature appears at further distance unless it's a steep curve. So, this basic lane finding technique is still very useful.
