# PandocTemplate

一个简单好用的 **Markdown → HTML** 导出方案，基于 [Pandoc](https://pandoc.org/) 和自定义 HTML 模板。

## ✨ 特性

- 🎨 现代化深蓝配色主题，阅读体验舒适
- 📑 **自动生成侧边栏目录**（TOC，最多 3 级），粘性定位跟随滚动
- 💻 代码块 **语法高亮**（tango 主题），鼠标悬停显示 **一键复制** 按钮
- 🏷️ 支持 Pandoc fenced div 语法：`:::tip` / `:::warning` / `:::info` 彩色提示框
- ⌨️ `<kbd>` 键盘按键样式、任务列表 (`- [x]`)、脚注、图片自适应
- 🖨️ **打印/导出 PDF 友好**（模板内置打印样式，侧边栏自动隐藏）
- 🔤 自动识别文档一级标题作为页面标题，副标题默认显示用户名 / 目录 · 时间
- 🖱️ 锚点平滑滚动、移动端响应式布局

## 📦 目录结构

```bash
PandocTemplate/ 
├── export_html.py # Python 导出脚本 
└── template.html # Pandoc 自定义 HTML 模板
```

## 🛠️ 环境依赖

| 依赖 | 说明 |
|------|------|
| Python ≥ 3.6 | 已安装即可，无需额外第三方库 |
| [Pandoc](https://pandoc.org/installing.html) | 必须安装并加入系统 PATH |

### 安装 Pandoc

- **Windows**：访问 [pandoc.org/installing.html](https://pandoc.org/installing.html) 下载安装包，或用 `winget install Pandoc.Pandoc`
- **Linux**：`sudo apt install pandoc` 或 `sudo pacman -S pandoc`
- **macOS**：`brew install pandoc`

## 🚀 快速开始

最简单的用法——一行命令导出：

```bash
python export_html.py example.md
```

这会在同目录下生成 `example.html`，标题自动取文档第一个 `#` 一级标题。

### 常用命令示例

```bash
# 指定输出文件路径
python export_html.py example.md -o output/report.html

# 自定义页面标题和副标题
python export_html.py example.md --title "我的文档" --subtitle "2026年度"

# 添加页脚文字
python export_html.py example.md --footer "© 2026 My Company"

# 关闭彩色语法高亮（改用单色）
python export_html.py example.md --no-highlight
```

### 完整参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `md` | 输入的 Markdown 文件路径（位置参数，必填） | — |
| `-o`, `--output` | 输出 HTML 路径 | 与输入同名 `.html` |
| `-t`, `--title` | 页面标题 | 文档首个 `#` 标题，否则用文件名 |
| `-s`, `--subtitle` | 横幅副标题 | 用户名 / 目录 · 当前时间 |
| `-f`, `--footer` | 页脚文字 | 无页脚 |
| `--no-highlight` | 关闭彩色语法高亮 | `false`（使用 tango 主题） |

## 🎯 使用小技巧

### 在 Markdown 中写彩色提示框

```markdown
:::tip
这是一个小技巧提示。
:::

:::warning
⚠️ 注意事项，左边红色边框。
:::

:::info
ℹ️ 信息提示，左边蓝色边框。
:::
```

### 打印 / 保存 PDF

导出的 HTML 页面右上角有 **"打印／保存PDF"** 按钮，点击后浏览器会弹出打印对话框。建议在打印设置中：
- 纸张方向：纵向
- 边距：默认或最小
- 勾选 **背景图形**（Chrome/Edge 中）以保留页面底色

### 自定义样式

`template.html` 是标准 Pandoc 模板，顶部 `<style>` 中的 CSS 可以自由修改。例如想换主题色，把 `#163c57`（深蓝）替换成你喜欢的颜色即可。
