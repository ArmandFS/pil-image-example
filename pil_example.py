from PIL import Image
im = Image.open("example.png")
new_im = im.resize((640,480))
new_im.save("example_resized.png")
