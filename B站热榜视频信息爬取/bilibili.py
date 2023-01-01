import asyncio
import time
import pymysql
import requests
import aiohttp


async def main():
    for i in url:
        task = [asyncio.create_task(zhuaqu(i))]
    await asyncio.wait(task)


async def zhuaqu(url):
    cursor.execute('truncate table bilibili')
    cursor.execute('SET NAMES utf8mb4;')
    item = {'BV': "", 'title': "", 'tname': "", 'pic': "", 'desc': "", 'upname': "", 'upface': "", 'short_link': "",
            'view': "", 'favorite': "", 'coin': "", 'share': "", 'like': ""}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as resp:
            data = await resp.json(encoding='utf-8')
            list = data['data']['list']
            for i in data['data']['list']:
                item['BV'] = i['short_link'].split("/")[-1]
                item['title'] = i['title'].replace('"', '')
                item['upname'] = i['owner']['name']
                item['pic'] = i['pic']
                item['desc'] = i['desc']
                item['upface'] = i['owner']['face']
                item['short_link'] = i['short_link']
                item['tname'] = i['tname']
                item['view'] = i['stat']['view']
                item['favorite'] = i['stat']['favorite']
                item['coin'] = i['stat']['coin']
                item['share'] = i['stat']['share']
                item['like'] = i['stat']['like']
                try:
                    cursor.execute(
                        'insert into bilibili values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",'
                        '"%s")' % (
                            item['BV'], item['title'], item['upname'], item['upface'], item['pic'], item['desc'],
                            item['short_link'], item['tname'],
                            item['view'], item['favorite'], item['coin'], item['share'], item['like']))
                    conn.commit()
                except Exception as e:
                    print(e)
                conn.rollback()


if __name__ == '__main__':
    t1 = time.perf_counter()
    conn = pymysql.connect(user='root', password='123456', port=3306, charset='utf8', database='b站视频', host='127.0.0.1')
    cursor = conn.cursor()
    url = []
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70 '
    }
    for i in range(1, 50):
        url.append(f'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={i}')
    asyncio.get_event_loop().run_until_complete(main())
