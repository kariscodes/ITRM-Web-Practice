import k_search

def do_write(web_driver, keywords):
    print('##### 오늘의 검색 결과 #####' + '\n')
    for input_keyword in keywords:
        s = k_search.Search()
        try:
            titles, links = s.search_in_goolenews(web_driver, input_keyword, 1)
        except Exception as e:
            print(e)
        print('\n' + 'Keyword: ' + input_keyword)
        for title, link in zip(titles, links):
            print('\n', title, '\n', link)