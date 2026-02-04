#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小学六年级英语练习题生成器
生成第2天（词汇基础）和第3天（句型基础）的练习题 Word 文档
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

def set_chinese_font(run, font_name='宋体', font_size=12):
    """设置中文字体"""
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)

def add_title(doc, title, subtitle):
    """添加主标题和副标题"""
    # 主标题
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.bold = True
    run.font.color.rgb = RGBColor(255, 0, 0)
    set_chinese_font(run, '黑体', 18)

    # 副标题
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(subtitle)
    set_chinese_font(run, '宋体', 14)
    doc.add_paragraph()  # 空行

def add_section_title(doc, title):
    """添加分节标题（带下划线）"""
    p = doc.add_paragraph()
    run = p.add_run(title)
    run.bold = True
    run.underline = True
    set_chinese_font(run, '黑体', 14)

def add_question_header(doc, number, title):
    """添加大题标题"""
    p = doc.add_paragraph()
    run = p.add_run(f'{number}、{title}')
    run.bold = True
    set_chinese_font(run, '宋体', 12)

def add_question(doc, text, indent=True):
    """添加题目"""
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.left_indent = Inches(0.3)
    run = p.add_run(text)
    set_chinese_font(run, '宋体', 11)

def add_answer_section(doc, answers):
    """添加参考答案部分"""
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('参考答案')
    run.bold = True
    run.font.color.rgb = RGBColor(255, 0, 0)
    set_chinese_font(run, '黑体', 16)
    doc.add_paragraph()

    for section, ans_list in answers.items():
        p = doc.add_paragraph()
        run = p.add_run(section)
        run.bold = True
        set_chinese_font(run, '宋体', 12)
        for ans in ans_list:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            run = p.add_run(ans)
            set_chinese_font(run, '宋体', 11)


# ============ 第2天：词汇基础 题库 ============

DAY2_PHRASES_TRANSLATE = [
    ('寻找', 'look for'),
    ('看', 'look at'),
    ('照顾', 'look after'),
    ('起床', 'get up'),
    ('上床睡觉', 'go to bed'),
    ('醒来', 'wake up'),
    ('穿上', 'put on'),
    ('脱下', 'take off'),
    ('打开（电器）', 'turn on'),
    ('关闭（电器）', 'turn off'),
    ('在周末', 'on the weekend'),
    ('在晚上', 'at night'),
    ('在早上', 'in the morning'),
    ('在学校', 'at school'),
    ('准时', 'on time'),
    ('及时', 'in time'),
    ('回家', 'go home'),
    ('做作业', 'do homework'),
    ('吃早餐', 'have breakfast'),
    ('上学', 'go to school'),
]

DAY2_FILL_BLANKS = [
    ('I am _______ my keys. Have you seen them?', 'looking for', '我正在找我的钥匙。你看到了吗？'),
    ('Please _______ the baby while I cook dinner.', 'look after', '我做晚饭时请照顾宝宝。'),
    ('He usually _______ at 7 o\'clock every morning.', 'gets up', '他通常每天早上7点起床。'),
    ('It\'s cold outside. Please _______ your coat.', 'put on', '外面很冷。请穿上你的外套。'),
    ('Don\'t forget to _______ the lights before you leave.', 'turn off', '离开前别忘了关灯。'),
    ('She does her homework _______ every day.', 'at night', '她每天晚上做作业。'),
    ('We have PE class _______.', 'in the morning', '我们早上有体育课。'),
    ('Please _______ the blackboard.', 'look at', '请看黑板。'),
    ('I _______ at 6:30 and then have breakfast.', 'wake up', '我6:30醒来然后吃早餐。'),
    ('Can you _______ the TV? I want to watch the news.', 'turn on', '你能打开电视吗？我想看新闻。'),
    ('It\'s hot. Please _______ your jacket.', 'take off', '很热。请脱下你的夹克。'),
    ('We must arrive _______ for the meeting.', 'on time', '我们必须准时到达会议。'),
    ('The doctor came _______ to save the patient.', 'in time', '医生及时赶到救了病人。'),
    ('I _______ at 9 o\'clock every night.', 'go to bed', '我每晚9点上床睡觉。'),
    ('What do you usually do _______?', 'on the weekend', '你周末通常做什么？'),
]

