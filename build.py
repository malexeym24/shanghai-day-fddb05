#!/usr/bin/env python3
"""Shanghai one-day site (Tue 27.10.2026 + night flight from PVG T1). Run: python3 build.py -> index.html + page per place.
Facts: en.wikipedia intros, official yugarden.com.cn, english.shanghai.gov.cn, marriott.com.cn, travel guides 2026 (named on pages).
Walking legs: walk.json (OSRM foot), taxi legs: car.json (OSRM car). Photos: fetch_photos.py -> img/, t/, credits.json."""
import json, html, subprocess
from urllib.parse import quote

E = html.escape
HOTEL_Q = "Fairfield by Marriott Shanghai Pudong Eshan Road"
SRC_DATE = subprocess.run(["date", "+%d.%m.%Y %H:%M"], capture_output=True, text=True, env={"TZ": "Asia/Shanghai"}).stdout.strip() + " по Шанхаю"

def gm(q):
    return "https://www.google.com/maps/search/?api=1&query=" + quote(q)

CR = json.load(open("credits.json"))
def credit(f):
    c = CR.get(f, {})
    return f'{c.get("author") or "автор на странице файла"}, {c.get("lic", "")}', c.get("page", "#")

CAP = {
 "yu-1.jpg": "Павильон над прудом в Yu Garden", "yu-2.jpg": "Чайный домик Huxinting посреди пруда, рядом с садом",
 "yu-3.jpg": "Крытая галерея вдоль воды", "yu-4.jpg": "Двухэтажный зал над прудом", "yu-5.jpg": "Искусственные скалы из пористого камня",
 "yu-6.jpg": "Камни, пруд и павильоны", "yu-7.jpg": "Ворота со львами внутри сада",
 "xlb-1.jpg": "Сяолунбао в Nanxiang Mantou Dian", "xlb-2.jpg": "Очередь в Nanxiang у храма бога города",
 "xlb-3.jpg": "Сяолунбао с крабом", "xlb-4.jpg": "Корзинки сяолунбао на столе",
 "bund-1.jpg": "Здание банка HSBC (1923, слева) и Таможня с часовой башней", "bund-2.jpg": "Набережная Bund: широкий променад вдоль домов",
 "bund-3.jpg": "Бывшее здание HSBC на закате", "bund-4.jpg": "Колонны бывшего здания HSBC, сейчас банк SPDB",
 "bund-5.jpg": "Бронзовый бык на Bund", "bund-6.jpg": "Закат над зданиями Bund, вид через реку",
 "waibaidu-1.jpg": "Мост Waibaidu и небоскрёбы Пудуна", "waibaidu-2.jpg": "Стальные фермы моста над Suzhou Creek",
 "waibaidu-3.jpg": "Пешеходная дорожка по мосту", "waibaidu-4.jpg": "Мост, за ним Oriental Pearl Tower",
 "ljz-1.jpg": "Lujiazui с реки: Oriental Pearl Tower и Shanghai Tower", "ljz-2.jpg": "Небоскрёбы Lujiazui над рекой Huangpu",
 "ljz-3.jpg": "Высотки Lujiazui с пешеходного моста",
 "tower-1.jpg": "Shanghai Tower, 632 м", "tower-2.jpg": "Пудун: Oriental Pearl Tower и Shanghai Tower",
 "tower-3.jpg": "Смотровая 118 этажа, на окне «118F 546M»", "tower-4.jpg": "Вид со смотровой: излучина реки и Oriental Pearl Tower",
 "tower-5.jpg": "Вид вниз на Lujiazui и реку", "tower-6.jpg": "Река Huangpu сверху",
 "wukang-1.jpg": "Wukang Mansion (1924, архитектор László Hudec)", "wukang-2.jpg": "Дом клином на перекрёстке",
 "wukang-3.jpg": "Wukang Mansion со стороны Huaihai Road", "wukang-4.jpg": "Wukang Road у Huaihai Road",
 "wukang-5.jpg": "Wukang Road: особняки и деревья",
 "anfu-1.jpg": "Особняк театра Shanghai Dramatic Arts Center, Anfu Road 284", "anfu-2.jpg": "Платаны на Hengshan Road, соседней улице концессии",
 "anfu-3.jpg": "Hengshan Road: так выглядят улицы бывшей концессии", "anfu-4.jpg": "Старый особняк, Anfu Road 201",
 "museum-1.jpg": "Shanghai Museum на People's Square", "museum-2.jpg": "Музей и фонтан на People's Square",
 "museum-3.jpg": "Атриум внутри музея",
 "pvg-1.jpg": "Зал вылета Terminal 1", "pvg-2.jpg": "Terminal 1 снаружи", "pvg-3.jpg": "Terminal 1, вид сбоку",
}

