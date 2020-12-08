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

    with open('static/json/safe_restaurant.json', encoding='utf-8') as json_file:
        safe_restaurants = json.load(json_file)['data']

    restaurantdict = []
    #불러온 json 객체들 중 필요한 데이터만 뽑기
    for restaurant in safe_restaurants:
        content = {
            "title": restaurant['사업장명'],
            "tel": str(restaurant['전화번호']),
            "menu": str(restaurant['업종상세']),
            "addr": str(restaurant['주소']),
        }
    restaurantdict.append(content)
    print(restaurantdict)

    with open('static/json/good_price.json', encoding='utf-8') as json_file:
        good_prices = json.load(json_file)['data']


    with open('static/json/markets.json', encoding='utf-8') as json_file:
        markets = json.load(json_file)['data']


    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    saferestaurantJson = json.dumps(restaurantdict, ensure_ascii=False)
    goodpriceJson = json.dumps(good_prices, ensure_ascii=False)
    marketsJson = json.dumps(markets, ensure_ascii=False)

    return render(request, 'map/map.html', {'attractionJson': attractionJson, 'saferestaurantJson': saferestaurantJson,
                                            'goodpriceJson': goodpriceJson, 'marketsJson': marketsJson})





# Create your views here.
