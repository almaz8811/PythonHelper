from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
price = 345
template = env.get_template('template.html')
rendered_page = template.render(cap1_title='Красная кепка',
                                cap1_text='$ 100.00',
                                cap2_title='Черная кепка',
                                cap2_text=f'$ {price}.00')
print(rendered_page)
with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)