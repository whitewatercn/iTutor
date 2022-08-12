import time
import jieba
import wordcloud
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


# 待查询信息
end_year = 2022
begin_year = input("请输入最早年份:")
author = input("请输入作者名称:")
work_unit = input("请输入作者单位:")

# get网站
wd = webdriver.Chrome(service=Service(r"DRIVER—_PATH")) #手动填写webdriver本地路径
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
numbers = 0
var = 1
while var == 1 :
	element = wd.find_element(By.CLASS_NAME,'result-table-list')
	Names = element.find_elements(By.CLASS_NAME,'name')
	# Data = element.find_element(By.CLASS_NAME,'data')
	# Authors = element.find_elements(By.CLASS_NAME,'author') #将来也许会用到,获取作者信息
	for Name in Names :
		author_output = author_output + ' '+Name.text 
		# numbers = numbers + 1
		# year = data.text
	try :
		time.sleep(1)
		switch_next = wd.find_element(By.ID,'PageNext').click()
	except NoSuchElementException :
		break
wd.quit()





# jieba分词
jieba.load_userdict(r"TXT_PATH") #手动填写自定义词库路径
words = jieba.lcut(author_output)
words_output = ' '.join(words)

# wordcloud
from wordcloud import STOPWORDS
STOPWORDS.add('的') #手动填写更多阻止词

wcloud = wordcloud.WordCloud(font_path = "TFF_PATH", width = 1920, height = 1080,background_color = "white",max_words = 300,stopwords=STOPWORDS) #手动填写字体路径
wcloud.generate(words_output)
wcloud.to_file("outfile.png")