def cap(f):
    a, u = credit(f)
    return f'{E(CAP.get(f, ""))}. <a href="{E(u)}">{E(a)}</a>'

# ---------- places ----------
P = [
 dict(id="yu", n=1, name="Yu Garden и старый город", zh="豫园", ll=(31.22893, 121.48798), q="Yu Garden Shanghai",
      photos=["yu-1.jpg", "yu-2.jpg", "yu-3.jpg", "yu-4.jpg", "yu-5.jpg", "yu-6.jpg", "yu-7.jpg"],
      sub="Классический китайский сад 1559 года, вокруг старый город",
      what=["Сад заложил в 1559 году, при династии Мин, чиновник Pan Yunduan: для отца-министра на старость. «Yu» значит «радовать родителей». Сейчас это памятник под охраной государства: больше 40 видовых точек, павильоны, пруды, искусственные скалы.",
            "Главная реликвия - камень Exquisite Jade Rock (玉玲珑): пористая глыба 3,3 м и 5 тонн. По легенде её везли в императорский сад династии Сун, лодка затонула, и камень достали из реки Huangpu.",
            "Вплотную к саду, без билета: чайный домик Huxinting посреди пруда, храм бога города (City God Temple) и базар Yuyuan."],
      facts=[("Часы", "9:00-16:30, вход до 16:00"), ("Выходной", "понедельник (во вторник открыт)"),
             ("Билет", "40 ¥ (высокий сезон, сентябрь-ноябрь)"), ("Где купить", "кассы у северных и южных ворот или мини-программа «上海豫园»"),
             ("С собой", "паспорт"), ("На месте", "1-1,5 ч")],
      src="официальный сайт yugarden.com.cn (часы, кассы, цены); история - Wikipedia",
      how=["Такси от отеля 6 км, 15-20 мин днём. Показать водителю: <b>豫园 北门 · 福佑路168号</b> (северные ворота).",
           "Метро: станция Yuyuan Garden, линии 10 и 14."],
      near=["nanxiang", "bund"]),
 dict(id="nanxiang", n=2, name="Обед: сяолунбао в Nanxiang", zh="南翔馒头店", ll=(31.22853, 121.48710), q="Nanxiang Mantou Dian Yu Garden Shanghai",
      photos=["xlb-1.jpg", "xlb-2.jpg", "xlb-3.jpg", "xlb-4.jpg"],
      sub="Пельмени с бульоном внутри, рядом с садом",
      what=["Сяолунбао - маленькие пельмени с бульоном внутри, их готовят на пару в бамбуковых корзинках. Считается, что они родом из Шанхая, шанхайский вариант называют Nanxiang.",
            "Nanxiang Mantou Dian - известная пельменная на базаре у Yu Garden. По путеводителю 2026 года очередь к окну на вынос 45-60 мин, лучше прийти пораньше. Залы наверху дороже: на верхнем этаже около 200-500 ¥ на человека."],
      facts=[("Очередь", "45-60 мин к окну на вынос (путеводитель 2026)"), ("На месте", "40-60 мин")],
      src="путеводитель wanderinchina.com (2026); о сяолунбао - Wikipedia. Часы работы я не проверял",
      how=["3 мин пешком от Yu Garden."], near=["yu", "bund"]),
 dict(id="bund", n=3, name="Набережная Bund", zh="外滩", ll=(31.2400, 121.4880), q="The Bund Shanghai",
      photos=["bund-1.jpg", "bund-2.jpg", "bund-3.jpg", "bund-4.jpg", "bund-5.jpg"],
      sub="Банки и конторы 1920-30-х вдоль реки",
      what=["С 1860-х по 1930-е здесь был финансовый центр иностранных концессий Шанхая. Вдоль улицы Zhongshan East 1st Road стоят здания в стилях неоклассики, ар-деко, барокко и готики, напротив через реку - небоскрёбы Lujiazui.",
            "Самые узнаваемые - бывшее здание банка HSBC (1923) с куполом и Таможня с часовой башней рядом. Вдоль домов идёт широкий приподнятый променад у воды."],
      facts=[("Вход", "бесплатно, всегда открыто"), ("Прогулка", "от южного конца до Peace Hotel 1,1 км (15 мин), ещё 8 мин до моста Waibaidu")],
      src="Wikipedia (The Bund); расстояния - OSRM",
      how=["От Yu Garden 10 мин пешком до южного конца набережной.", "Такси: <b>和平饭店 · 南京东路20号</b> (Peace Hotel, середина набережной)."],
      near=["waibaidu", "riverside"]),
 dict(id="waibaidu", n=4, name="Мост Waibaidu", zh="外白渡桥", ll=(31.24531, 121.48574), q="Waibaidu Bridge Shanghai",
      photos=["waibaidu-1.jpg", "waibaidu-2.jpg", "waibaidu-3.jpg", "waibaidu-4.jpg"],
      sub="Стальной мост 1908 года в конце Bund",
      what=["Первый в Китае цельностальной мост, открыт 20 января 1908 года у впадения Suzhou Creek в Huangpu. Один из символов Шанхая, с 1994 года - охраняемый памятник архитектуры.",
            "Северный конец Bund: отсюда хороший вид на набережную и на небоскрёбы Пудуна."],
      facts=[("Вход", "бесплатно"), ("На месте", "15-20 мин")], src="Wikipedia (Waibaidu Bridge)",
      how=["8 мин пешком от Peace Hotel на север по набережной.", "Оттуда 15 мин пешком до метро East Nanjing Road."],
      near=["bund", "riverside"]),
 dict(id="riverside", n=5, name="Набережная Lujiazui: вид на Bund", zh="陆家嘴滨江", ll=(31.23841, 121.49173), q="Lujiazui Riverside Promenade Shanghai",
      photos=["ljz-1.jpg", "bund-6.jpg", "ljz-2.jpg", "ljz-3.jpg"],
      sub="Другой берег: Bund через реку, закат за ним",
      what=["Lujiazui - полуостров в излучине реки Huangpu. С начала 1990-х здесь строят новый финансовый район, прямо напротив старого Bund.",
            "С набережной видно весь Bund через реку. Солнце 27.10 садится в 17:10, на западе - со стороны Bund."],
      facts=[("Вход", "бесплатно"), ("Закат 27.10", "17:10")], src="Wikipedia (Lujiazui); закат - open-meteo",
      how=["Метро Line 2 (зелёная) от East Nanjing Road 1 остановка до Lujiazui, дальше 13 мин пешком к реке."],
      near=["tower", "bund"]),
 dict(id="tower", n=6, name="Shanghai Tower, 118 этаж", zh="上海中心大厦", ll=(31.23564, 121.50125), q="Shanghai Tower",
      photos=["tower-1.jpg", "tower-3.jpg", "tower-4.jpg", "tower-5.jpg", "tower-2.jpg", "tower-6.jpg"],
      sub="Самое высокое здание Китая, смотровая на закате",
      what=["632 м и 128 этажей - самое высокое здание Китая. Смотровая на 118-119 этажах, на окне табличка «118F 546M» (на фото). Лифты до 2017 года были самыми быстрыми в мире, 20,5 м/с.",
            "Рядом ещё две высотки - Jin Mao и Shanghai World Financial Center. Если подняться к 16:30, застанешь день и закат в 17:10."],
      facts=[("Часы", "8:30-22:00, вход до 21:30 (путеводители, официально на 2026 год не подтверждено)"),
             ("Билет", "около 180 ¥ (путеводитель, июнь 2026)"), ("На месте", "около часа")],
      src="Wikipedia (высота, лифты); часы и цена - путеводители wanderinchina.com, trvlogue.com 2026",
      how=["18 мин пешком от набережной Lujiazui.", "Такси: <b>上海中心大厦 · 银城中路501号</b>.", "Обратно в отель такси 4,6 км, 10-15 мин."],
      near=["riverside"]),
 dict(id="wukang", n=7, name="Wukang Mansion и Wukang Road", zh="武康大楼", ll=(31.20626, 121.43373), q="Wukang Mansion Shanghai",
      photos=["wukang-1.jpg", "wukang-2.jpg", "wukang-3.jpg", "wukang-4.jpg", "wukang-5.jpg"],
      sub="Бывшая Французская концессия: дом-клин 1924 года",
      what=["Французская концессия существовала с 1849 по 1943 год. Большую часть XX века это был лучший жилой район Шанхая, характер места сохранился.",
            "Wukang Mansion (бывшие Normandie Apartments) - жилой дом венгерского архитектора László Hudec, 1924 год. Стоит клином на перекрёстке Huaihai Road и Wukang Road, здесь жили многие знаменитости.",
            "От дома на север идёт тихая Wukang Road с особняками и деревьями."],
      facts=[("Вход", "снаружи, бесплатно"), ("На месте", "30-60 мин с прогулкой")], src="Wikipedia (Wukang Mansion, French Concession)",
      how=["Такси от отеля 11 км, 25-30 мин днём. Показать: <b>武康大楼 · 淮海中路1850号</b>."],
      near=["anfu"]),
 dict(id="anfu", n=8, name="Anfu Road", zh="安福路", ll=(31.21562, 121.43804), q="Anfu Road Shanghai",
      photos=["anfu-1.jpg", "anfu-4.jpg", "anfu-2.jpg", "anfu-3.jpg"],
      sub="Улица с платанами и кафе, там же обед",
      what=["Около 850 м в центре бывшей концессии. По путеводителю chinavigators это улица с самым большим числом кафе в Шанхае: свои обжарщики кофе, эспрессо-бары, японская пекарня. Вдоль улицы старые платаны.",
            "В будни утром здесь спокойно, к позднему утру людей больше. На улице особняки 1920-30-х, в одном из них театр Shanghai Dramatic Arts Center."],
      facts=[("Вход", "бесплатно"), ("Кафе", "часы у каждого свои, не проверял")],
      src="SCMP, chinavigators.com, enprimeurclub.com; адреса домов - описания фото на Wikimedia Commons",
      how=["19 мин пешком от Wukang Mansion.", "Дальше такси до Bund 7 км, ~20 мин: <b>和平饭店 · 南京东路20号</b>."],
      near=["wukang", "bund"]),
 dict(id="museum", n=9, name="Shanghai Museum", zh="上海博物馆", ll=(31.23016, 121.47100), q="Shanghai Museum People's Square",
      photos=["museum-1.jpg", "museum-2.jpg", "museum-3.jpg"],
      sub="Древнее китайское искусство: бронза, фарфор, каллиграфия",
      what=["Городской музей древнего китайского искусства на People's Square, в этом здании с 1996 года. Известен большой коллекцией редких предметов.",
            "Восточный филиал музея в Пудуне по вторникам закрыт. Сегодня ехать только сюда, на People's Square."],
      facts=[("Часы", "9:00-17:00, вход до 16:00"), ("Выходной", "понедельник (во вторник открыт)"), ("Бронь", "не нужна с 01.09.2025, вход по документу"), ("На месте", "1,5-2 ч")],
      src="english.shanghai.gov.cn (26.08.2025 и 05.12.2024); Wikipedia",
      how=["Такси от отеля 8 км, ~20 мин. Показать: <b>上海博物馆 · 人民大道201号</b>.", "От музея до Bund такси 3 км, ~10 мин."],
      near=["bund"]),
]
BY = {p["id"]: p for p in P}

