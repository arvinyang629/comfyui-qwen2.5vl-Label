## 一个comfyui节点，节点使用通义千问2.5-vl的api对本地图像进行打标，使用工作流可批量对本地图片打标处理，不需要下载模型，通过api打标速度很快，打标质量也不错
***
* 节点会调用通义千问2.5-VL-7B和通义千问2.5-VL-72B进行图像理解打标，调整系统提示词可输出不同打标效果
* 需要申请阿里云百炼api_key，url：https://bailian.console.aliyun.com/
  * 访问页面后，在右上角有api申请按钮
![QQ_1741568886780](https://github.com/user-attachments/assets/6ede3590-5bff-42cf-89d4-db1c61bc1e4d)
***
## 使用流程：
* 下载节点：将节点文件放在comfyui的custom_nodes中，即可在comfyui中搜索节点"通义千问VL图像分析"
* ![QQ_1741569136616](https://github.com/user-attachments/assets/75189e81-9fda-4254-a6fe-5fdbb3b038b3)
* 填写api_key：可在节点中输出api_key直接填写 或 在qwen_vl_node.py文件中填写api_key
  * 目前有免费赠送额度1000000
* system_prompt：可在节点中修改和填写，也可以在qwen_vl_node.py文件中修改和填写
  * （system_prompt例如：Please provide a detailed and accurate description of the content of this image in English, avoiding any grammatical errors and accurately stating the gender of the character.）
***
## 图像打标：
* 可参考我使用的工作流进行打标，也可以自行搭建工作流打标
![QQ_1741569352343](https://github.com/user-attachments/assets/a9f78266-b0e1-46ad-97f8-0a1377e9d072)
* 工作流：
  * 可前往下载（有具体的使用教程）：https://www.liblib.art/modelinfo/951d781f7cae4a0c80e3db093c486a83
## 其他：
* 除开批量对图像打标外，也可接入到图生图的工作流中使用，大家自行组合搭建
