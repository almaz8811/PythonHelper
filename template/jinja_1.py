from jinja2 import Template

site = 'almaz8811'
domain = 'com'
print(f'{site}.{domain}')

tm = Template('My site name is {{site}}.{{domain}}')
msg = tm.render(site=site, domain=domain)
print(msg)