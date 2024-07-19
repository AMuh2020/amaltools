from rembg import remove
from io import BytesIO

def remove_background(image):
    output_bytes = BytesIO()
    with image.open(mode='rb') as image:
        image = image.read()
        result = remove(image)
        output_bytes.write(result)

    # for testing
    with open('test.png', 'wb') as image:
        image.write(output_bytes.getvalue())
    # return output_bytes

    return output_bytes