#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pandoc 风格文档导出脚本，Windows / Linux 通用。
依赖：pandoc（已加入 PATH）、本脚本同目录下的 template.html

用法：
  python export_html.py input.md                          # 全自动，无页脚
  python export_html.py input.md --footer "页脚文字"        # 带页脚
  python export_html.py input.md --title "标题" --subtitle "副标题" -o out.html
"""
import argparse
import getpass
import re
import subprocess
import sys
import shutil
from datetime import datetime
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description="Markdown → 风格 HTML")
    p.add_argument("md", help="输入的 Markdown 文件")
    p.add_argument("-o", "--output", help="输出 HTML 路径（默认与输入同名）")
    p.add_argument("-t", "--title", help="页面标题（默认取文档第一个一级标题，否则用文件名）")
    p.add_argument("-s", "--subtitle", help="横幅副标题（默认：用户名 / 文件所在目录 · 当前时间）")
    p.add_argument("-f", "--footer", help="页脚文字（不传则没有页脚）")
    p.add_argument("--no-highlight", action="store_true", help="启用 monochrome(单色) 语法高亮关闭")
    args = p.parse_args()

    md = Path(args.md)
    if not md.is_file():
        sys.exit(f"找不到文件: {md}")
    out = Path(args.output) if args.output else md.with_suffix(".html")
    template = Path(__file__).resolve().parent / "template.html"
    if not template.is_file():
        sys.exit(f"找不到模板: {template}（请与脚本放在同一目录）")

    # 标题：优先取文档第一个 “# ” 一级标题，取不到用文件名
    title = args.title
    if not title:
        m = re.search(r"^#\s+(.+)$", md.read_text(encoding="utf-8"), re.M)
        title = m.group(1).strip() if m else md.stem

    # 副标题：用户名 / 文件所在目录 · 当前时间
    folder = md.resolve().parent.name or md.resolve().parent.as_posix()
    subtitle = args.subtitle or (
        f"{getpass.getuser()} / {folder} · "
        f"{datetime.now():%Y-%m-%d %H:%M}"
    )
    # # 副标题：用户名 / 终端当前目录 · 当前时间
    # subtitle = args.subtitle or (
    #     f"{getpass.getuser()} / {Path.cwd().name} · "
    #     f"{datetime.now():%Y-%m-%d %H:%M}"
    # )

    cmd = [
        "pandoc", str(md), "-o", str(out),
        "--standalone", f"--template={template}",
        "--toc", "--toc-depth=3",
        "--metadata", f"title={title}",
        "--metadata", f"subtitle={subtitle}",
        "--from", "markdown+fenced_divs",
    ]
    if args.footer:
        cmd += ["--metadata", f"footer={args.footer}"]

    if args.no_highlight:
        cmd += ["--syntax-highlighting", "monochrome"]
    else:
        cmd += ["--syntax-highlighting", "tango"]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ 已导出: {out}")
    except subprocess.CalledProcessError as e:
        sys.exit(f"❌ Pandoc 转换失败，退出代码: {e.returncode}")


if __name__ == "__main__":
    exe = shutil.which("pandoc")
    if not exe:
        sys.exit(
            "❌ 错误：未找到 pandoc 命令。\n"
            "请确保已安装 Pandoc 并将其加入系统环境变量 (PATH) 中。\n"
            "下载地址：https://pandoc.org/installing.html"
        )
    main()
