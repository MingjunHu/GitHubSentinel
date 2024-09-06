# langchain-ai/langchain - 2024-09-05

## 新增功能:
- 添加 PiecesOS LLM 集成
- 在 FeatureTables.js 中更新以反映 Cohere 对 JSON 模式的支持
- 在 templates 中添加 Aerospike Vector Store RAG 模板
- 支持 epsilla 云向量数据库在 langchain 中的集成
- 在核心部分修复了不能将 "template" 作为提示参数的问题
- 为 ChatOllama 设置描述进行了小的改进
- 可以忽略结构化输出方法将 LLM 图变换中的选项添加该设置
- 添加警告当页面内容为空时

## 主要改进:
- 修复 HuggingFacePipeline model_id 参数的问题
- 更新文档中 ChatOllama 的设置描述
- 在新版本的 clickhouse 中修复嵌入的问题
- 为 Bedrock 跨地区推理模型添加支持
- 更新 agent_executor.ipynb 文档
- 添加获取输入、输出和配置 JSON 架构的功能

## 修复问题:
- 修复了在 Partnes-HuggingFace 合作中的一个问题，无法在 PR #23309 后跳过登录
- 修复了在 langchain_openai 的 OpenAIEmbeddings 中 retry_min_seconds 和 retry_max_seconds 不起作用的问题
- 修复 ChatGoogleGenerativeAI 中使用 @tool 修饰方法执行 Tool 调用时的 TypeError
- 修复了DOC中与 /v0.2/docs/tutorials/chatbot/ 相关的问题，以及如何检查 LangSmith 跟踪的问题
- 修复了 Neo4j 示例无法使用 APOC 过程的问题
- 修复了 get_num_tokens_from_message 在消息列表中特定图像上会导致 302 重定向的问题
- 修复在 community 中使用 create_xml_agent 且参数为空的函数时崩溃的问题
- 修复在 ChatMistralAI 类中 safe_mode 参数默认设置为 False 或 safe_prompt 体参数未发送到 mistral api 的问题
- 修复在 Python 3.13 需要 Numpy > 2.0 的问题
- 修复了关于 /v0.2/docs/integrations/text_embedding/nomic/ 相关的问题
- 通过使用 session_id 过滤文档来优化跳过计数计算
- 防止客服支持代理 (LangGraph) 中出现无限工具调用循环的问题