W = json.load(open("walk.json")); C = json.load(open("car.json")); ST = W["P"]
def walk(v, a, b):
    for l in W["legs"][v]:
        if l["a"] == a and l["b"] == b:
            return dict(kind="walk", coords=l["coords"])
    raise KeyError((v, a, b))
def taxi(a, b):
    return dict(kind="taxi", coords=C[f"{a}-{b}"]["coords"])
def metro(color, *names):
    return dict(kind="metro", color=color, coords=[list(ST[n]) for n in names])
GREEN = "#16a34a"

TAXI_HOTEL = "上海浦东万豪万枫酒店 · 峨山路91弄38号"
DAYS = [
 dict(key="v1", label="★ Вариант 1", title="Вариант 1 (рекомендую): старый город → Bund → Lujiazui на закате",
      why="Самое главное в Шанхае за один день: старый китайский сад, набережная колониальных банков и небоскрёбы на другом берегу. Ходьбы около 6 км с остановками, переезды короткие. Закат встречаешь на 118 этаже или у реки.",
      steps=[
        ("10:00", None, "Такси от отеля до северных ворот Yu Garden, 6 км, 15-20 мин. Показать: <b>豫园 北门 · 福佑路168号</b>.", [("📍 Yu Garden", gm("Yu Garden Shanghai"))]),
        ("10:20", "yu", "Сад, 1-1,5 ч. Билет 40 ¥ в кассе у ворот, паспорт с собой. После сада - чайный домик Huxinting и храм бога города рядом.", []),
        ("12:00", "nanxiang", "Обед. Очередь к окну на вынос по путеводителю 2026 года 45-60 мин, залы наверху дороже.", []),
        ("13:00", "bund", "10 мин пешком до южного конца Bund, по набережной на север 15 мин до Peace Hotel.", []),
        ("14:00", "waibaidu", "Ещё 8 мин на север до моста. Потом 15 мин пешком до метро <b>East Nanjing Road</b>.", []),
        ("14:40", None, "Метро <b>Line 2 (зелёная)</b>, поезд в сторону Pudong Airport / Guanglan Road, <b>1 остановка</b> под рекой до <b>Lujiazui</b>. Оплата: приложи Visa / Mastercard к турникету.", [("📍 East Nanjing Road", gm("East Nanjing Road Station Shanghai"))]),
        ("15:00", "riverside", "13 мин от метро к реке. Вид на весь Bund через реку.", []),
        ("16:20", "tower", "18 мин пешком. Смотровая 118 этажа на закат в 17:10, около часа.", []),
        ("18:00", None, "Ужин в Lujiazui.", []),
        ("~20:30", None, f"Такси в отель, 4,6 км, 10-15 мин. Показать: <b>{TAXI_HOTEL}</b>.", [("🏨 Отель", gm(HOTEL_Q))]),
        ("~22:00", None, "Такси в аэропорт, Terminal 1, 40-50 мин - смотри «Аэропорт» ниже.", []),
      ],
      legs=[taxi("H", "YU"), walk("v1", "YU", "NX"), walk("v1", "NX", "BUNDS"), walk("v1", "BUNDS", "PEACE"), walk("v1", "PEACE", "WBD"),
            walk("v1", "WBD", "ENR"), metro(GREEN, "ENR", "LJZ"), walk("v1", "LJZ", "RIV"), walk("v1", "RIV", "TOWER"), taxi("TOWER", "H")],
      pins=["yu", "nanxiang", "bund", "waibaidu", "riverside", "tower"]),
 dict(key="v2", label="Вариант 2", title="Вариант 2: утро во Французской концессии вместо старого города",
      why="Вместо сада - тихие улицы бывшей Французской концессии: дома 1920-х, платаны, кафе. Это про то, как живёт город сегодня. С обеда - тот же Bund и Lujiazui на закате.",
      steps=[
        ("10:00", None, "Такси от отеля 11 км, 25-30 мин. Показать: <b>武康大楼 · 淮海中路1850号</b>.", [("📍 Wukang Mansion", gm("Wukang Mansion Shanghai"))]),
        ("10:30", "wukang", "Дом-клин 1924 года, потом пешком на север по Wukang Road.", []),
        ("11:30", "anfu", "19 мин пешком. Кафе и платаны, здесь же обед.", []),
        ("13:30", None, "Такси до Bund 7 км, ~20 мин. Показать: <b>和平饭店 · 南京东路20号</b>.", []),
        ("14:00", "waibaidu", "8 мин на север до моста, потом 15 мин до метро East Nanjing Road.", []),
        ("14:40", None, "Метро <b>Line 2 (зелёная)</b>, 1 остановка до <b>Lujiazui</b>.", []),
        ("15:00", "riverside", "Вид на Bund через реку.", []),
        ("16:20", "tower", "Смотровая на закат 17:10.", []),
        ("~20:30", None, f"Ужин, такси в отель. Показать: <b>{TAXI_HOTEL}</b>.", [("🏨 Отель", gm(HOTEL_Q))]),
      ],
      legs=[taxi("H", "WUK"), walk("v2", "WUK", "ANFU"), taxi("ANFU", "PEACE"), walk("v2", "PEACE", "WBD"), walk("v2", "WBD", "ENR"),
            metro(GREEN, "ENR", "LJZ"), walk("v2", "LJZ", "RIV"), walk("v2", "RIV", "TOWER"), taxi("TOWER", "H")],
      pins=["wukang", "anfu", "bund", "waibaidu", "riverside", "tower"]),
 dict(key="v3", label="Вариант 3: после обеда", title="Вариант 3: если до обеда работаешь",
      why="Только главное, с 14:00: Bund, мост, другой берег и закат. Если хочется музея - начни с Shanghai Museum (до 17:00).",
      steps=[
        ("14:00", None, "Такси от отеля до Bund 8 км, ~20 мин. Показать: <b>和平饭店 · 南京东路20号</b>.", []),
        ("(или 12:30)", "museum", "Музей на People's Square, 1,5-2 ч, потом такси 10 мин до Bund.", []),
        ("14:20", "bund", "Набережная и мост Waibaidu, около часа.", []),
        ("15:30", None, "Метро <b>Line 2 (зелёная)</b> от East Nanjing Road, 1 остановка до Lujiazui.", []),
        ("15:50", "riverside", "Вид на Bund.", []),
        ("16:20", "tower", "Смотровая на закат 17:10.", []),
        ("~20:30", None, f"Ужин, такси в отель. Показать: <b>{TAXI_HOTEL}</b>.", [("🏨 Отель", gm(HOTEL_Q))]),
      ],
      legs=[taxi("H", "PEACE"), walk("v1", "PEACE", "WBD"), walk("v1", "WBD", "ENR"), metro(GREEN, "ENR", "LJZ"),
            walk("v1", "LJZ", "RIV"), walk("v1", "RIV", "TOWER"), taxi("TOWER", "H")],
      pins=["museum", "bund", "waibaidu", "riverside", "tower"]),
 dict(key="air", label="✈ Аэропорт", title="Вечер: аэропорт Pudong, Terminal 1",
      why="Вылет с того же Terminal 1, куда ты прилетел (MU249, по Trip.com и AirNavRadar). Номер в отеле твой до выезда.",
      steps=[
        ("утром", None, "⚠️ <b>Сверь время вылета в приложении China Eastern</b>: в билете 01:20, а сайты слежения за рейсами пишут 00:40-00:50.", []),
        ("~22:00", None, "Такси от отеля, 36 км, 40-50 мин. До 23:00 дневной тариф 120-140 ¥, после 23:00 - 150-170 ¥. Плати Alipay / WeChat или наличными. Показать: <b>浦东国际机场 1号航站楼 出发</b> (Terminal 1, вылет).", [("📍 Terminal 1", gm("Shanghai Pudong International Airport Terminal 1"))]),
        ("~22:45", None, "Зал вылета на 3 этаже, регистрация China Eastern по табло.", []),
      ],
      legs=[taxi("H", "T1")], pins=[]),
]

