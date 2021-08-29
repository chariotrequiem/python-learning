# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/29 16:44
# 2.1下载世界人口数据
"""
将文件population_data.json复制到本章程序所在的文件夹中，这个文件包含全球大部分国家1960~2010年的人口数据。
OpenKnowledge Foundation（http://data.okfn.org/ ）提供了大量可以免费使用的数据集，这些数据就来自其中一个数据集。
"""
# 2.2提取相关的数据
"""
我们来研究一下population_data.json，看看如何着手处理这个文件中的数据：
这个文件实际上就是一个很长的Python列表，其中每个元素都是一个包含四个键的字典：
国家名、国别码、年份以及表示人口数量的值。我们只关心每个国家2010年的人口数量，因此我们首先编写一个打印这些信息的程序：
import json
# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ": " + population)
"""

# 2.3将字符串转换成数字值
"""
population_data.json中的每个键和值都是字符串。为处理这些人口数据，
我们需要将表示人口数量的字符串转换为数字值，为此我们使用函数int() ：
然而，对于有些值，这种转换会导致错误，
原始数据的格式常常不统一，因此经常会出现错误。导致上述错误的原因是，
Python不能直接将包含小数点的字符串'1127437398.85751'转换为整数（这个小数值可能是人口数据缺失时通过插值得到的）。
为消除这种错误，我们先将字符串转换为浮点数，再将浮点数转换为整数：
"""

# 2.4获取两个字母的国别码
"""
制作地图前，还需要解决数据存在的最后一个问题。
Pygal中的地图制作工具要求数据为特定的格式：用国别码表示国家，以及用数字表示人口数量。
处理地理政治数据时，经常需要用到几个标准化国别码集。
population_data.json中包含的是三个字母的国别码，但Pygal使用两个字母的国别码。
我们需要想办法根据国家名获取两个字母的国别码。 
Pygal使用的国别码存储在模块i18n（internationalization的缩写）中。(pygal.il8n已弃用，现存于pygal_maps_world中)
字典COUNTRIES 包含的键和值分别为两个字母的国别码和国家名。
要查看这些国别码，可从模块i18n中导入这个字典，并打印其键和值：
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
    
为获取国别码，我们将编写一个函数，它在COUNTRIES 中查找并返回国别码。
我们将这个函数放在一个名为country_codes 的模块中，以便能够在可视化程序中导入它：
from pygal_maps_world.i18n import COUNTRIES 
def get_country_code(country_name): 
    #根据指定的国家，返回Pygal使用的两个字母的国别码
    for code, name in COUNTRIES.items(): 
        if name == country_name: 
            return code           
    # 如果没有找到指定的国家，就返回None 
    return None   
print(get_country_code('Andorra')) 
print(get_country_code('United Arab Emirates')) 
print(get_country_code('Afghanistan'))
get_country_code()接受国家名，并将其存储在形参country_name中。
接下来，我们遍历COUNTRIES中的国家名—国别码对；如果找到指定的国家名，就返回相应的国别码。
在循环后面，我们在没有找到指定的国家名时返回None

接下来，在world_population.py中导入get_country_code ：
import json
from country_codes import get_country_code
# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + "：" + str(population))
        else:
            print('ERROR - ' + country_name)
提取国家名和人口数量后，我们将国别码存储在code中，如果没有国别码，就在其中存储None 。
如果返回了国别码，就打印国别码和相应国家的人口数量。 如果没有找到国别码，就显示一条错误消息，其中包含无法找到国别码的国家的名称

导致显示错误消息的原因有两个。首先，并非所有人口数量对应的都是国家，有些人口数量对应的是地区（阿拉伯世界）和经济类群（所有收入水平）。
其次，有些统计数据使用了不同的完整国家名（如Yemen, Rep.，而不是Yemen）。
当前，我们将忽略导致错误的数据，看看根据成功恢复了的数据制作出的地图是什么样的。
"""

# 2.5制作世界地图
"""
有了国别码后，制作世界地图易如反掌。Pygal提供了图表类型Worldmap ，可帮助你制作呈现各国数据的世界地图。
为演示如何使用Worldmap ，我们来创建一个突出北美、中 美和南美的简单地图：
import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
创建了一个wm = pygal.maps.world.World()实例，并设置了该地图的的title属性。
使用了方法add()，它接受一个标签和一个列表，其中后者包含我们要突出的国家的国别码。
每次调用add()都将为指定的国家选择一种新颜色，并在图表左边显示该颜色和指定的标签。
我们要以同一种颜色显示整个北美地区，因此第一次调用add()时， 在传递给它的列表中包含'ca' 、'mx' 和'us'，
以同时突出加拿大、墨西哥和美国。接下来，对中美和南美国家做同样的处理。
方法render_to_file()创建一个包含该图表的.svg文件，你可以在浏览器中打开它。
"""

