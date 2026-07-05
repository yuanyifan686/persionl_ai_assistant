import os
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

client = OpenAI(
    api_key=os.getenv("MINIMAX_API_KEY"),       # 从 .env 读取
    base_url="https://api.minimax.chat/v1"         # 修改
)

console = Console()

SYSTEM_PROMPT = """你是一个聪明、友好、专业的个人 AI 助手。
你的名字叫“小助手”。
回答问题时要简洁、准确、有帮助。
如果不知道答案，就诚实地说不知道。
"""

MAX_HISTORY = 10
MODEL = "MiniMax-M3"                         # 修改


def chat_with_ai():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    
    console.print("[bold green]✅ 个人 AI 助手已启动！（MiniMax）[/bold green]")
    console.print("输入 [bold]exit[/bold] 或 [bold]quit[/bold] 退出对话\n")
    
    while True:
        try:
            user_input = console.input("[bold blue]你：[/bold blue]").strip()
            
            if user_input.lower() in ["exit", "quit", "退出"]:
                console.print("[yellow]再见！期待下次对话～[/yellow]")
                break
            
            if not user_input:
                continue
            
            messages.append({"role": "user", "content": user_input})
            
            with console.status("[bold green]小助手思考中...[/bold green]"):
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=messages,
                    temperature=0.7,
                    max_tokens=2000,
                )
            
            assistant_reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": assistant_reply})
            
            if len(messages) > MAX_HISTORY + 1:
                messages = [messages[0]] + messages[-(MAX_HISTORY):]
            
            console.print("[bold green]小助手：[/bold green]")
            console.print(Markdown(assistant_reply))
            console.print()
            
        except KeyboardInterrupt:
            console.print("\n[yellow]对话已中断，再见！[/yellow]")
            break
        except Exception as e:
            console.print(f"[red]出错了：{str(e)}[/red]\n")


if __name__ == "__main__":
    chat_with_ai()