WX = [("Утро", "18-20°, облачно с прояснениями"), ("День", "19-20°, облачно с прояснениями, ветер до 17 км/ч"),
      ("Вечер", "15-17°, ясно; закат 17:10"), ("Дождь", "почти нет: вероятность 0-2%")]

# ---------- HTML ----------
HEAD = '''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow"><title>{t}</title>{extra}<link rel="stylesheet" href="style.css?v=3"></head><body><div class="wrap">'''
FOOT = '</div><script src="lightbox.js?v=4" defer></script></body></html>'
XCSS = '<style>.zh{font-size:22px;line-height:1.35;font-weight:700;background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:8px 10px;margin:6px 0}.zh small{display:block;font-size:13px;font-weight:400;color:var(--mute)}</style>'

def strip_pics(p, n=4):
    return "".join(f'<figure><img src="t/{f}" data-full="img/{f}" alt="{E(CAP.get(f, p["name"]))}" loading="lazy"><figcaption>{cap(f)}</figcaption></figure>' for f in p["photos"][:n])

def place_page(p):
    grid = "".join(f'<figure class="{"w" if i == 0 else ""}"><a href="img/{f}"><img src="img/{f}" alt="{E(CAP.get(f, ""))}" loading="lazy"></a><figcaption>{cap(f)}</figcaption></figure>' for i, f in enumerate(p["photos"]))
    near = "".join(f'<a class="city" href="{q}.html"><img src="t/{BY[q]["photos"][0]}" alt="{E(BY[q]["name"])}" loading="lazy"><div><b>{BY[q]["n"]}. {E(BY[q]["name"])}</b><span class="n">{E(BY[q]["sub"])}</span></div></a>' for q in p["near"])
    days = [d for d in DAYS if p["id"] in d["pins"]]
    inplan = ('<div class="verdict">В плане: ' + ", ".join(f'<a href="index.html#{d["key"]}">{E(d["label"])}</a>' for d in days) + '</div>') if days else ""
    facts = "<table>" + "".join(f"<tr><th>{E(k)}</th><td>{E(v)}</td></tr>" for k, v in p["facts"]) + "</table>"
    body = f'''<a class="back" href="index.html">← ко всему плану</a>
<header><h1><span class="pin" style="display:inline-block;vertical-align:middle;margin-right:8px">{p["n"]}</span>{E(p["name"])}</h1><div class="sub">{E(p["zh"])} · {E(p["sub"])}</div></header>
{inplan}
<div class="grid">{grid}</div>
{"".join(f"<p>{E(x)}</p>" for x in p["what"])}
<div class="card">{facts}<p class="hint">Источник: {E(p["src"])}. Проверено {SRC_DATE}.</p></div>
<h3>Как добраться</h3><ul>{"".join(f"<li>{s}</li>" for s in p["how"])}</ul>
<div class="btns"><a class="btn" href="{gm(p["q"])}" target="_blank" rel="noopener">📍 Google Maps</a></div>
{"<h3>Рядом</h3><div class='cities'>" + near + "</div>" if near else ""}
<p class="foot">Фото: Wikimedia Commons, автор и лицензия под каждым. Пешие отрезки и такси: OSRM. <a href="index.html">← ко всему плану</a></p>'''
    open(f'{p["id"]}.html', "w").write(HEAD.format(t=E(p["name"]) + " - Shanghai", extra=XCSS) + body + FOOT)

