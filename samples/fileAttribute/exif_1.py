from exif import Image
from function.core import format_dms_coordinates, dms_coordinates_to_dd_coordinates, degrees_to_direction

with open('./photo/tree_2.jpg', 'rb') as tree_2_file:
    tree_2_photo = Image(tree_2_file)
with open('./photo/tree_3.jpg', 'rb') as tree_3_file:
    tree_3_photo = Image(tree_3_file)
images = [tree_2_photo, tree_3_photo]

# Проверить что фото содержит exif
for index, image in enumerate(images):
    if image.has_exif:
        status = f'содержит EXIF (версия {image.exif_version}).'
    else:
        status = 'не содержит EXIF.'
    print(F'Image {index + 1} {status}')
print('')

# Отображает список тегов каждого объекта Image
image_members = []
for image in images:
    image_members.append(dir(image))
for index, image_member_list in enumerate(image_members):
    print(f'Image {index} содержит {len(image_member_list)} тегов:')
    print(f'{image_member_list}')
print('')

# Стандартный метод set() для определения общих элементов изображения
common_members = set(image_members[0]).intersection(set(image_members[1]))
common_members_sorted = sorted(list(common_members))
print('Изображения имеют одинаковые теги:')
print(f'{common_members_sorted}')
print('')

# Марка и модель устройства, на котором было сделано фото
for index, image in enumerate(images):
    print(f'Устройство - Image {index + 1}')
    print('--------------------------------')
    print(f'Производитель: {image.get('make', 'Нет данных')}')
    print(f'Модель: {image.get('model', 'Нет данных')}')
    # Дополнительная информация об устройствах
    print(f'Производитель линзы: {image.get('lens_make', 'Нет данных')}')
    print(f'Модель линзы: {image.get('lens_model', 'Нет данных')}')
    print(f'Характеристики линзы: {image.get('lens_specification', 'Нет данных')}')
    print(f'OS версия: {image.get('software', 'Нет данных')}')
    # Код отображает дату и время, когда была сделана каждая из фотографий
    print(f'{image.datetime_original}.{image.subsec_time_original} {image.get('offset_time', '')}')
    # Получение GPS-координат фотографии
    print(f'GPS широта: {format_dms_coordinates(image.gps_latitude)} {image.gps_latitude_ref} '
          f'({dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)})')
    print(f'GPS долгота: {format_dms_coordinates(image.gps_longitude)} {image.gps_longitude_ref} '
          f'({dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)})')
    print(f'GPS высота: {image.gps_altitude}, {image.gps_altitude_ref}')
    print(f'GPS время: {image.get('gps_timestamp')}, {image.get('gps_timestamp_ref', 'Нет данных')}')
    print(f'GPS скорость: {image.get('gps_speed')}, {image.get('gps_speed_ref')}')
    print(f'GPS путь: {image.get('gps_track')}, {image.get('gps_track_ref')}')
    print(f'GPS направление: {image.get('gps_img_direction')}, {image.get('gps_img_direction_ref')}')
    # Получение координат компаса
    # print(f'Компас: {degrees_to_direction(image.get('gps_img_direction'))} ({image.get('gps_img_direction')}°)')
    print('')

# Изменить атрибуты фото
images[0].set('make', 'Samsung')
images[0].model = 'Galaxy S10'
with open('./photo/tree_2.jpg', 'wb') as updated_hotel_file:
    updated_hotel_file.write(images[0].get_file())

# Заполнение неиспользуемых тегов EXIF
