from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers

class Cloud():

    def appraise(self, file):
        appid = '1256911928'
        secretid = 'AKIDSq495t2JbjhVRUIXMIUkcc6VpNo5QKv0'
        secretkey = 'Ac4mbinjcsLGh1oVxj1jXknfh6c1GQQS'
        bucket = 'BUCKET'
        client = Client(appid, secretid, secretkey, bucket)
        client.use_http()
        client.set_timeout(30)
        files = []
        files.append(file)
        print(files)
        people = client.idcard_detect(CIFiles(files), 0)["result_list"][0]['data']
        print(people)
        return people




