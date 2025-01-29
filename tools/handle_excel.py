"""
函数封装步骤： 任何功能代码都可以封装函数。
1、第一步：先把功能代码写出来 【逻辑】
2、第二步： def，封装函数
3、第三步：参数化，变化的数据参数化 ：不是固定，用户输入的数据，从其他地方获取数据等
4、第四步：判断是否需要返回值，return定义返回值  [别人调用函数为了拿什么数据？]

这个封装好的方法要进行代码分层管理 --tools
"""
from openpyxl import load_workbook

def read_excel(excel,sheet):
    """
    这是读取excel表格数据的一个方法
    :param excel: excel文件路径和名字
    :param sheet: 读取数据的表单
    :return: 读取后所有数据， 保存为列表嵌套字典的格式
    """
    wb = load_workbook(excel)
    sh = wb[sheet]
    # 列表嵌套元组-- 每个元组是一行数据
    cases = list(sh.values)
    list_case = []
    # 每个用例都要跟标题元组压缩，取出来标题的元组
    title = cases[0]
    #遍历后面的每一行【 每条用例】 分别跟标题行压缩 zip
    for case in cases[1:]:
        data = dict(zip(title,case))
        list_case.append(data)
    return list_case

if __name__ == '__main__':
    from tools.handle_path import excel_path

    print(read_excel(excel_path, "login"))