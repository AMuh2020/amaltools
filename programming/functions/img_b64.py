# write a function that takes an image file and returns a base64 string
import base64
# from io import BytesIO
def img_to_b64(img):
    # with open(img,"rb") as f:
    #     img = f.read()
    img = base64.b64encode(img)
    base64_string = img.decode("utf-8")
    return base64_string

# write a function that takes a base64 string and returns an image file
# def b64_to_img(b64):
#     with BytesIO() as fh:
#         fh.write(base64.decodebytes(b64.encode("utf-8")))
#         b64_string = fh.getvalue()
#         out = base64.b64encode(b64_string).decode()
#         return out

# since it is in base64 already it can be used in the img tag without having to be processed. Can be done fully client side