# 墨影纪 · 部署指南

> 版本：1.0
> 最后更新：2026-01-18

---

## 1. 部署概述

### 1.1 部署架构

```
Internet
    ↓
[Nginx (端口80/443)]
    ↓
[Gunicorn (端口8000, 3 workers)]
    ↓
[Django Application]
    ↓
[PostgreSQL] + [Redis]
```

### 1.2 部署要求

**服务器配置（最低）**
- CPU: 2核
- 内存: 4GB
- 硬盘: 40GB SSD
- 操作系统: Ubuntu 20.04+ / CentOS 8+

**软件要求**
- Python 3.9+
- PostgreSQL 13+
- Redis 7+
- Nginx 1.18+
- Docker & Docker Compose（可选）

---

## 2. Docker部署（推荐）

### 2.1 快速部署

```bash
# 1. 克隆项目
git clone https://github.com/tianhaishun/moyinji_blog.git
cd moyinji_blog

# 2. 配置环境变量
cp .env.example .env
nano .env  # 修改配置

# 3. 启动服务
docker-compose up -d

# 4. 创建管理员
docker-compose exec web python manage.py createsuperuser

# 5. 收集静态文件
docker-compose exec web python manage.py collectstatic --noinput
```

### 2.2 环境变量配置

```bash
# .env
DEBUG=False
SECRET_KEY=your-production-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=moyinji_db
DB_USER=moyinji
DB_PASSWORD=your-secure-password
DB_HOST=db
DB_PORT=5432

# Redis
REDIS_URL=redis://redis:6379/0

# Email (可选)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=your-email-password
```

### 2.3 Docker Compose管理

```bash
# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f web

# 重启服务
docker-compose restart

# 停止服务
docker-compose down

# 停止并删除数据卷
docker-compose down -v

# 更新镜像
docker-compose pull
docker-compose up -d
```

---

## 3. 传统部署方式

### 3.1 系统准备

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3-pip python3-venv postgresql redis-server nginx

# CentOS/RHEL
sudo yum install python3-pip postgresql-server redis nginx
```

### 3.2 项目部署

```bash
# 1. 创建用户
sudo useradd -m -s /bin/bash moyinji
sudo su - moyinji

# 2. 克隆项目
git clone https://github.com/tianhaishun/moyinji_blog.git
cd moyinji_blog

# 3. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. 配置环境变量
cp .env.example .env
nano .env

# 5. 配置PostgreSQL
sudo -u postgres createdb moyinji_db
sudo -u postgres createuser -P moyinji
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE moyinji_db TO moyinji;"

# 6. 运行迁移
python manage.py migrate

# 7. 创建管理员
python manage.py createsuperuser

# 8. 收集静态文件
python manage.py collectstatic --noinput
```

### 3.3 Gunicorn配置

```bash
# /etc/systemd/system/moyinji.service
[Unit]
Description=Moyinji Django Application
After=network.target postgresql.service

[Service]
User=moyinji
Group=moyinji
WorkingDirectory=/home/moyinji/moyinji_blog
Environment="PATH=/home/moyinji/moyinji_blog/venv/bin"
ExecStart=/home/moyinji/moyinji_blog/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/home/moyinji/moyinji_blog/moyinji.sock \
    moyinji.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# 启动服务
