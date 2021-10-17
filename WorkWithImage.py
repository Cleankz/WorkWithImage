from PIL import Image, ImageDraw, ImageFont
from file_reader import File_reader


def change_format(ext_1,ext_2):
    """ Эта функция изменяет расширение файлов в директории(ext_1)  на заданное (ext_2) """
    file_in_dir = File_reader(ext_1)
    new_ext_files = change_str(ext_1)
    for i in range(len(file_in_dir)):
        myimage = Image.open(file_in_dir[i])
        myimage.save(new_ext_files[i],ext_2)
    return True

def change_str(extention):
    """ Эта функция заменяет расширение файлов в массиве   на заданное (extention) """
    array = File_reader(extention)
    new_array =[]
    for i in range(len(array)):
        if extention in array[i]:
            changed_str  = array[i].replace(".jpg", ".png")
            new_array.append(changed_str)
    return new_array

def get_text_size(text):
    """Эта функция возвращает размер текста в пикселях"""
    font = ImageFont.truetype("123.ttf", 1)
    text_size = 0
    for char in text:
        text_size += font.getsize(char)[0]
    return text_size


def print_quadro(image_name):
    """Эта фнукция рисует белый квадрат посреди изображения и добавляет туда текст"""
    myimage = Image.open(image_name)
    draw = ImageDraw.Draw(myimage)
    quadro = (20, 20, 240, 240)
    size = myimage.size
    text = 'Hello,\nWorld!'
    text_size = get_text_size(text)
    draw.rectangle([(size[0]-quadro[0])/2,
                    (size[1]-quadro[1])/2,
                    (size[0]+quadro[0])/2,
                    (size[1]+quadro[1])/2],
                   fill=(255,255,255))
    draw.multiline_text(([(size[0]-text_size)/2,
                          (size[1]-text_size)/2,
                          (size[0]+text_size)/2,
                          (size[1]+text_size)/2]),
                        text,fill = 'black')
    myimage.save("test2.jpg", "JPEG")
    del draw
    return myimage.show()


print(change_format('.jpg','PNG'))
#print_quadro('123.jpg')
