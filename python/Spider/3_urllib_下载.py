import urllib.request as ur

# 下载网页
# url_page = 'http://www.baidu.com'
# ur.urlretrieve(url_page , 'baidu.html')

#下载图片
# url_img = 'https://img1.baidu.com/it/u=2835220188,4227150300&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=585'
# ur.urlretrieve(url=url_img , filename='lisa.jpg')

#下载视频
url_video = 'https://vd2.bdstatic.com/mda-nheeq5900isz00z3/sc/cae_h264/1660559392745397918/mda-nheeq5900isz00z3.mp4?v_from_s=bdapp-bdappcore-nanjing'
ur.urlretrieve(url_video , 'v1.mp4')