DAY2_DISTINGUISH = [
    ('look at / look for / look after',
     [('Please _______ the picture on the wall.', 'look at'),
      ('I\'m _______ my pen. Where is it?', 'looking for'),
      ('Can you _______ my dog this weekend?', 'look after')]),
    ('put on / take off',
     [('It\'s raining. _______ your raincoat.', 'Put on'),
      ('It\'s warm inside. You can _______ your sweater.', 'take off')]),
    ('turn on / turn off',
     [('It\'s dark. Please _______ the light.', 'turn on'),
      ('Before you go to bed, _______ the computer.', 'turn off')]),
    ('on time / in time',
     [('The train arrived _______.', 'on time'),
      ('We got to the station just _______ to catch the train.', 'in time')]),
    ('get up / wake up',
     [('I _______ at 6:00 but I don\'t _______ until 6:30.', 'wake up, get up')]),
]

DAY2_COMPLETE = [
    ('我每天早上六点半起床。', 'I _______ _______ at 6:30 every morning.', 'get up'),
    ('请照顾好你的妹妹。', 'Please _______ _______ your little sister.', 'look after'),
    ('他正在找他的书包。', 'He is _______ _______ his schoolbag.', 'looking for'),
    ('上课前请关掉手机。', 'Please _______ _______ your phone before class.', 'turn off'),
    ('天冷了，穿上你的毛衣。', 'It\'s cold. _______ _______ your sweater.', 'Put on'),
    ('我们周末去公园。', 'We go to the park _______ _______ _______.', 'on the weekend'),
    ('她每天晚上九点上床睡觉。', 'She _______ _______ _______ at 9 p.m. every day.', 'goes to bed'),
    ('请看这张地图。', 'Please _______ _______ this map.', 'look at'),
    ('我早上七点醒来。', 'I _______ _______ at 7 a.m.', 'wake up'),
    ('进屋后请脱掉你的鞋子。', 'Please _______ _______ your shoes after entering the room.', 'take off'),
]


# ============ 第3天：句型基础 题库 ============

DAY3_SENTENCE_JUDGE = [
    ('I am a student.', '主系表', 'am 是 be 动词，a student 是表语'),
    ('She is happy.', '主系表', 'is 是 be 动词，happy 是表语'),
    ('They are teachers.', '主系表', 'are 是 be 动词，teachers 是表语'),
    ('He likes apples.', '主谓宾', 'likes 是实义动词，apples 是宾语'),
    ('We play football.', '主谓宾', 'play 是实义动词，football 是宾语'),
    ('She reads books every day.', '主谓宾', 'reads 是实义动词，books 是宾语'),
    ('The cat is on the table.', '主系表', 'is 是 be 动词，on the table 是表语'),
    ('I have a dog.', '主谓宾', 'have 是实义动词，a dog 是宾语'),
    ('Tom watches TV at night.', '主谓宾', 'watches 是实义动词，TV 是宾语'),
    ('My mother is a doctor.', '主系表', 'is 是 be 动词，a doctor 是表语'),
    ('The flowers are beautiful.', '主系表', 'are 是 be 动词，beautiful 是表语'),
    ('He does his homework.', '主谓宾', 'does 是实义动词，his homework 是宾语'),
    ('We are in the classroom.', '主系表', 'are 是 be 动词，in the classroom 是表语'),
    ('She eats breakfast at 7.', '主谓宾', 'eats 是实义动词，breakfast 是宾语'),
    ('The book is interesting.', '主系表', 'is 是 be 动词，interesting 是表语'),
]

