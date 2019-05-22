import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Chromeを起動する --- (*1)
driver = webdriver.Chrome()
# Googleのページを開く --- (*2)
url = 'https://www.nikkei.com/markets/kabu/'
driver.get(url)
# ページが開くまで待つ --- (*3)
time.sleep(5)

# HTML を取得
html = driver.page_source.encode('utf-8')

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")


# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
# title_tag = soup.title

# タイトル要素を出力
# print(title_tag)

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
# title = title_tag.string

# タイトルを文字列を出力
# print (title)
print (soup.title.string)

# span要素全てを摘出する→全てのspan要素が配列に入ってかえされます→[<span class="m-wficon triDown"></span>, <span class="l-h...
span = soup.find_all("span")

# print時のエラーとならないように最初に宣言しておきます。
nikkei_heikin = ""
# for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
for tag in span:
    # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
    try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        if string_ in "mkc-stock_prices":
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            nikkei_heikin = tag.string
            # 摘出が完了したのでfor分を抜けます
            break
    except:
        # パス→何も処理を行わない
        pass

# 摘出した日経平均株価を出力します。
print(nikkei_heikin)

# 検索ボックスのオブジェクトを得る --- (*4)
# q = driver.find_element_by_name('q')
# 検索ボックスにキーを送信する --- (*5)
# q.send_keys('ゼロからはじめるPython')
# フォームを投稿する --- (*6)
# q.submit()
# 結果を30秒表示して終了する --- (*7)
# time.sleep(30)
driver.quit()