# 任务管理API
    
-  一个用于学习后端开发和软件架构的任务管理 API。

## 项目目标

- 学习 REST API 设计
- 学习数据库增删改查
- 练习分层结构：API 层、Service 层、Repository 层
- 学会写测试、Docker 和 README
- 记录架构决策

## 核心功能：

- 创建任务：标题、描述、状态、截止时间
- 查询任务列表：支持按状态过滤、分页
- 查看单个任务
- 更新任务：改标题、改状态
- 删除任务
- 健康检查：GET /health []

## 技术栈

- Python 3.12
- FastAPI
- SQLite
- SQLAlchemy
- pytest
- Docker / Docker Compose（可选）

## 环境要求

- Python 3.10+
- Git
- 可选：Docker

## 设计说明

- 先做单体应用，不拆微服务。
- 先用 SQLite，方便本地运行，后续可以换 PostgreSQL。
- API 层负责处理 HTTP 请求和响应。
- Service 层负责业务逻辑。
- Repository 层负责数据库操作。

## 架构决策记录

- ADR-001：为什么先用 SQLite？
- ADR-002：为什么先做单体，不拆微服务？

## 学习记录

- 2026-09-21：创建仓库，完成第一版 README。

## 下载的依赖

- pip install fastapi uvicorn

## 运行测试

```bash
pytest
```

## 数据库

项目使用 SQLite + SQLAlchemy。

数据库文件 `tasks.db` 在项目根目录，首次启动自动创建。

表结构：

- tasks
  - id: INTEGER, 主键
  - title: VARCHAR(255), 非空
  - description: TEXT
  - done: BOOLEAN