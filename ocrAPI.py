import requests

def text_array_from_image(imagefile):
    print("Get array text")
    writefile = "array.txt"
    key = '6085b04c132cb3bf1b3cfd998e901d6e' # GET KEY
    POSTURL = 'http://api.newocr.com/v1/upload?key=' + key #GET API KEY BEFORE RUNNING

    multipartdata = {"name":"file", "filename":imagefile, "Content-Type":"image/jpeg"}
    req = requests.post(POSTURL, files=multipartdata)

    if req.status_code != 200:
        raise Exception('API call failed (POST) [{} {}]'.format(req.status_code, req.reason))

    print("r.headers:", req.headers)
    print("r.content:", req.content)

    f_ID = req.content["file_id"]

    print("f_ID", f_ID)
    GETURL = 'http://api.newocr.com/v1/ocr?key=' + key + '&file_id=' + f_ID + '&page=1&lang=eng&psm=3'
    data = requests.get(GETURL)

    if data.status_code != 200:
        raise Exception('API call failed (GET) [{} {}]'.format(req.status_code, req.reason))

    print("data.headers:", data.headers)
    print("data.content:", data.content)

    text = data.content["text"]

    with open(writefile, 'w') as f:
        f.write(text)
        f.close()



def text_wordlist_from_image(imagefile):
    print("Get words text")
    writefile = "words.txt"
    key = '6085b04c132cb3bf1b3cfd998e901d6e'

    POSTURL = 'http://api.newocr.com/v1/upload?key=' + key#GET API KEY BEFORE RUNNING

    multipartdata = {"name":"file", "filename":imagefile, "Content-Type":"image/jpeg"}

    req = requests.post(POSTURL, files=multipartdata)

    if req.status_code != 200:
        raise Exception('API call failed (POST) [{} {}]'.format(req.status_code, req.reason))

    print("r.headers:", req.headers)
    print("r.content:", req.content)

    f_ID = req.content["file_id"]

    print("f_ID", f_ID)
    GETURL = 'http://api.newocr.com/v1/ocr?key=' + key + '&file_id=' + f_ID + '&page=1&lang=eng&psm=3'
    data = requests.get(GETURL)

    if data.status_code != 200:
        raise Exception('API call failed (GET) [{} {}]'.format(data.status_code, data.reason))

    print("data.headers:", data.headers)
    print("data.content:", data.content)

    text = data.content["text"]

    with open(writefile, 'w') as f:
        f.write(text)
        f.close()