def day_card(d, i):
    rows = ""
    for t, pid, txt, btns in d["steps"]:
        if pid:
            p = BY[pid]
            head = f'<span class="pin" style="display:inline-block">{p["n"]}</span> <a href="{pid}.html"><b>{E(p["name"])}</b></a>'
            b = [("📍 Google Maps", gm(p["q"])), ("Подробнее →", f"{pid}.html")]
            pics = f'<div class="pics">{strip_pics(p, 3)}</div>'
        else:
            head, b, pics = "", btns, ""
        bt = "".join(f'<a class="btn{" o" if "Подробнее" in l else ""}" href="{u}"{"" if u.endswith(".html") else " target=_blank rel=noopener"}>{l}</a>' for l, u in b)
        rows += f'<div class="day"><span class="dt">{t}</span> {head}<div class="d">{txt}</div>{pics}<div class="btns">{bt}</div></div>'
    cls = ["", " o2", " o3", " e1"][i]
    return f'''<div class="card opt{cls}" id="{d["key"]}"><h2>{E(d["title"])}</h2><div class="why">{E(d["why"])}</div>{rows}
<div class="btns"><button class="btn o showday" data-k="{d["key"]}">🗺 Показать на карте</button></div></div>'''

def tile(p):
    return f'''<div class="card"><div class="top"><span class="pin">{p["n"]}</span><div><h2><a href="{p["id"]}.html">{E(p["name"])}</a></h2><div class="hint">{E(p["zh"])} · {E(p["sub"])}</div></div></div>
<div class="pics">{strip_pics(p, 7)}</div>
<div class="btns"><a class="btn" href="{p["id"]}.html">Подробнее →</a><a class="btn o" href="{gm(p["q"])}" target="_blank" rel="noopener">📍 Maps</a></div></div>'''

