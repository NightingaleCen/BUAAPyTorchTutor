# PyTorch框架教程实验：图像分类
这是北京航空航天大学人工智能研究院所开设的深度学习框架暑期课程PyTorch图像分类上机实验官方仓库，该课程面向不具备深度学习框架基础的本科低年级学生，教授使用PyTorch进行深度学习训练的一般流程。本仓库提供了实验相关指导、实验代码以及评测代码.  
本仓库不提供原本教学使用的植物分类数据集，请将`10 plants dataset`替换为自定义的数据集并修改相关数据读取代码，具体要求请参见[`10 plants dataset/README.md`](./10%20plants%20dataset/README.md)

## 实验指导文件说明
- [PyTorch：配环境ABC.md](./PyTorch%EF%BC%9A%E9%85%8D%E7%8E%AF%E5%A2%83ABC.md)：面向零基础学生的PyTorch环境配置指南。
- [Jupyter ABC.ipynb](./Jupyter%20ABC.ipynb)：与环境配置指南配套的Jupyter Notebook教程。
- [植物识别：结果提交.md](./10%20plants%20dataset/%E6%A4%8D%E7%89%A9%E8%AF%86%E5%88%AB%EF%BC%9A%E7%BB%93%E6%9E%9C%E6%8F%90%E4%BA%A4.md)：实验结果的提交指南。
- [result_example.json](./10%20plants%20dataset/result_example.json)：学生实验结果提交格式的样例文件，格式与测试集标签格式保持一致。

## 实验代码文件说明
- [实验：植物识别.ipynb](./%E5%AE%9E%E9%AA%8C%EF%BC%9A%E6%A4%8D%E7%89%A9%E8%AF%86%E5%88%AB.ipynb)：提供给学生的实验主体notebook代码，网络架构部分留空作为实验内容。
- [baseline_CNN.ipynb](./baseline_CNN.ipynb)：使用简单CNN的baseline，可以在实验结束后提供给学生。
- [baseline_resnet18.ipynb](./baseline_resnet18.ipynb)：微调resnet18的baseline，可以在实验结束后提供给学生。

## 结果评测
将学生提交的文件放置在[review](./review/)文件夹下，运行`python review.py`将结果准确率排名输出到`review_result.xlsx`.

## License
MIT

