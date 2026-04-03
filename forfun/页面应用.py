import tkinter as tk
from tkinter import messagebox
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage
import pygame
import asyncio
import edge_tts
import subprocess
import json
import threading
import os

# 配置 Rhubarb 路径
RHUBARB_PATH = r"D:\Downloads\Rhubarb-Lip-Sync-1.14.0-Windows\rhubarb.exe"


class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        # 初始化 AI
        self.chat = ChatTongyi(model="qwen-max")  # 纠正了模型名称
        # 初始化音频混音器
        pygame.mixer.init()

    def setup_ui(self):
        self.root.title("AI 数字人对话系统")
        self.root.geometry("600x600")
        self.root.configure(bg="#34516e")

        main_frame = tk.Frame(self.root, bg="#34516e")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # AI回复显示区域
        self.ai_text = tk.Text(main_frame, font=("微软雅黑", 11), bg="#f0f8ff", height=12, state="disabled")
        self.ai_text.pack(fill="both", expand=True, pady=10)

        # 口型数据显示区域（实时显示口型代码）
        self.lip_label = tk.Label(main_frame, text="当前口型: -", font=("黑体", 16, "bold"), bg="#34516e", fg="#00ff00")
        self.lip_label.pack(pady=10)

        # 输入区域
        self.user_input = tk.Entry(main_frame, font=("微软雅黑", 12))
        self.user_input.pack(fill="x", side="left", expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", lambda e: self.send_message())

        send_btn = tk.Button(main_frame, text="发送", command=self.send_message, bg="#2196f3", fg="white")
        send_btn.pack(side="right")

    async def process_ai_voice_and_lips(self, text):
        """核心逻辑：文本 -> 语音 -> 口型 -> 播放"""
        audio_file = "temp_voice.wav"

        # 1. TTS 语音合成
        communicate = edge_tts.Communicate(text, "zh-CN-YunxiNeural")
        await communicate.save(audio_file)

        # 2. Rhubarb 分析口型
        result = subprocess.run(
            [RHUBARB_PATH, "-f", "json", audio_file],
            capture_output=True, text=True, encoding='utf-8'
        )
        lip_data = json.loads(result.stdout)
        cues = lip_data.get('mouthCues', [])

        # 3. 播放声音并在控制台/UI打印口型
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # 记录开始时间，同步显示口型字母
        import time
        start_time = time.time()

        for cue in cues:
            # 简单的时间同步逻辑
            while (time.time() - start_time) < cue['start']:
                continue
            # 更新界面显示的口型代码
            self.lip_label.config(text=f"当前口型: {cue['value']}")
            self.root.update_idletasks()

    def run_async_task(self, text):
        """在后台线程运行异步语音任务，避免卡死界面"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.process_ai_voice_and_lips(text))
        loop.close()

    def send_message(self):
        user_text = self.user_input.get().strip()
        if not user_text: return
        self.user_input.delete(0, tk.END)

        try:
            # 获取 AI 文本
            messages = [SystemMessage(content="你是一个学生"), HumanMessage(content=user_text)]
            ai_response = self.chat.invoke(messages).content

            # 显示文本
            self.ai_text.config(state="normal")
            self.ai_text.delete(1.0, tk.END)
            self.ai_text.insert(tk.END, ai_response)
            self.ai_text.config(state="disabled")

            # 开启新线程处理语音和口型（防止主界面卡死）
            threading.Thread(target=self.run_async_task, args=(ai_response,), daemon=True).start()

        except Exception as e:
            messagebox.showerror("错误", f"失败：{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()