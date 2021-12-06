from bs4 import BeautifulSoup
import requests

basic_url = "https://movie.naver.com"
title_url = "https://movie.naver.com/movie/search/result.naver?query={name}&section=all&ie=utf8"


# 네이버 영화 페이지 상에서 영화 검색 후 개봉년도와 맞는 영화의 URL 코드 값을 크롤링 하는 함수.
def getMovieCode(target):
    title_kr, year = target
    try:
        req = requests.get(title_url.format(name=title_kr)).text
        bs = BeautifulSoup(req, features="lxml")
        search_list = bs.find("ul", {"class": "search_list_1"}).findAll("dl")
        for case in search_list:
            if case.find("dd", {"class": "etc"}).findAll("a")[-1].text == year:
                target_code_url = basic_url + case.find("a")["href"]
                break
    except AttributeError as e:
        print(e)
    return target_code_url


"""
@description
해당 영화의 상세 정보 페이지에서 메타 데이터를 수집하는 함수.
(한글명, 영문제목, 컨텐츠 종류, 개봉일, 상영시간, 감독, 출연, 극장상영여부, 줄거리)
(titel_kr, title_eng, contents_type, rel_days, shwg_time, director, actors, shwg_flag, synob)
@return: json or tuple
"""


def getMetadata(title, target_code_url):

    meta_dic = {"title_kr": title,
                "title_eng": "",
                "contents_type": "movie",
                "rel_days": "",
                "shwg_time": "",
                "director": "",
                "actors": "",
                "shwg_flag": "1",
                "synob": ""
                }

    req = requests.get(target_code_url).text
    bs = BeautifulSoup(req, features="lxml")

    tmp_list = bs.find("strong", {"class": "h_movie2"}).text.split(",")

    # year = tmp_list.pop().strip()
    # 영어이름 뒤에 년도가 붙어있어 [:-1]로 슬라이싱.
    meta_dic["title_eng"] = ", ".join([case.strip() for case in tmp_list[:-1]])
    meta_dic["synob"] = bs.find("p", {"class": "con_tx"}).text.strip()

    tmp_list = bs.find("dl", {"class": "info_spec"}).findAll("span")
    meta_dic["shwg_time"] = tmp_list[2].text.strip()
    meta_dic["rel_days"] = "".join([case.text.strip() for case in tmp_list[3].findAll("a")])

    # # genre
    # genre = ", ".join([g.text.strip() for g in tmp_list[0].findAll('a')])

    # director and actors
    tmp_list = bs.find("dl", {"class": "info_spec"}).findAll('dd')
    meta_dic["director"] = ", ".join([case.text.strip() for case in tmp_list[1]])
    # 마지막은 "더보기"이기 때문에 슬라이싱
    meta_dic["actors"] = ", ".join([case.text.strip() for case in tmp_list[2].findAll("a")][:-1])

    return meta_dic

