def area_volum(length, height, width):

    area = length * width
    area_vol = length * width * height

    return area, area_vol, length,height,width

result = area_volum(1,2,3)
convert_to_list = list(result)
convert_to_list[0] = 4
convert_to_tuple = tuple(convert_to_list)
print(convert_to_tuple)
