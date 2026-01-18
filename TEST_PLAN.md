# 墨影纪 · 测试计划

> 版本：1.0
> 最后更新：2026-01-18

---

## 1. 测试概述

### 1.1 测试目标

确保**墨影纪**项目的功能完整性、性能达标、安全可靠，提供优质的用户体验。

**核心目标**
- ✅ 功能覆盖率 100%
- ✅ 代码覆盖率 ≥ 80%
- ✅ 关键Bug 0个
- ✅ 性能指标达标

### 1.2 测试范围

**包含测试**
- ✅ 博客系统（CRUD、筛选、搜索）
- ✅ 相册系统（上传、展示、灯箱）
- ✅ 管理后台（所有管理功能）
- ✅ 响应式布局（桌面、平板、移动）
- ✅ 缓存系统（Redis集成）
- ✅ 性能优化（页面加载、图片优化）

**不包含测试**
- ❌ 第三方服务（如支付、社交登录）
- ❌ 浏览器兼容性（IE及过时浏览器）

---

## 2. 测试类型

### 2.1 单元测试

**目标**: 测试单个函数/方法的功能

**范围**
- 模型方法测试
- 视图函数测试
- 表单验证测试
- 工具函数测试
- 信号处理器测试

**工具**: pytest, unittest.mock

**示例**
```python
def test_blog_post_creation():
    """测试文章创建"""
    post = BlogPost.objects.create(
        title='测试文章',
        slug='test-post'
    )
    assert post.title == '测试文章'
    assert post.slug == 'test-post'
    assert post.is_published is False
```

---

### 2.2 集成测试

**目标**: 测试多个模块协作

**范围**
- 完整的用户流程
- API端点测试
- 数据库交互测试
- 缓存集成测试

**工具**: Django TestCase, pytest-django

**示例**
```python
def test_blog_list_flow():
    """测试博客列表完整流程"""
    # 创建测试数据
    BlogPost.objects.create(title='文章1', is_published=True)

    # 访问页面
    response = client.get(reverse('blog:list'))

    # 验证结果
    assert response.status_code == 200
    assert '文章1' in response.content.decode()
```

---

### 2.3 功能测试

**目标**: 从用户角度测试功能

**关键流程**
1. **文章发布流程**
   - 创建文章 → 编辑内容 → 上传封面 → 发布 → 查看详情

2. **相册管理流程**
   - 创建相册 → 上传照片 → 设置EXIF → 发布 → 查看灯箱

3. **搜索筛选流程**
   - 输入关键词 → 查看结果 → 点击详情 → 浏览相关

**工具**: Selenium, Playwright

---

### 2.4 性能测试

**目标**: 验证性能指标

**测试项**
- 页面加载时间（目标 < 2秒）
- 数据库查询优化（N+1检查）
- 并发用户支持（目标 100+）
- 缓存命中率（目标 ≥ 70%）
- 图片加载优化

**工具**
- Django Debug Toolbar
- Lighthouse
- Apache Bench (ab)
- pytest-benchmark

---

### 2.5 安全测试

**目标**: 发现安全漏洞

**测试项**
- SQL注入
- XSS（跨站脚本）
- CSRF（跨站请求伪造）
- 敏感数据泄露
- 权限控制
- 文件上传漏洞

**工具**
- bandit（Python安全扫描）
- OWASP ZAP
- Burp Suite

---

### 2.6 兼容性测试

**目标**: 确保跨平台兼容

**浏览器测试**
- ✅ Chrome（最新版）
- ✅ Safari（最新版）
- ✅ Firefox（最新版）
- ✅ Edge（最新版）
- ✅ iOS Safari
- ✅ Android Chrome

**设备测试**
- ✅ 桌面（1920x1080）
- ✅ 笔记本（1366x768）
- ✅ 平板（768x1024）
- ✅ 手机（375x667）

---

## 3. 测试用例

### 3.1 博客系统测试用例