def index():
    wx = "".join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in WX)
    markers = json.dumps([dict(n=p["n"], id=p["id"], name=p["name"], lat=p["ll"][0], lng=p["ll"][1]) for p in P], ensure_ascii=False)
    days = json.dumps({d["key"]: dict(legs=d["legs"], pins=d["pins"]) for d in DAYS}, ensure_ascii=False)
    cards = [("Отель", "上海浦东万豪万枫酒店<br>上海市浦东新区峨山路91弄38号", "Fairfield by Marriott Shanghai Pudong · тел. +86 21 3880 9777"),
             ("Yu Garden, северные ворота", "豫园 北门<br>黄浦区福佑路168号", "1. Yu Garden"),
             ("Bund, Peace Hotel", "和平饭店<br>南京东路20号", "3. Набережная Bund"),
             ("Shanghai Tower", "上海中心大厦<br>银城中路501号", "6. Shanghai Tower"),
             ("Wukang Mansion", "武康大楼<br>淮海中路1850号", "7. Французская концессия"),
             ("Shanghai Museum", "上海博物馆<br>人民大道201号", "9. Музей"),
             ("Аэропорт, Terminal 1, вылет", "浦东国际机场<br>1号航站楼 出发", "Pudong Airport T1 departures")]
    taxi_cards = "".join(f'<div class="card"><b>{E(a)}</b><div class="zh">{b}<small>{E(c)}</small></div></div>' for a, b, c in cards)
    photos_air = "".join(f'<figure><img src="t/{f}" data-full="img/{f}" alt="{E(CAP[f])}" loading="lazy"><figcaption>{cap(f)}</figcaption></figure>' for f in ["pvg-1.jpg", "pvg-2.jpg", "pvg-3.jpg"])
    body = f'''<header><h1>Shanghai: один день</h1><div class="sub">Вторник 27.10.2026 · отель Fairfield by Marriott Pudong · ночью вылет из Terminal 1 · срез {SRC_DATE}</div></header>
<div class="alert"><b>Коротко.</b> Рекомендую <b>вариант 1</b>: в 10:00 такси до старого китайского сада Yu Garden, обед сяолунбао, пешком по набережной Bund до моста Waibaidu, метро 1 остановка на другой берег, закат 17:10 на 118 этаже Shanghai Tower. Около 20:30 в отель, около 22:00 такси в аэропорт. ⚠️ Утром сверь время вылета в приложении China Eastern.</div>
<div class="card"><h2>Погода 27.10</h2><table class="wxt">{wx}</table><p class="hint">Open-Meteo, прогноз на 27.10. Восход 6:05, закат 17:10.</p></div>
<div class="vsw" id="sw"><button data-k="all" class="on">Все места</button>{"".join(f'<button data-k="{d["key"]}">{E(d["label"])}</button>' for d in DAYS)}</div>
<div id="map"></div>
<div class="legend">H - отель, A - аэропорт. Синяя линия - пешком, зелёный пунктир - метро Line 2, серый пунктир - такси. Нажми на номер - откроется место.</div>
<div class="btns"><button class="btn o" id="me">📍 Показать, где я</button></div>
<h3>План по вариантам</h3>
{"".join(day_card(d, i) for i, d in enumerate(DAYS))}
<h3>Карточки для таксиста</h3><div class="hint">Покажи водителю нужную. Такси: Alipay / WeChat или наличные, иностранную карту обычно не берут.</div>
{taxi_cards}
<h3>Все места</h3><div class="hint">Номера как на карте. Листай фото вбок, нажми - откроется крупно.</div>
{"".join(tile(p) for p in P)}
<h3>Аэропорт Pudong, Terminal 1</h3><div class="pics">{photos_air}</div>
<p class="foot">Срез {SRC_DATE}. Погода: Open-Meteo. Часы и цены: официальный сайт Yu Garden, правительство Шанхая (english.shanghai.gov.cn), путеводители 2026 (названы на страницах мест). История: Wikipedia. Пешком и такси: OSRM, время такси днём с запасом на пробки. Фото: Wikimedia Commons, автор и лицензия под каждым. Ничего не бронировалось.</p>'''
    script = '''<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script><script>
var M=%s, D=%s, H=[31.2190,121.5272], A=[31.1503,121.8040];
var map=L.map('map',{scrollWheelZoom:false});window.map=map;
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution:'© OpenStreetMap',maxZoom:19}).addTo(map);
var mk={};
M.forEach(function(p){var ic=L.divIcon({className:'',html:'<div class="pin">'+p.n+'</div>',iconSize:[28,28],iconAnchor:[14,14]});
 var m=L.marker([p.lat,p.lng],{icon:ic,zIndexOffset:(20-p.n)*100}).bindTooltip(p.n+'. '+p.name,{direction:'top',offset:[0,-14]});m.on('click',function(){location.href=p.id+'.html'});mk[p.id]=m;});
L.marker(H,{icon:L.divIcon({className:'',html:'<div class="pin h">H</div>',iconSize:[28,28],iconAnchor:[14,14]}),zIndexOffset:1000}).bindTooltip('Отель Fairfield by Marriott Pudong',{direction:'top',offset:[0,-14]}).addTo(map);
var am=L.marker(A,{icon:L.divIcon({className:'',html:'<div class="pin g">A</div>',iconSize:[28,28],iconAnchor:[14,14]})}).bindTooltip('Аэропорт Pudong, Terminal 1',{direction:'top',offset:[0,-14]});
var layer=L.layerGroup().addTo(map);
function show(k){layer.clearLayers();var pts=[H];map.removeLayer(am);
 Object.keys(mk).forEach(function(id){map.removeLayer(mk[id])});
 if(k=='all'){M.forEach(function(p){mk[p.id].addTo(map);pts.push([p.lat,p.lng]);});}
 else{var d=D[k];d.pins.forEach(function(id){mk[id].addTo(map);var p=M.filter(function(x){return x.id==id})[0];pts.push([p.lat,p.lng]);});
  if(k=='air'){am.addTo(map);pts.push(A);}
  d.legs.forEach(function(l){var o=l.kind=='walk'?{color:'#1d4ed8',weight:4,opacity:.85}:(l.kind=='metro'?{color:l.color,weight:5,opacity:.9,dashArray:'8 8'}:{color:'#64748b',weight:4,opacity:.8,dashArray:'4 8'});L.polyline(l.coords,o).addTo(layer);if(k!='air')l.coords.forEach(function(c){pts.push(c)});});}
 map.fitBounds(pts,{padding:[24,24]});
 document.querySelectorAll('#sw button').forEach(function(b){b.classList.toggle('on',b.dataset.k==k)});}
document.querySelectorAll('#sw button').forEach(function(b){b.onclick=function(){show(b.dataset.k)}});
document.querySelectorAll('.showday').forEach(function(b){b.onclick=function(){show(b.dataset.k);document.getElementById('sw').scrollIntoView({behavior:'smooth'})}});
var h=location.hash.replace('#','');show(D[h]?h:'v1');
var me=null;document.getElementById('me').onclick=function(){if(!navigator.geolocation)return;navigator.geolocation.getCurrentPosition(function(p){var ll=[p.coords.latitude,p.coords.longitude];if(me)map.removeLayer(me);me=L.circleMarker(ll,{radius:8,color:'#fff',weight:3,fillColor:'#2563eb',fillOpacity:1}).addTo(map).bindTooltip('Ты здесь');map.setView(ll,15);document.getElementById('map').scrollIntoView({behavior:'smooth'});});};
</script>''' % (markers, days)
    extra = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">' + XCSS
    open("index.html", "w").write(HEAD.format(t="Shanghai: один день", extra=extra) + body + "</div>" + script + '<script src="lightbox.js?v=4" defer></script></body></html>')

for p in P:
    place_page(p)
index()
print("ok", len(P), "places", SRC_DATE)
