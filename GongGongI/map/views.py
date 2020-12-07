from django.shortcuts import render
import json

def showattractions(request):
    #with와 json 모듈을 이용해 Json파일 불러오기
    with open('static/json/attractions.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)['response']['body']['items']['item']

    attractiondict = []
    #불러온 json 객체들 중 필요한 데이터만 뽑기
    for attraction in attractions:
        if attraction.get('mapx'):
            content = {
                "title": attraction['title'],
                "mapx": str(attraction['mapx']),
                "mapy": str(attraction['mapy']),
                "addr1": str(attraction['addr1']),
            }
            if attraction.get('tel'):
                content['tel'] = str(attraction['tel'])
            else:
                content['tel'] = ''
            attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'map/map.html', {'attractionJson': attractionJson})


# Create your views here.
