import numpy as np
import matplotlib.pyplot as plt
import csv

# 1、绘制不同学校课程数量分布图（条状图）。
def task_0():
    import numpy as np
    import matplotlib.pyplot as plt
    import csv
    # 读取第一列(跳过第一行)
    Institution = np.loadtxt("datasets_736_1367_appendix.csv", str,encoding='utf-8',delimiter=',', usecols=(0), unpack=True,skiprows=1)
    Institution_name = list(set(Institution))
    #print(Institution_name)
    MITx_num , HarvardX_num= 0,0
    for i in Institution:
        if i == Institution_name[0]:
            MITx_num+=1
        elif i == Institution_name[1]:
            HarvardX_num+=1
    #print(MITx_num,HarvardX_num)
    Institution_num = [MITx_num,HarvardX_num]

    plt.figure()
    plt.bar(Institution_name,Institution_num)


    # 网图像上加上数字标签
    for x,y in zip(Institution_name,Institution_num):
        plt.text(x,y+0.6,str(y),ha='center', va='bottom', fontsize=10.5)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("不同学校课程数量分布图")
    plt.xlabel('学校')
    plt.ylabel('课程数量')
    plt.savefig("task0.png")
    plt.show()

# 绘制不同学校上线课程数量随年份的分布图（线性图）。
def task_1():
    import numpy as np
    import matplotlib.pyplot as plt
    import csv
    # 读取第一列和第三列 （跳过第一行）
    Institution,Launch_Date = np.loadtxt("datasets_736_1367_appendix.csv", str, encoding='utf-8', delimiter=',', usecols=(0,2),
                             unpack=True, skiprows=1)

    # 处理每门课程的日期，将日期只保留年份
    Launch_Date =[ i.split("/")[-1] for i in Launch_Date]

    Institution_name = list(set(Institution))
    year_label = list(set(Launch_Date))
    year_label = [int(i) for i in year_label]
    year_label.sort()
    year_label = [str(i) for i in year_label]
    print(Institution_name)
    print(year_label)

    # 一共有多少年份
    year_nums = len(list(set(Launch_Date)))
    # 一共有多少学校
    Institution_num = len(list(set(Institution)))

    date = np.zeros((Institution_num,year_nums))
    for i in range(len(Launch_Date)):
        if Institution[i]==Institution_name[0] and Launch_Date[i] == year_label[0]:
            date[0][0]+=1
        elif Institution[i]==Institution_name[0] and Launch_Date[i] == year_label[1]:
            date[0][1] += 1
        elif Institution[i]==Institution_name[0] and Launch_Date[i] == year_label[2]:
            date[0][2] += 1
        elif Institution[i]==Institution_name[0] and Launch_Date[i] == year_label[3]:
            date[0][3] += 1
        elif Institution[i]==Institution_name[0] and Launch_Date[i] == year_label[4]:
            date[0][4] += 1
        elif Institution[i]==Institution_name[1] and Launch_Date[i] == year_label[0]:
            date[1][0]+=1
        elif Institution[i]==Institution_name[1] and Launch_Date[i] == year_label[1]:
            date[1][1] += 1
        elif Institution[i]==Institution_name[1] and Launch_Date[i] == year_label[2]:
            date[1][2] += 1
        elif Institution[i]==Institution_name[1] and Launch_Date[i] == year_label[3]:
            date[1][3] += 1
        elif Institution[i]==Institution_name[1] and Launch_Date[i] == year_label[4]:
            date[1][4] += 1

    print(date)

    plt.rcParams['font.sans-serif'] = ['SimHei']

    for i in range(len(Institution_name)):
        #plt.plot(year_label,date[i])
        if i==0:
            plt.plot(year_label, date[i],'ro--')
        else :
            plt.plot(year_label, date[i],'bo-.')


    # 图示：在左上角显示图示
    plt.legend(Institution_name, loc=2)

    # 网图像上加上数字标签
    for x, y in zip(year_label, date[0]):
        plt.text(x, y + 4, str(int(y)), ha='center', va='bottom', fontsize=10.5,color='black')

    for x, y in zip(year_label, date[1]):
        plt.text(x, y + 3, str(int(y)), ha='center', va='bottom', fontsize=10.5,color='green')

    plt.title("学校上线课程数量随年份的分布图")
    plt.xlabel('年份')
    plt.ylabel('课程数量')
    plt.savefig("task1.png")
    plt.show()

