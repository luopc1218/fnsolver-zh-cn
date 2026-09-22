#!/usr/bin/env python3
"""将人工维护的简体中文译文写入 Qt Linguist TS 文件。"""

from pathlib import Path
import xml.etree.ElementTree as ET

TS_FILE = Path(__file__).parents[1] / "fnsolver/gui/translations/fnsolver_zh_CN.ts"

T = {
    '<a href="aboutqt">About Qt...</a>': '<a href="aboutqt">关于 Qt...</a>',
    '<a href="https://felldragon.tumblr.com/post/781458744593809408/ah-yeah-if-anyone-needs-image-assets-from">DE Icons ripped by calico</a>': '<a href="https://felldragon.tumblr.com/post/781458744593809408/ah-yeah-if-anyone-needs-image-assets-from">终极版图标由 calico 提取</a>',
    'Minimum Resources': '最低稀有资源产量', 'Minimum Yields': '最低产出要求',
    'Min. Mining': '最低米拉矿产量', 'Min. Revenue': '最低收益', 'Min. Storage': '最低储藏量',
    '%n territories': '%n 个未探索区域', 'No probe': '无探针',
    'Original': '原版', 'Definitive': '终极版',
    'Name': '名称', 'Count': '持有数', 'Used': '已使用', 'Remaining': '剩余', 'Max': '上限',
    '&File': '文件(&F)', '&View': '视图(&V)', '&Layout': '布局(&L)', '&Inventory': '探针库存(&I)',
    '&Help': '帮助(&H)', 'Toolbar': '工具栏', 'Game': '游戏版本', 'Inventory': '探针库存', 'Results': '计算结果',
    '&New': '新建(&N)', '&Open': '打开(&O)', 'Recent Documents': '最近使用的文件', '&Save': '保存(&S)',
    'Save &As': '另存为(&A)', 'E&xit': '退出(&X)', 'Zoom &In': '放大(&I)', 'Zoom &Out': '缩小(&O)',
    'Zoom &All': '显示全部(&A)', 'Load from FrontierNav.net': '从 FrontierNav.net 导入',
    'Show in FrontierNav.net': '在 FrontierNav.net 中查看', 'Unlock All': '全部解锁', 'Lock All': '全部锁定',
    'Set All to Basic': '全部设为基础探针', 'Get All in Game': '填入游戏内全部探针',
    'Remove Mining': '移除所有采掘探针', 'Remove Research': '移除所有调查探针',
    'About': '关于', 'Website': '项目网站', 'Solve': '开始计算', 'Unsaved file[*]': '未保存的配置[*]',
    'Error opening file': '打开文件失败', '%1 is not valid.': '%1 不是有效的配置文件。',
    'Error saving file': '保存文件失败', 'The file could not be opened for writing.': '无法打开文件进行写入。',
    'This layout has been modified.': '当前布局已被修改。', 'Would you like to save your changes?': '是否保存更改？',
    'Open Simulation...': '打开计算配置…', 'Simulations (*.toml)': 'FnSolver 配置 (*.toml)',
    'Save Simulation...': '保存计算配置…', 'FrontierNav.net URL:': 'FrontierNav.net 网址：',
    'Invalid FrontierNav.net URL': 'FrontierNav.net 网址无效', 'Enter a URL from FrontierNav.net.': '请输入 FrontierNav.net 的布局网址。',
    'Score Function': '评分函数', 'Tiebreaker': '平分判定', 'Constraints': '限制条件',
    'Solver Parameters': '求解参数', 'Score Function and Tiebreaker must be different.': '评分函数和平分判定不能相同。',
    'Calculating...': '正在计算…', 'Overall Best Score': '全局最佳得分', 'Solutions Killed': '已淘汰布局数',
    'Last Improvement': '最近一次改进', 'Mining': '米拉矿产量', 'Revenue': '收益', 'Storage': '储藏量',
    'Cancel': '取消', '%1 of %2': '%1 / %2', '%1 / %2': '%1 / %2', '%1 remaining': '剩余 %1',
    '%n bonus iteration(s) remaining': '剩余 %n 次奖励迭代', 'This iteration': '本轮迭代',
    '%n iteration(s) ago': '%n 次迭代前', 'Production:': '产出力：', 'Revenue:': '收益力：',
    'Storage:': '储藏量：', 'Resources:': '稀有资源：', '%1/%2': '%1/%2', '%1%': '%1%',
    'Quantity': '数量', 'Percent': '百分比', 'Seed': '布局种子', 'Force Seed': '强制保留种子',
    'Iterations': '迭代次数', 'Bonus Iterations': '奖励迭代次数', 'Population': '种群规模',
    'Offspring': '子代数量', 'Mutation rate': '变异率', 'Max Age': '最大存活轮数', 'Threads': '线程数',
    'Use Defaults': '恢复默认值', 'All': '全部满足', 'Any': '任意满足', 'Percent': '百分比',
    'Min. Avg. Yield': '最低平均产量', 'of %1': '（满产量 %1）', 'None': '无',
    'Max Mining': '米拉矿产量最大化', 'Max Effective Mining': '有效米拉矿产量最大化',
    'Max Revenue': '收益最大化', 'Max Storage': '储藏量最大化', 'Ratio': '按比例优化', 'Weights': '加权优化',
    'Mining Factor': '米拉矿系数', 'Revenue Factor': '收益系数', 'Storage Factor': '储藏系数',
    'Mining Weight': '米拉矿权重', 'Revenue Weight': '收益权重', 'Storage Weight': '储藏权重',
    'Locked': '未解锁', 'Basic': '基础探针', 'Duplicator': '复制探针', 'Combat': '战斗探针',
    'Arc Sand Ore': '弧砂矿石', 'Aurorite': '极光石', 'White Cometite': '白彗石',
    'Enduron Lead': '恩杜隆铅矿', 'Everfreeze Ore': '永冻矿石', 'Foucaultium': '傅科矿',
    'Lionbone Bort': '狮骨硼石', 'Infernium': '地狱矿', 'Boiled-Egg Ore': '煮蛋矿石',
    'Marine Rutile': '海洋金红石', 'Dawnstone': '曙光石', 'Cimmerian Cinnabar': '辛梅里安朱砂',
    'Ouroboros Crystal': '衔尾蛇水晶', 'Parhelion Platinum': '幻日铂', 'Bonjelium': '硼琼矿',
}

