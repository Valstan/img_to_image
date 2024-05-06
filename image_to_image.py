from PIL import Image

# Откуда брать изображения
path_in_file = "d:/old/"  # "d:/2222222/"
name_in_file = "old - "  # "S2360033.MP4"

# Где лежит накладываемое изображение
img_insert = Image.open('c:/Users/valstan/Downloads/Ознакомлен Симонов печать.png')

# Получить размеры вставляемого изображения
img_insert_width, img_insert_height = img_insert.size

# Куда сохранять новые изображения
path_out_file = "d:/rezult/"
name_out_file = "out_video.mp4"

# Расширение файлов, например '.png'
file_ext = '.tif'

# Смещение в пикселях по ширине от левого края
left_offset = 10
right_offset = 10


for a in range(1,138):  # На единицу больше чем число изображений
    if a == 0:
        continue
    name_image = name_in_file + '000' + str(a)
    if 10 <= a < 100:
        name_image = name_in_file + '00' + str(a)
    elif 100 <= a < 1000:
        name_image = name_in_file + '0' + str(a)

    old_image = Image.open(path_in_file + name_image + file_ext)

    # Получить размеры изображения
    old_image_width, old_image_height = old_image.size

    # Координаты правого нижнего угла
    right_bottom = (old_image_width - 1, old_image_height - 1)

    # Смещение в пикселях от левого верхнего угла
    # два раза img это чтобы прозрачность сработала
    old_image.paste(img_insert,
                    (old_image_width - img_insert_width - left_offset,
                     old_image_height- img_insert_height - right_offset),
                    img_insert)
    old_image.save(path_out_file + name_image + file_ext)
    old_image.close()

    print(name_image)
