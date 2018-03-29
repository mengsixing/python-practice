"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

giveTexts=set([])
givecalls=set([])

resiveTexts=set([])
resiveCalls=set([])



with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
    	if text[0] not in giveTexts:
    		giveTexts.add(text[0])
    	if text[1] not in resiveTexts:
    		resiveTexts.add(text[1])


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
    	if call[0] not in givecalls:
    		givecalls.add(call[0])
    	if call[1] not in resiveCalls:
    		resiveCalls.add(call[1])

allGive=giveTexts | givecalls;
allResive=resiveTexts | resiveCalls;

result=allGive - allResive

print('hese numbers could be telemarketers: ')

for item in sorted(result):
	print(item)


"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

