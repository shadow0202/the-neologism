
### 新词分词工具

从网络热门网站获取即时信息，对获取内容进行分词 \ 获取新词操作。


### 启动方式

* 执行launch.py运行爬虫任务，爬取内容暂存在cawler_result目录下
* 执行/new_word_md/demo_run.py运行新词发现任务，结果暂存在/new_word_md/result/目录下
* 执行/jieba_md/jieba_fenci.py运行jieba分词任务，结果暂存在/jieba_md/result/目录下
* 执行/word_seg_md/newWordsfind.py运行无词库分词任务，结果暂存在/jieba_md/result/目录下

### 爬取\分词：

* 爬取的内容大致分娱乐信息流、国内外热点、体育新闻以及新兴产业电竞等。详见cawler_pages目录。
* 普通分词由jieba实现。
* 新词发现由[中文分词新词发现](https://github.com/zhanzecheng/Chinese_segment_augment.git)完成，感谢作者。


### 整体逻辑

1、通过结巴分词，剔除停用词和停用词性，获取所有分词结果，吊起权威词典API，检测词语是否在词典中，筛选出所有不在词典中的词语，记为新词。

2、[中文分词新词发现](https://github.com/zhanzecheng/Chinese_segment_augment.git) 可以直接切分出新词。

3、结果记录词频、排序。