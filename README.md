# 墨影纪 · 宋代美学摄影博客

<div align="center">

**以宋代美学为基调的 Django 摄影博客平台**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 项目简介

**墨影纪** 是一个基于 Django 开发的个人摄影博客平台，融合了宋代美学理念（简约、留白、自然、雅致），为摄影作品提供一个具有古典韵味的展示空间。

### 核心特性

- **📝 博客系统**：支持 Markdown 编辑，分类和标签管理
- **📷 影集管理**：瀑布流布局，支持 EXIF 数据展示
- **🎨 宋代美学设计**：月白、鸦青、琥珀等传统色彩
- **✨ 精致交互**：Alpine.js 驱动的灯箱效果，键盘导航
- **📱 响应式布局**：完美适配移动端和桌面端
- **🐳 Docker 支持**：一键部署到生产环境

---

## 技术栈

### 后端
- **Django 4.2+** - Python Web 框架
- **Django REST Framework** - API 支持
- **django-imagekit** - 图片处理与缩略图生成

### 前端
- **Tailwind CSS** - 原子化 CSS 框架
- **Alpine.js** - 轻量级 JavaScript 框架
- **Django Templates** - 服务端渲染

### 数据库
- **SQLite** - 开发环境
- **PostgreSQL** - 生产环境（推荐）

### 部署
- **Docker** + **Docker Compose**
- **Nginx** + **Gunicorn**

---

## 视觉设计

### 色彩系统

| 名称 | 色值 | 寓意 |
|------|------|------|
| 月白 | #F6F8FA | 主背景色，宁静如月 |
| 鸦青 | #3C4856 | 主文字色，沉稳典雅 |
| 琥珀 | #B78B5D | 强调色，温润如玉 |
| 朱砂 | #D03B40 | 点缀色，醒目典雅 |
| 黛蓝 | #2A5CAA | 辅助色，深邃悠远 |

### 设计特点

- **留白美学**：边距至少 5%，营造呼吸感
- **水墨晕染**：图片悬停时的渐变遮罩效果
- **书法字体**：使用思源宋体等衬线字体
- **卷轴展开**：页面切换时的淡入动画

---

## 快速开始

### 环境要求

- Python 3.9+
- pip

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/tianhaishun/moyinji_blog.git
cd moyinji_blog
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **运行迁移**
```bash
python manage.py migrate
```

4. **创建示例数据**（可选）
```bash
python manage.py create_sample_data
```

5. **创建管理员账户**
```bash
python manage.py createsuperuser
```

6. **启动开发服务器**
```bash
python manage.py runserver
```

7. **访问网站**
- 首页：http://localhost:8000/
- 管理后台：http://localhost:8000/admin/

---

## 项目结构

```
moyinji_blog/
├── blog/                  # 博客应用
│   ├── models.py         # BlogPost, Category, Tag
│   ├── views.py          # 列表、详情视图
│   ├── templates/        # 博客模板
│   └── management/       # 管理命令
│       └── commands/
│           └── create_sample_data.py
├── gallery/              # 相册应用
│   ├── models.py         # PhotoAlbum, Photo
│   ├── views.py          # 列表、详情视图
│   └── templates/        # 相册模板
├── moyinji/              # 项目配置
│   ├── settings.py       # Django 设置
│   ├── urls.py           # URL 配置
│   └── views.py          # 首页、关于页视图
├── static/               # 静态文件
│   ├── css/
│   │   └── song-style.css  # 宋代美学样式
│   └── js/               # 自定义 JavaScript
├── templates/            # 基础模板
│   ├── base.html         # 基础模板
│   ├── home.html         # 首页
│   └── about.html        # 关于页
├── media/                # 媒体文件（用户上传）
├── Dockerfile            # Docker 镜像
├── docker-compose.yml    # Docker Compose 配置
├── nginx.conf            # Nginx 配置
└── requirements.txt      # Python 依赖
```

---

## 功能模块

### 博客系统

- **文章管理**：创建、编辑、发布文章
- **分类系统**：山水意境、器物特写、光影实验、随笔
- **标签系统**：灵活的内容标签
- **封面图**：自动提取首图作为缩略图
- **浏览统计**：文章阅读次数统计

### 相册系统

- **相册管理**：创建主题相册，支持主题色设置
- **照片上传**：批量上传照片
- **EXIF 数据**：自动显示相机、镜头、光圈、ISO 等参数
- **灯箱浏览**：全屏浏览，支持键盘导航（左右箭头、ESC）
- **瀑布流布局**：Masonry 响应式网格

---

## Docker 部署

### 使用 Docker Compose

1. **构建并启动**
```bash
docker-compose up -d
```

2. **创建管理员**
```bash
docker-compose exec web python manage.py createsuperuser
```

3. **访问网站**
- 网站：http://localhost/
- 管理后台：http://localhost/admin/

### 单独构建

```bash
# 构建镜像
docker build -t moyinji_blog .

# 运行容器
docker run -p 8000:8000 moyinji_blog
```

---

## 配置说明

### 环境变量

创建 `.env` 文件：

```bash
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,your-domain.com

# 数据库（生产环境）
DB_ENGINE=django.db.backends.postgresql
DB_NAME=moyinji_db
DB_USER=moyinji
DB_PASSWORD=your-password
DB_HOST=db
DB_PORT=5432
```

### 静态文件

开发环境会自动处理静态文件。生产环境需要运行：

```bash
python manage.py collectstatic
```

---

## 管理命令

### 创建示例数据

```bash
python manage.py create_sample_data
```

这将创建：
- 4 个分类（山水意境、器物特写、光影实验、随笔）
- 6 个标签
- 5 篇示例文章
- 3 个相册

---

## 路由配置

| 路径 | 说明 |
|------|------|
| `/` | 首页 |
| `/blog/` | 文章列表 |
| `/blog/<slug>/` | 文章详情 |
| `/gallery/` | 相册列表 |
| `/gallery/<slug>/` | 相册详情 |
| `/about/` | 关于页面 |
| `/admin/` | 管理后台 |

---

## 开发指南

### 添加新的博客分类

编辑 `blog/models.py`，在 `BlogPost.CATEGORY_CHOICES` 中添加：

```python
CATEGORY_CHOICES = [
    ('landscape', '山水意境'),
    ('still_life', '器物特写'),
    ('experimental', '光影实验'),
    ('essay', '随笔'),
    ('your_category', '你的分类'),  # 新增
]
```

### 自定义色彩

编辑 `moyinji/settings.py` 中的色彩定义：

```python
THEME_COLOR_CHOICES = [
    ('#3C4856', '鸦青'),
    ('#B78B5D', '琥珀'),
    ('#2A5CAA', '黛蓝'),
    ('#D03B40', '朱砂'),
    ('#YOUR_COLOR', '你的颜色'),  # 新增
]
```

---

## 贡献

欢迎提交 Issue 和 Pull Request！

---

## 许可证

[MIT License](LICENSE)

---

## 致谢

- 设计灵感来源于宋代《千里江山图》
- 交互参考 Unsplash 和故宫博物院网站
- 技术栈基于 Django 官方文档

---

## 联系方式

- GitHub: [@tianhaishun](https://github.com/tianhaishun)
- Email: contact@example.com

---

**墨影纪** - 用镜头记录时光，以光影描绘心境
