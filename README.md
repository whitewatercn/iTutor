# 项目简介

这是一个小爬虫，用于爬取并导师在CNKI收录文献的相关信息，通过生成词云，直观了解导师研究方向

# 简易使用教程
https://www.bilibili.com/video/BV1XN4y1K7KQ

# 复杂使用说明
1. 需自行下载适配个人电脑的浏览器driver至目录 `iTutor_tool` (本项目自带chromedriver) [下载地址点这里](https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/install_drivers/)
2. 目录 `iTutor_setting` 中的 `jieba_dict.txt`为自定义分词配置文件,一行一词
3. 目录 `iTutor_setting` 中的 `stopwords.txt`为自定义排除词配置文件,一行一词

# 目前已实现
爬取文献名，绘制词云

# 项目进展
详见 https://github.com/users/whitewatercn/projects/3

# 依赖库
selenium
jieba
wordcloud
xlrd
