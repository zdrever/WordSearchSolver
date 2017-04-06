import requests

def txt_array_from_jpg(jpeg):
    writefile = "array.txt"
    key = '' # GET KEY

    POSTURL = 'http://api.newocr.com/v1/upload?key=api_key'#GET API KEY BEFORE RUNNING
    files = {jpeg: open(jpeg, 'rb')}

    req = requests.post(POSTURL, files = files)
    if r.status_code != 200:
        raise Exception("API call failed (POST)")

    print("r.headers", r.headers)
    print("r.content", r.content)

    f_ID = r.content["file_id"]

    print("f_ID", f_ID)
    GETURL = 'http://api.newocr.com/v1/ocr?key=' + key + '&file_id=' + file_id '&page=1&lang=eng&psm=3'
    data = requests.get(GETURL)

    if data.status_code != 200:
        raise Exception("API call failed (GET)")

    print("data.headers", data.headers)
    print("data.content", data.content)

    text = data.content["text"]

    with open(writefile, 'w') as f:
        f.write(text)
        f.close


def txt_words_from_jpg(jpeg):
    writefile = "words.txt"

    POSTURL = 'http://api.newocr.com/v1/upload?key=api_key'#GET API KEY BEFORE RUNNING
    files = {jpeg: open(jpeg, 'rb')}

    req = requests.post(POSTURL, files = files)
    if r.status_code != 200:
        raise Exception("API call failed (POST)")

    print("r.headers", r.headers)
    print("r.content", r.content)

    f_ID = r.content["file_id"]

    print("f_ID", f_ID)
    GETURL = 'http://api.newocr.com/v1/ocr?key=' + key + '&file_id=' + file_id '&page=1&lang=eng&psm=3'
    data = requests.get(GETURL)

    if data.status_code != 200:
        raise Exception("API call failed (GET)")

    print("data.headers", data.headers)
    print("data.content", data.content)

    text = data.content["text"]

    with open(writefile, 'w') as f:
        f.write(text)
        f.close
