#! python3
#! /usr/bin/env python3
#! /usr/bin/python3

# translate.py is a program that could translate your text troughth command line


import pyperclip
import requests as req
from sys import argv

def connect(text,from_,to) :
    try :
        res = req.get(f"https://hadi-api.herokuapp.com/api/terjemahan?text={text}&from={from_}&to={to}")
        res.raise_for_status()
        result = res.json()
        return result
    except Exception as err :
        raise Exception(f"error : {err}")

def translate(text) :
    from_ = argv[1]
    to = argv[2]
    res = connect(text,from_,to)
    status = res['status']

    if status == 200 :
        result = res['result']['translated']
        return result
    elif status == False :
        return res['msg']


if (len(argv) == 2) and (argv[1] == '--help') :
    print("usage : ")
    print("tranlate [FROM] [TO] [TEXT]")
    print("""
    auto: "",
    af: "afrikaans",
    sq: "Albania",
    am: "Amharik",
    ar: "Arab",
    hy: "Armenia",
    az: "Azerbaijani",
    eu: "Basque",
    nl: "Belanda",
    be: "Belarusia",
    bn: "Bengali",
    bs: "Bosnia",
    bg: "Bulgaria",
    my: "Burma",
    ceb: "Cebuano",
    cs: "Cheska",
    zh-cn: "China (Aks. Sederhana)",
    zh-tw: " China (Aks. Tradisional)",
    da: "Dansk",
    eo: "Esperanto",
    et: "Esti",
    fy: "Frisia Barat",
    gd: "Gaelik Skotlandia",
    gl: "Galisia",
    ka: "Georgia",
    gu: "Gujarat",
    ha: "Hausa",
    haw: "Hawaii",
    hi: "Hindi",
    hmn: "Hmong",
    hu: "Hungaria",
    iw: "Ibrani",
    ig: "Igbo",
    id: "Indonesia",
    en: "Inggris",
    ga: "Irlandia",
    is: "Islandia",
    it: "Italia",
    jv: "Jawa",
    ja: "Jepang",
    de: "Jerman",
    kn: "Kanada",
    ca: "Katalan",
    kk: "Kazakh",
    km: "Khmer",
    rw: "Kinyarwanda",
    ky: "Kirgiz",
    ko: "Korea",
    co: "Korsika",
    ht: "Kreol Haiti",
    hr: "Kroasia",
    ku: "Kurdi",
    lo: "Lao",
    la: "Latin",
    lv: "Latvi",
    lt: "Lituavi",
    lb: "Luksemburg",
    mk: "Makedonia",
    mg: "Malagasi",
    ml: "Malayalam",
    mt: "Malta",
    mi: "Maori",
    mr: "Marathi",
    ms: "Melayu",
    mn: "Mongolia",
    ne: "Nepali",
    no: "Norwegia",
    ny: "Nyanja",
    or: "Oriya",
    ps: "Pashto",
    fa: "Persia",
    pl: "Polski",
    pt: "Portugis",
    fr: "Prancis",
    pa: "Punjabi",
    ro: "Rumania",
    ru: "Rusia",
    sm: "Samoa",
    sr: "Serbia",
    sn: "Shona",
    sd: "Sindhi",
    si: "Sinhala",
    sk: "Slovak",
    sl: "Sloven",
    so: "Somalia",
    st: "Sotho Selatan",
    es: "Spanyol",
    su: "Sunda",
    fi: "Suomi",
    sw: "Swahili",
    sv: "Swedia",
    tl: "Tagalog",
    tg: "Tajik",
    ta: "Tamil",
    tt: "Tatar",
    te: "Telugu",
    th: "Thai",
    tr: "Turki",
    tk: "Turkmen",
    uk: "Ukraina",
    ur: "Urdu",
    ug: "Uyghur",
    uz: "Uzbek",
    vi: "Vietnam",
    cy: "Welsh",
    xh: "Xhosa",
    yi: "Yiddish",
    yo: "Yoruba",
    el: "Yunani",
    zu: "Zulu"
    """)

# if (argv[3] == "-t") and (len(argv) == 5) :
#     text = argv[4]
#     result = translate(text)
#     print(result) 
# elif (argv[3] == "-t") and (len(argv) == 4) :
#     print("[no text to translate]")

# if (argv[3] == "-p") and (len(argv) == 4) :
#     text = pyperclip.paste()
#     if text == "" :
#         print("[no text to translate]")
#     else :
#         result = translate(text,from_,to)
#         print(result) 

if len(argv) == 4 :

    if argv[3] == "-t" :
        print("[no text to translate]")

    elif argv[3] == "-p" :
        text = pyperclip.paste()
        if text == "" :
            print("[no text to translate]")
        else :
            result = translate(text)
            print(result)

    else :
        raise Exception("there is no such a command")


elif len(argv) == 5 :

    if argv[3] == "-t" :
        text = argv[4]
        result = translate(text)
        print(result)
    
    elif argv[3] == "-p" :
        if argv[4] == "-c" :
            text = pyperclip.paste()
            result = translate(text)
            pyperclip.copy(result)
            print(result)
            print("\ncopied !")
        else :
            raise Exception("there is no such a command")
 
elif len(argv) == 6 :

    if argv[3] == "-t" :
        if argv[5] == "-c" :
            text = argv[4]
            result = translate(text)
            pyperclip.copy(result)
            print(result)
            print("\ncopied !")
        else :
            raise Exception("there is no such a command")
    
    elif argv[3] == "-p" :
        raise Exception("4 arguments expected,5 given")
    
    else : 
        raise Exception("there is no such a command")

elif len(argv) < 4 :
    raise Exception(f"at least 3 argumenst expected,{len(argv) - 1} given")

elif len(argv) > 6 :
    if argv[3] == "-p" :
        raise Exception(f"4 argumens expected,{len(argv) - 1} given")
    else :
        raise Exception(f"5 argumens expected,{len(argv) - 1} given")

