import qrcode

# ========qrcode using qrcode generator=======

# img = qrcode.make("hello world! this is eggplc")
# img.save("mycode.png")


# =========custom management of your qrcode======

# qr = qrcode.QRCode(version=1,
#                    error_correction=qrcode.constants.ERROR_CORRECT_L,
#                    box_size=20,
#                    border = 2)
# qr.add_data("https://www.clarencemabeya-portfolio.vercel.app")
# qr.make(fit=True)

# img = qr.make_image(fill_color = "green",back_color = "grey")
# img.save("portfolio.png")

# =======vector graphics qrcode=========

import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("hello world!!", image_factory = factory)
svg_img.save("letsee.svg")