"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

give_texts=[]
give_calls=set([])
resive_texts=set([])
resive_calls=set([])

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    give_texts = [x[0] for x in texts]
    resive_texts = [x[1] for x in texts]

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    give_calls = [x[0] for x in calls]
    resive_calls = [x[1] for x in calls]

all_give=set(give_texts) | set(give_calls)
all_resive= set(resive_texts) | set(resive_calls)

result=all_give - all_resive
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

