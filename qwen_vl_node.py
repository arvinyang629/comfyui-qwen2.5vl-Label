import os
import json
import base64
import requests
from io import BytesIO
from PIL import Image

class QwenVLNode:
    """
    通义千问2.5-VL图像分析节点
    支持qwen2.5-vl-7b-instruct和qwen2.5-vl-72b-instruct模型
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "model_name": (["qwen2.5-vl-7b-instruct", "qwen2.5-vl-72b-instruct"], {"default": "qwen2.5-vl-7b-instruct"}),
                "api_key": ("STRING", {"default": "填写apikey"}),
                "system_prompt": ("STRING", {"default": "Please describe the content of this image in detail in English"}),
            },
        }

    RETURN_TYPES = ("STRING", "IMAGE")
    RETURN_NAMES = ("text", "image")
    FUNCTION = "analyze_image"
    CATEGORY = "image/text"

    def analyze_image(self, image, model_name, api_key, system_prompt):
        # 将ComfyUI图像格式转换为PIL图像
        # ComfyUI中的图像是PyTorch张量
        import torch
        import numpy as np
        # 将张量转换为numpy数组，然后再转为PIL图像
        pil_image = Image.fromarray((image[0].cpu().numpy() * 255).astype(np.uint8))
        
        # 将图像转换为base64编码
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        # 准备API请求
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        payload = {
            "model": model_name,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}
                        }
                    ]
                }
            ]
        }
        
        try:
            # 发送API请求
            response = requests.post(
                "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
                headers=headers,
                json=payload
            )
            
            # 解析响应
            if response.status_code == 200:
                result = response.json()
                description = result.get("choices", [{}])[0].get("message", {}).get("content", "No description available")
                print(f"Image analysis result: {description}")
                return (description, image)
            else:
                error_message = f"API请求失败: {response.status_code} - {response.text}"
                print(error_message)
                return (error_message, image)
        except Exception as e:
            error_message = f"处理图像时出错: {str(e)}"
            print(error_message)
            return (error_message, image)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "QwenVLImageAnalysis": QwenVLNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QwenVLImageAnalysis": "通义千问VL图像分析"
}