| 用例ID | 测试场景 | 前置条件 | 操作步骤 | 预期结果 |
|--------|----------|----------|----------|----------|
| TC-BLOG-001 | 文章列表显示 | 已发布5篇文章 | 访问/blog/ | 显示5篇文章 |
| TC-BLOG-002 | 文章分页 | 已发布15篇文章 | 访问/blog/ | 显示12篇，有分页 |
| TC-BLOG-003 | 分类筛选 | 已创建分类"山水" | 点击分类"山水" | 仅显示该分类文章 |
| TC-BLOG-004 | 文章详情 | 文章slug为"test" | 访问/blog/test/ | 显示文章详情 |
| TC-BLOG-005 | 浏览计数 | 文章浏览数为0 | 访问文章详情 | 浏览数+1 |
| TC-BLOG-006 | Markdown渲染 | 文章内容为Markdown | 查看文章详情 | Markdown正确渲染 |
| TC-BLOG-007 | 相关文章推荐 | 文章有同分类其他文章 | 滚动到底部 | 显示相关文章 |
| TC-BLOG-008 | 搜索功能 | 有标题包含"山水"的文章 | 搜索"山水" | 显示匹配文章 |

---

### 3.2 相册系统测试用例

| 用例ID | 测试场景 | 前置条件 | 操作步骤 | 预期结果 |
|--------|----------|----------|----------|----------|
| TC-GAL-001 | 相册列表显示 | 已创建3个相册 | 访问/gallery/ | 显示3个相册 |
| TC-GAL-002 | 相册主题色 | 相册设置琥珀色 | 查看相册卡片 | 显示琥珀色边框 |
| TC-GAL-003 | 照片上传 | 登录管理员 | 上传3张照片 | 上传成功 |
| TC-GAL-004 | EXIF显示 | 照片有EXIF数据 | 查看灯箱 | 显示相机/镜头信息 |
| TC-GAL-005 | 灯箱打开 | 相册有照片 | 点击照片 | 打开灯箱全屏显示 |
| TC-GAL-006 | 键盘导航 | 灯箱打开 | 按右箭头键 | 切换到下一张 |
| TC-GAL-007 | 触摸滑动 | 移动设备打开灯箱 | 左滑屏幕 | 切换到下一张 |
| TC-GAL-008 | 图片懒加载 | 页面有20张照片 | 滚动页面 | 图片按需加载 |

---

### 3.3 性能测试用例

| 用例ID | 测试指标 | 目标值 | 测试方法 |
|--------|----------|--------|----------|
| TC-PERF-001 | 首页加载时间 | < 2秒 | Lighthouse测试 |
| TC-PERF-002 | 博客列表加载 | < 1.5秒 | Lighthouse测试 |
| TC-PERF-003 | 灯箱打开速度 | < 0.5秒 | 手动测试 |
| TC-PERF-004 | 数据库查询数 | < 5次 | Debug Toolbar |
| TC-PERF-005 | 并发用户支持 | 100+ | Apache Bench |
| TC-PERF-006 | 图片压缩率 | ≥ 80% | 文件大小对比 |
| TC-PERF-007 | 缓存命中率 | ≥ 70% | Redis监控 |

---

### 3.4 安全测试用例

| 用例ID | 测试项 | 测试方法 | 预期结果 |
|--------|--------|----------|----------|
| TC-SEC-001 | SQL注入 | 输入`' OR '1'='1` | 查询失败 |
| TC-SEC-002 | XSS攻击 | 输入`<script>alert(1)</script>` | 脚本不执行 |
| TC-SEC-003 | CSRF保护 | POST请求无token | 请求被拒绝 |
| TC-SEC-004 | 文件上传 | 上传.php文件 | 上传失败 |
| TC-SEC-005 | 敏感数据 | 查看页面源码 | 无SECRET_KEY |
| TC-SEC-006 | 权限控制 | 未登录访问/admin/ | 重定向到登录页 |

---

## 4. 测试环境

### 4.1 开发环境

```bash
Python: 3.11+
Django: 4.2+
数据库: SQLite (开发), PostgreSQL (生产)
缓存: LocMemCache (开发), Redis (生产)
```

### 4.2 测试数据

**示例数据生成**
```bash
python manage.py create_sample_data
```

**数据规模**
- 文章：50篇
- 分类：4个
- 标签：10个
- 相册：5个
- 照片：100张

---

## 5. 测试执行计划

### 5.1 测试时间表

