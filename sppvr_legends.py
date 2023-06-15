y = ''
v = 'smth.'
#БАЛЛЫ СКГЛ
skgl = 0
if "29Б" in y:
    skgl += 1
elif "28Б" in y:
    skgl += 2
elif ("1А" and ("4А" or "4Б" or "4В") and ("14Б" or "14В"  or  "12Б"  or  "13Б" or "13В")) in y:
    skgl += 2
elif ("1А" and ("4А" or "4Б" or "4В") and "19Б") in y:
    skgl += 1
elif ("1Б" and ("4А" or "4Б" or "4В" or "4Г") and ("14Б" or "14В"  or  "12Б"  or  "13Б" or "13В")) in y:
    skgl += 2
elif ("1Б" and ("4А" or "4Б" or "4В" or "4Г") and "19Б") in y:
    skgl += 1
if "28Б" in y:
    skgl += 6
if "22Ж" in y:
    skgl += 1
if "22З" in y:
    skgl += 3
if "22И" in y:
    skgl += 5
if "22К" in y:
    skgl += 8
if "27Б" in y:
    skgl += 8
#ОВРССС
if ("12Б" or "13Б" or "13В" or "14Б" or "14В" or "16Б" or "17Б" or "18Б" or "19Б" or (("9Б" or "9В") and "10Б")
or (("9В" and '5Б' and ('8В' or '8Г' or '8Д')) and (('21В' or '21Г' or '21Д' or '21Е') or ('22Е' or '22Ж')))
or '20А' or ('СКГЛД' and ('5Б' or ('8В' or '8Г' or '8Д') or ("9Б" or "9В")))
or ('СКГЛВ' and ('5Б' or ('8В' or '8Г' or '8Д') or ("9Б" or "9В"))) or ('1Б' and ("4Е" or "4Ж") and ("5А" or "5В") and
"8Д" and ("21Д" or "21Е")) or ("1Б" and ("4Е" or "4Ж") and "5Б" and "8Г" and ('21Б' or '21В' or '21Г' or '21Д' or '21Е'))
or ("1Б" and ("4Е" or "4Ж") and "5Б" and "8Д") or ("1Б" and ("4Е" or "4Ж") and "5Б" and "8В" and ("21Д" or "21Е"))
or ("1А" and "4В" and "5Б" and "8Г" and ("21Д" or "21Е")) or ("1А" and "4В" and "5Б" and "8Д" and ('21В' or '21Г' or '21Д' or '21Е'))
or ("1А" and "4Г" and "5Б" and "8В" and ("21Д" or "21Е")) or ("1А" and "4Г" and "5Б" and "8Г" and ('21В' or '21Г' or '21Д' or '21Е'))
or ("1А" and "4Г" and "5Б" and "8Д") or ("1А" and "4Д" and "5Б" and ("8А" or "8Б") and ("21Д" or "21Е"))
or ("1А" and "4Д" and "5Б" and ('8В' or '8Г' or '8Д')) or ("1А" and ("4Е" or "4Ж") and "5Б" and ("8А" or "8Б") and ('21Б' or '21В' or '21Г' or '21Д' or '21Е'))
or ("1А" and ("4Е" or "4Ж") and "5Б" and ('8В' or '8Г' or '8Д')) or ("1А" and "4Г" and ("5А" or "5В") and "8Д" and ("21Д" or "21Е"))
or ("1А" and ("4Д" or "4Е" or "4Ж") and "8Г" and ("21Д" or "21Е")) or ("1А" and "4Д" and ("5А" or "5В") and "8Д" and ('21В' or '21Г' or '21Д' or '21Е'))
or ("1А" and ("4Е" or "4Ж" or "4Е" or "4Ж") and "8В" and ("21Д" or "21Е")) or ("1А" and ("4Е" or "4Ж") and ("5А" or "5В") and "8Г" and ('21В' or '21Г' or '21Д' or '21Е'))
or ("1А" and ("4Е" or "4Ж") and ("5А" or "5В") and '8Д')) in y:
   v = 'Очень высокий риск сердечно-сосудистых осложнений – более 10% в течение 10 лет. \
Рекомендуется снижение ЛПНП как минимум, на ≥50% от исходного уровня, цель <1,4 ммоль/л (<55 мг/дл). При повторном сосудистом событии в течение последних 2 лет целевой уровень ЛПНП <1 ммоль/л (<40 мг/дл).'
#ВРССС
if ("21Е" or "22Ж" or "8Д" or ("СКГЛД" and (not "5Б") and (not('8Б' or '8Г' or '8Д')) and (not ("9Б" or "9В"))) or
("СКГЛВ" and (not "5Б") and (not ("8В" or "8Г" or "8Д")) and (not ("9Б" or "9В"))) or
("9Б" or "9В" and "10А" and ("5Б" or ("8В" or "8Г" or "8Д") or ("21В" or "21Г" or "21Д" or "21Е") or ("22Е" or "22Ж"))) or
"20Б" or (("1Б" and "5Б" and "4Д" and "8В" and ("21В" or "21Г" or "21Д" or "21Е")) or ("1Б" and "5Б" and "4Д" and "8Г")) or
("1Б" and "5Б" and "4Д" and "8Д" and ("21А" or "21Б")) or
("1Б" and "5Б" and ("4Е" or "4Ж") and ("8А" or "8Б") and ("21В" or "21Г" or "21Д" or "21Е")) or
("1Б" and "5Б" and ("4Е" or "4Ж") and "8В" and ("21А" or "21Б" or "21В" or "21Г")) or
("1Б" and "5Б" and ("4Е" or "4Ж") and "8Г" and "21А") or
("1Б" and ("5А" or "5В") and "4Д" and "8Г" and "21Е") or
("1Б" and ("5А" or "5В") and "4Д" and "8Д" and ("21В" or "21Г" or "21Д" or "21Е")) or
("1Б" and ("5А" or "5В") and ("4Е" or "4Ж") and "8В" and ("21Г" or "21Д" or "21Е")) or
("1Б" and ("5А" or "5В") and ("4Е" or "4Ж") and "8Г") or
("1Б" and ("5А" or "5В") and ("4Е" or "4Ж") and "8Д" and ("21А" or "21Б" or "21В")) or
("1А" and ("5А" or "5В") and "4В" and "8Г" and "21Е") or
("1А" and ("5А" or "5В") and "4В" and "8Д" and ("21Г" or "21Д" or "21Е")) or
("1А" and ("5А" or "5В") and "4Г" and "8В" and ("21Г" or "21Д" or "21Е")) or
("1А" and ("5А" or "5В") and "4Г" and "8Г" and ("21Б" or "21В" or "21Г" or "21Д" or "21Е")) or
("1А" and ("5А" or "5В") and "4Г" and "8Д" and ("21А" or "21Б" or "21В")) or
("1А" and ("5А" or "5В") and "4Д" and ("8А" or "8Б") and ("21Г" or "21Д" or "21Е")) or
("1А" and ("5А" or "5В") and "4Д" and "8В" and ("21Б" or "21В" or "21Г" or "21Д" or "21Е")) or
("1А" and ("5А" or "5В") and "4Д" and "8Г" and ("21А" or "21Б" or "21В")) or
("1А" and ("5А" or "5В") and "4Д" and "8Д" and "21А") or
("1А" and ("5А" or "5В") and ("4Е" or "4Ж") and ("8А" or "8Б") and ("21Б" or"21В" or "21Г" or "21Д" or "21Е")) or
("1А" and ("5А" or "5В") and ("4Е" or "4Ж") and "8В" and ("21А" or "21Б" or "21В")) or
("1А" and ("5А" or "5В") and ("4Е" or "4Ж") and "8Г" and "21А") or
("1А" and "5Б" and "4В" and ("8А" or "8Б") and ("21Д" or "21Е")) or
("1А" and "5Б" and "4В" and "8В" and ("21В" or "21Г" or "21Д" or "21Е")) or
("1А" and "5Б" and "4В" and "8Г" and ("21А" or "21Б" or "21В" or "21Г")) or
("1А" and "5Б" and "4В" and "8Д" and ("21А" or "21Б")) or
("1А" and "5Б" and "4Г" and ("8А" or "8Б") and ("21В" or "21Г" or "21Д" or "21Е")) or
("1А" and "5Б" and "4Г" and "8В" and ("21А" or "21Б" or "21В" or "21Г")) or
("1А" and "5Б" and "4Г" and "8Г" and ("21А" or "21Б")) or
("1А" and "5Б" and "4Г" and ("8А" or "8Б") and ("21А" or "21Б" or "21В")) or
("1А" and "5Б" and "4Г" and "8В" and "21А") or
("1А" and "5Б" and ("4Е" or "4Ж") and ("8А" or "8Б") and "21А")) in y:
   v = 'Высокий риск сердечно-сосудистых осложнений – 5-10% в течение 10 лет. ' \
        'Рекомендуется снижение ЛПНП как минимум, на ≥50% от исходного уровня, цель <1,8 ммоль/л (<70 мг/дл)'
