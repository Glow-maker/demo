# Enterprise-Level Dify Projects Learning Resources

This document compiles high-quality enterprise-level Dify projects, focusing on large language model applications, for developers to learn and reference.

## Table of Contents
- [Core Platforms & Frameworks](#core-platforms--frameworks)
- [Workflows & Application Templates](#workflows--application-templates)
- [Instant Messaging Bot Integrations](#instant-messaging-bot-integrations)
- [Enterprise WeChat Integrations](#enterprise-wechat-integrations)
- [Intelligent Customer Service & Dialogue Systems](#intelligent-customer-service--dialogue-systems)
- [Deployment & Infrastructure](#deployment--infrastructure)
- [Plugins & Extensions](#plugins--extensions)
- [Development Tools & SDKs](#development-tools--sdks)
- [Special Use Cases](#special-use-cases)

---

## Core Platforms & Frameworks

### 1. Dify - Official Core Platform
- **Repository**: https://github.com/langgenius/dify
- **Stars**: 119,151+ ⭐
- **Language**: TypeScript, Python
- **Description**: Production-ready platform for agentic workflow development, supporting Agent, RAG, workflow orchestration, and more. This is the official Dify core project.
- **Key Features**:
  - No-code/Low-code AI application development
  - Built-in Agent, RAG, and workflow capabilities
  - Integration with mainstream LLMs (OpenAI, Claude, Gemini, etc.)
  - Comprehensive API and plugin system
- **Use Cases**: AI application development, enterprise LLM application building, workflow automation

### 2. BuildingAI - Enterprise-Grade Agent Platform
- **Repository**: https://github.com/BidingCC/BuildingAI
- **Stars**: 779+ ⭐
- **Language**: TypeScript
- **Description**: Enterprise-grade open-source intelligent agent platform inspired by Coze and Dify. Build native enterprise AI applications without code through a visual configuration interface (DIY).
- **Key Features**:
  - Visual configuration interface
  - Support for agents, MCP, and other native capabilities
  - Optimized for enterprise scenarios
  - Node.js tech stack
- **Use Cases**: Rapid enterprise AI application development, agent building

### 3. Flock - Workflow-Based Low-Code Platform
- **Repository**: https://github.com/Onelevenvy/flock
- **Stars**: 1,048+ ⭐
- **Language**: TypeScript
- **Description**: Workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams. Built with LangGraph, Langchain, FastAPI, and NextJS.
- **Key Features**:
  - Visual workflow orchestration
  - Multi-agent collaboration support
  - LangGraph and Langchain integration
  - Complete RAG support
- **Use Cases**: Complex workflow scenarios, multi-agent collaboration, RAG applications

### 4. 53AIHub - AI Portal Platform
- **Repository**: https://github.com/53AI/53AIHub
- **Stars**: 4,043+ ⭐
- **Language**: Vue, Go
- **Description**: Open-source AI portal platform that enables quick building of operational-level AI portals for launching and operating AI agents, prompts, and AI tools. Supports seamless integration with Coze, Dify, FastGPT, RAGFlow, and more.
- **Key Features**:
  - Operational-level AI portal
  - Multi-platform integration support
  - Agent and prompt management
  - Complete operational features
- **Use Cases**: AI application portal, AI tool integration platform

### 5. Art - AI Platform for Java Developers
- **Repository**: https://github.com/springboot4/Art
- **Stars**: 114+ ⭐
- **Language**: Java
- **Description**: Enterprise-grade open-source agent platform providing Java developers with a familiar, efficient, stable, and easily extensible AI application building environment. Inspired by Coze and Dify.
- **Key Features**:
  - Spring Boot 3 + Spring Cloud tech stack
  - Optimized for Java developers
  - Supports chatbots and RAG
  - Enterprise-grade stability
- **Use Cases**: Java tech stack enterprises, Spring Boot project integration

---

## Workflows & Application Templates

### 6. Awesome-Dify-Workflow - Workflow Collection
- **Repository**: https://github.com/svcvit/Awesome-Dify-Workflow
- **Stars**: 9,591+ ⭐
- **Description**: Sharing practical Dify DSL workflows covering various application scenarios, suitable for learning and practical use.
- **Key Features**:
  - Rich workflow templates
  - DSL configuration files
  - Real-world cases
  - Continuously updated
- **Use Cases**: Learning Dify workflows, quick project startup

### 7. dify-chat - Application Management Platform
- **Repository**: https://github.com/lexmin0412/dify-chat
- **Stars**: 646+ ⭐
- **Language**: TypeScript
- **Description**: Dify application management platform built on Dify API, providing deeply optimized user-side interaction interface, supporting Chatflow, Workflow, and other Dify application types.
- **Key Features**:
  - Optimized user interface
  - Support for deep thinking and chain-of-thought
  - Chart rendering and file processing
  - Ant Design component library
- **Use Cases**: Dify application frontend development, user experience optimization

### 8. Open-Deep-Research-workflow-on-Dify
- **Repository**: https://github.com/AdamPlatin123/Open-Deep-Research-workflow-on-Dify
- **Stars**: 301+ ⭐
- **Description**: Deep research workflow implemented on Dify.
- **Use Cases**: Deep research, knowledge mining

### 9. dify_course - Course Generation Workflow
- **Repository**: https://github.com/pekingmuge/dify_course
- **Stars**: 35+ ⭐
- **Description**: A project that automatically generates complete courses through Dify workflows.
- **Use Cases**: Education, course creation

### 10. dify-flow - Personal Workflow Sharing
- **Repository**: https://github.com/akira0912/dify-flow
- **Stars**: 37+ ⭐
- **Description**: Sharing personal Dify workflow configurations.
- **Use Cases**: Learning reference, workflow inspiration

---

## Instant Messaging Bot Integrations

### 11. LangBot - Global IM Bot Platform
- **Repository**: https://github.com/langbot-app/LangBot
- **Stars**: 14,031+ ⭐
- **Language**: Python
- **Description**: Easy-to-use LLM-based instant messaging bot development platform supporting QQ, Discord, WeChat, Telegram, Feishu, DingTalk, and more.
- **Key Features**:
  - Multi-IM platform support
  - Integration with mainstream LLMs (ChatGPT, DeepSeek, Dify, Coze, etc.)
  - Plugin system
  - Agent and RAG support
- **Use Cases**: Multi-platform chatbots, enterprise internal IM assistants

### 12. AstrBot - Intelligent Dialogue Bot Platform
- **Repository**: https://github.com/AstrBotDevs/AstrBot
- **Stars**: 13,407+ ⭐
- **Language**: Python
- **Description**: One-stop LLM chatbot platform and development framework supporting multiple messaging platform integrations and an easy-to-use plugin system.
- **Key Features**:
  - Multi-platform support (QQ, Telegram, Enterprise WeChat, Feishu, DingTalk, etc.)
  - Easy-to-use plugin system
  - Built-in knowledge base and Agent
  - Multiple LLM platform support
- **Use Cases**: IM chatbots, enterprise intelligent assistants

---

## Enterprise WeChat Integrations

### 13. Dify-Enterprise-WeChat-bot - Enterprise WeChat Knowledge Base Bot
- **Repository**: https://github.com/luolin-ai/Dify-Enterprise-WeChat-bot
- **Stars**: 600+ ⭐
- **Description**: Dify-based Enterprise WeChat knowledge base bot that automatically replies to Enterprise WeChat messages, supporting private and group chats with contextual memory.
- **Key Features**:
  - Enterprise WeChat integration
  - Contextual memory
  - Whitelist control
  - Private and group chat support
- **Use Cases**: Internal enterprise knowledge base, customer service automation

### 14. chatgpt-wechat - Enterprise WeChat/WeChat LLM Assistant
- **Repository**: https://github.com/whyiyhw/chatgpt-wechat
- **Stars**: 1,112+ ⭐
- **Language**: Go
- **Description**: Secure LLM personal assistant/customer service for Enterprise WeChat/WeChat, supporting Dify workflows.
- **Key Features**:
  - Support for DeepSeek, Gemini, GPT-4, and other models
  - Dify workflow integration
  - Enterprise WeChat and personal WeChat support
  - Go language implementation with excellent performance
- **Use Cases**: Enterprise WeChat intelligent assistant, personal assistant

### 15. XYBotV2 - Feature-Rich WeChat Bot Framework
- **Repository**: https://github.com/HenryXiaoYang/XYBotV2
- **Stars**: 780+ ⭐
- **Language**: Python
- **Description**: Feature-rich WeChat bot framework supporting AI dialogue, Dify integration, point system, game interaction, and more. Cross-platform support (Windows, Linux, MacOS).
- **Key Features**:
  - Non-Hook, non-Web implementation
  - Rich features (points, games, news, weather)
  - Dify integration
  - Cross-platform support
- **Use Cases**: WeChat group management, community interaction

### 16. dify-on-wechat
- **Repository**: https://github.com/mengdahuang/dify-on-wechat
- **Stars**: 132+ ⭐
- **Language**: Python
- **Description**: Project integrating Dify with WeChat.
- **Use Cases**: WeChat bot, Dify WeChat integration

### 17. dow-ipad-859 - iPad Protocol WeChat Bot
- **Repository**: https://github.com/Lingyuzhou111/dow-ipad-859
- **Stars**: 162+ ⭐
- **Language**: Python
- **Description**: WeChat bot based on iPad protocol version 859, integrating dify-on-wechat framework for intelligent dialogue.
- **Key Features**:
  - iPad protocol implementation
  - Message sending and receiving
  - AI dialogue
  - Image recognition
- **Use Cases**: WeChat automation, intelligent customer service

### 18. ChatBot-Next - Visual Management Platform
- **Repository**: https://github.com/onenov/ChatBot-Next
- **Stars**: 71+ ⭐
- **Language**: Vue
- **Description**: Seamlessly integrates and schedules Dify & Dify on WeChat with Web-based visual multi-user management.
- **Key Features**:
  - Web-based visual management
  - Multi-user support
  - One-click startup
  - Vue frontend
- **Use Cases**: WeChat bot management, multi-user scenarios

### 19. difytimetask - Scheduled Task Plugin
- **Repository**: https://github.com/cm04918/difytimetask
- **Stars**: 65+ ⭐
- **Language**: Python
- **Description**: Scheduled task plugin based on gewechat channel dify-on-wechat.
- **Use Cases**: Scheduled message sending, automation tasks

### 20. dify_wechat_plugin - WeChat Official Account Plugin
- **Repository**: https://github.com/bikeread/dify_wechat_plugin
- **Stars**: 57+ ⭐
- **Language**: Python
- **Description**: Dify plugin marketplace application, out-of-the-box for quickly integrating WeChat Official Accounts.
- **Use Cases**: WeChat Official Account intelligent customer service

---

## Intelligent Customer Service & Dialogue Systems

### 21. ChatGPT-On-CS - Intelligent Dialogue Customer Service Tool
- **Repository**: https://github.com/cs-lazy-tools/ChatGPT-On-CS
- **Stars**: 3,509+ ⭐
- **Language**: TypeScript
- **Description**: LLM-based intelligent dialogue customer service tool supporting WeChat, Pinduoduo, Qianniu, Bilibili, Douyin, Xiaohongshu, Zhihu, and more.
- **Key Features**:
  - Multi-platform support (WeChat, e-commerce, social media)
  - Text, voice, and image processing
  - Customizable based on proprietary knowledge base
  - Plugin system
- **Use Cases**: E-commerce customer service, social media operations, multi-channel customer service

### 22. wechat-assistant-pro - Intelligent WeChat Secretary
- **Repository**: https://github.com/leochen-g/wechat-assistant-pro
- **Stars**: 2,357+ ⭐
- **Language**: JavaScript
- **Description**: All-in-one WeChat bot management platform supporting ChatGPT, FastGPT, Dify, Coze, DeepSeek integration.
- **Key Features**:
  - Multiple LLM platform support
  - Image generation, voice recognition
  - Scheduled tasks
  - Enterprise WeChat, Official Account, WhatsApp support
- **Use Cases**: WeChat assistant, enterprise automation

### 23. PlugBot - Multi-Bot Unified Platform
- **Repository**: https://github.com/shamspias/PlugBot
- **Stars**: 36+ ⭐
- **Language**: Python
- **Description**: Unified platform connecting multiple Dify bots and Telegram with a unified management interface.
- **Key Features**:
  - Multi-bot management
  - Unified dashboard
  - API key management
  - Telegram integration
- **Use Cases**: Multi-bot scenarios, centralized management

### 24. wordpress_kefu_ai_agent - WordPress Customer Service Agent
- **Repository**: https://github.com/liangdabiao/wordpress_kefu_ai_agent
- **Stars**: 56+ ⭐
- **Language**: TypeScript
- **Description**: Adaptive intelligent customer service project (Agentic agent), suitable for programmers' intelligent customer service.
- **Key Features**:
  - WordPress integration
  - Simple configuration
  - Controllable agent
  - Only 2 files needed
- **Use Cases**: WordPress website customer service

### 25. Dify-ChatApp-Embedded-Exp - Embedded Chat Application
- **Repository**: https://github.com/HugoWw/Dify-ChatApp-Embedded-Exp
- **Stars**: 61+ ⭐
- **Language**: JavaScript
- **Description**: Encapsulate Dify chatbot to achieve custom styles and smooth zooming.
- **Use Cases**: Website embedded customer service, UI customization

---

## Deployment & Infrastructure

### 26. dify-google-cloud-terraform - Google Cloud Deployment
- **Repository**: https://github.com/DeNA/dify-google-cloud-terraform
- **Stars**: 239+ ⭐
- **Language**: HCL (Terraform)
- **Description**: Terraform configuration for deploying Dify on Google Cloud with scalability, high availability, and production-level readiness.
- **Key Features**:
  - Infrastructure as Code
  - High availability configuration
  - Scalable architecture
  - Production-grade deployment
- **Use Cases**: Enterprise-level deployment, Google Cloud users

---

## Plugins & Extensions

### 27. dify-mcp-server - MCP Server for Dify
- **Repository**: https://github.com/YanxingLiu/dify-mcp-server
- **Stars**: 269+ ⭐
- **Language**: Python
- **Description**: Model Context Protocol (MCP) server for Dify workflows.
- **Key Features**:
  - MCP protocol support
  - Workflow integration
  - Python implementation
- **Use Cases**: MCP integration, workflow extension

### 28. mcp-difyworkflow-server - MCP Dify Workflow Server
- **Repository**: https://github.com/gotoolkits/mcp-difyworkflow-server
- **Stars**: 59+ ⭐
- **Language**: Go
- **Description**: MCP server tools application implementing Dify workflow query and invocation, supporting on-demand operation of multiple custom workflows.
- **Key Features**:
  - Go language implementation
  - MCP server
  - Multi-workflow support
- **Use Cases**: Workflow as a service, MCP integration

### 29. dify-mcp-client - MCP Client Plugin
- **Repository**: https://github.com/3dify-project/dify-mcp-client
- **Stars**: 158+ ⭐
- **Language**: Python
- **Description**: MCP Client as Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.
- **Key Features**:
  - MCP Client implementation
  - Agent strategy plugin
  - UI-TARS-SDK integration
  - GUI operation support
- **Use Cases**: Agent development, UI automation

### 30. dify-plugin-agent-mcp_sse - MCP Tools Agent
- **Repository**: https://github.com/junjiem/dify-plugin-agent-mcp_sse
- **Stars**: 117+ ⭐
- **Language**: Python
- **Description**: Dify 1.0 plugin supporting MCP Tools Agent strategies.
- **Use Cases**: Dify plugin development, MCP tools

### 31. dify-plugin-webhook - Webhook Plugin
- **Repository**: https://github.com/perzeuss/dify-plugin-webhook
- **Stars**: 44+ ⭐
- **Language**: Python
- **Description**: Dify plugin to call Dify workflows and chatflows via webhook.
- **Use Cases**: Webhook integration, external triggering

### 32. awesome-cow-plugins - CoW and DoW Plugin Collection
- **Repository**: https://github.com/WoodGoose/awesome-cow-plugins
- **Stars**: 217+ ⭐
- **Description**: Collection of CoW (chatgpt-on-wechat) and DoW (dify-on-wechat) plugins.
- **Use Cases**: Plugin discovery, feature extension

### 33. Dify_Pipeline_OpenwebUI - OpenWebUI Pipeline
- **Repository**: https://github.com/JiangYain/Dify_Pipeline_OpenwebUI
- **Stars**: 38+ ⭐
- **Language**: Python
- **Description**: Integrates Dify into OpenWebUI through Pipeline, combining OpenWebUI's frontend advantages with Dify's workflow capabilities.
- **Use Cases**: OpenWebUI integration

---

## Development Tools & SDKs

### 34. evolution-api - WhatsApp Integration API
- **Repository**: https://github.com/EvolutionAPI/evolution-api
- **Stars**: 6,238+ ⭐
- **Language**: TypeScript
- **Description**: Open-source WhatsApp integration API supporting integration with Dify, n8n, and other platforms.
- **Key Features**:
  - WhatsApp API
  - Multi-platform integration support
  - Cloud API compatibility
  - RabbitMQ support
- **Use Cases**: WhatsApp bots, message automation

### 35. dify-client-python - Python SDK
- **Repository**: https://github.com/haoyuhu/dify-client-python
- **Stars**: 47+ ⭐
- **Language**: Python
- **Description**: Python package providing a convenient interface to interact with the Dify API.
- **Key Features**:
  - Python SDK
  - Complete API encapsulation
  - Easy-to-use interface
- **Use Cases**: Python application integration, API development

### 36. chatbot-chrome-extension - Chrome Extension
- **Repository**: https://github.com/langgenius/chatbot-chrome-extension
- **Stars**: 53+ ⭐
- **Language**: CSS, JavaScript
- **Description**: Official Dify Chrome extension.
- **Use Cases**: Browser integration, web assistant

---

## Special Use Cases

### 37. comfyui_LLM_party - ComfyUI LLM Agent Framework
- **Repository**: https://github.com/heshengtao/comfyui_LLM_party
- **Stars**: 1,994+ ⭐
- **Language**: Python
- **Description**: LLM Agent Framework in ComfyUI including MCP server, Omost, GPT-sovits, ChatTTS, and more, with graphRAG support.
- **Key Features**:
  - ComfyUI integration
  - Multiple LLM support
  - Local model support
  - GraphRAG
- **Use Cases**: AI image generation, multimodal applications

### 38. super-agent-party - 3D Desktop Companion
- **Repository**: https://github.com/heshengtao/super-agent-party
- **Stars**: 1,276+ ⭐
- **Language**: JavaScript
- **Description**: Zero-barrier 3D desktop companion supporting QQ, Bilibili live, RAG, Dify, Home Assistant, MCP, and more.
- **Key Features**:
  - 3D visualization
  - Multi-platform integration
  - Desktop pet
  - Long-term memory
- **Use Cases**: Desktop assistant, live streaming interaction

### 39. xiaozhi-android-client - Android/iOS Voice Dialogue Application
- **Repository**: https://github.com/TOM88812/xiaozhi-android-client
- **Stars**: 1,206+ ⭐
- **Language**: Dart (Flutter)
- **Description**: Android and iOS voice dialogue application based on xiaozhi and xiaozhi-server, supporting real-time voice interaction and text dialogue.
- **Key Features**:
  - Flutter cross-platform
  - Real-time voice interaction
  - Text dialogue
  - Dify integration
- **Use Cases**: Mobile voice assistant

### 40. ChatSQL - Database Learning Platform
- **Repository**: https://github.com/ffy6511/ChatSQL
- **Stars**: 51+ ⭐
- **Language**: TypeScript
- **Description**: Database system learning platform empowered by agent design and workflow orchestration.
- **Key Features**:
  - Database learning
  - Visualization
  - Agent design
  - Workflow orchestration
- **Use Cases**: Education, database learning

### 41. DifyDSL4RedTeam - Red Team Workflows
- **Repository**: https://github.com/din4e/DifyDSL4RedTeam
- **Stars**: 33+ ⭐
- **Description**: Collection of Dify workflows for red team use.
- **Use Cases**: Security testing, red team exercises

---

## Learning Recommendations

### Entry Path
1. **Start with the official platform**: Familiarize yourself with the basic features of [Dify](https://github.com/langgenius/dify)
2. **Learn workflows**: Reference templates from [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)
3. **Choose use cases**: Select relevant integration projects based on your needs

### Advanced Directions
- **Enterprise application development**: Study enterprise platforms like BuildingAI and Flock
- **IM integration**: Learn multi-platform bot frameworks like LangBot and AstrBot
- **Customer service systems**: Dive into intelligent customer service solutions like ChatGPT-On-CS
- **Infrastructure**: Understand deployment solutions like dify-google-cloud-terraform

### Recommended Practice Projects
- **Knowledge base applications**: Dify-Enterprise-WeChat-bot
- **Workflow orchestration**: Flock or Awesome-Dify-Workflow
- **Multi-channel customer service**: ChatGPT-On-CS
- **Mobile applications**: xiaozhi-android-client

---

## Tech Stack Distribution

- **TypeScript/JavaScript**: Frontend applications, full-stack platforms
- **Python**: Bots, backend services, plugins
- **Go**: High-performance services, MCP servers
- **Java**: Enterprise applications (Spring Boot)
- **Dart/Flutter**: Mobile applications

---

## Contribution & Updates

This document will be continuously updated. PRs are welcome to add more quality projects.

**Last Updated**: 2025-11-18

**Star Count Note**: All star counts are as of the document creation time and may have changed.

---

## Related Resources

- [Dify Official Documentation](https://docs.dify.ai/)
- [Dify Official Community](https://github.com/langgenius/dify/discussions)
- [Dify Plugin Marketplace](https://github.com/langgenius/dify-plugins)

---

## Disclaimer

This document is for learning and research purposes only. The use of listed projects must comply with their respective open-source licenses. Please carefully read the LICENSE file of each project before use.

When deploying and using these projects, please ensure:
- Compliance with relevant laws and regulations
- Protection of user privacy and data security
- Compliant use of LLM services
- Attention to API cost control
