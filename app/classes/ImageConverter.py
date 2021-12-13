import base64

def base64_to_img(stringbase64, id):
    img_path = f'app/images/{id}.jpeg'
    decodeit = open(img_path, 'wb')
    decodeit.write(base64.b64decode(stringbase64))
    decodeit.close()
    return img_path
