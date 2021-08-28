import sys
import requests
from bs4 import BeautifulSoup
import pprint

def bunseki(url):
    
    tag_summary = []    #分析対象HTMLのタグ別の情報を格納

    #タグの一覧を取得
    tagList = getTagList()
    
    #対象URLのレスポンスを取得
    HttpResponse = requests.get(url)
    html = BeautifulSoup(HttpResponse.content, "html.parser")

    #tagHTMLからcodeタグを抽出
    for tag in tagList:
        tagobj = {}
        #html、bodyタグの場合はスルー
        if(tag != "html" and tag != "body"):
            tagobj["tag"] = tag

            #対象サイトのタグ使用箇所を取得
            target_html = html.find_all(tag)
            tagobj["elm"] = target_html
        
            tagobj["count"] = len(target_html)
            tag_summary.append(tagobj)
    
    return tag_summary

#タグの一覧を取得
def getTagList():
    
    tagList = []    
    #タグ一覧サイトのレスポンスを取得
    tagHttpResponse = requests.get("https://www.tagindex.com/html_tag/elements/")
    # htmlタグサイトのhtmlを取得
    tagHTML = BeautifulSoup(tagHttpResponse.content, "html.parser")
        #tagHTMLからcodeタグを抽出
    for tag in tagHTML.find_all("code"):
        #タグ一覧を出力
        tag = str(tag)[10:len(str(tag))-11]
        tagList.append(tag)

    return tagList

# 表示する関数
def hyoji(tag_summary ,mode):
    if mode == "0":
        return viewContent(tag_summary )
    elif mode == "1":
        return viewCount(tag_summary )

# タグに含まれる要素すべてを表示
def viewContent(tag_summary ):
    array = []
    for tag in tag_summary:
        # print(tag["tag"],end="")
        # pprint.pprint(tag["elm"])
        array.append(tag["tag"],tag["elm"])

    return array

# タグごとに数を集計
def viewCount(tag_summary ):
    tag_summary  = sorted(tag_summary , key=lambda x:x['count'], reverse=True)
    array = []
    for tag in tag_summary:
        if tag["count"] != 0:
            array.append(tag["tag"],":",tag["count"])

    return array

def main():
    
    url = sys.argv[1]   #分析対象のURLを指定
    mode = sys.argv[2]  #出力モードを指定

    tag_summary = bunseki(url)  #構成分析

    print(hyoji(tag_summary, mode))  #プログラム戻り値

main()