| 阶段 | 开始时间 | 结束时间 | 测试类型 | 责任人 |
|------|----------|----------|----------|--------|
| 单元测试 | Day 1 | Day 10 | 开发中持续进行 | 开发人员 |
| 集成测试 | Day 15 | Day 20 | 功能完成后 | 开发人员 |
| 功能测试 | Day 20 | Day 23 | 全部功能完成后 | 测试人员 |
| 性能测试 | Day 24 | Day 25 | 部署到测试环境 | DevOps |
| 安全测试 | Day 25 | Day 26 | 部署到测试环境 | 安全专家 |
| 用户验收测试 | Day 26 | Day 27 | 部署到预发布环境 | 产品+用户 |

### 5.2 测试优先级

**P0（阻塞性）- 必须修复**
- 系统崩溃
- 数据丢失
- 安全漏洞
- 核心功能不可用

**P1（严重）- 优先修复**
- 功能异常但不影响核心流程
- 性能严重下降
- 用户体验差

**P2（一般）- 计划修复**
- 非核心功能小问题
- UI细节问题
- 文档错误

**P3（建议）- 可延后**
- 优化建议
- 代码重构
- 文档改进

---

## 6. 测试工具

### 6.1 单元测试工具

```bash
# 安装
pip install pytest pytest-django pytest-cov

# 运行测试
pytest --cov=. --cov-report=html

# 查看覆盖率报告
open htmlcov/index.html
```

### 6.2 性能测试工具

```bash
# Django Debug Toolbar
pip install django-debug-toolbar

# Lighthouse（Chrome扩展）
# 在Chrome DevTools中使用

# Apache Bench
ab -n 1000 -c 10 http://localhost:8000/
```

### 6.3 安全测试工具

```bash
# bandit
pip install bandit
bandit -r . --skip B101

# OWASP ZAP
# 下载并运行ZAP，进行扫描
```

---

## 7. 缺陷管理

### 7.1 缺陷报告模板

```markdown
## 缺陷标题

**缺陷ID**: BUG-001
**发现日期**: 2026-01-18
**严重程度**: P0/P1/P2/P3
**优先级**: 高/中/低
**状态**: 新建/已确认/修复中/已修复/已验证/关闭

### 环境信息
- 浏览器: Chrome 120
- 操作系统: macOS 14
- 设备: 桌面

### 重现步骤
1. 步骤1
2. 步骤2
3. 步骤3

### 实际结果
描述实际发生的情况

### 预期结果
描述应该发生的情况

### 截图/日志
[附上截图或日志]
```

### 7.2 缺陷生命周期

```
新建 → 已确认 → 修复中 → 已修复 → 已验证 → 关闭
                    ↓
                  重新打开
```

---

## 8. 测试报告

### 8.1 测试总结报告

**报告内容**
1. 测试概述
2. 测试范围
3. 测试用例执行情况
4. 缺陷统计
5. 遗留问题
6. 测试结论
7. 建议

**报告模板**
```markdown
# 测试总结报告

## 1. 测试概述
- 测试时间: YYYY-MM-DD ~ YYYY-MM-DD
- 测试人员: XXX
- 测试环境: XXX

## 2. 测试用例
- 总用例数: 100
- 执行用例数: 100
- 通过用例数: 95
- 失败用例数: 5
- 通过率: 95%

## 3. 缺陷统计
- P0: 0个
- P1: 2个（已修复）
- P2: 3个（已修复）
- P3: 5个（延后修复）

## 4. 测试结论
✅ 系统可以发布

## 5. 建议
- 持续监控性能
- 收集用户反馈
```

---

## 9. 持续集成

### 9.1 CI配置

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.11
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-django pytest-cov
      - name: Run tests
        run: pytest --cov=. --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v2
```

---

## 10. 验收标准

### 10.1 上线前检查清单

**功能完整性**
- [x] 所有核心功能正常
- [x] 所有P0/P1缺陷已修复
- [x] 用户流程畅通无阻

**性能指标**
- [x] 页面加载时间 < 2秒
- [x] Lighthouse评分 ≥ 90
- [x] 代码覆盖率 ≥ 80%

**安全性**
- [x] 无高危安全漏洞
- [x] 敏感数据已加密
- [x] 权限控制正确

**兼容性**
- [x] 主流浏览器测试通过
- [x] 移动设备测试通过
- [x] 响应式布局正常

**文档**
- [x] README完整
- [x] 部署文档清晰
- [x] API文档准确

---

**本文档由墨影纪团队维护**
**最后更新：2026-01-18**
