# 墨影纪 · 变更日志

本文档记录墨影纪项目的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [未发布]

### 计划中
- 用户注册/登录系统
- 评论功能
- 社交分享
- 全文搜索（Elasticsearch）
- 邮件通知

---

## [1.0.0] - 2026-01-18

### 新增
- ✅ 博客系统
  - 文章列表（分页、筛选、搜索）
  - 文章详情（Markdown渲染）
  - 分类管理
  - 标签管理
  - 浏览统计
- ✅ 相册系统
  - 相册列表（瀑布流布局）
  - 相册详情（主题色设置）
  - 照片上传（批量处理）
  - EXIF数据展示
  - 灯箱浏览（键盘导航、触摸手势）
- ✅ 响应式设计
  - 桌面端优化
  - 平板端优化
  - 移动端优化
  - 触摸手势支持
- ✅ 缓存系统
  - Redis集成
  - 视图缓存
  - 查询结果缓存
  - 缓存自动失效
- ✅ 管理后台
  - Django Admin配置
  - 批量操作
  - 图片预览
- ✅ Docker部署
  - Dockerfile
  - docker-compose.yml
  - Nginx配置
- ✅ 文档体系
  - README.md
  - DEVELOPMENT_GUIDE.md
  - CODING_STANDARDS.md
  - DEVELOPMENT_PLAN.md
  - TEST_PLAN.md
  - TEST_STANDARDS.md
  - DEPLOYMENT_GUIDE.md
  - API_DOCUMENTATION.md
  - CONTRIBUTING.md
  - PROJECT_MANAGEMENT.md

### 优化
- 性能优化（图片压缩、懒加载）
- SEO优化（meta标签、结构化数据）
- 可访问性（ARIA标签、键盘导航）

### 安全
- CSRF保护
- XSS防护
- SQL注入防护
- 文件上传验证

---

## [0.2.0] - 2026-01-15

### 新增
- 基础项目结构
- 数据模型定义
- 基础视图
- 管理后台基础配置

### 变更
- 切换到PostgreSQL数据库

---

## [0.1.0] - 2026-01-10

### 新增
- 项目初始化
- Django基础配置
- Tailwind CSS集成
- Alpine.js集成

---

## 版本说明

### 版本格式：主版本号.次版本号.修订号

- **主版本号**: 不兼容的API修改
- **次版本号**: 向下兼容的功能性新增
- **修订号**: 向下兼容的问题修正

### 变更类型

- **新增** (Added): 新功能
- **变更** (Changed): 现有功能的变更
- **废弃** (Deprecated): 即将移除的功能
- **移除** (Removed): 已移除的功能
- **修复** (Fixed): Bug修复
- **安全** (Security): 安全相关修复

---

**本文档由墨影纪团队维护**
**最后更新：2026-01-18**
