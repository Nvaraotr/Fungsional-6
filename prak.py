from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

# TODO 1 : Buka Kedua Gambar memakai Pillow
background_image = Image.open("assets/bgumm.jpg")
logo_image = Image.open("assets/logoumm.jpg")
font_arial = "fonts/arial.ttf"

# TODO 2 : Ubah background menjadi grayscale, berotasi sebesar 30 derajat, dan blur
bgBW = background_image.convert("L")
bgRotate = bgBW.rotate(30)
bgBlur = bgRotate.filter(ImageFilter.BLUR)
finalBg = bgBlur.resize((1920, 1080))

# TODO 3 : Ubah tingkat kecerahan, tingkat kontras (2 Nim terakhir 58) dan resize
enhancer = ImageEnhance.Brightness(logo_image)
brightened_image = enhancer.enhance(1.58)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.58)

new_logo = final_image.resize((458, 458))

# TODO 4 & 5 : Sisipkan logo ke dalam BG dan Tambahkan teks pada logo dengan font arial dengan ukuran 24
font = ImageFont.truetype(font_arial, 24)
draw = ImageDraw.Draw(new_logo)
text = "Informatika JOSSS!"
text_width = draw.textlength(text, font)
text_height = draw.textlength(text, font)
text_position = ((new_logo.width - text_width) // 2,
                 new_logo.height - text_height + 158)
draw.text(text_position, text, font=font, fill="black")

finalBg.paste(new_logo, (600, 300))

# TODO 6 : Simpan gambar dengan nama "tugas_praktikum_enam.jpg"
finalBg.show()
finalBg.save("assets/tugas_praktikum_enam.jpg")