sudo systemctl start moyinji
sudo systemctl enable moyinji
sudo systemctl status moyinji
```

### 3.4 Nginx配置

```nginx
# /etc/nginx/sites-available/moyinji
upstream moyinji_backend {
    server unix:/home/moyinji/moyinji_blog/moyinji.sock;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    # Static files
    location /static/ {
        alias /home/moyinji/moyinji_blog/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Media files
    location /media/ {
        alias /home/moyinji/moyinji_blog/media/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Proxy to Gunicorn
    location / {
        proxy_pass http://moyinji_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
# 启用配置
sudo ln -s /etc/nginx/sites-available/moyinji /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## 4. SSL证书配置

### 4.1 使用Let's Encrypt

```bash
# 安装Certbot
sudo apt install certbot python3-certbot-nginx

# 获取证书
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# 自动续期
sudo certbot renew --dry-run
```

---

## 5. 数据库优化

### 5.1 PostgreSQL配置

```bash
# /etc/postgresql/13/main/postgresql.conf
# 内存设置（根据服务器调整）
shared_buffers = 256MB
effective_cache_size = 1GB
maintenance_work_mem = 64MB
checkpoint_completion_target = 0.9
wal_buffers = 16MB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 200
work_mem = 2621kB
min_wal_size = 1GB
max_wal_size = 4GB
```

### 5.2 数据库备份

```bash
#!/bin/bash
# /home/moyinji/backup.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/home/moyinji/backups"
DB_NAME="moyinji_db"
DB_USER="moyinji"

# 创建备份目录
mkdir -p $BACKUP_DIR

# 备份数据库
pg_dump -U $DB_USER $DB_NAME | gzip > $BACKUP_DIR/db_$DATE.sql.gz

# 备份媒体文件
tar -czf $BACKUP_DIR/media_$DATE.tar.gz /home/moyinji/moyinji_blog/media/

# 删除30天前的备份
find $BACKUP_DIR -name "*.gz" -mtime +30 -delete
```

```bash
# 添加到crontab（每天凌晨2点备份）
crontab -e
0 2 * * * /home/moyinji/backup.sh
```

---

## 6. Redis配置

### 6.1 持久化配置

```bash
# /etc/redis/redis.conf
# RDB快照
save 900 1
save 300 10
save 60 10000

# AOF持久化
appendonly yes
appendfilename "appendonly.aof"
appendfsync everysec

# 内存管理
maxmemory 256mb
maxmemory-policy allkeys-lru
```

---

## 7. 监控与日志

### 7.1 应用日志

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/moyinji/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

```bash
# 创建日志目录
sudo mkdir -p /var/log/moyinji
sudo chown moyinji:moyinji /var/log/moyinji
```

### 7.2 Nginx日志

```bash
# 查看访问日志
sudo tail -f /var/log/nginx/access.log

# 查看错误日志
sudo tail -f /var/log/nginx/error.log
```

---

## 8. 性能优化

### 8.1 缓存优化

```python
# settings.py
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        },
        "KEY_PREFIX": "moyinji",
    }
}

# Session存储到Redis
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
```

### 8.2 静态文件CDN（可选）

```python
# settings.py
STATIC_URL = 'https://cdn.yourdomain.com/static/'
MEDIA_URL = 'https://cdn.yourdomain.com/media/'
```

---

## 9. 安全加固

### 9.1 防火墙配置

```bash
# UFW (Ubuntu)
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP
sudo ufw allow 443/tcp   # HTTPS
sudo ufw enable

# firewalld (CentOS)
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

### 9.2 fail2ban防护

```bash
# 安装fail2ban
sudo apt install fail2ban

# 配置Nginx防护
# /etc/fail2ban/jail.local
[nginx-http-auth]
enabled = true
port = http,https
logpath = /var/log/nginx/error.log
```

---

## 10. 故障排查

### 10.1 常见问题

**问题1: 502 Bad Gateway**
```bash
# 检查Gunicorn是否运行
sudo systemctl status moyinji

# 查看Gunicorn日志
sudo journalctl -u moyinji -n 50
```

**问题2: 静态文件404**
```bash
# 重新收集静态文件
python manage.py collectstatic --noinput

# 检查Nginx配置
sudo nginx -t
```

**问题3: 数据库连接失败**
```bash
# 检查PostgreSQL状态
sudo systemctl status postgresql

# 检查连接
psql -U moyinji -d moyinji_db
```

### 10.2 日志查看

```bash
# Django日志
tail -f /var/log/moyinji/django.log

# Gunicorn日志
sudo journalctl -u moyinji -f

# Nginx日志
sudo tail -f /var/log/nginx/error.log

# 系统日志
sudo journalctl -xe
```

---

## 11. 更新与维护

### 11.1 应用更新

```bash
# 1. 备份数据
./backup.sh

# 2. 拉取最新代码
git pull origin main

# 3. 更新依赖
source venv/bin/activate
pip install -r requirements.txt

# 4. 运行迁移
python manage.py migrate

# 5. 收集静态文件
python manage.py collectstatic --noinput

# 6. 重启服务
sudo systemctl restart moyinji
```

### 11.2 依赖更新

```bash
# 检查过时的包
pip list --outdated

# 更新包
pip install --upgrade Django

# 更新requirements.txt
pip freeze > requirements.txt
```

---

**本文档由墨影纪团队维护**
**最后更新：2026-01-18**
