from PIL import Image

# Откуда брать изображения
old_patch = '' # Пример 'first/second/' слеш не может быть вначале или один

# Где лежит накладываемое изображение
overlay_path = ''

# Куда сохранять новые изображения
new_patch = ''

# Расширение файлов, например '.png'
file_ext = ''

# Смещение в пикселях по ширине от левого края
left_offset = 0
right_offset = 0

img = Image.open('00001111.png')

name = "24.03.15 №60 КОН.АНАЛИЗ - "

for a in range(1,441):
    if a == 0:
        continue
    name_image = name + '000' + str(a)
    if 10 <= a < 100:
        name_image = name + '00' + str(a)
    elif 100 <= a < 1000:
        name_image = name + '0' + str(a)

    old_image = Image.open(old_patch + name_image + file_ext)

    # Смещение в пикселях от левого верхнего угла
    # два раза img это чтобы прозрачность сработала
    old_image.paste(img, (1420, 2960), img)
    old_image.save('5678/' + name_image + '.png')
    old_image.close()

    print(name_image)
