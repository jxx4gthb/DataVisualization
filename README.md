# 网吧大数据分析与可视化

## 项目背景

随着网络宽带的普及，网吧的经营面临挑战。一些网吧通过接纳未成年人、通宵营业等违规方式吸引顾客，但这些行为影响社会秩序。为提高执法效率，某市公安局采用数据分析技术，从海量网吧上网记录中探索人群行为特征、检测非法操作行为，为整治黑网吧和犯罪预防提供新思路。

---

## 项目目标

1. **数据清洗**：
   - 处理出生日期、上下线时间、姓名及区域代码等无效数据。
   - 确保数据准确性和可靠性。

2. **统计分析**：
   - 分析上网人数时段分布、人员省份、性别及年龄段分布。
   - 统计网吧接待人次及违法经营行为。

3. **数据可视化**：
   - 使用交互式图表展示上网行为及区域分布特征。
   - 利用 D3.js 和百度地图 API 构建交互式大屏。

4. **核心问题**：
   - 标记接待未成年人的网吧。
   - 检测冒用身份信息的违法行为。

---

## 数据集

- **网吧基础信息表**：
  包括网吧编号、名称、经纬度等信息。
- **上网记录表**：
  包括上网人编号、上线时间、下线时间、出生日期等约 1600 万条记录。

---

## 技术栈

- **编程语言**：Python
- **前端**：D3.js、百度地图 API
- **后端**：Flask
- **数据分析**：Pandas、Plotly
- **数据库**：CSV 格式文件

---

## 功能实现

### 1. 数据清洗

- **删除无效记录**：
  - 不合理的出生日期。
  - 上下线时间不匹配的记录。
  - 包含数字的姓名字段。
- **校验区域代码**：
  - 仅保留有效的身份证区域编码。

### 2. 数据统计分析

- **上网时刻分析**：
  - 每小时上网人数分布。
  - 分析活跃时间段和非活跃时间段。
- **人口特征分析**：
  - 性别比例：男性与女性人数。
  - 年龄分布：18 岁以下、18-25 岁、26-35 岁、36-45 岁、45 岁以上。
- **省份来源分析**：
  - 统计上网人群的籍贯分布。
  - 使用玫瑰图展示省份占比。
- **网吧接待分析**：
  - 每个网吧接待人次统计。
  - 统计接待人数不足 10 人/天的网吧。

### 3. 违法行为检测

- **接待未成年人**：
  - 标记年龄小于 18 岁的上网记录。
- **冒用身份信息**：
  - 检测连续上网时间超过 24 小时的记录。
  - 针对不同年龄段的特殊行为进行标注。

### 4. 数据可视化

- **主界面交互设计**：
  - D3.js 和百度地图 API 构建的交互式可视化大屏。
  - 分为网吧分布图、区域统计图、违法行为展示等模块。
- **可视化图表**：
  - 桑基图：展示年龄段与上网时长的关联。
  - 饼状图：性别与年龄分布。
  - 散点图：上网人数与时间分布。
  - 气泡图：上网时刻的活跃程度。

---

## 项目结构
```
project/
├── data/
│   ├── cafe_info.csv            # 网吧基础信息
│   ├── age1_info.csv            # 清洗后的上网记录数据
│   ├── gender_distribution.csv  # 性别分布统计
│   ├── province_counts.csv      # 人员省份统计
│   ├── remarked_cyber_info.csv  # 标注后的网吧违法行为
│   └── …                      # 其他数据文件
├── src/
│   ├── data_cleaning.py         # 数据清洗脚本
│   ├── statistical_analysis.py  # 数据分析脚本
│   ├── visualization.py         # 可视化脚本
│   ├── illegal_detection.py     # 违法行为检测脚本
│   └── server.py                # Flask 后端服务
├── static/
│   ├── css/                     # 样式文件
│   ├── js/                      # 前端交互逻辑
│   └── img/                     # 图片资源
└── README.md                    # 项目说明文件
```
---

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/jxx4gthb/DataVisualization.git
cd DataVisualization
```
### 2. 安装依赖

确保安装 Python 和 pip，运行以下命令安装所需库：
```bash
pip install -r requirements.txt
```
### 3. 运行服务

启动 Flask 后端服务：
```bash
python src/server.py
```
### 4. 打开可视化界面

在浏览器中访问 http://localhost:5000。

## 核心成果

	•	大数据分析能力：
	•	从 1.7GB 的数据中挖掘关键行为模式。
	•	高效执法支持：
	•	提供接待未成年人和冒用身份信息的网吧名单。
	•	直观数据展示：
	•	通过交互式大屏可视化提升数据可读性。
 ## 许可证

该项目采用 MIT 许可证。详情请查看 LICENSE。
