from util.encode_decode import toBase62

def tolist(collection=None, host=None):
    res_list = []
    for obj in collection:
        encode = toBase62(obj.id)
        url = host + '/' + encode
        res_list.append( {"url" : url ,"creation_date": str(obj.creation_date), "visited": obj.visitcount})
    return res_list
