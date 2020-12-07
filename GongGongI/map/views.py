from django.shortcuts import render
import json

def showmap(request):
    # with open('static/json/attractions.json', encoding='utf-8') as json_file:
    #     attractions = json.load(json_file)['response']['body']['items']['item']
    #
    # attractiondict = []
    # for attraction in attractions:
    #     if attraction.get('mapx'):
    #         content = {
    #             "title": attraction['title'],
    #             "mapx": str(attraction['mapx']),
    #             "mapy": str(attraction['mapy'])
    #         }
    #         attractiondict.append(content)
    # attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'map/map.html')#, {'attractionJson': attractionJson})


# Create your views here.
