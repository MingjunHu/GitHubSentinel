# Formal Daily Report

## 新增功能:
1. 支持 epsilla 云向量数据库。
2. 添加了 `get_input_jsonschema`, `get_output_jsonschema`, `get_config_jsonschema` 核心功能。
3. 支持 Aerospike 向量存储 RAG 模板。
4. 引入 Sineps 模块。
5. 添加了 MonsterAPI 集成。
6. 在文档中更新了 ChatOllama 设置描述。

## 主要改进:
1. 修复了一些与模板名称冲突相关的问题。
2. 通过使用请求常见头部而非 httpx 避免了 302 重定向错误。
3. 更新 FeatureTables.js 以反映 Cohere 对 JSON 模式的支持。
4. 为 community 添加了对 Bedrock 跨区域推理模型的支持。
5. 更新了 agent_executor.ipynb 文档。
6. 改进了 ChatMistralAI 类中的 safe_mode 参数默认值以及 safe_prompt 参数不发送到 mistral api 的问题。

## 修复问题:
1. 修复了 Neo4j 示例无法使用 APOC 过程的问题。
2. 解决了使用特定图像在消息列表中会导致 302 重定向的问题。
3. 修正了 create_xml_agent 函数中使用无参数函数时导致崩溃的问题。
4. 修复了在新版本的 clickhouse 中嵌入的问题。

以上是项目在 2024-09-05 的最新进展简报。