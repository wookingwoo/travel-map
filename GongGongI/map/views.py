from django.shortcuts import render
import json

def showattractions():
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
    return attractionJson

def showsaferests():
    with open('static/json/safe_restaurant.json', encoding='utf-8') as json_file:
        safe_restaurants = json.load(json_file)['data']
    restaurantdict = []
    #불러온 json 객체들 중 필요한 데이터만 뽑기
    for restaurant in safe_restaurants:
        content = {
            "title": restaurant['title'],
            "tel": str(restaurant['tel']),
            "menu": str(restaurant['category']),
            "addr": str(restaurant['addr']),
        }
        restaurantdict.append(content)
    saferestaurantJson = json.dumps(restaurantdict, ensure_ascii=False)
    return saferestaurantJson

def showgoodprices():
    with open('static/json/good_price.json', encoding='utf-8') as json_file:
        good_prices = json.load(json_file)['data']
    goodpricedict = []
    #불러온 json 객체들 중 필요한 데이터만 뽑기
    for good_price in good_prices:
        content = {
            "title": good_price['title'],
            "tel": str(good_price['tel']),
            "menu": str(good_price['category']),
            "addr": str(good_price['addr']),
            "mainmenu": str(good_price['mainmenu']),
            "price": str(good_price['price']),
        }
        goodpricedict.append(content)
    goodpriceJson = json.dumps(goodpricedict, ensure_ascii=False)
    return goodpriceJson

def showmarkets():
    with open('static/json/markets.json', encoding='utf-8') as json_file:
        markets = json.load(json_file)['data']
    marketdict = []
    #불러온 json 객체들 중 필요한 데이터만 뽑기
    for market in markets:
        content = {
            "title": market['title'],
            "menu": str(market['mainmenu']),
            "addr": str(market['addr1']),
        }
        marketdict.append(content)
    marketsJson = json.dumps(marketdict, ensure_ascii=False)
    return marketsJson

def showmarks(request):
    attractionJson = showattractions()
    saferestaurantJson = showsaferests()
    goodpriceJson = showgoodprices()
    marketsJson = showmarkets()

    return render(request, 'map/map.html', {'attractionJson': attractionJson, 'saferestaurantJson': saferestaurantJson,
                                            'goodpriceJson': goodpriceJson, 'marketsJson': marketsJson})

