b1 = open(r'D:\合曜AI\golden-flower-ei\lib\i18n.tsx','rb').read()
b2 = open(r'D:\合曜AI\golden-flower-ei\app\page.tsx','rb').read()
s1 = b1.decode('utf-8')
s2 = b2.decode('utf-8')
print('i18n.tsx: total chars', len(s1))
keys = ['home.projects.title','home.projects.deqi.body','home.projects.xg.body','home.projects.ys.body']
print('i18n: home.projects keys count:', sum(1 for k in keys if k in s1))
print('page.tsx: total chars', len(s2))
print('page: ProjectCard defined:', 'function ProjectCard' in s2)
print('page: Project section rendered:', 'home.projects.title' in s2)
print('page: 3 project cards:', s2.count('ProjectCard'))
print('---')
# extract zh patch area
idx = s1.find('home.projects.title')
end = s1.find('home.projects.ys.body', idx)
if idx >= 0 and end >= 0:
    excerpt = s1[idx:end+80]
    print('zh patch area first 600 chars:')
    print(excerpt[:600])