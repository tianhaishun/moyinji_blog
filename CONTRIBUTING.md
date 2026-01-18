# 墨影纪 · 贡献指南

> 版本：1.0
> 最后更新：2026-01-18

感谢您对墨影纪项目的关注！我们欢迎任何形式的贡献。

---

## 1. 如何贡献

### 1.1 报告Bug

🐛 **发现Bug？请报告！**

在提交Bug前，请检查：
- [ ] Bug未被报告过（搜索Issues）
- [ ] Bug可重现
- [ ] 提供最小复现步骤
- [ ] 附上截图或错误日志

**Bug报告模板**:

```markdown
### Bug描述
简明扼要地描述Bug

### 复现步骤
1. 访问页面 '...'
2. 点击按钮 '....'
3. 滚动到 '....'
4. 看到错误

### 预期行为
应该发生什么

### 实际行为
实际发生了什么

### 环境信息
- 操作系统: [e.g. macOS 14]
- 浏览器: [e.g. Chrome 120]
- Python版本: [e.g. 3.11]
- Django版本: [e.g. 4.2]

### 截图/日志
如果适用，添加截图或日志
```

---

### 1.2 功能建议

💡 **有好想法？请告诉我们！**

在提交功能建议前，请考虑：
- [ ] 功能符合项目定位
- [ ] 功能对多数用户有价值
- [ ] 可以实际实现

**功能建议模板**:

```markdown
### 功能描述
简明扼要地描述功能

### 问题背景
当前的问题或痛点

### 解决方案
详细描述你的解决方案

### 替代方案
是否考虑过其他方案

### 附加信息
其他有助于理解的信息
```

---

### 1.3 提交代码

📝 **准备贡献代码！**

**工作流程**:

1. **Fork项目**
   ```bash
   # 在GitHub上Fork项目
   ```

2. **克隆到本地**
   ```bash
   git clone https://github.com/YOUR_USERNAME/moyinji_blog.git
   cd moyinji_blog
   ```

3. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **编写代码**
   - 遵循编码规范
   - 编写测试
   - 更新文档

5. **提交代码**
   ```bash
   git add .
   git commit -m "feat: 添加新功能"
   ```

6. **推送到GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建Pull Request**
   - 访问GitHub
   - 点击"New Pull Request"
   - 填写PR描述

**PR模板**:

```markdown
### 变更类型
- [ ] Bug修复
- [ ] 新功能
- [ ] 代码重构
- [ ] 文档更新
- [ ] 性能优化

### 变更说明
描述你的改动

### 相关Issue
关闭 #(issue number)

### 测试
- [ ] 代码通过所有测试
- [ ] 添加了新的测试用例
- [ ] 手动测试通过

### 截图
如果有UI变更，请添加截图

### 检查清单
- [ ] 遵循编码规范
- [ ] 添加了文档
- [ ] 更新了CHANGELOG.md
```

---

## 2. 开发规范

### 2.1 编码规范

- 遵循PEP 8
- 使用有意义的变量名
- 添加必要的注释
- 编写文档字符串
- 保持函数简短

详细规范请参考: [CODING_STANDARDS.md](CODING_STANDARDS.md)

### 2.2 提交信息规范

使用**Conventional Commits**格式:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**类型 (type)**:
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式
- `refactor`: 重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建/工具链

**示例**:
```bash
feat(blog): 添加文章搜索功能

- 实现全文搜索
- 添加搜索结果高亮
- 支持拼音搜索

Closes #123
```

---

## 3. 测试要求

### 3.1 编写测试

所有代码变更需要包含测试：

```python
def test_new_feature():
    """测试新功能"""
    # 准备
    data = {...}

    # 执行
    result = new_function(data)

    # 断言
    assert result == expected
```

### 3.2 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_models.py

# 生成覆盖率报告
pytest --cov=. --cov-report=html
```

**测试覆盖率要求**: ≥ 80%

---

## 4. 文档要求

### 4.1 代码文档

- 所有公共方法需要文档字符串
- 复杂逻辑需要行内注释
- README.md需要更新（如有新功能）

### 4.2 API文档

如有API变更，更新 [API_DOCUMENTATION.md](API_DOCUMENTATION.md)

### 4.3 变更日志

重要变更需要更新 [CHANGELOG.md](CHANGELOG.md)

---

## 5. 代码审查

### 5.1 审查标准

所有PR需要通过以下检查：

- [ ] 代码符合规范
- [ ] 测试通过
- [ ] 新功能有测试
- [ ] 文档已更新
- [ ] 无安全漏洞
- [ ] 性能无明显下降

### 5.2 审查流程

1. 自动化检查（CI）
2. 代码审查（至少1人批准）
3. 合并到主分支

---

## 6. 社区准则

### 6.1 尊重他人

- 友善和包容
- 尊重不同观点
- 建设性反馈

### 6.2 协作精神

- 乐于助人
- 分享知识
- 共同改进

### 6.3 行为准则

**不可接受的行为**:
- 使用性化语言或图像
- 人身攻击或侮辱
- 公开或私下骚扰
- 未经许可发布他人隐私信息

**举报**: contact@example.com

---

## 7. 获得帮助

### 7.1 获取帮助

- 📖 查看 [README.md](README.md)
- 📖 查看 [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md)
- 💬 提交Issue提问
- 📧 发邮件: contact@example.com

### 7.2 讨论渠道

- GitHub Issues
- GitHub Discussions（未来）
- 邮件列表（未来）

---

## 8. 许可证

提交代码即表示您同意:
- 代码采用MIT许可证
- 您拥有代码的版权
- 代码可以自由使用、修改、分发

---

## 9. 致谢

感谢所有贡献者！您的贡献让墨影纪变得更好。

**核心贡献者**:
- tianhaishun (创建者)

**特别感谢**:
- Django团队
- Tailwind CSS团队
- 所有开源贡献者

---

## 10. 常见问题

### Q: 我不懂编程，可以贡献吗？

A: 当然可以！你可以：
- 报告Bug
- 提出功能建议
- 改进文档
- 帮助翻译
- 推广项目

### Q: 我的PR多久会被审查？

A: 通常在1-3天内。如未收到回复，请在PR中@维护者。

### Q: 如何成为维护者？

A: 通过持续高质量的贡献，你可能被邀请成为维护者。

---

**一起构建更好的墨影纪！** 🎨📷

**本文档由墨影纪团队维护**
**最后更新：2026-01-18**
