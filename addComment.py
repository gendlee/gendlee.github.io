import os

comment_scrpit = open('comment.script','r')
'''
comment.script是一个文件，内容为：
<script src="https://utteranc.es/client.js"
        repo="gendlee/gendlee.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
'''

comment_scrpit_str = comment_scrpit.read()
keyword = '</article>'
keyword_before = '<span>Home</span>'
keyword_after_replace = '<span>回到主页</span>'

file_dir = '.\\public\\'


def file_name(file_dir):   
    my_blog_files=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.html' and os.path.splitext(file)[0].startswith('0'):  
                my_blog_files.append(file)  
    return my_blog_files;


my_blog_files = file_name(file_dir)

print(my_blog_files)


def replace(file, old_content, new_content):
    content = read_file(file)
    content = content.replace(old_content, new_content)
    rewrite_file(file, content)

# 读文件内容
def read_file(file):
    with open(file, 'r', encoding='UTF-8') as f:
        read_all = f.read()
        f.close()

    return read_all

# 写内容到文件
def rewrite_file(file, data):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(data)
        f.close()

# 将Home换成回到主页
for blog_file_name in my_blog_files:
    file_path = file_dir+blog_file_name
    replace(file_path, keyword_before, keyword_after_replace)

# 文章尾部添加评论脚本
for blog_file_name in my_blog_files:
    file_path = file_dir+blog_file_name
    file = open(file_path,'r', encoding='utf-8')
    content = file.read()
    post = content.find(keyword)
    if post != -1:
        content = content[:post+len(keyword)]+comment_scrpit_str+content[post+len(keyword):]
        file = open(file_path,'w', encoding='utf-8')
        file.write(content)
        file.close()

print("给所有文章添加评论功能完成！")