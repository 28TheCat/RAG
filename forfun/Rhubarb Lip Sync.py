import subprocess
import os


def get_mouth_data(audio_path):
    rhubarb_cmd = r"D:\Rhubarb-Lip-Sync-1.14.0-Windows\rhubarb.exe"

    if not os.path.exists(rhubarb_cmd):
        return "错误：找不到 rhubarb.exe，请检查路径是否正确。"

    try:
        result = subprocess.run(
            [rhubarb_cmd, "-f", "json", audio_path],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return result.stdout
    except Exception as e:
        return f"运行出错: {e}"


# 调用
data = get_mouth_data("got_it.wav")
print(data)