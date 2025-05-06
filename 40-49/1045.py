import re

a = input()
b = re.sub('6666666666+', '27', a)
b = re.sub('6666+', '9', b)
print(b)

"""
https://www.runoob.com/python/python-reg-expressions.html
https://abigailqin.blog.csdn.net/article/details/136187262?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-2-136187262-blog-83864210.235%5Ev43%5Epc_blog_bottom_relevance_base9&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-2-136187262-blog-83864210.235%5Ev43%5Epc_blog_bottom_relevance_base9
"""