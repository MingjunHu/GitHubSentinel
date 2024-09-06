## 新增功能：
- PiecesOS LLM 集成 #26080
- Aerospike Vector Store RAG 模板 #26066
- 支持 epsilla 云向量数据库在 langchain 中的使用 #26065
- 在索引中支持 mssql 后端 #25966
- MonsterAPI 集成 #25948

## 主要改进：
- huggingface: 修复 _convert_TGI_message_to_LC_message 问题，该问题将替换所有 … #26075
- 更新 FeatureTables.js 以反映 Cohere 对 JSON 模式的支持 #26074
- 解决使用 requests 和 common headers 而非 httpx 导致 302 重定向错误的问题 #26047
- 完善通过过滤带有 `session_id` 的文档进行跳过计数计算 #26020
- 在社区中添加 Sineps 模块 #26016

## 修复问题：
- 修复 ChatGoogleGenerativeAI 使用 @tool 装饰方法执行 Tool Calling 时出现的 **TypeError** 问题 #26083
- 修复 Neo4j 示例无法使用 APOC 过程的问题 #26077
- 修复 Embeddings 在新版本 ClickHouse 中出现问题的问题 #26041
- 修复在使用参数名为 "template" 的 mustache/jinja2 模板时出现的问题 #26058
- 修复 `get_num_tokens_from_message` 在特定图像中会导致 302 重定向的问题 #26046