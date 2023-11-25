import requests
import json

base_url = "http://127.0.0.1:8000"


def create_chat_completion(model, messages, functions, use_stream=False):
    data = {
        "function": functions,  # 函数定义
        "model": model,  # 模型名称
        "messages": messages,  # 会话历史
        "stream": use_stream,  # 是否流式响应
        "max_tokens": 500,  # 最多生成字数
        "temperature": 0.8,  # 温度
        "top_p": 0.8,  # 采样概率
    }

    response = requests.post(f"{base_url}/v1/chat/completions", json=data, stream=use_stream)
    if response.status_code == 200:
        if use_stream:
            # 处理流式响应
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')[6:]
                    try:
                        response_json = json.loads(decoded_line)
                        content = response_json.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        print(content)
                    except:
                        print("Special Token:", decoded_line)
        else:
            # 处理非流式响应
            decoded_line = response.json()
            content = decoded_line.get("choices", [{}])[0].get("message", "").get("content", "")
            print(content)
    else:
        print("Error:", response.status_code)
        return None

def jiangdiwendu(use_stream=True):
    functions = None
    chat_messages = [
        {
            "role": "system",
            "content": "你是一个家庭控制系统，你的任务是根据用户的指令给与对应设备的命令",
        },
        {
            "role": "user",
            "content": "降低空调温度"
        }
    ]
    create_chat_completion("chatglm3-6b", messages=chat_messages, functions=functions, use_stream=use_stream)
    
def prompt(use_stream=True):
    functions = None
    chat_messages = [
        {
            "role": "system",
            "content": "操作指南查询：如何设置智能恒温器以节约能源但保持舒适？我的智能洗衣机发出奇怪的噪音，应该怎么处理？我该如何利用我的智能照明系统创造浪漫晚餐的氛围？故障排除建议："
    "智能门锁反应迟缓，我该如何解决？"
    "我的智能音箱无法连接到Wi-Fi，有什么快速的修复方法吗？"
    "设备维护提示："
    "我该如何定期维护我的智能家庭安全系统？"
    "智能冰箱的最佳保养方法是什么？"
    "智能设备控制相关提示"
    "远程控制指令："
    "关闭所有楼上的灯光。"
    "将客厅空调温度调至22度。"
    "播放我最喜欢的放松音乐播放列表。"
    "自动化设置配置："
    "每天早上7点自动开启咖啡机。"
    "当室内温度超过25度时，自动打开空调。"
    "个性化服务相关提示"
    "日常习惯学习："
    "根据我的日常起床时间，自动调整卧室窗帘的开合。"
    "学习我的晚餐时间，提前预热烤箱。"
    "个性化建议和提醒："
    "基于我的健康数据，推荐今晚的晚餐菜谱。"
    "提醒我每两周检查一次智能烟雾探测器的电池。"
    "Prompt 1"
    "问题：我怎样才能提高智能家居的能源效率？"
    "答案：为提高能源效率，您可以调整智能恒温器以在白天使用较低的能源设置，夜间则维持舒适温度。此外，利用智能照明系统的定时功能，在不需要时自动关闭灯光，或者使用运动传感器只在有人时点亮灯光。智能插座也可以帮助监控电器的能源使用，并在不使用时自动关闭它们。"
    "Prompt 2"
    "问题：我的智能冰箱突然停止工作，我应该怎么办？"
    "答案：首先，请检查冰箱是否正确接通电源，并检查家庭电路是否跳闸。接着，检查冰箱的显示屏，看是否有故障代码或警告信息。如果有，您可以根据用户手册中的指示进行故障排除。如果没有显示任何错误信息，尝试将冰箱从电源断开一分钟，然后重新连接，以重置系统。如果问题依然存在，建议联系专业维修服务。",
        },
        {
            "role": "user",
            "content": "我该如何使用智能家居系统照顾老年家庭成员？"
        }
    ]
    create_chat_completion("chatglm3-6b", messages=chat_messages, functions=functions, use_stream=use_stream)
    


if __name__ == "__main__":
    # function_chat(use_stream=False)
    # prompt(use_stream=False)
    jiangdiwendu(use_stream=False)
