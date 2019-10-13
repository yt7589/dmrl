#
import numpy as np
import matplotlib.pyplot as plt

def read_file_in_project():
    print('读取项目中文件，如README.md')
    with open('README.md', 'r', encoding='utf-8') as fd:
        readme = fd.read()
    print('README.md文件内容：{0}'.format(readme))
    # 写入文件
    with open('a1.txt', 'w', encoding='utf-8') as f1:
        f1.write('The 中文内容 is great')
    # 读出内容
    with open('a1.txt', 'r', encoding='utf-8') as f2:
        s2 = f2.read()
    print('f2:{0}'.format(s2))
    
def read_file_on_disk():
    with open('/content/drive/My Drive/dmrl/data/t1.txt', 'r', encoding='utf-8') as fd:
        s1 = fd.read()
    print('s1:{0}'.format(s1))
    with open('/content/drive/My Drive/dmrl/data/t2.txt', 'w', encoding='utf-8') as f2:
        f2.write('The content:中文语言模型')
    print('The End')

def draw_matplotlib():
  x = np.linspace(0, 10, 100)
  fig = plt.figure()
  plt.plot(x, np.sin(x), '-')
  plt.plot(x, np.cos(x), '--')
  #plt.show()
  plt.savefig('/content/drive/My Drive/dmrl/log/a1.png')


def main():
  print('DMRL v0.0.1 build 3')
  #read_file_in_project()
  #read_file_on_disk()
  draw_matplotlib()

if '__main__' == __name__:
  main()