DAY3_TO_QUESTION = [
    ('I am a student.', 'Are you a student?', 'be 动词提前'),
    ('She is happy.', 'Is she happy?', 'be 动词提前'),
    ('They are teachers.', 'Are they teachers?', 'be 动词提前'),
    ('He likes apples.', 'Does he like apples?', '加 Does，动词变原形'),
    ('We play football.', 'Do you play football?', '加 Do'),
    ('She reads books.', 'Does she read books?', '加 Does，动词变原形'),
    ('Tom watches TV.', 'Does Tom watch TV?', '加 Does，动词变原形'),
    ('I have a dog.', 'Do you have a dog?', '加 Do'),
    ('He is a doctor.', 'Is he a doctor?', 'be 动词提前'),
    ('They like music.', 'Do they like music?', '加 Do'),
    ('She goes to school.', 'Does she go to school?', '加 Does，动词变原形'),
    ('We are happy.', 'Are you happy?', 'be 动词提前'),
    ('He does homework.', 'Does he do homework?', '加 Does，动词变原形'),
    ('I am tired.', 'Are you tired?', 'be 动词提前'),
    ('She has a cat.', 'Does she have a cat?', '加 Does，动词变原形'),
]

DAY3_TO_NEGATIVE = [
    ('I am a student.', 'I am not a student.', 'be 动词后加 not'),
    ('She is happy.', 'She is not happy.', 'be 动词后加 not'),
    ('They are teachers.', 'They are not teachers.', 'be 动词后加 not'),
    ('He likes apples.', 'He does not like apples.', '加 does not，动词变原形'),
    ('We play football.', 'We do not play football.', '加 do not'),
    ('She reads books.', 'She does not read books.', '加 does not，动词变原形'),
    ('Tom watches TV.', 'Tom does not watch TV.', '加 does not，动词变原形'),
    ('I have a dog.', 'I do not have a dog.', '加 do not'),
    ('He is a doctor.', 'He is not a doctor.', 'be 动词后加 not'),
    ('They like music.', 'They do not like music.', '加 do not'),
    ('She goes to school.', 'She does not go to school.', '加 does not，动词变原形'),
    ('We are happy.', 'We are not happy.', 'be 动词后加 not'),
    ('He does homework.', 'He does not do homework.', '加 does not，动词变原形'),
    ('I am tired.', 'I am not tired.', 'be 动词后加 not'),
    ('She has a cat.', 'She does not have a cat.', '加 does not，动词变原形'),
]

DAY3_BE_DO_FILL = [
    ('_______ you a student? Yes, I _______.', 'Are, am', '主语 you 用 Are'),
    ('_______ she like apples? Yes, she _______.', 'Does, does', '第三人称单数用 Does'),
    ('He _______ not a teacher.', 'is', 'be 动词否定'),
    ('They _______ not play football.', 'do', '复数主语用 do'),
    ('_______ it cold today? Yes, it _______.', 'Is, is', '主语 it 用 Is'),
    ('She _______ not go to school on Sunday.', 'does', '第三人称单数用 does'),
    ('_______ your mother a doctor? Yes, she _______.', 'Is, is', '主语 your mother 用 Is'),
    ('_______ they have a car? No, they _______.', 'Do, don\'t', '复数主语用 Do'),
    ('I _______ not happy today.', 'am', '主语 I 用 am'),
    ('_______ Tom like music? Yes, he _______.', 'Does, does', '第三人称单数用 Does'),
    ('We _______ students.', 'are', '主语 We 用 are'),
    ('_______ you play basketball? Yes, I _______.', 'Do, do', '主语 you 用 Do'),
    ('The cat _______ on the table.', 'is', '主语 The cat 用 is'),
    ('_______ he do his homework? Yes, he _______.', 'Does, does', '第三人称单数用 Does'),
    ('My parents _______ not at home.', 'are', '复数主语用 are'),
]

