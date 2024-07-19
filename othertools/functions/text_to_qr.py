import qrcode
import base64
from io import  BytesIO
# now to make it load in memory: done
def qr_code_function(text,settings):
    
    if settings["version"] == "0":
        settings["version"] = None
    
    if settings["error_correction"] != "L" and settings["error_correction"] != "M" and settings["error_correction"] != "Q" and settings["error_correction"] != "H":
        return "error correction must be L, M, Q, or H"
    else:
        if settings["error_correction"] == "L":
            settings["error_correction"] = qrcode.constants.ERROR_CORRECT_L
        elif settings["error_correction"] == "M":
            settings["error_correction"] = qrcode.constants.ERROR_CORRECT_M
        elif settings["error_correction"] == "Q":
            settings["error_correction"] = qrcode.constants.ERROR_CORRECT_Q
        elif settings["error_correction"] == "H":
            settings["error_correction"] = qrcode.constants.ERROR_CORRECT_H


    qr = qrcode.QRCode(
        version=settings["version"],
        error_correction=settings["error_correction"],
        box_size=settings["box_size"],
        border=settings["border"],
    )
    qr.add_data(text)
    if settings["version"] == "auto":
        qr.make(fit=True)
    img = qr.make_image(fill_color=settings["fill_color"], back_color=settings["back_color"])
    # img = qrcode.make(text)
    with BytesIO() as output:
        img.save(output, format="PNG")
        contents = output.getvalue()
    
    out = base64.b64encode(contents).decode()
    return out