# 2.6在世界地图上呈现数字数据
"""
为练习在地图上呈现数字数据，我们来创建一幅地图，显示三个北美国家的人口数量：(na_populations.py)
import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')

首先，创建了一个实例并设置了标题。
接下来，使用了方法add()，但这次通过第二个实参传递了一个字典而不是列表。
这个字典将两个字母的Pygal国别码作为键，将人口数量作为值。
Pygal根据这些数字自动给不同国家着以深浅不一的颜色（人口最少的国家颜色最浅，人口最多的国家颜色最深）

"""

# 2.7绘制完整的世界人口地图
"""
要呈现其他国家的人口数量，需要将前面处理的数据转换为Pygal要求的字典格式：
键为两个字母的国别码，值为人口数量。为此，在world_population.py中添加如下代码：
import json
import pygal
from country_codes import get_country_code
# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

wm = pygal.maps.world.World()
wm.title = "World population in 2010, by Country"
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')

"""

# 2.8根据人口数量将国家分组
"""
印度和中国的人口比其他国家多得多，但在当前的地图中，它们的颜色与其他国家差别较小。
中国和印度的人口都超过了10亿，接下来人口最多的国家是美国，但只有大约3亿。 
下面不将所有国家都作为一个编组，而是根据人口数量分成三组——少于1000万的、介于1000万和10亿之间的以及超过10亿的：
# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# 看看每个分组包含多少国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm = pygal.maps.world.World()
wm.title = "World population in 2010, by Country"
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
"""

# 2.9使用pygal设置世界地图的样式
"""
在这个地图中，根据人口将国家分组虽然很有效，但默认的颜色设置很难看。
例如，在这里，Pygal选择了鲜艳的粉色和绿色基色。下面使用Pygal样式设置指令来调整颜色。 
我们也让Pygal使用一种基色，但将指定该基色，并让三个分组的颜色差别更大：
from pygal.style import RotateStyle

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
Pygal样式存储在模块style中，我们从这个模块中导入了样式RotateStyle。
创建这个类的实例时，需要提供一个实参——十六进制的RGB颜色；Pygal将根据指定的颜色为每组选择颜色。
十六进制格式的RGB颜色是一个以井号（#）打头的字符串，后面跟着6个字符，
其中前两个字符表示红色分量，接下来的两个表示绿色分量，最 后两个表示蓝色分量。
每个分量的取值范围为00 （没有相应的颜色）~FF （包含最多的相应颜色）。
如果你在线搜索hex colorchooser（十六进制颜色选择器 十 ），可找到让你能够尝试选择不同的颜色并显示其RGB值的工具。

这里使用的颜色值（#336699）混合了少量的红色（33）、多一些的绿色（66）和更多一些的蓝色（99），它为RotateStyle提供了一种淡蓝色基色。 

RotateStyle返回一个样式对象，我们将其存储在wm_style中。
为使用这个样式对象，我们在创建World实例时以关键字实参的方式传递它
"""

# 2.10加亮颜色主题
"""
Pygal通常默认使用较暗的颜色主题。为方便印刷，使用LightColorizedStyle加亮了地图的颜色。
这个类修改整个图表的主题，包括背景色、标签以及各个国家的颜色。 
要使用这个样式，先导入它：
from pygal.style import LightColorizedStyle
然后就可独立地使用LightColorizedStyle 了，例如：
wm_style = LightColorizedStyle
然而使用这个类时，你不能直接控制使用的颜色，Pygal将选择默认的基色。
要设置颜色，可使用RotateStyle，并将LightColorizedStyle作为基本样式。
为此，导入LightColorizedStyle和RotateStyle:
from pygal.style import LightColorizedStyle, RotateStyle
再使用RotateStyle创建一种样式，并传入另一个实参base_style ： 
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
这设置了较亮的主题，同时根据通过实参传递的颜色给各个国家着色。使用这种样式时，生成的图表与本书的屏幕截图更一致。 
尝试为不同的可视化选择合适的样式设置指令时，在import 语句中指定别名会有所帮助：
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
这样，样式定义将更短： 
wm_style = RS('#336699', base_style=LCS)
"""
