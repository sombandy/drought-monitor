import cv2
import numpy as np
import urllib.request

# Define the URLs file name
file_name = 'urls.txt'

# Define the video frame size and FPS
width, height = 640, 360
fps = 30

# Create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# Open the URLs file and iterate over the lines
with open(file_name) as f:
    for line in f:
        # Remove any leading/trailing whitespaces and line breaks
        url = line.strip()
        try:
            print("Processing", url)
            # Download the image from the URL
            with urllib.request.urlopen(url) as url_response:
                img_array = bytearray(url_response.read())

            # Convert the byte array to a numpy array and reshape it to the desired frame size
            img = np.asarray(img_array, dtype=np.uint8)
            img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
            img = cv2.resize(img, (width, height))

            # Add the frame to the video
            out.write(img)

            # Wait for 0.1 seconds before downloading the next image
            cv2.waitKey(100)

        except:
            # If there is an error in downloading the image, skip it and continue with the next URL
            continue

# Release the VideoWriter object and destroy any remaining windows
out.release()
cv2.destroyAllWindows()
