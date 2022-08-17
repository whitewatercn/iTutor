from ast import keyword
import time
from unittest import result 
import jieba
import wordcloud
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

# 待查询信息
end_year = 2022
begin_year = input("请输入最早年份:")
author = input("请输入作者名称:")
work_unit = input("请输入作者单位:")

# get网站
wd = webdriver.Chrome(service=Service(r"iTutor_tool/chromedriver"))
wd.get('https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS')
wd.implicitly_wait(2)




# 切换至专业检索
switch_majorsearch=wd.find_element(By.CSS_SELECTOR,'li[name="majorSearch"]')
switch_majorsearch.click()

# 输入检索式
switch_input_majorsearch = wd.find_element(By.CSS_SELECTOR,'.textarea-major')
search_text =  "AU % "+ "'"+ author +"' "+ "AND AF % "+ "'"+ work_unit +"'" 
switch_input_majorsearch.send_keys(search_text)
wd.find_element(By.CSS_SELECTOR,'.btn-search').click()


# 切换至下一页
author_output = ""
var = 1
while var == 1 :
	element = wd.find_element(By.CLASS_NAME,'result-table-list')
	Names = element.find_elements(By.CLASS_NAME,'name')
	# Data = element.find_element(By.CLASS_NAME,'data')
	# Authors = element.find_elements(By.CLASS_NAME,'author') #将来也许会用到,获取作者信息
	for Name in Names :
		author_output = author_output + ' '+Name.text 
	try :
		time.sleep(1)
		switch_next = wd.find_element(By.ID,'PageNext').click()
		time.sleep(1)
	except NoSuchElementException :
		break
	# except StaleElementReferenceException :
	# 	break
wd.quit()



# jieba分词
jieba.load_userdict(r"iTutor_setting/jieba_dict.txt")
words = jieba.lcut(author_output)
words_output = ' '.join(words)

# wordcloud
from wordcloud import STOPWORDS

# 读取自定义屏蔽词
add_stopwords = open("iTutor_setting/stopwords.txt","rt")
for line in add_stopwords.readlines():
	line = str(line)
	line = line[:-1]
	STOPWORDS.add(line)
add_stopwords.close()

wcloud = wordcloud.WordCloud(font_path = "iTutor_setting/font.ttf", width = 1920, height = 1080,background_color = "white",max_words = 300,stopwords=STOPWORDS)
wcloud.generate(words_output)
wcloud.to_file("outfile.png")
