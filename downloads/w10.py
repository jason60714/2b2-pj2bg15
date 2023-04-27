import random
from browser import html, document
bcd_tem = "https://mdecd2023.github.io/2b2-pj2bg"
bgithub = "https://github.com/mdecd2023/2b2-pj2bg"
brython_div = document["brython_div1"]
# 產生1到17的亂數排列
random_list = random.sample(range(1, 18), 17)

# 將亂數排列的結果儲存在陣列中
array = []
for i in random_list:
    array.append(i)
for i in range(1, 17):
    url = bcd_tem + str(array[i])
    github = bgithub + str(array[i])
    brython_div <= html.A("pj2bg"+str(array[i]), href=url)
    brython_div <= " ("
    brython_div <= html.A("repo", href=github)
    brython_div <= ")"
    brython_div <= html.BR()