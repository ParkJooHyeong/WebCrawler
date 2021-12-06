import crawlerEx.metaDataCrawler as metaCrawler

if __name__ == '__main__':

    target = [("모가디슈", "2021"),("듄", "2021")]

    mc = metaCrawler.MetaDataCrawler(target)
    mc.getMetaList()
    print(mc.getTargetUrl())

