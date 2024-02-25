#first will install the package qrcode #
# using this command "pip install qrcode" #
import qrcode
 # Editing the size for QRcode order #
features = qrcode.QRCode(version=1,box_size=30,border=4)
# import the webite address #
features.add_data('https://github.com/Kushal1726')
features.make(fit = True)
# coloring the image in this part #
generate_image = features.make_image(fill_color="black",back_color="white")
#generate image randomly in this part #
generate_image.save("image1.png")
