from PIL import Image

# Откуда брать изображения
path_in_file = "d:/old/"  # "d:/old/"
name_in_file = "old - "  # "old - "

# Где лежит накладываемое изображение 'c:/Users/valstan/Downloads/Ознакомлен Симонов печать.png'
img_insert = Image.open('c:/Users/valstan/Downloads/Ознакомлен Симонов печать.png')

# Получить размеры вставляемого изображения
img_insert_width, img_insert_height = img_insert.size

# Куда сохранять новые изображения "d:/rezult/"
path_out_file = "d:/rezult/"

# Расширение файлов, например '.png'
file_ext = '.tif'

# Смещение в пикселях от края
width_offset = 10  # по горизонтали
height_offset = 10  # по вертикали

# Режим вставки - 1 левый верхний, 2 правый верхний, 3 левый нижний, 4 правый нижний
ugol = 4

# Сколько картинок нужно обработать
count_pages = 5

for a in range(1,count_pages + 1):  # На единицу больше чем число изображений
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
    if ugol == 1:
        old_image.paste(img_insert,
                        (width_offset,
                         height_offset),
                        img_insert)
        old_image.save(path_out_file + name_image + file_ext)
    if ugol == 2:
        old_image.paste(img_insert,
                        (old_image_width - img_insert_width - width_offset,
                         height_offset),
                        img_insert)
        old_image.save(path_out_file + name_image + file_ext)
    if ugol == 3:
        old_image.paste(img_insert,
                        (width_offset,
                         old_image_height - img_insert_height - height_offset),
                        img_insert)
        old_image.save(path_out_file + name_image + file_ext)

    if ugol == 4:
        old_image.paste(img_insert,
                        (old_image_width - img_insert_width - width_offset,
                         old_image_height- img_insert_height - height_offset),
                        img_insert)
        old_image.save(path_out_file + name_image + file_ext)

    old_image.close()

    print(name_image)
