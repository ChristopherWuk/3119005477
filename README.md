Hi there.


| 这个作业属于哪个课程  |[信安1912-软件工程 (广东工业大学 - 计算机学院)](https://edu.cnblogs.com/campus/gdgy/InformationSecurity1912-Softwareengineering/)|
|--------------------|------------------------------------------------------------------------------------------------------------------------------|
| 这个作业要求在哪里 	  |[个人项目作业](https://edu.cnblogs.com/campus/gdgy/InformationSecurity1912-Softwareengineering/homework/12146)                 |
| 这个作业的目标   	  |1.                                                                                                                           |


|PSP2.1						|Personal Software Process Stages	|预估耗时（分钟） 	|实际耗时（分钟） 	|
|:--						|:--								|:--:				|:--:				|
|Planning					|计划								|__640__    		|					|
|· Estimate					|· 估计这个任务需要多少时间			|640   		    	|					|
|Development				|开发								|__560__			|					|
|· Analysis					|· 需求分析 (包括学习新技术)      	    |240    			|					|
|· Design Spec              |· 生成设计文档					    |60     			|					|
|· Design Review			|· 设计复审					    	|30             	|					|
|· Coding Standard			|· 代码规范 (为目前的开发制定合适的规范)|10		    		|					|
|· Design			    	|· 具体设计       					|60		    		|					|
|· Coding					|· 具体编码  						|120				|					|
|· Code Review				|· 代码复审  						|20		     		|					|
|· Test					    |· 测试（自我测试，修改代码，提交修改） |20 				|					|
|Reporting					|报告    							|__80__				|					|
|· Test Report				|· 测试报告							|20 				|					|
|· Size Measurement			|· 计算工作量						|20 				|					|
|· Postmortem & Process Improvement Plan|· 事后总结, 并提出过程改进计划|40				|					|
|							|· 合计          					|640				|					|




## 题目

> 题目：论文查重
>
>描述如下：
>
>设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。
>
>原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
>抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。
>要求输入输出采用文件输入输出，规范如下：
>
>从命令行参数给出：论文原文的文件的绝对路径。
>从命令行参数给出：抄袭版论文的文件的绝对路径。
>从命令行参数给出：输出的答案文件的绝对路径。
>我们提供一份样例，课堂上下发，上传到班级群，使用方法是：orig.txt是原文，其他orig_add.txt等均为抄袭版论文。
>
>注意：答案文件中输出的答案为浮点型，精确到小数点后两位
 

## 需求分析

1.设计一个论文查重算法
  首先联想到目前学术论文届基本都会用的知网算法，但是知网算法在网络上并没有公开其算法，且其算法会根据段落和目录这些因素来进行查重。
  
  考虑到在密码学中一般来说有一种流程是校验，即校验数据和数字签名是否一样，这其中用到md5算法，这应该是一种hash算法。
  
  而如果收到的数据和原数据有出入，那么得到的哈希值将大相径庭。因此联想到这个方面，查重算法也许可以往hash方向上靠。
  
  后来发现事实上谷歌公司曾提出过一种simhash算法并发表，原论文名为
  _Detecting Near-Duplicates for Web Crawling_, 作者为Gurmeet Singh Manku, Arvind Jain和Anish Das Sarma.
  
  后面会对此算法具体分析说明，于是本项目决定采用simhash算法进行查重。
  
2.需要用文件进行输入输出，且需要精确到小数点后两位。


### simhash算法

#### Keywords
Hamming distance, near-duplicate, similarity, search, sketch,
fingerprint, web crawl, web document

在引言中，文章提到，关于如何消除网络上爬下来的的相似文章的问题没有被重视。

>A system for detection of near-duplicate pages faces a
>number of challenges. First and foremost is the issue of scale:
>search engines index billions of web-pages; this amounts to
>a multi-terabyte database. Second, the crawl engine should
>be able to crawl billions of web-pages per day. So the decision to mark a newly-crawled page as a near-duplicate of an
>existing page should be made quickly. Finally, the system
>should use as few machines as possible.

引言中提到这样的一个查重系统面临许多挑战。一是文章的规模巨大，互联网上有很多很多文章和页面；二是爬虫引擎能够
在一天之内爬下很多很多页面，这些决定了这个系统必须要快；三是这个系统必须尽可能少地用机器。

文章在第二阶段着重介绍simhash算法，故我们对第二阶段进行翻译和研究。

simhash算法主要有五个阶段
1.分词，这一步是为了把具体的语句分词之后转化为通用的向量来进行下一步运算。

2.hash，通过hash函数计算每个向量的hash值。

3.加权，给特征向量加权，得到若干个序列串。

4.合并，把所有向量相加，即把分出来的词最终转化为一个序列串。

5.降维，大于0置1，小于0置0，把上面的序列串降维成只有0，1组成的串，形成simhash签名


第三阶段说明了如何得到相似度，此处用到hammer distance即汉明距离。

64位的simhash值，若汉明距离在3以内可认为相似度较高。

汉明距离算法：两个simhash值每一位进行异或，得到1的个数为汉明距离大小。






















































