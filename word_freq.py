import pymysql
import re
from wordfreqcount import get_words

conn = pymysql.connect(host='localhost', user='I339493', password='test123', db='ml_features_en')
cursor = conn.cursor()


def word_freq(sents_list: list):
    word_freq = {}
    f_word = []
    for sentence in sents_list:
        sentence = str(sentence)
        if "(Read more about how we rate cars.)" in sentence:
            sentence = sentence.replace("(Read more about how we rate cars.)", "")
        sentence = sentence.lower()
        punctuation = '[,，。.!?:"@#$%^&*()+=_:;“”‘’]'
        sentence = str(re.sub(punctuation, '', sentence))
        for word in sentence.split(" "):
            if word in f_word:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
                f_word.append(word)

    return word_freq


def en_freq():
    sql = "select data from RAW_DATA"
    cursor.execute(sql)
    result = list(cursor.fetchall())
    cursor.close()
    conn.close()
    # result = [
    #     "The Ford is not engaging to drive, in part due to the body roll evident when pitching the car into a turn...Our stance hasn't changed since we drove the Fusion in 2006.",
    #     "4Matic all-wheel drive is optional on the sedan and standard on the coupe.",
    #     "A $500 tow package increases it to 6,600 pounds.The Q7's power steering has ideal effort-pretty unusual for an SUV-with some feedback and a bit of road feel.",
    #     "A few effective styling changes, Car and Driver says, include a new single-bar grille that evokes most of its SL forebears, flanked by L-shaped headlamps that evoke none of them. Kelley Blue Book remarks the new deeply sculpted side scoops and a protruding nose mark a revolutionary departure from the conservative styling found on the previous generation SL. The rear end is also tidied, and in all, the changes to the Benz SL successfully convey a more sporting intent, Edmunds points out.",
    #     "A prominent 'gunsight' crossbar grille surrounded by bold brightwork (dark grey on the base ST) with squared-off fenders and wraparound headlamps adorns the 2008 Dodge Ram HD, according to Kelley Blue Book, who comment, Additional shiny bits and chrome wheels are part of higher trim levels. J.D.",
    #     "A laundry list of safety features, reports Motor Trend, includes standard dual front airbags, driver and front passenger side impact airbags, side curtain airbags [for all three rows], active headrests, and seatbelt pretensioners. That laundry list doesn't even mention the standard ABS, traction control, antiskid system, and standard full-time all-wheel drive (SH-AWD)."]
    word_freq_dict = word_freq(result)
    word_freq_sort = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)
    index = 1
    # for (key, value) in word_freq_sort:
    #     print(key + ' : ' + str(value))
    with open('./word_freq_en_v2.txt', 'w') as f:
        for (key, value) in word_freq_sort:
            line = str(index) + " : " + key + " : " + str(value) + "\n"
            index += 1
            f.write(line)


def cn_freq():
    sql = "select translate from RAW_DATA"
    cursor.execute(sql)
    result = cursor.fetchall()
    index = 1
    with open('./cn_translations.txt', 'w') as f:
        for line in result:
            if index % 10000 == 0:
                print(index)
            f.write(line[0] + '\n')
            index += 1
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # en_freq()
    # cn_freq()
    with open('./cn_translations.txt', 'r', encoding='utf8') as f:
        k_list = get_words(f.read())
    with open('./word_freq_cn_v1.txt', 'w') as f:
        for k in k_list:
            f.write(k + '\n')
