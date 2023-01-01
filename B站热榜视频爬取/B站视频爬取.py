import os
import time

import aiohttp
import requests
import asyncio
import re
import json
from lxml import etree
import subprocess
from tqdm import tqdm
import aiofiles


# =============================================================================================
# 输入BV号爬取
# BV=input()
# header = {
#         'referer': "http://www.bilibili.com/",
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
#         'cookie': "buvid3=7FE10E98-5253-46EB-9780-D3992422C761148808infoc; LIVE_BUVID=AUTO3816339517344834; "
#                   "CURRENT_BLACKGAP=0; blackside_state=0; fingerprint3=7ab8bd1423058ca8535916339732f6d6; "
#                   "fingerprint_s=ea8300ae807e7ce35822c0ce36bd04d3; buvid_fp_plain=undefined; nostalgia_conf=-1; "
#                   "hit-dyn-v2=1; PVID=1; is-2022-channel=1; "
#                   "buvid4=005AA5A2-A41A-2187-69FF-BB6046195F1976451-022012415-g%2F7ryolvhgnQghovjiNV6g%3D%3D; "
#                   "i-wanna-go-back=-1; DedeUserID=57172925; DedeUserID__ckMd5=bb057fda04faae4f; b_ut=5; "
#                   "_uuid=63D78A910-64FD-54C4-1210B-D10FA3E84992E83194infoc; "
#                   "buvid_fp=7FE10E98-5253-46EB-9780-D3992422C761148808infoc; b_nut=100; hit-new-style-dyn=0; rpdid=|("
#                   "umYRmJl|lY0J'uYY)l)lkRm; CURRENT_FNVAL=4048; b_lsid=1F5769D8_185494476B1; "
#                   "fingerprint=13e30fdb583d66336244d120532bf654; CURRENT_QUALITY=32; "
#                   "bp_video_offset_57172925=743610142239490000; SESSDATA=d9ce1f4e%2C1687533067%2C85e9e%2Ac1; "
#                   "bili_jct=ab9aa37b2ba256b5004d68173c8a6896; sid=8i2651ac; innersign=0 "
#
# } response = requests.get(f'https://www.bilibili.com/video/{BV}', headers=header)
# html = response.text
# html_data =re.findall('<script>window.__playinfo__=(.*?)</script>', html)[0]
# json_data = json.loads(html_data) video_url =json_data['data']['dash']['video'][0]['baseUrl']
# audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
# html1= etree.HTML(response.text)
# title = html1.xpath('/html/body/div[2]/div[4]/div[1]/div[1]/h1/text()')[0]
# video_content = requests.get(video_url, headers=header).content
# audio_content = requests.get(audio_url,headers=header).content
# with open(f'D:/B站视频/{title}.mp4', mode='wb') as f:
#     f.write(video_content)
# with open(f'D:/B站视频/{title}.mp3', mode='wb') as f:
#     f.write(audio_content)
# cmd = f"ffmpeg -i D:/B站视频/{title}.mp4 -i D:/B站视频/{title}.mp3 -c:v copy -c:a aac -strict experimental D:/B站视频/{title}_output.mp4 "
# subprocess.run(cmd, shell=True)
# os.remove(f'D:/B站视频/{title}.mp3')
# os.remove(f'D:/B站视频/{title}.mp4')
# print("over")
# ============================================================================================= 热榜视频爬取 async
async def download_video(video_src, session, title):
    async with session.get(video_src, headers=header) as resp:
        async with aiofiles.open(f'D:/B站视频/{title}.mp4', mode="wb") as f:
            await f.write(await resp.content.read())


async def download_audio(audio_src, session, title):
    async with session.get(audio_src, headers=header) as resp:
        async with aiofiles.open(f'D:/B站视频/{title}.mp3', mode="wb") as f:
            await f.write(await resp.content.read())


async def main():
    background_task = set()
    for i in tqdm(url):
        task = asyncio.create_task(getsrc(i))
        background_task.add(task)
        task.add_done_callback(background_task.discard)
    await asyncio.wait(background_task)


async def video_info(video_url, session, title):
    async with session.get(video_url, headers=header) as resp:
        html = await resp.text()
        html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', html)[0]
        HTML = etree.HTML(html)
        json_data = json.loads(html_data)
        video_src = json_data['data']['dash']['video'][0]['baseUrl']
        audio_src = json_data['data']['dash']['audio'][0]['baseUrl']
        await download_audio(audio_src, session, title)
        await download_video(video_src, session, title)
        # he_bing(title)


async def getsrc(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as resp:
            data = await resp.json(encoding='utf-8')
            for i in data['data']['list']:
                BV = i['short_link'].split("/")[-1]
                title = i['title'].replace('"', '')
                video_url = f'http://www.bilibili.com/{BV}'
                await video_info(video_url, session, title)


if __name__ == '__main__':
    url = []
    header = {
        'referer': "http://www.bilibili.com/",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'cookie': "buvid3=7FE10E98-5253-46EB-9780-D3992422C761148808infoc; LIVE_BUVID=AUTO3816339517344834; "
                  "CURRENT_BLACKGAP=0; blackside_state=0; fingerprint3=7ab8bd1423058ca8535916339732f6d6; "
                  "fingerprint_s=ea8300ae807e7ce35822c0ce36bd04d3; buvid_fp_plain=undefined; nostalgia_conf=-1; "
                  "hit-dyn-v2=1; PVID=1; is-2022-channel=1; "
                  "buvid4=005AA5A2-A41A-2187-69FF-BB6046195F1976451-022012415-g%2F7ryolvhgnQghovjiNV6g%3D%3D; "
                  "i-wanna-go-back=-1; DedeUserID=57172925; DedeUserID__ckMd5=bb057fda04faae4f; b_ut=5; "
                  "_uuid=63D78A910-64FD-54C4-1210B-D10FA3E84992E83194infoc; "
                  "buvid_fp=7FE10E98-5253-46EB-9780-D3992422C761148808infoc; b_nut=100; hit-new-style-dyn=0; rpdid=|("
                  "umYRmJl|lY0J'uYY)l)lkRm; fingerprint=13e30fdb583d66336244d120532bf654; CURRENT_QUALITY=80; "
                  "CURRENT_FNVAL=4048; go_old_video=1; bp_video_offset_57172925=745452588730679300; "
                  "SESSDATA=a499f4d8%2C1687955168%2C3320a%2Ac1; bili_jct=f2c2f8df03726a5726a9fd9ec3efc495; "
                  "sid=ed19ca4m; innersign=0 "

    }
    for i in range(1, 50):
        url.append(f'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={i}')
    asyncio.get_event_loop().run_until_complete(main())
    os.system("hebing.py")


# =============================================================================================
# 番剧视频爬取
# resp=requests.get('https://www.bilibili.com/bangumi/play/ep683040')
# print(resp.text)
