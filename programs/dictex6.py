

info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

alist = [10,20,30]
print(type(alist))
print(isinstance(alist,list))
print(isinstance(alist,dict))

for key,value in info.items():
    if isinstance(value,str):
        print(key.upper().ljust(20),":",value)
    if isinstance(value,dict):
        for skey,svalue in value.items():
            finalkey = key + " " +  skey
            print(finalkey.upper().ljust(20),":",svalue)

