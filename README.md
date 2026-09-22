# FnSolver 简体中文版

用于《异度神剑X》和《异度神剑X 终极版》的边境网络布局求解工具，可根据持有的探针、已解锁地点和目标产出生成适合自己的布局方案。

本仓库是 [beta382/fnsolver](https://github.com/beta382/fnsolver) 的非官方简体中文特供版。界面固定使用简体中文，不提供语言切换。原版英文文档见 [README.en.md](README.en.md)。

## 汉化原则

- 游戏名称采用大陆简体中文官方写法《异度神剑X 终极版》。
- 游戏系统及探针名称优先采用大陆玩家通行术语，不进行逐词机翻。
- `FrontierNav.net`、`FnSolver` 等产品或网站名称保留原文。
- 术语有疑问时，以游戏内简体中文文本为最高优先级。

具体用词见 [简体中文术语表](doc/translation-glossary.zh-CN.md)。

## 构建

需要：

- CMake 3.28 或更高版本
- Ninja
- 支持 C++20 的编译器
- Qt 6（Core、Widgets、Svg、LinguistTools）

macOS/Linux：

```bash
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH="$(brew --prefix)"
cmake --build build
```

Windows 的详细环境配置和打包方式可参考[英文原版文档](README.en.md#building)。

## Windows 下载与发布

每个正式版本会在仓库的 [Releases](https://github.com/luopc1218/fnsolver-zh-cn/releases) 页面提供：

- `.exe`：Windows 安装包。
- `.zip`：免安装便携包。

维护者推送以 `v` 开头的版本标签后，GitHub Actions 会自动使用 MinGW 和 Qt 构建上述两个文件并创建 Release：

```bash
git tag v1.1.1-zh.1
git push origin v1.1.1-zh.1
```

## 更新翻译

先用 Qt `lupdate` 从源码更新中文 TS 文件，再运行人工翻译映射脚本：

```bash
lupdate fnsolver/gui \
  -no-obsolete \
  -locations none \
  -source-language en_US \
  -target-language zh_CN \
  -ts fnsolver/gui/translations/fnsolver_zh_CN.ts

python3 scripts/apply_zh_translations.py
```

如果上游新增了界面文字，脚本会列出尚未翻译的内容并以非零状态退出，避免发布夹杂英文的版本。

## 上游同步

```bash
git fetch upstream
git merge upstream/main
```

解决冲突后重新执行“更新翻译”中的命令，并重新构建。

## 版权与声明

FnSolver 原项目由 beta382 开发，并采用 [MIT License](LICENSE) 开源。本仓库保留原作者版权及第三方许可证声明。

《异度神剑X》及相关名称、图像和游戏素材的权利归其各自权利人所有。本项目是玩家制作的非官方工具，与 Nintendo、MONOLITHSOFT 及原项目作者不存在官方隶属或授权关系。