DAY3_TRANSFORM = [
    ('He is a good boy.', '一般疑问句', 'Is he a good boy?'),
    ('She likes reading.', '否定句', 'She does not like reading.'),
    ('They are in the park.', '一般疑问句', 'Are they in the park?'),
    ('I play games every day.', '否定句', 'I do not play games every day.'),
    ('Tom has a new bike.', '一般疑问句', 'Does Tom have a new bike?'),
    ('We are happy.', '否定句', 'We are not happy.'),
    ('She watches TV at night.', '一般疑问句', 'Does she watch TV at night?'),
    ('He is my friend.', '否定句', 'He is not my friend.'),
    ('They do homework.', '一般疑问句', 'Do they do homework?'),
    ('I am a student.', '否定句', 'I am not a student.'),
    ('She is beautiful.', '一般疑问句', 'Is she beautiful?'),
    ('He plays football.', '否定句', 'He does not play football.'),
    ('We have lunch at 12.', '一般疑问句', 'Do you have lunch at 12?'),
    ('The dog is cute.', '否定句', 'The dog is not cute.'),
    ('They like swimming.', '一般疑问句', 'Do they like swimming?'),
]


# ============ 生成第2天文档函数 ============

def generate_day2_doc(version, output_path):
    """生成第2天词汇基础练习题"""
    doc = Document()

    # 根据版本确定题目数量
    if version == '简洁版':
        trans_count, fill_count, dist_count, comp_count = 4, 4, 2, 3
    elif version == '完整版':
        trans_count, fill_count, dist_count, comp_count = 8, 8, 4, 6
    else:  # 充实版
        trans_count, fill_count, dist_count, comp_count = 15, 15, 5, 10

    add_title(doc, '小学六年级英语练习题【词汇基础】', f'（基础+提升）第2天 - {version}')
    add_section_title(doc, '短语与固定搭配专项练习')

    answers = {}

    # 一、短语汉译英
    add_question_header(doc, '一', '短语汉译英（根据中文写出英文短语）')
    ans_list = []
    for i, (cn, en) in enumerate(DAY2_PHRASES_TRANSLATE[:trans_count], 1):
        add_question(doc, f'{i}. {cn} _______________________')
        ans_list.append(f'{i}. {en}')
    answers['一、短语汉译英'] = ans_list

    # 二、选词填空
    add_question_header(doc, '二', '选词填空（从词库中选择正确短语填入句子）')
    word_bank = ['look for', 'look after', 'get up', 'put on', 'turn off',
                 'at night', 'in the morning', 'look at', 'wake up', 'turn on',
                 'take off', 'on time', 'in time', 'go to bed', 'on the weekend']
    add_question(doc, f'词库：{", ".join(word_bank[:min(fill_count+2, len(word_bank))])}')
    doc.add_paragraph()
    ans_list = []
    for i, (sent, ans, _) in enumerate(DAY2_FILL_BLANKS[:fill_count], 1):
        add_question(doc, f'{i}. {sent}')
        ans_list.append(f'{i}. {ans}')
    answers['二、选词填空'] = ans_list

    # 三、短语辨析
    add_question_header(doc, '三', '短语辨析（选择正确的短语填空）')
    ans_list = []
    q_num = 1
    for phrase_group, questions in DAY2_DISTINGUISH[:dist_count]:
        add_question(doc, f'【{phrase_group}】', indent=False)
        for sent, ans in questions:
            add_question(doc, f'{q_num}. {sent}')
            ans_list.append(f'{q_num}. {ans}')
            q_num += 1
    answers['三、短语辨析'] = ans_list

    # 四、完成句子
    add_question_header(doc, '四', '完成句子（根据中文提示完成英文句子）')
    ans_list = []
    for i, (cn, en, ans) in enumerate(DAY2_COMPLETE[:comp_count], 1):
        add_question(doc, f'{i}. {cn}')
        add_question(doc, f'   {en}')
        ans_list.append(f'{i}. {ans}')
    answers['四、完成句子'] = ans_list

    add_answer_section(doc, answers)
    doc.save(output_path)
    print(f'已生成: {output_path}')


