# 墨影纪 · 测试标准

> 版本：1.0
> 最后更新：2026-01-18

---

## 1. 测试标准总则

### 1.1 测试原则

1. **测试先行** - 优先编写测试用例
2. **自动化优先** - 能自动化的测试尽量自动化
3. **持续测试** - 集成到CI/CD流程
4. **可重复性** - 测试结果可重复
5. **独立性** - 测试之间互不依赖

---

## 2. 代码覆盖率标准

### 2.1 覆盖率要求

| 模块 | 最低覆盖率 | 推荐覆盖率 |
|------|-----------|-----------|
| 模型层（models.py） | 85% | 95% |
| 视图层（views.py） | 75% | 85% |
| 表单（forms.py） | 80% | 90% |
| 工具函数（utils.py） | 90% | 100% |
| 信号（signals.py） | 70% | 85% |
| 整体项目 | 80% | 85% |

### 2.2 覆盖率计算

```bash
# 运行测试并生成覆盖率报告
pytest --cov=. --cov-report=html --cov-report=term

# 查看详细报告
open htmlcov/index.html

# 仅统计特定应用
pytest --cov=blog --cov=gallery
```

---

## 3. 单元测试标准

### 3.1 命名规范

```python
# ✅ 正确：描述性命名
def test_blog_post_creation_with_valid_data():
    """测试使用有效数据创建文章"""
    pass

def test_blog_post_slug_is_unique():
    """测试文章slug唯一性"""
    pass

# ❌ 错误：模糊命名
def test1():
    pass

def test_post():
    pass
```

### 3.2 测试结构（AAA模式）

```python
def test_blog_post_publish():
    """测试文章发布功能"""

    # Arrange（准备）
    post = BlogPost.objects.create(
        title='测试文章',
        is_published=False
    )

    # Act（执行）
    post.publish()

    # Assert（断言）
    assert post.is_published is True
    assert post.published_at is not None
```

### 3.3 测试隔离

```python
# ✅ 正确：使用setUp/tearDown
class BlogPostTest(TestCase):
    def setUp(self):
        """每个测试前执行"""
        self.post = BlogPost.objects.create(
            title='测试文章'
        )

    def test_title(self):
        assert self.post.title == '测试文章'

# ❌ 错误：测试间有依赖
def test_first():
    global post
    post = BlogPost.objects.create(title='测试')

def test_second():
    assert post.title == '测试'  # 依赖test_first
```

---

## 4. 集成测试标准

### 4.1 视图测试规范

```python
class BlogViewTest(TestCase):
    """博客视图测试"""

    def setUp(self):
        self.client = Client()

    def test_list_view_status_code(self):
        """测试列表页状态码为200"""
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_list_view_uses_correct_template(self):
        """测试使用正确的模板"""
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_list_view_contains_posts(self):
        """测试页面包含文章数据"""
        post = BlogPost.objects.create(
            title='测试文章',
            is_published=True
        )
        response = self.client.get('/blog/')
        self.assertContains(response, '测试文章')
```

### 4.2 API测试规范

```python
from rest_framework.test import APITestCase

class BlogAPITest(APITestCase):
    """博客API测试"""

    def test_list_endpoint_returns_200(self):
        """测试列表端点返回200"""
        url = reverse('blog-api:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_endpoint_returns_correct_data(self):
        """测试返回正确的数据格式"""
        BlogPost.objects.create(title='测试')
        url = reverse('blog-api:list')
        response = self.client.get(url)

        self.assertEqual(response.data['count'], 1)
        self.assertEqual(
            response.data['results'][0]['title'],
            '测试'
        )
```

---

## 5. 性能测试标准

### 5.1 响应时间标准

| 页面类型 | 目标响应时间 | 最大可接受时间 |
|---------|-------------|--------------|
| 首页 | < 1秒 | < 2秒 |
| 列表页 | < 1秒 | < 2秒 |
| 详情页 | < 1.5秒 | < 3秒 |
| API端点 | < 0.5秒 | < 1秒 |

### 5.2 数据库查询标准

```python
# ✅ 正确：使用assertNumQueries
def test_blog_list_uses_fixed_queries():
    """测试列表页使用固定数量的查询"""
    # 创建测试数据
    BlogPost.objects.create_batch(10, is_published=True)

    # 验证查询次数
    with self.assertNumQueries(3):  # 根据实际情况调整
        response = self.client.get('/blog/')

    self.assertEqual(response.status_code, 200)
```

