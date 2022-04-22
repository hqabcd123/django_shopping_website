import base64

def img_base64_convert(url_list, img_name):
    #print(url)
    base64_img_list = {}
    i = 0
    for url in url_list:
        with open(url, 'rb')as img_file:
            #base64.b16encode(img_file.read())
            temp = base64.b16encode(img_file.read())
            if i == 0:
                print (temp)
            temp = temp.decode('ascii')
            # base64_img_list.append({img_name[i]: temp})
            base64_img_list[img_name[i]] = temp
            i = i + 1
    #print (base64_img_list)
    return base64_img_list