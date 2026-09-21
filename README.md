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