from PIL import Image

# open image file
img = Image.open("example.jpg")

# get original image size
width, height = img.size
print("Original image size:", width, "x", height)

# resize image to half its original size
new_width = int(width / 2)
new_height = int(height / 2)
resized_img = img.resize((new_width, new_height))

# get resized image size
resized_width, resized_height = resized_img.size
print("Resized image size:", resized_width, "x", resized_height)

# save resized image to file
resized_img.save("resized_example.