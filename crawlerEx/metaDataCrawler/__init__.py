from . import metaCrawlFunctions as mcf

"""
@author: 박주형
@description: 영화의 한글 타이틀 및 개봉년도를 활용해 네이버상 해당 영화의 메타 데이터를 수집하는 패키지.
@date: 2021.12.03
"""


class MetaDataCrawler:
    def __init__(self, target_list):
        self.target_list = target_list        # tuple or list : [[titleKr, year]...]
        self.target_code_url = ""
        self.meta_data = list()


    # 리뷰 및 평점 크롤링을 위한 함수.
    def getTargetUrl(self):
        data_url = list()
        for case in self.target_list:
            url = (case[0], mcf.getMovieCode(case))
            data_url.append(url)
        return data_url

    # 영화 리스트의 모든 메타 데이터를 가져옴
    def getMetaList(self):
        for case in self.target_list:
            self.meta_data.append(mcf.getMetadata(case[0], mcf.getMovieCode(case)))