# ============ 生成第3天文档函数 ============

def generate_day3_doc(version, output_path):
    """生成第3天句型基础练习题"""
    doc = Document()

    # 根据版本确定题目数量
    if version == '简洁版':
        judge_count, quest_count, neg_count, fill_count, trans_count = 4, 4, 4, 4, 4
    elif version == '完整版':
        judge_count, quest_count, neg_count, fill_count, trans_count = 8, 8, 8, 8, 8
    else:  # 充实版
        judge_count, quest_count, neg_count, fill_count, trans_count = 15, 15, 15, 15, 15

    add_title(doc, '小学六年级英语练习题【句型基础】', f'（基础+提升）第3天 - {version}')
    add_section_title(doc, '陈述句、一般疑问句与否定句专项练习')

    answers = {}

    # 一、句型判断
    add_question_header(doc, '一', '句型判断（判断下列句子是"主系表"还是"主谓宾"结构）')
    ans_list = []
    for i, (sent, ans, reason) in enumerate(DAY3_SENTENCE_JUDGE[:judge_count], 1):
        add_question(doc, f'{i}. {sent}  （        ）')
        ans_list.append(f'{i}. {ans}（{reason}）')
    answers['一、句型判断'] = ans_list

    # 二、陈述句转一般疑问句
    add_question_header(doc, '二', '陈述句转一般疑问句')
    ans_list = []
    for i, (sent, ans, rule) in enumerate(DAY3_TO_QUESTION[:quest_count], 1):
        add_question(doc, f'{i}. {sent}')
        add_question(doc, '   _______________________________________')
        ans_list.append(f'{i}. {ans}（{rule}）')
    answers['二、陈述句转一般疑问句'] = ans_list

    # 三、陈述句转否定句
    add_question_header(doc, '三', '陈述句转否定句')
    ans_list = []
    for i, (sent, ans, rule) in enumerate(DAY3_TO_NEGATIVE[:neg_count], 1):
        add_question(doc, f'{i}. {sent}')
        add_question(doc, '   _______________________________________')
        ans_list.append(f'{i}. {ans}（{rule}）')
    answers['三、陈述句转否定句'] = ans_list

    # 四、be动词与do/does选择填空
    add_question_header(doc, '四', 'be动词与do/does选择填空')
    ans_list = []
    for i, (sent, ans, rule) in enumerate(DAY3_BE_DO_FILL[:fill_count], 1):
        add_question(doc, f'{i}. {sent}')
        ans_list.append(f'{i}. {ans}（{rule}）')
    answers['四、be动词与do/does选择填空'] = ans_list

    # 五、句型转换综合练习
    add_question_header(doc, '五', '句型转换综合练习（按要求改写句子）')
    ans_list = []
    for i, (sent, req, ans) in enumerate(DAY3_TRANSFORM[:trans_count], 1):
        add_question(doc, f'{i}. {sent}（改为{req}）')
        add_question(doc, '   _______________________________________')
        ans_list.append(f'{i}. {ans}')
    answers['五、句型转换综合练习'] = ans_list

    add_answer_section(doc, answers)
    doc.save(output_path)
    print(f'已生成: {output_path}')


# ============ 主函数 ============

def main():
    """生成所有练习题文档"""
    import os

    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    versions = ['简洁版', '完整版', '充实版']

    print('开始生成英语练习题文档...\n')

    # 生成第2天文档
    for version in versions:
        filename = f'第2天_词汇基础_{version}.docx'
        output_path = os.path.join(script_dir, filename)
        generate_day2_doc(version, output_path)

    # 生成第3天文档
    for version in versions:
        filename = f'第3天_句型基础_{version}.docx'
        output_path = os.path.join(script_dir, filename)
        generate_day3_doc(version, output_path)

    print('\n所有文档生成完成！')


if __name__ == '__main__':
    main()
