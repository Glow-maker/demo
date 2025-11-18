# 企业级 Dify 项目学习资源

本文档整理了优质的企业级 Dify 项目，主要聚焦于大模型应用方向，供开发者学习和参考使用。

## 目录
- [核心平台与框架](#核心平台与框架)
- [工作流与应用模板](#工作流与应用模板)
- [即时通讯机器人集成](#即时通讯机器人集成)
- [企业微信集成](#企业微信集成)
- [智能客服与对话系统](#智能客服与对话系统)
- [部署与基础设施](#部署与基础设施)
- [插件与扩展](#插件与扩展)
- [开发工具与SDK](#开发工具与sdk)

---

## 核心平台与框架

### 1. Dify - 官方核心平台
- **项目地址**: https://github.com/langgenius/dify
- **Stars**: 119,151+ ⭐
- **语言**: TypeScript, Python
- **简介**: 生产就绪的智能体工作流开发平台，支持 Agent、RAG、工作流编排等功能。这是 Dify 的官方核心项目。
- **主要特性**:
  - 支持无代码/低代码 AI 应用开发
  - 内置 Agent、RAG、工作流等能力
  - 集成主流大模型（OpenAI、Claude、Gemini 等）
  - 完善的 API 和插件系统
- **适用场景**: AI 应用开发、企业级 LLM 应用构建、工作流自动化

### 2. BuildingAI - 企业级智能体平台
- **项目地址**: https://github.com/BidingCC/BuildingAI
- **Stars**: 779+ ⭐
- **语言**: TypeScript
- **简介**: 企业级开源智能体平台，灵感来源于 Coze 和 Dify。通过可视化配置界面（DIY），无需代码即可构建企业级 AI 应用。
- **主要特性**:
  - 可视化配置界面
  - 支持智能体、MCP 等原生能力
  - 专为企业场景优化
  - Node.js 技术栈
- **适用场景**: 企业 AI 应用快速开发、智能体构建

### 3. Flock - 工作流低代码平台
- **项目地址**: https://github.com/Onelevenvy/flock
- **Stars**: 1,048+ ⭐
- **语言**: TypeScript
- **简介**: 基于工作流的低代码平台，用于快速构建聊天机器人、RAG 和多智能体协作系统。采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。
- **主要特性**:
  - 可视化工作流编排
  - 支持多智能体协作
  - 集成 LangGraph 和 Langchain
  - 完整的 RAG 支持
- **适用场景**: 复杂工作流场景、多智能体协作、RAG 应用

### 4. 53AIHub - AI 门户平台
- **项目地址**: https://github.com/53AI/53AIHub
- **Stars**: 4,043+ ⭐
- **语言**: Vue, Go
- **简介**: 开源 AI 门户平台，能够快速构建运营级 AI 门户，用于发布和运营 AI 智能体、提示词和 AI 工具。支持与 Coze、Dify、FastGPT、RAGFlow 等平台无缝集成。
- **主要特性**:
  - 运营级 AI 门户
  - 支持多平台集成
  - 智能体和提示词管理
  - 完整的运营功能
- **适用场景**: AI 应用门户、AI 工具集成平台

### 5. Art - Java 开发者的 AI 平台
- **项目地址**: https://github.com/springboot4/Art
- **Stars**: 114+ ⭐
- **语言**: Java
- **简介**: 企业级开源智能体平台，为 Java 开发者提供熟悉、高效、稳定且易于扩展的 AI 应用构建环境。灵感来源于 Coze 和 Dify。
- **主要特性**:
  - Spring Boot 3 + Spring Cloud 技术栈
  - 为 Java 开发者优化
  - 支持聊天机器人、RAG
  - 企业级稳定性
- **适用场景**: Java 技术栈企业、Spring Boot 项目集成

---

## 工作流与应用模板

### 6. Awesome-Dify-Workflow - 工作流集合
- **项目地址**: https://github.com/svcvit/Awesome-Dify-Workflow
- **Stars**: 9,591+ ⭐
- **简介**: 分享实用的 Dify DSL 工作流程，涵盖各种应用场景，适合学习和实际使用。
- **主要特性**:
  - 丰富的工作流模板
  - DSL 配置文件
  - 实战案例
  - 持续更新
- **适用场景**: 学习 Dify 工作流、快速启动项目

### 7. dify-chat - 应用管理平台
- **项目地址**: https://github.com/lexmin0412/dify-chat
- **Stars**: 646+ ⭐
- **语言**: TypeScript
- **简介**: Dify 应用管理平台，基于 Dify API 构建，提供深度优化的用户端交互界面，支持 Chatflow、Workflow 等多种应用类型。
- **主要特性**:
  - 优化的用户界面
  - 支持深度思考、思维链
  - 图表渲染、文件处理
  - Ant Design 组件库
- **适用场景**: Dify 应用前端开发、用户体验优化

### 8. Open-Deep-Research-workflow-on-Dify
- **项目地址**: https://github.com/AdamPlatin123/Open-Deep-Research-workflow-on-Dify
- **Stars**: 301+ ⭐
- **简介**: 在 Dify 上实现的深度研究工作流。
- **适用场景**: 深度研究、知识挖掘

### 9. dify_course - 课程生成工作流
- **项目地址**: https://github.com/pekingmuge/dify_course
- **Stars**: 35+ ⭐
- **简介**: 通过 Dify 工作流自动生成完整课程的项目。
- **适用场景**: 教育、课程制作

### 10. dify-flow - 个人工作流分享
- **项目地址**: https://github.com/akira0912/dify-flow
- **Stars**: 37+ ⭐
- **简介**: 分享个人的 Dify 工作流配置。
- **适用场景**: 学习参考、工作流灵感

---

## 即时通讯机器人集成

### 11. LangBot - 全球 IM 机器人平台
- **项目地址**: https://github.com/langbot-app/LangBot
- **Stars**: 14,031+ ⭐
- **语言**: Python
- **简介**: 易用的大模型即时通信机器人开发平台，支持 QQ、Discord、微信、Telegram、飞书、钉钉等多个平台。
- **主要特性**:
  - 支持多个即时通讯平台
  - 集成主流 LLM（ChatGPT、DeepSeek、Dify、Coze 等）
  - 插件系统
  - Agent 和 RAG 支持
- **适用场景**: 多平台聊天机器人、企业内部 IM 助手

### 12. AstrBot - 智能对话机器人平台
- **项目地址**: https://github.com/AstrBotDevs/AstrBot
- **Stars**: 13,407+ ⭐
- **语言**: Python
- **简介**: 一站式大模型聊天机器人平台及开发框架，支持多消息平台集成和易用的插件系统。
- **主要特性**:
  - 多平台支持（QQ、Telegram、企微、飞书、钉钉等）
  - 易用的插件系统
  - 内置知识库和 Agent 智能体
  - 支持多种 LLM 平台
- **适用场景**: IM 聊天机器人、企业智能助手

---

## 企业微信集成

### 13. Dify-Enterprise-WeChat-bot - 企业微信知识库机器人
- **项目地址**: https://github.com/luolin-ai/Dify-Enterprise-WeChat-bot
- **Stars**: 600+ ⭐
- **简介**: 基于 Dify 的企业微信知识库机器人，能够自动回复企业微信消息，支持私聊和群聊，具备上下文记忆能力。
- **主要特性**:
  - 企业微信集成
  - 上下文记忆
  - 白名单控制
  - 私聊和群聊支持
- **适用场景**: 企业内部知识库、客服自动化

### 14. chatgpt-wechat - 企业微信/微信 LLM 助手
- **项目地址**: https://github.com/whyiyhw/chatgpt-wechat
- **Stars**: 1,112+ ⭐
- **语言**: Go
- **简介**: 企业微信/微信安全使用的 LLM 个人助手/客服，支持 Dify 工作流。
- **主要特性**:
  - 支持 DeepSeek、Gemini、GPT-4 等模型
  - Dify 工作流集成
  - 企业微信和个人微信支持
  - Go 语言实现，性能优秀
- **适用场景**: 企业微信智能助手、个人助手

### 15. XYBotV2 - 功能丰富的微信机器人框架
- **项目地址**: https://github.com/HenryXiaoYang/XYBotV2
- **Stars**: 780+ ⭐
- **语言**: Python
- **简介**: 功能丰富的微信机器人框架，支持 AI 对话、对接 Dify、积分系统、游戏互动等。跨平台支持（Windows、Linux、MacOS）。
- **主要特性**:
  - 非 Hook 非 Web 实现
  - 丰富的功能（积分、游戏、新闻、天气）
  - Dify 集成
  - 跨平台支持
- **适用场景**: 微信群管理、社群互动

### 16. dify-on-wechat
- **项目地址**: https://github.com/mengdahuang/dify-on-wechat
- **Stars**: 132+ ⭐
- **语言**: Python
- **简介**: 将 Dify 集成到微信的项目。
- **适用场景**: 微信机器人、Dify 微信集成

### 17. dow-ipad-859 - iPad 协议微信机器人
- **项目地址**: https://github.com/Lingyuzhou111/dow-ipad-859
- **Stars**: 162+ ⭐
- **语言**: Python
- **简介**: 基于 859 版 iPad 协议的微信机器人，集成 dify-on-wechat 框架，实现智能对话功能。
- **主要特性**:
  - iPad 协议实现
  - 消息收发
  - AI 对话
  - 图片识别
- **适用场景**: 微信自动化、智能客服

### 18. ChatBot-Next - 可视化管理平台
- **项目地址**: https://github.com/onenov/ChatBot-Next
- **Stars**: 71+ ⭐
- **语言**: Vue
- **简介**: 无缝集成处理和调度 Dify & Dify on WeChat，提供 Web 可视化多用户管理。
- **主要特性**:
  - Web 可视化管理
  - 多用户支持
  - 一键启动
  - Vue 前端
- **适用场景**: 微信机器人管理、多用户场景

### 19. difytimetask - 定时任务插件
- **项目地址**: https://github.com/cm04918/difytimetask
- **Stars**: 65+ ⭐
- **语言**: Python
- **简介**: 基于 gewechat 渠道 dify-on-wechat 的定时任务插件。
- **适用场景**: 定时消息发送、自动化任务

### 20. dify_wechat_plugin - 微信公众号插件
- **项目地址**: https://github.com/bikeread/dify_wechat_plugin
- **Stars**: 57+ ⭐
- **语言**: Python
- **简介**: Dify 插件市场应用，开箱即用，用于快速对接微信公众号。
- **适用场景**: 微信公众号智能客服

---

## 智能客服与对话系统

### 21. ChatGPT-On-CS - 智能对话客服工具
- **项目地址**: https://github.com/cs-lazy-tools/ChatGPT-On-CS
- **Stars**: 3,509+ ⭐
- **语言**: TypeScript
- **简介**: 基于大模型的智能对话客服工具，支持微信、拼多多、千牛、哔哩哔哩、抖音、小红书、知乎等多平台接入。
- **主要特性**:
  - 多平台支持（微信、电商、社交媒体）
  - 文本、语音、图片处理
  - 基于自有知识库定制
  - 插件系统
- **适用场景**: 电商客服、社交媒体运营、多渠道客服

### 22. wechat-assistant-pro - 智能微秘书
- **项目地址**: https://github.com/leochen-g/wechat-assistant-pro
- **Stars**: 2,357+ ⭐
- **语言**: JavaScript
- **简介**: 全能微信机器人管理平台，支持接入 ChatGPT、FastGPT、Dify、Coze、DeepSeek。
- **主要特性**:
  - 支持多个 LLM 平台
  - 绘图、语音识别
  - 定时任务
  - 企业微信、公众号、WhatsApp 支持
- **适用场景**: 微信助手、企业自动化

### 23. PlugBot - 多 Bot 统一平台
- **项目地址**: https://github.com/shamspias/PlugBot
- **Stars**: 36+ ⭐
- **语言**: Python
- **简介**: 连接多个 Dify 机器人和 Telegram 的统一平台，提供统一的管理界面。
- **主要特性**:
  - 多 Bot 管理
  - 统一的 Dashboard
  - API 密钥管理
  - Telegram 集成
- **适用场景**: 多 Bot 场景、集中管理

### 24. wordpress_kefu_ai_agent - WordPress 客服智能体
- **项目地址**: https://github.com/liangdabiao/wordpress_kefu_ai_agent
- **Stars**: 56+ ⭐
- **语言**: TypeScript
- **简介**: 自适应智能客服项目（Agentic agent），适合程序员的智能客服。
- **主要特性**:
  - WordPress 集成
  - 简单配置
  - 可控的智能体
  - 仅需 2 个文件
- **适用场景**: WordPress 网站客服

### 25. Dify-ChatApp-Embedded-Exp - 嵌入式聊天应用
- **项目地址**: https://github.com/HugoWw/Dify-ChatApp-Embedded-Exp
- **Stars**: 61+ ⭐
- **语言**: JavaScript
- **简介**: 封装 Dify 聊天机器人以实现自定义样式和平滑缩放。
- **适用场景**: 网站嵌入式客服、UI 定制

---

## 部署与基础设施

### 26. dify-google-cloud-terraform - Google Cloud 部署
- **项目地址**: https://github.com/DeNA/dify-google-cloud-terraform
- **Stars**: 239+ ⭐
- **语言**: HCL (Terraform)
- **简介**: 在 Google Cloud 上部署 Dify 的 Terraform 配置，具备可扩展性、高可用性和生产级就绪能力。
- **主要特性**:
  - 基础设施即代码
  - 高可用性配置
  - 可扩展架构
  - 生产级部署
- **适用场景**: 企业级部署、Google Cloud 用户

---

## 插件与扩展

### 27. dify-mcp-server - MCP Server for Dify
- **项目地址**: https://github.com/YanxingLiu/dify-mcp-server
- **Stars**: 269+ ⭐
- **语言**: Python
- **简介**: Dify 工作流的模型上下文协议（MCP）服务器。
- **主要特性**:
  - MCP 协议支持
  - 工作流集成
  - Python 实现
- **适用场景**: MCP 集成、工作流扩展

### 28. mcp-difyworkflow-server - MCP Dify Workflow Server
- **项目地址**: https://github.com/gotoolkits/mcp-difyworkflow-server
- **Stars**: 59+ ⭐
- **语言**: Go
- **简介**: MCP 服务器工具应用，实现 Dify 工作流的查询和调用，支持按需运行多个自定义工作流。
- **主要特性**:
  - Go 语言实现
  - MCP 服务器
  - 多工作流支持
- **适用场景**: 工作流服务化、MCP 集成

### 29. dify-mcp-client - MCP Client 插件
- **项目地址**: https://github.com/3dify-project/dify-mcp-client
- **Stars**: 158+ ⭐
- **语言**: Python
- **简介**: MCP Client 作为 Agent 策略插件，支持通过 UI-TARS-SDK 进行 GUI 操作。
- **主要特性**:
  - MCP Client 实现
  - Agent 策略插件
  - UI-TARS-SDK 集成
  - GUI 操作支持
- **适用场景**: Agent 开发、UI 自动化

### 30. dify-plugin-agent-mcp_sse - MCP Tools Agent
- **项目地址**: https://github.com/junjiem/dify-plugin-agent-mcp_sse
- **Stars**: 117+ ⭐
- **语言**: Python
- **简介**: Dify 1.0 插件，支持 MCP Tools Agent 策略。
- **适用场景**: Dify 插件开发、MCP 工具

### 31. dify-plugin-webhook - Webhook 插件
- **项目地址**: https://github.com/perzeuss/dify-plugin-webhook
- **Stars**: 44+ ⭐
- **语言**: Python
- **简介**: Dify 插件，通过 webhook 调用 Dify 工作流和聊天流。
- **适用场景**: Webhook 集成、外部触发

### 32. awesome-cow-plugins - CoW 和 DoW 插件集合
- **项目地址**: https://github.com/WoodGoose/awesome-cow-plugins
- **Stars**: 217+ ⭐
- **简介**: 收集 CoW (chatgpt-on-wechat) 与 DoW (dify-on-wechat) 的插件。
- **适用场景**: 插件发现、功能扩展

### 33. Dify_Pipeline_OpenwebUI - OpenWebUI Pipeline
- **项目地址**: https://github.com/JiangYain/Dify_Pipeline_OpenwebUI
- **Stars**: 38+ ⭐
- **语言**: Python
- **简介**: 通过 Pipeline 将 Dify 接入 OpenWebUI，结合 OpenWebUI 的前端优势和 Dify 的工作流能力。
- **适用场景**: OpenWebUI 集成

---

## 开发工具与SDK

### 34. evolution-api - WhatsApp 集成 API
- **项目地址**: https://github.com/EvolutionAPI/evolution-api
- **Stars**: 6,238+ ⭐
- **语言**: TypeScript
- **简介**: 开源 WhatsApp 集成 API，支持与 Dify、n8n 等平台集成。
- **主要特性**:
  - WhatsApp API
  - 多平台集成支持
  - Cloud API 兼容
  - RabbitMQ 支持
- **适用场景**: WhatsApp 机器人、消息自动化

### 35. dify-client-python - Python SDK
- **项目地址**: https://github.com/haoyuhu/dify-client-python
- **Stars**: 47+ ⭐
- **语言**: Python
- **简介**: Python 包，提供与 Dify API 交互的便捷接口。
- **主要特性**:
  - Python SDK
  - 完整的 API 封装
  - 易用的接口
- **适用场景**: Python 应用集成、API 开发

### 36. chatbot-chrome-extension - Chrome 扩展
- **项目地址**: https://github.com/langgenius/chatbot-chrome-extension
- **Stars**: 53+ ⭐
- **语言**: CSS, JavaScript
- **简介**: Dify 官方 Chrome 扩展。
- **适用场景**: 浏览器集成、网页助手

---

## 特殊应用场景

### 37. comfyui_LLM_party - ComfyUI LLM Agent 框架
- **项目地址**: https://github.com/heshengtao/comfyui_LLM_party
- **Stars**: 1,994+ ⭐
- **语言**: Python
- **简介**: ComfyUI 中的 LLM Agent 框架，包含 MCP 服务器、Omost、GPT-sovits、ChatTTS 等，支持图形化 RAG。
- **主要特性**:
  - ComfyUI 集成
  - 多种 LLM 支持
  - 本地模型支持
  - GraphRAG
- **适用场景**: AI 图像生成、多模态应用

### 38. super-agent-party - 3D 桌面伴侣
- **项目地址**: https://github.com/heshengtao/super-agent-party
- **Stars**: 1,276+ ⭐
- **语言**: JavaScript
- **简介**: 零门槛的 3D 桌面伴侣，支持 QQ、B 站直播、RAG、Dify、Home Assistant、MCP 等。
- **主要特性**:
  - 3D 可视化
  - 多平台集成
  - 桌面宠物
  - 长期记忆
- **适用场景**: 桌面助手、直播互动

### 39. xiaozhi-android-client - Android/iOS 语音对话应用
- **项目地址**: https://github.com/TOM88812/xiaozhi-android-client
- **Stars**: 1,206+ ⭐
- **语言**: Dart (Flutter)
- **简介**: 基于小智、xiaozhi-server 的 Android、iOS 语音对话应用，支持实时语音交互和文字对话。
- **主要特性**:
  - Flutter 跨平台
  - 实时语音交互
  - 文字对话
  - Dify 集成
- **适用场景**: 移动端语音助手

### 40. ChatSQL - 数据库学习平台
- **项目地址**: https://github.com/ffy6511/ChatSQL
- **Stars**: 51+ ⭐
- **语言**: TypeScript
- **简介**: 智能体设计与工作流编排赋能的数据库系统学习平台。
- **主要特性**:
  - 数据库学习
  - 可视化
  - Agent 设计
  - 工作流编排
- **适用场景**: 教育、数据库学习

### 41. DifyDSL4RedTeam - 红队工作流
- **项目地址**: https://github.com/din4e/DifyDSL4RedTeam
- **Stars**: 33+ ⭐
- **简介**: 收集红队使用的 Dify Workflow。
- **适用场景**: 安全测试、红队演练

---

## 学习建议

### 入门路径
1. **从官方平台开始**: 先熟悉 [Dify](https://github.com/langgenius/dify) 官方平台的基本功能
2. **学习工作流**: 参考 [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow) 中的模板
3. **选择应用场景**: 根据自己的需求选择相应的集成项目

### 进阶方向
- **企业应用开发**: 研究 BuildingAI、Flock 等企业级平台
- **即时通讯集成**: 学习 LangBot、AstrBot 等多平台机器人框架
- **客服系统**: 深入 ChatGPT-On-CS 等智能客服解决方案
- **基础设施**: 了解 dify-google-cloud-terraform 等部署方案

### 实战项目推荐
- **知识库应用**: Dify-Enterprise-WeChat-bot
- **工作流编排**: Flock 或 Awesome-Dify-Workflow
- **多渠道客服**: ChatGPT-On-CS
- **移动端应用**: xiaozhi-android-client

---

## 技术栈分布

- **TypeScript/JavaScript**: 前端应用、全栈平台
- **Python**: 机器人、后端服务、插件
- **Go**: 高性能服务、MCP 服务器
- **Java**: 企业级应用（Spring Boot）
- **Dart/Flutter**: 移动端应用

---

## 贡献与更新

本文档将持续更新，欢迎提交 PR 补充更多优质项目。

**更新时间**: 2025-11-18

**Star 数据说明**: 所有 Star 数据截至文档创建时间，实际数据可能已有变化。

---

## 相关资源

- [Dify 官方文档](https://docs.dify.ai/)
- [Dify 官方社区](https://github.com/langgenius/dify/discussions)
- [Dify 插件市场](https://github.com/langgenius/dify-plugins)

---

## 免责声明

本文档仅用于学习和研究目的，所列项目的使用需遵守各自的开源协议。使用前请仔细阅读各项目的 LICENSE 文件。

部署和使用这些项目时，请确保：
- 遵守相关法律法规
- 保护用户隐私和数据安全
- 合规使用 LLM 服务
- 注意 API 成本控制
