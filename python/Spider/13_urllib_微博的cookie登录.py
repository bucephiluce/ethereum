# 适用场景: 数据采集的时候 需要绕过登陆 然后进入到某个页面

headers = {
    # 带冒号的都没有用
    # ':authority':'weibo.com',
    # ':method':'GET',
    # ':path':'/u/page/follow/1195242865',
    # ':scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    # cookie中携带着你的登陆信息 
    'cookie':'SINAGLOBAL=4851259786641.526.1523501117533; XSRF-TOKEN=XRwTxT3LMzy6CU7LVnS8ou1m; login_sid_t=5a8a6933a930e8ca410b32ada21be153; cross_origin_proto=SSL; wb_view_log=1920*10801; _s_tentry=weibo.com; Apache=9940817140641.48.1660804451878; ULV=1660804451884:3:1:1:9940817140641.48.1660804451878:1638761305409; ALF=1692340489; SSOLoginState=1660804489; SCF=Ak88v4o6V2gjH3rFdHHi2kAHQqeLf3escRtTL0hod0C_EFRlecGe8paoCAu-BPUcvw1OlmpZpgLZifKdfVTCUPY.; SUB=_2A25P-a3ZDeRhGeRK6VUQ9yrFwzuIHXVsjpgRrDV8PUNbmtAKLWmhkW9NU00geRxemRml3IWBT-prQQ9Qm2H4Fyjy; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWBF3g9SURw_9VgnOF3DY-.5JpX5KzhUgL.FozXeoMpS0B41hM2dJLoI7_bUgSLMsyDdGHo9Btt; WBPSESS=GebZzzmi-V9tYMt2ZLOzHbwQp1WkUs5DVx591WaUOkRhLW2r6lb5ftHRMztQs_bRAAYZa3J-lq-DRGqPkIh2yTPSIc0VYm2dDu35CXIE4eUgJ1pyx0v8XFsKFL5Rvru3Qn-Zhbp3ZVfCJcMXMuC8RQ==',
    # referer 判断当前路径是不是由上一个路径进来的 一般情况下是做图片防盗链
    'referer':'https://s.weibo.com/',
    'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}