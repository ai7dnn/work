import requests
from bs4 import BeautifulSoup

def crawl_naver_blog(search_keyword):
    base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
    url = base_url + search_keyword

    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page.")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    blog_elements = soup.select("li.sh_blog_top")

    for element in blog_elements:
        blog_url = element.select_one("a.sh_blog_title")["href"]
        blog_title = element.select_one("a.sh_blog_title").text
        blog_date = element.select_one("dd.txt_inline").text

        results.append({
            "url": blog_url,
            "title": blog_title,
            "date": blog_date
        })

    return results

if __name__ == "__main__":
    search_keyword = input("검색어를 입력하세요: ")
    search_keyword = search_keyword.replace(" ", "+")  # 공백을 +로 치환

    search_results = crawl_naver_blog(search_keyword)

    if search_results:
        for idx, result in enumerate(search_results, start=1):
            print(f"{idx}. 제목: {result['title']}")
            print(f"   주소: {result['url']}")
            print(f"   날짜: {result['date']}")
            print("-" * 50)
    else:
        print("검색 결과를 가져올 수 없습니다.")