# 3、绘制不同主题（Course Subject）课程数量分布占比图（条状图）。
def task_2():
    import numpy as np
    import matplotlib.pyplot as plt
    import csv
    # 读取第6列，跳过第一行
    with open("datasets_736_1367_appendix.csv","r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        Course_Subject = [row['Course Subject'] for row in reader]

    # 保证每次生成的图片一致
    Course_Subject_name = list(set(Course_Subject))
    Course_Subject_name.sort()
    print(Course_Subject_name)
    total = np.zeros(len(Course_Subject_name))
    for i in Course_Subject:
        for j in range(len(Course_Subject_name)):
            if i==Course_Subject_name[j]:
                total[j]+=1
                break
    total = [round(i/290*1.0*100,2) for i in total]
    print(total)


    plt.figure()

    plt.rcParams['font.sans-serif'] = ['SimHei']

    for i in range(len(Course_Subject_name)):
        plt.bar(Course_Subject_name[i],total[i])

    # 图示：在左上角显示图示
    plt.legend(Course_Subject_name, loc=2)

    # 网图像上加上数字标签
    for x, y in zip(Course_Subject_name,total):
        plt.text(x, y + 1, str(y)+'%', ha='center', va='bottom', fontsize=10.5, color='black')

    # 横坐标的字体大小，偏移角度
    plt.xticks(rotation=10,size=8)

    plt.title("不同主题（Course Subject）课程数量分布占比")
    plt.xlabel('Course Subject')
    plt.ylabel('课程数量占比')
    plt.savefig("task2.png")
    plt.show()

# 绘制不同主题课程学生平均人数随年份分布图（线性图）
def task_3():
    import numpy as np
    import matplotlib.pyplot as plt
    import csv
    Launch_Date = np.loadtxt("datasets_736_1367_appendix.csv", str, encoding='utf-8', delimiter=',', usecols=(2),
                             unpack=True, skiprows=1)

    # 处理每门课程的日期，将日期只保留年份
    Launch_Date = [i.split("/")[-1] for i in Launch_Date]

    year_label = list(set(Launch_Date))
    year_label = [int(i) for i in year_label]
    year_label.sort()
    year_label = [str(i) for i in year_label]

    # 获取不同主题课程列表
    with open("datasets_736_1367_appendix.csv","r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        Course_Subject = [row['Course Subject'] for row in reader]

    with open("datasets_736_1367_appendix.csv","r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        Participants = [row['Participants (Course Content Accessed)'] for row in reader]

    # 获取课程名字数组
    # 保证每次生成的图片一致
    Course_Subject_name = list(set(Course_Subject))
    Course_Subject_name.sort()

    # 记录每年每门课程的中人数
    datesets = np.zeros((len(Course_Subject_name),len(year_label)))
    # # 记录每年每门课程出现的次数
    course_nums = np.zeros((len(Course_Subject_name), len(year_label)))

    for std_nums in range(len(Participants)):
        for i in range(len(Course_Subject_name)):
            for j in range(len(year_label)):
                if Launch_Date[std_nums]==year_label[j] and Course_Subject[std_nums]==Course_Subject_name[i]:
                    datesets[i][j]+=int(Participants[std_nums])
                    course_nums[i][j]+=1
                    break

    # print(datesets)
    # print(course_nums)

    # 获取不同主题课程每年学生平均人数
    for i in range(len(Course_Subject_name)):
        for j in range(len(year_label)):
            if course_nums[i][j]>0:
                datesets[i][j] = int(datesets[i][j]/course_nums[i][j])
            else:
                datesets[i][j] = 0

    #print(datesets)
    plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']

    for i in range(len(Course_Subject_name)):
        plt.plot(year_label,datesets[i],'o-.')

    # 图示：在右上角显示图示
    plt.legend(Course_Subject_name, loc=1)

    # 网图像上加上数字标签
    for i in range(len(Course_Subject_name)):
        for x, y in zip(year_label, datesets[i]):
            plt.text(x, y + 1, str(int(y)) , ha='center', va='bottom', fontsize=10.5, color='black')

    plt.title("不同主题课程学生平均人数随年份分布图")
    plt.xlabel('年份')
    plt.ylabel('学生平均人数')
    plt.savefig("task3.png")
    plt.show()

# 绘制不同学校不同主题课程男性学员平均占比图(（条状图）)
def task_4():
    import numpy as np
    import matplotlib.pyplot as plt
    import csv
    # 不同学校
    Institution = np.loadtxt("datasets_736_1367_appendix.csv", str, encoding='utf-8', delimiter=',', usecols=(0),
                             unpack=True, skiprows=1)

    # 不同主题课程
    with open("datasets_736_1367_appendix.csv","r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        Course_Subject = [row['Course Subject'] for row in reader]

    # 男性学员平均占比
    with open("datasets_736_1367_appendix.csv","r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        Male = [row['% Male'] for row in reader]

    #print(Male)

    Institution_name = list(set(Institution))
    Institution_name.sort()

    Course_Subject_name = list(set(Course_Subject))
    Course_Subject_name.sort()

    # 记录每个学校不同科目的男性占比总数
    datesets = np.zeros((len(Institution_name),len(Course_Subject_name)))
    # 出现的次数
    course_nums = np.zeros((len(Institution_name), len(Course_Subject_name)))

    for one in range(len(Male)):
        for i in range(len(Institution_name)):
            for j in range(len(Course_Subject_name)):
                if Institution_name[i]==Institution[one] and Course_Subject_name[j]==Course_Subject[one]:
                    datesets[i][j]+=float(Male[one])
                    course_nums[i][j]+=1
                    break

    # 计算平均男生占比
    for i in range(len(Institution_name)):
        for j in range(len(Course_Subject_name)):
            if course_nums[i][j]==0:
                datesets[i][j]=0
            else:
                datesets[i][j] = round(datesets[i][j]/course_nums[i][j],2)

    print(datesets)

    X = np.arange(0,len(Course_Subject_name),1)
    plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    width = 0.36

    plt.bar(X - width / 2, datesets[0], tick_label = Course_Subject_name, width=width)
    plt.bar(X + width / 2, datesets[1],tick_label = Course_Subject_name, width=width)


    # 图示：在左上角显示图示
    plt.legend(Institution_name, loc=2)
    # 网图像上加上数字标签
    for i in range(len(Institution_name)):
        for x, y in zip(X, datesets[i]):
            if i==0:
                plt.text(x - width / 2, y , str(y) + "%", ha='center', va='bottom', fontsize=10.5, color='black')
            else:
                plt.text(x + width / 2, y , str(y) + "%", ha='center', va='bottom', fontsize=10.5, color='black')
    # 横坐标的字体大小，偏移角度
    plt.xticks(rotation=10, size=8)
    X=[i*10 for i in range(11) if i>0]
    plt.yticks(X)


    plt.title("不同学校不同主题课程男性学员平均占比图")
    plt.xlabel('不同主题课程')
    plt.ylabel('男性学员平均占比(%)')
    plt.savefig("task4.png")
    plt.show()


def main():
    # task_0()
    #
    # task_1()
    #
    # task_2()
    #
    # task_3()

    task_4()
    return 0

if __name__ == '__main__':
    main()