### 5.3 负载测试标准

```bash
# 使用Apache Bench进行负载测试
# 1000个请求，10个并发
ab -n 1000 -c 10 http://localhost:8000/

# 通过标准
# - 失败率 < 1%
# - 平均响应时间 < 500ms
# - 95%请求响应时间 < 1s
```

---

## 6. 安全测试标准

### 6.1 输入验证测试

```python
def test_sql_injection_prevention():
    """测试SQL注入防护"""
    malicious_input = "'; DROP TABLE blog_blogpost; --"

    # 应该安全处理，不会导致SQL注入
    posts = BlogPost.objects.filter(title__icontains=malicious_input)

    # 验证数据库未被破坏
    self.assertEqual(BlogPost.objects.count(), 0)

def test_xss_prevention():
    """测试XSS防护"""
    response = self.client.get('/blog/')

    # 包含恶意脚本的内容应被转义
    self.assertNotContains(response, '<script>alert(1)</script>')
```

### 6.2 权限测试

```python
from django.test import Client
from django.contrib.auth.models import User

class PermissionTest(TestCase):
    """权限测试"""

    def test_admin_requires_authentication(self):
        """测试管理后台需要认证"""
        client = Client()
        response = client.get('/admin/')

        # 未登录应重定向到登录页
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/admin/login/'))
```

---

## 7. 测试数据标准

### 7.1 Fixture使用

```python
from django.test import TestCase
from django.core.management import call_command

class BlogPostTest(TestCase):
    fixtures = ['test_data.json']

    @classmethod
    def setUpTestData(cls):
        # 或使用management命令加载
        call_command('loaddata', 'test_data.json')
```

### 7.2 测试数据工厂

```python
import factory
from .models import BlogPost

class BlogPostFactory(factory.django.DjangoModelFactory):
    """文章测试数据工厂"""

    class Meta:
        model = BlogPost

    title = factory.Sequence(lambda n: f'测试文章{n}')
    slug = factory.Sequence(lambda n: f'test-post-{n}')
    is_published = True

# 使用
def test_with_factory():
    post = BlogPostFactory()
    assert post.is_published is True
```

---

## 8. 测试报告标准

### 8.1 测试结果报告

每次测试后应生成：

1. **控制台输出**
   ```
   ========================= test session starts =========================
   collected 150 items

   blog/test_models.py::test_blog_post_creation PASSED
   blog/test_views.py::test_blog_list PASSED

   ================= 150 passed in 5.23s ===========================
   ```

2. **覆盖率报告**
   ```
   Name                         Stmts   Miss  Cover
   ------------------------------------------------
   blog/models.py                  50      2    96%
   blog/views.py                   80     10    88%
   ------------------------------------------------
   TOTAL                          500     80    84%
   ```

3. **HTML报告**
   - 生成在 `htmlcov/` 目录
   - 可视化查看每行代码的覆盖情况

---

## 9. 持续集成标准

### 9.1 CI检查项

每次提交必须通过：

```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - checkout代码
      - 安装依赖
      - 代码格式检查（black）
      - 代码质量检查（flake8）
      - 类型检查（mypy）
      - 安全检查（bandit）
      - 运行测试（pytest）
      - 生成覆盖率报告
      - 上传到Codecov
```

### 9.2 质量门槛

| 检查项 | 通过标准 |
|--------|----------|
| 代码格式 | 100%通过 |
| Flake8 | 0个错误 |
| 类型检查 | 主要模块通过 |
| 安全扫描 | 0个高危漏洞 |
| 测试通过率 | 100% |
| 代码覆盖率 | ≥ 80% |

---

## 10. 测试维护标准

### 10.1 测试更新时机

- ✅ 新增功能时：同步添加测试
- ✅ 修复Bug时：添加回归测试
- ✅ 重构代码时：更新相关测试
- ✅ 发现Bug时：先写测试再修复

### 10.2 测试清理

定期（每季度）审查测试：

- 删除重复测试
- 删除无效测试
- 优化慢速测试
- 更新过时断言

---

## 附录：测试最佳实践

### DO ✅

- 保持测试简短专注
- 使用描述性命名
- 测试边界条件
- Mock外部依赖
- 使用setUp/tearDown
- 保持测试独立性

### DON'T ❌

- 测试私有方法
- 测试第三方库
- 编写重复测试
- 硬编码测试数据
- 忽略随机性
- 过度使用Mock

---

**本文档由墨影纪团队维护**
**最后更新：2026-01-18**