#УРССС
if (("9Б" and "4А" and (not ("5Б" or ("8В" or "8Г" or "8Д")) or ("21В" or "21Г" or "21Д" or "21Е") or "22Е" or "22Ж") and (not ("ВРССС" and "ОВРССС"))) or
("9В" and ("4А" or "4Б") and (not ("5Б" or ("8В" or "8Г" or "8Д")) or ("21В" or "21Г" or "21Д" or "21Е" or "22Е") or ("22Е" or "22Ж")) and (not ("ВРССС" and "ОВРССС"))) or
("1Б" and "4В" and ("5А" or "5В") and ("8А" or "8Б") and ("21В" or "21Г" or "21Д" or "21Е" or "22Е") and (not ("ВРССС" and "ОВРССС"))) or
("1Б" and "4В" and ("5А" or "5В") and "8В" and ("21Б" or "21В" or "21Г" or "21Д" or "21Е" or "22Е") and (not ("ВРССС" and "ОВРССС"))) or
("1Б" and "4В" and ("5А" or "5В") and "8Г" and (not ("ВРССС" and "ОВРССС"))) or
("1Б"and "4В" and ("5А" or "5В") and "8Д" and (not ("ВРССС" and "ОВРССС"))) or
("1Б" and ("4Г" or "4Д" or "4Е" or "4Ж") and ("5А" or "5В") and (not ("ВРССС" and "ОВРССС"))) or
("1Б" and "4Б" and "5Б" and "8Д" and ("21Г" or "21Д" or "21Е" or "22Е") and (not ("ВРССС" and "ОВРССС"))) or
("1Б" and ("4В" or "4Г" or "4Д" or "4Е" or "4Ж") and "5Б" and (not ("ВРССС" and "ОВРССС"))) or
("1А" and ("4Б" or "4В" or "4Г") and "5Б" and (not ("ВРССС" and "ОВРССС"))) or
("1А" and ("4В" or "4Г" or "4Д" or "4Е" or "4Ж") and ("5А" or "5В") and (not ("ВРССС" and "ОВРССС"))) or
("1А" and "4Б" and ("5А" or "5В") and ("8А" or "8Б") and ("21В" or "21Г" or "21Д" or "21Е" or "22Е") and (not ("ВРССС" and "ОВРССС"))) or
("1А" and "4Б" and ("5А" or "5В") and "8В" and "21А" and (not ("ВРССС" and "ОВРССС"))) or
("1А" and "4Б" and ("5А" or "5В") and ("8Г" or "8Д") and (not ("ВРССС" and "ОВРССС"))) or
("1А" and ("4В" or "4Г" or "4Д" or "4Е" or "4Ж") and ("5А" or "5В") and (not ("ВРССС" and "ОВРССС")))) in y:
    v = 'Умеренный риск сердечно-сосудистых событий – 1-5% в течение 10 лет. Рекомендуется снижение ЛПНП <2,6 ммоль/л (<100 мг/дл)'
#НРССС
if (((not "УРССС") and (not "ВРССС") and (not "ОВРССС")) or ("4А" and (not "ВРССС") and (not "ОВРССС"))) in y:
    v = "Низкий риск сердечно-сосудистых событий – менее 1% в течение 10 лет. Рекомендуется снижение ЛПНП <3 ммоль/л (<116 мг/дл)"
























