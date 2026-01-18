# 墨影纪 · API文档

> 版本：1.0
> 基础路径: `/api/`
> 最后更新：2026-01-18

---

## 概述

墨影纪提供RESTful API用于数据交互，基于Django REST Framework实现。

**认证方式**: 暂不需要认证（公开API）

**数据格式**: JSON

**字符编码**: UTF-8

---

## 通用说明

### 响应格式

**成功响应**
```json
{
    "id": 1,
    "title": "文章标题",
    "slug": "article-slug",
    "created_at": "2026-01-18T10:00:00Z"
}
```

**错误响应**
```json
{
    "detail": "未找到",
    "status_code": 404
}
```

---

## 1. 博客API

### 1.1 文章列表

**端点**: `GET /api/blog/posts/`

**查询参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| page | integer | 否 | 页码，默认1 |
| page_size | integer | 否 | 每页数量，默认12 |
| category | string | 否 | 分类slug |
| tag | string | 否 | 标签slug |
| search | string | 否 | 搜索关键词 |
| ordering | string | 否 | 排序，默认`-created_at` |

**响应示例**:
```json
{
    "count": 100,
    "next": "http://api.example.com/api/blog/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "山水意境",
            "slug": "landscape",
            "excerpt": "山水画是中国画的...",
            "cover_image": "http://example.com/media/covers/landscape.jpg",
            "category": {
                "id": 1,
                "name": "山水意境",
                "slug": "landscape"
            },
            "tags": [
                {"id": 1, "name": "风景", "slug": "scenery"}
            ],
            "is_published": true,
            "view_count": 128,
            "created_at": "2026-01-18T10:00:00Z",
            "updated_at": "2026-01-18T12:00:00Z"
        }
    ]
}
```

### 1.2 文章详情

**端点**: `GET /api/blog/posts/{slug}/`

**路径参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| slug | string | 文章slug |

**响应示例**:
```json
{
    "id": 1,
    "title": "山水意境",
    "slug": "landscape",
    "content": "# 山水画\n\n山水画是中国画的...",
    "excerpt": "山水画是中国画的...",
    "cover_image": "http://example.com/media/covers/landscape.jpg",
    "category": {
        "id": 1,
        "name": "山水意境",
        "slug": "landscape",
        "description": "山水类摄影作品"
    },
    "tags": [
        {"id": 1, "name": "风景", "slug": "scenery"}
    ],
    "is_published": true,
    "view_count": 128,
    "created_at": "2026-01-18T10:00:00Z",
    "updated_at": "2026-01-18T12:00:00Z",
    "related_posts": [
        {
            "id": 2,
            "title": "云雾缭绕",
            "slug": "clouds"
        }
    ]
}
```

### 1.3 分类列表

**端点**: `GET /api/blog/categories/`

**响应示例**:
```json
{
    "count": 4,
    "results": [
        {
            "id": 1,
            "name": "山水意境",
            "slug": "landscape",
            "description": "山水类摄影作品",
            "post_count": 25
        }
    ]
}
```

### 1.4 标签列表

**端点**: `GET /api/blog/tags/`

**响应示例**:
```json
{
    "count": 10,
    "results": [
        {
            "id": 1,
            "name": "风景",
            "slug": "scenery",
            "post_count": 30
        }
    ]
}
```

---

## 2. 相册API

### 2.1 相册列表

**端点**: `GET /api/gallery/albums/`

**查询参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| page | integer | 否 | 页码 |
| is_featured | boolean | 否 | 仅精选相册 |

**响应示例**:
```json
{
    "count": 10,
    "results": [
        {
            "id": 1,
            "title": "春日山水",
            "slug": "spring-landscape",
            "description": "春季山水摄影",
            "theme_color": "#3C4856",
            "cover_photo": {
                "id": 1,
                "thumbnail": "http://example.com/media/cache/...",
                "image": "http://example.com/media/gallery/..."
            },
            "photo_count": 15,
            "is_featured": true,
            "created_at": "2026-01-01T00:00:00Z"
        }
    ]
}
```

### 2.2 相册详情

**端点**: `GET /api/gallery/albums/{slug}/`

**路径参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| slug | string | 相册slug |

**响应示例**:
```json
{
    "id": 1,
    "title": "春日山水",
    "slug": "spring-landscape",
    "description": "春季山水摄影",
    "theme_color": "#3C4856",
    "photos": [
        {
            "id": 1,
            "title": "黄山日出",
            "thumbnail": "http://example.com/media/cache/...",
            "thumbnail_large": "http://example.com/media/cache/...",
            "image": "http://example.com/media/gallery/...",
            "description": "黄山日出美景",
            "location": "安徽黄山",
            "exif": {
                "camera": "Canon EOS R5",
                "lens": "24-70mm f/2.8",
                "focal_length": "50mm",
                "aperture": "f/8",
                "shutter_speed": "1/250s",
                "iso": "100"
            },
            "order": 1
        }
    ],
    "created_at": "2026-01-01T00:00:00Z"
}
```

---

## 3. 状态码

| 状态码 | 说明 |
|--------|------|
| 200 | 请求成功 |
| 201 | 创建成功 |
| 204 | 删除成功 |
| 400 | 请求参数错误 |
| 401 | 未认证 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 500 | 服务器错误 |

---

## 4. 错误处理

### 4.1 验证错误

**状态码**: 400

**响应示例**:
```json
{
    "detail": "验证失败",
    "errors": {
        "title": ["此字段不能为空"],
        "slug": ["已存在相同slug的文章"]
    }
}
```

### 4.2 资源不存在

**状态码**: 404

**响应示例**:
```json
{
    "detail": "未找到"
}
```

---

## 5. 速率限制

当前版本未实现速率限制。

建议生产环境配置:
- 匿名用户: 100请求/小时
- 认证用户: 1000请求/小时

---

## 6. 使用示例

### Python

```python
import requests

# 获取文章列表
response = requests.get('https://api.example.com/api/blog/posts/')
posts = response.json()

# 获取文章详情
response = requests.get('https://api.example.com/api/blog/posts/landscape/')
post = response.json()

# 搜索文章
params = {'search': '山水', 'category': 'landscape'}
response = requests.get('https://api.example.com/api/blog/posts/', params=params)
results = response.json()['results']
```

### JavaScript

```javascript
// 获取文章列表
fetch('https://api.example.com/api/blog/posts/')
    .then(response => response.json())
    .then(data => console.log(data));

// 获取文章详情
fetch('https://api.example.com/api/blog/posts/landscape/')
    .then(response => response.json())
    .then(post => console.log(post));

// 搜索文章
const url = new URL('https://api.example.com/api/blog/posts/');
url.searchParams.append('search', '山水');
url.searchParams.append('category', 'landscape');
fetch(url)
    .then(response => response.json())
    .then(data => console.log(data));
```

---

## 7. SDK（可选）

未来可提供官方SDK:
- Python SDK
- JavaScript SDK
- PHP SDK

---

**本文档由墨影纪团队维护**
**最后更新：2026-01-18**
