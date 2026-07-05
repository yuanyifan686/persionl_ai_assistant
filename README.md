# 个人 AI 助手 (Personal AI Assistant)

一个基于命令行的智能聊天助手，支持多轮对话、简单记忆管理，可轻松切换不同大模型（目前使用 MiniMax）。

## 项目简介

这是一个适合初学者学习 AI 应用开发的练手项目。通过这个项目，你可以理解：

- 如何调用大模型 API（OpenAI 兼容接口）
- 如何实现多轮对话记忆
- 如何使用环境变量保护 API Key
- 如何构建一个可扩展的命令行 AI 应用

## 功能特点

- ✅ 支持多轮连续对话（带简单记忆）
- ✅ 美观的终端输出（支持 Markdown 渲染）
- ✅ 通过 `.env` 安全管理 API Key
- ✅ 易于切换不同大模型（Grok、MiniMax、通义千问等）
- ✅ 完善的异常处理和退出机制
- ✅ 轻量级，无需复杂依赖

## 技术栈

- Python 3.10+
- OpenAI SDK（兼容 MiniMax / Grok 等）
- python-dotenv
- rich（美化终端输出）

## 项目结构

```
personal-ai-assistant/
├── main.py                 # 主程序
├── requirements.txt        # 依赖列表
├── .env                    # 环境变量（API Key）
├── README.md
└── venv/                   # 虚拟环境（可选）
```

## 快速开始

### 1. 克隆或下载项目

```bash
git clone <你的仓库地址>
cd personal-ai-assistant
```

### 2. 创建虚拟环境并安装依赖

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. 配置 API Key

在项目根目录创建 `.env` 文件，并填入你的 API Key：

```env
MINIMAX_API_KEY=sk-你的MiniMax_API_Key
```

> **支持切换模型**：只需修改 `base_url` 和 `MODEL` 即可切换为 Grok、DeepSeek、通义千问等支持 OpenAI 兼容接口的模型。

### 4. 运行程序

```bash
python main.py
```

## 使用说明

启动后直接输入问题即可对话：

```
✅ 个人 AI 助手已启动！（MiniMax）
输入 exit 或 quit 退出对话

你：你好
小助手：
（AI 回复内容，支持 Markdown 格式）

你：exit
```

支持的退出命令：`exit`、`quit`、`退出`

## 核心代码说明

- `messages` 列表：用于存储完整对话历史，实现多轮记忆
- `SYSTEM_PROMPT`：定义 AI 的角色和行为
- `MAX_HISTORY`：限制记忆长度，避免 token 消耗过高
- `base_url`：通过修改此参数可快速切换不同大模型服务商

## 自定义配置

### 修改 AI 性格

编辑 `main.py` 中的 `SYSTEM_PROMPT` 常量即可自定义 AI 的回复风格。

### 切换其他模型

修改以下两处即可：

```python
client = OpenAI(
    api_key=os.getenv("YOUR_API_KEY"),  #修改.env文件
    base_url="https://api.xxx.com/v1"   # 改成对应平台的地址
)

MODEL = "模型名称"                       # 改成对应平台的模型 ID
```



