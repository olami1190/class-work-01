top_html = open('./templates/top.html') .read()
bottom_html = open('./templates/bottom.html') .read()
middle_html = open('./content/index.html') .read()
combined= top_html + middle_html + bottom_html

open ('docs/index.html', 'w+') .write(combined)


middle_html = open('./content/project.html') .read()
combined= top_html + middle_html + bottom_html

open ('docs/project.html', 'w+') .write(combined)


middle_html = open('./content/blog.html') .read()
combined= top_html + middle_html + bottom_html

open ('docs/blog.html', 'w+') .write(combined)