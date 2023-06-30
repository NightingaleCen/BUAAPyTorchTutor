# PyTorch：配环境ABC

PyTorch是当今世界上使用最为广泛的深度学习框架之一，在本门课程的上机实验中，同学们将体验使用PyTorch从零开始搭建并训练一个简单的深度学习模型。由于配置PyTorch所需环境对于零基础的同学可能是一大挑战，我们撰写了这份配环境指南，同学们可以在上机实验前提前在电脑上配好环境，以避免在上机过程中遭遇困难。

> 使用PyTorch需要你具备Python基础，如果你还没有使用过Python，可以通过以下网址进行速成：
>
> - [Python3 菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)
> - [Python 3.11官方文档](https://docs.python.org/zh-cn/3/)

## 安装Conda

Python的强大之处在于其能够使用广泛的第三方库，这些库可能互相依赖，把所有库都安装在本机默认的Python环境下往往是不理智的，因此我们推荐使用虚拟环境管理工具Conda创建虚拟环境来安装Pytorch。

> **为什么要使用Conda创建虚拟环境？**
>
> 考虑这样一种（很可能发生的）情况：经过千辛万苦的配环境折磨，你的本地Python环境安装了最新最in的Tensorflow 2.x，这时你兴高采烈地准备跑一跑某篇论文的官方代码，但是你发现这篇论文是五年前发表的，而官方实现采用的是Tensorflow 1.x版本。
>
> 这时你可以选择：
>
> 1. 把Tensorflow 2.x及其相关依赖全部降级到八百年前的某个古早版本，但是如果你要复现的下一篇论文使用的是Tensorflow 2.x，这个痛苦的过程你还需要反向经历一遍。
> 2. 使用Conda建立一个完全独立于本地Python的虚拟环境，并在其中配置一套完整的从Python解释器到Tensorflow 1.x的环境。在你同时进行数个项目时，这些虚拟环境可以并列存在，你可以在它们之间自由切换。
>
> 出于以上考量，建议同学们为每个独立的项目都配置一个单独的Conda环境。

根据自己的需求，你可以从以下链接根据自己的系统类型下载对应的Conda安装包：

- [Anaconda](https://www.anaconda.com/download/)：Conda的完整版本，自带超过1500种常用的第三方库，需要约3GB的储存空间，有图形界面。如果你选择使用Anaconda，你可以不用手动安装本次试验所需的Jupyter库。
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)：Conda的轻量化版本，需要通过conda或pip手动安装所需的第三方库，安装包大小约为50MB.

安装完成后，打开终端（Windows用户打开Anaconda Prompt），应该能看到如下类似界面（提示符可能会有所不同，取决于你设备的系统）：

<img src="/Users/nightingalecen/Library/Application Support/typora-user-images/image-20230626111110046.png" alt="image-20230626111110046" style="zoom: 50%;" />

提示符前的`(base)`即为当前所属的conda环境，base为conda的默认环境。

> 在继续前，依照自己的网络条件，你可能需要更换conda仓库的源为国内镜像以在使用conda安装Python库时获得更高的下载速度，可以参考清华大学开源镜像站的[这篇使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)。

在终端执行下面的命令，创建一个名为DLframework且Python版本为3.11的环境：

```bash
conda create -n DLframework python=3.11
```

执行以下命令以激活此环境：

```bash
conda activate DLframework
```

此时，你应该能看到如下类似界面，你的虚拟环境就已经创建完毕了。

<img src="/Users/nightingalecen/Library/Application Support/typora-user-images/image-20230626113215017.png" alt="image-20230626113215017" style="zoom:50%;" />

在接下来的配环境过程中，请不要退出当前DLframework环境。如果你想要退出当前环境，只需要执行：

```bash
conda deactivate
```

更多conda相关操作请参阅[Conda User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).

## 安装PyTorch

如今的深度学习框架均从GPU的并行计算能力中大大受益，但考虑到并非所有同学的设备都有GPU，且本课程实验需要搭建的网络架构较为简单，同学们只需要安装Pytorch的CPU版本即可完成我们的实验任务。

> 如果你的设备有支持CUDA的Nvidia GPU，你也可以安装PyTorch的CUDA版本，可以参考[这篇Blog](https://blog.csdn.net/qq_45387412/article/details/121223082?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-121223082-blog-124012894.235^v38^pc_relevant_default_base&spm=1001.2101.3001.4242.2&utm_relevant_index=4).
>
> 此外，如果你的电脑上还没有安装CUDA，并且你此前没有配置类似环境的经验，你可能还需要一颗百折不挠的心。

打开[PyTorch官方网站](https://pytorch.org/)，在首页的Install PyTorch部分根据你的本机操作系统选择对应版本的安装包，以Windows系统为例，你的选择应如下图所示

<img src="/Users/nightingalecen/Library/Application Support/typora-user-images/image-20230626150727092.png" alt="image-20230626150727092" style="zoom:50%;" />

你应该选择的PyTorch版本为Stable，包管理工具为Conda，语言为Python，计算平台为CPU。保持当前conda环境为DLframework，将网页上的代码复制到终端中执行，即可在当前环境中安装CPU版本的PyTorch.

```bash
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

> Conda不仅是一个虚拟环境管理工具，还是一个包管理工具，因此你可以直接使用conda命令在环境中安装期望的Python包。
>
> 除此之外，你还可以使用更加常用的包管理工具pip来安装Pytorch：保持当前环境为DLframework，在网页上选择包管理器为Pip，将代码复制到终端中执行。
>
> ```bash
> pip3 install torch torchvision torchaudio
> ```
>
> 由于pip直接从最大的Python仓库PyPI下载包，它能够下载比conda更多的第三方库，且往往可以避免一些conda无法解决的玄学问题，如果你使用conda安装PyTorch失败，不妨使用pip再试试。
>
> 包括换源在内的更多pip使用说明请参见 [Python pip 菜鸟教程](https://www.runoob.com/w3cnote/python-pip-install-usage.html)。

现在，你可以在环境中运行`conda list`来检查PyTorch是否已被正确安装。

<img src="/Users/nightingalecen/Library/Application Support/typora-user-images/image-20230626155200643.png" alt="image-20230626155200643" style="zoom:50%;" />

或者你也可以运行`python`打开交互式解释器，写几行代码测试一下。

<img src="/Users/nightingalecen/Library/Application Support/typora-user-images/image-20230626155337716.png" alt="image-20230626155337716" style="zoom:50%;" />





## 安装Jupyter Notebook

Jupyter Notebook是基于网页的代码开发、运行与文档编写一体化工具，简而言之，你可以在一个文件中完成编程、逐块运行代码、以Markdown编写文档以及展示代码运行结果。

如果你使用的是Anaconda，Jupyter及其依赖应该已经自动安装好了，否则，你可以通过以下conda命令在已配置好的环境中安装Jupyter Notebook：

```bash
conda install jupyter notebook
```

或者你也可以通过Jupyter推荐方式pip来进行安装：

```bash
pip install notebook
```

Jupyter Notebook会在当前终端的工作目录下运行，将我们提供的`Jupyter ABC.ipynb`文件放置在当前终端的工作目录下，在终端中执行`jupyter notebook`以启动Jupyter Notebook，你应该能看到类似以下界面：

<img src="/Users/nightingalecen/Library/Application Support/typora-user-images/image-20230626162933852.png" alt="image-20230626162933852" style="zoom:50%;" />

同时，你的浏览器应该会自动跳转到http://localhost:8888/tree，这是一个通往你当前工作目录的接口，它可能是类似于这样的一个界面：

<img src="/Users/nightingalecen/Library/Application Support/typora-user-images/image-20230626163116855.png" alt="image-20230626163116855" style="zoom: 50%;" />

点击`Jupyter ABC.ipynb，打开该notebook，你可以体会Jupyter Notebook最为基本的用法。此外，Jupyter Notebook还有绘制图像、播放音频等实用功能，你可以访问[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/latest/)来获取完整的使用文档。

> 如果你使用的编辑器是VSCode，你也可以不使用Jupyter提供的官方服务从浏览器访问notebook。在VSCode应用商店中搜索并安装插件`Jupyter`，你就可以直接通过VSCode像打开其他文件一样打开、编辑并运行notebook，同时享受VSCode带来的各项开发便利。
>
> <img src="/Users/nightingalecen/Library/Application Support/typora-user-images/image-20230626164337435.png" alt="image-20230626164337435" style="zoom: 25%;" />
>
> 在使用VSCode插件时，你需要在打开notebook后在右上角手动指定Python内核，此时你只要选择之前配置好的Conda环境所对应的Python解释器即可。

## 其他准备

至此，我们实验需要用到的环境已经基本配置完毕了，但还有一些额外的包你可以通过conda或pip选择性安装，它们可能会在你今后的炼丹生涯中派上用场：

- [Matplotlib](https://matplotlib.org/)：Python最强大的图形绘制库，你可以用它来绘制训练过程中的各项指标曲线，或者是帮助你可视化数据并进行分析。
- [Tqdm](https://tqdm.github.io/)：一个超轻量且简单易用的进度条库，可帮助你时刻监控训练进度。
- [TensorBoard](https://tensorflow.google.cn/tensorboard?hl=zh-cn)或[wandb](https://wandb.ai/site)：在训练中实时可视化跟踪损失及准确率等指标，帮助你掌握并分析训练情况（你在网络上看到的炼丹师如同监控老大爷一样一次盯着十几个曲线看的梗图多是拜这两者所赐）。

除此之外，你还可以选择性参考一些深度学习以及PyTorch的入门教程，如：

- [CS231n: Deep Learning for Computer Vision](http://cs231n.stanford.edu/)：斯坦福李飞飞开设的计算机视觉入门课程，多年来一直被认为是深度学习最好的入门课程之一，其中讲解了PyTorch的基本用法。BiliBili上有16年的课程视频，讲义见课程官网。
- [PyTorch - Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)：PyTorch官方提供的入门教程，包含了以PyTorch训练深度学习模型的整个工作流，以notebook形式提供了相关代码。

祝各位配环境顺利。Happy coding!