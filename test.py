import cv2
import numpy as np

# Load three images
image1 = cv2.imread('alum (6).jpg')
image2 = cv2.imread('alum (29).jpg')
image3 = cv2.imread('spliced_image.jpg')

image1 = cv2.resize(image1, (500,500))
image2 = cv2.resize(image2, (500,500))
image3 = cv2.resize(image3, (500,500))

# Create the blank canvas
canvas = np.zeros_like(image1)

# Determine the slice sizes
num_slices = 4
slice_angle = 360 / num_slices

# Calculate the center of the canvas
center_x = canvas.shape[1] // 2
center_y = canvas.shape[0] // 2

# Initialize an angle variable to keep track of the slice angles
angle = 0

# Loop through each slice
for i in range(num_slices):
    # Calculate the start and end angles for the slice
    start_angle = angle
    end_angle = angle + slice_angle

    # Create a mask for the current slice
    slice_mask = np.zeros_like(canvas)
    cv2.ellipse(slice_mask, (center_x, center_y), (200, 200), 0, start_angle, end_angle, (255, 255, 255), -1)

    # Apply the mask to the current image
    if i == 0:
        slice_img = cv2.bitwise_and(image1, slice_mask)
    elif i == 1:
        slice_img = cv2.bitwise_and(image2, slice_mask)
    else:
        slice_img = cv2.bitwise_and(image3, slice_mask)

    # Add the sliced image to the canvas
    canvas = cv2.add(canvas, slice_img)

    # Update the angle for the next slice
    angle += slice_angle

# Display and save the pie chart
# cv2.imshow('Pie Chart', canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('pie_chart_image1.jpg', canvas)