for grade in range(1, 11):
    T[f'Mining G{grade}'] = f'采掘探针 G{grade}'
for grade in range(1, 7):
    T[f'Research G{grade}'] = f'调查探针 G{grade}'
for grade in range(1, 3):
    T[f'Booster G{grade}'] = f'强化探针 G{grade}'

# Storage 在不同上下文中既可能是数值，也可能是探针名；单独按上下文处理。
CONTEXT_T = {
    ('probe_ui', 'Storage'): '储藏探针',
}

LONG = {
    'Requires that a generated FrontierNav layout yield at least': '''要求生成的边境网络布局平均至少产出指定数量的稀有资源。

每个边境网络地点都有各自的稀有资源产出概率和判定次数。概率详情可查阅 Xeno Series Wiki（例如 [硼琼矿](https://www.xenoserieswiki.org/wiki/Bonjelium)）。不同地点的稀有资源预期掉落量可能相差很大，因此按“能够产出稀有资源的地点数量”进行限制并无实际意义。这里的限制条件采用“平均预期产出数量”。''',
    'Requires that a generated FrontierNav layout yield at least the specified Miranium': '''要求生成的边境网络布局至少达到指定的米拉矿产量、收益和/或储藏量。

**不建议使用此选项**。即使设定看似不高，也可能让 FnSolver 极难找到满足条件的布局。请优先使用“按比例优化”评分函数。本选项主要用于研究和尝试。''',
    '<strong>FN%1</strong>': '''<strong>FN%1</strong><br>
%2<br>
已发现 %3 / %4 个未探索区域<br>
<table>
  <tr><th align="right">产出力：</th><td align="left">%5</td></tr>
  <tr><th align="right">收益力：</th><td align="left">%6</td></tr>
  <tr><th align="right">战斗力：</th><td align="left">%7</td></tr>
  <tr><th align="right">矿石：</th><td align="left">%8</td></tr>
</table>''',
    'The Score Function is used to calculate': '评分函数用于计算每个边境网络布局的“得分”，以便比较不同布局并判断哪一个更优。',
    'Generally, this is only interesting with': '平分判定通常只适合搭配“储藏量最大化”“有效米拉矿产量最大化”或“按比例优化”。若评分函数为“米拉矿产量最大化”或“收益最大化”，调查探针和采掘探针仍会分别产生少量另一类产出，因此平分判定的影响通常很小。“加权优化”本身已经包含类似的取舍。',
    'The FnSolver algorithm can be simplified as follows:': '''FnSolver 算法可简化为：

- 随机生成 `<population>` 个边境网络布局
- 重复执行 `<iterations>` 轮：
  - 种群中的每个布局生成 `<offspring>` 个变异子代：
    - 按 `<mutation rate>` 的概率随机交换布局中的探针
    - 若最佳子代优于亲本，则由该子代取代亲本
    - 若所有子代均未改善亲本，且亲本不是当前最佳布局，则亲本的存活轮数增加
    - 亲本达到 `<max age>` 后，由新的随机布局取代

总运行时间大致与 `iterations * population * offspring` 成正比。

以下选项用于控制上述参数。将鼠标悬停在选项上可查看它对计算的影响。''',
    'The layout seed is used to alter': '''布局种子用于引导 FnSolver 生成随机边境网络布局。新生成的随机布局一定包含种子中的探针配置，但后续产生变异时可能偏离种子（参见“强制保留种子”）。

布局种子可用于：

- 提供一组你认为接近最优的核心探针配置，通常配合“强制保留种子”，让 FnSolver 更快找到优质布局，或找到原本难以发现的布局。
- 提供上一次计算或手工制作的完整布局，让 FnSolver 继续微调。这样会限制算法探索差异较大的布局，但可以集中算力优化当前方案。

勾选后，所有已解锁地点上的非基础探针都会加入布局种子。''',
    'Forces the layout seed to be retained': 'FnSolver 生成布局变异时强制保留布局种子。所有已指定的非基础探针都会出现在生成的每一个边境网络布局中。',
    'Increasing this will give FnSolver more time': '增加迭代次数可让 FnSolver 有更多时间发现并改进边境网络布局。你可以随时点击“取消”提前结束；当前迭代完成后，程序会停止计算并显示已找到的最佳布局。',
    'Sets the maximum number of additional iterations': '设置找到更优布局后最多追加的迭代次数。\n\n设为非零值后，如果 FnSolver 即将结束时发现了更优布局，实际迭代次数可以超过“迭代次数”。奖励迭代不会累加，但每次找到更优布局都会重新计数。换言之，只有总迭代达到设定值，并且距离最近一次改进已经经过指定的奖励迭代次数，计算才会结束。',
    'Increasing this will give FnSolver more opportunities to find potentially-optimal': '增加种群规模可以让 FnSolver 同时探索更多差异明显、可能接近最优的布局。该算法的子代通常与亲本相似，因此某条布局演化路线可能停在无法轻易改善、但并非真正最优的“局部最优”状态。更大的种群有助于缓解这一问题。',
    'Increasing this will give FnSolver more opportunities to find mutations': '增加子代数量可以提高找到有利变异的机会。连锁效果具有阈值特性，只交换少量探针时不容易形成；某些特定变异也很难随机出现。更多子代有助于缓解这一问题，但对于把整条连锁与另一处连锁互换等复杂变异，仍没有理想的解决方案。',
    'Sets the degree by which a FronterNav layout will mutate': '设置生成子代时边境网络布局的变异程度。\n\n该数值表示某个地点的探针与另一地点探针发生交换的概率。由于交换涉及两个位置，还可能交换相同探针或再次交换之前的位置，单个地点实际发生有效交换的概率约为变异率的 1.67 倍。存在未解锁地点或强制布局种子时，该概率会略微降低。\n\n变异率过低时难以找到需要复杂调整的改进；过高时又难以保留优质布局的核心结构，也不利于找到简单改进。通常建议设为约 0.03～0.08。',
    'Sets the maximum number of iterations a FrontierNav layout lineage': '设置一条布局演化路线在没有改进的情况下最多保留多少轮。\n\n提高该值，可让尚非最佳的布局获得更多时间寻找复杂或精细的改进；但设得过高，会使陷入次优局部最优的布局无法及时淘汰重启。通常应按“迭代次数”大致同比例调整。\n\n得分为 0（即不满足限制条件）的布局会以 5 倍速度增加存活轮数。',
    'Sets the number of threads to execute FnSolver': '设置 FnSolver 并行计算所用的线程数。\n\nFnSolver 会尝试以计算机的逻辑处理器数量作为默认值；若无法检测，则默认为 1，需要手动设置。通常建议设为逻辑处理器数量。设置更少会因资源闲置而降低性能（也可有意为系统保留资源）；设置更多则不会带来进一步提升。',
    '- Uses the lesser of "Total Storage"': '- 以“总储藏量”和“米拉矿产量 × 储藏系数”中较小的一项作为得分。\n- 表示“在储藏量上限内，经过指定边境网络周期后实际可获得多少米拉矿”。',
    '- Uses "Mining yield"': '- 以米拉矿产量作为得分。',
    '- It is recommended to use `Max Effective Mining`': '- 建议使用“有效米拉矿产量最大化”，通常更符合实际需求。',
    '- Uses "Revenue Yield"': '- 以收益作为得分。', '- Uses "Total Storage"': '- 以总储藏量作为得分。',
    '- Takes three argument: `Mining Factor`': '- 接受米拉矿系数、收益系数和储藏系数三个参数。\n- 对每个系数非零的产出类型，计算“产出 ÷ 对应系数 × 最大系数”，并以其中最小值作为得分。\n- 在保持指定产出比例的同时尽可能提高各项产出。',
    '- Takes three argument: `Mining Weight`': '- 接受米拉矿权重、收益权重和储藏权重三个参数。\n- 将各项产出乘以对应权重后求和作为得分。\n- **通常不建议使用**，因为结果往往只是最大化权重最高的产出。建议改用其他评分函数。本选项仅用于与 XenoProbes 保持功能一致。',
}

tree = ET.parse(TS_FILE)
root = tree.getroot()
missing = []
for context in root.findall('context'):
    context_name = context.findtext('name', '')
    for message in context.findall('message'):
        source = message.findtext('source', '')
        translation = CONTEXT_T.get((context_name, source), T.get(source))
        if translation is None:
            stripped = source.strip()
            for prefix, value in LONG.items():
                if stripped.startswith(prefix):
                    translation = value
                    break
        node = message.find('translation')
        if translation is None:
            missing.append(f'{context_name}: {source[:80]!r}')
            continue
        node.attrib.pop('type', None)
        if message.get('numerus') == 'yes':
            forms = list(node.findall('numerusform'))
            if not forms:
                forms = [ET.SubElement(node, 'numerusform')]
            forms[0].text = translation
        else:
            node.text = translation

ET.indent(tree, space='    ')
tree.write(TS_FILE, encoding='utf-8', xml_declaration=True)
if missing:
    raise SystemExit('仍有未翻译文本：\n' + '\n'.join(missing))
