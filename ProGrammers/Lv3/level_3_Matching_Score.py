def solution(word, pages):
    import re
    urlIdx = {}  # url별 idx 저장
    urlScore = {}  # url별 기본점수와 외부링크수 저장
    urlLink = {}  # 다른 웹페이지에서 링크한 url
    word = word.lower()
    for i in range(len(pages)):
        page = pages[i].lower()  # 모두 소문자
        url = re.search(r'<meta[^>]*content="https://([\S]*)"/>', page).group(1)

        urlIdx[url] = i

        basic_score = 0  # 기본 점수
        for w in re.findall(r'[a-zA-Z]+', page):
            if word == w:
                basic_score += 1

        link = set()
        for l in re.findall(r'<a href="https://[\S]*">', page):  # 외부 링크는 여러 개 있을 수 있음
            link.add(re.search(r'"https://([\S]*)"', l).group(1))
        urlScore[url] = [basic_score, len(link)]

        for e in list(link):
            if e not in urlLink:
                urlLink[e] = list()
            urlLink[e].append(url)

    answer = []
    for url, v in urlScore.items():
        score = v[0]
        if url in urlLink:
            for exL in urlLink[url]:
                score += urlScore[exL][0] / urlScore[exL][1]
        answer.append([score, urlIdx[url]])

    return sorted(answer, key=lambda x: [-x[0], x[1]])[0][1]
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution("blind", pages)) # 0

pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution("Muzi", pages)) # 1

