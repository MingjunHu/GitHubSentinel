# Formal Daily Report

## 新增功能:
- 添加了PiecesOS LLM集成
- 在FeatureTables.js中更新以反映Cohere对JSON模式的支持
- 为Aerospike Vector Store RAG模板添加了templates
- 在langchain中支持epsilla云向量数据库
- 新增了Sineps模块
- 添加了MonsterAPI集成

## 主要改进:
- 修正了HuggingFacePipeline模型ID参数
- 修复了Chroma集合删除中的kwargs传递问题
- 在文档中更新了对Links的参考文档
- 支持在索引中使用MSSQL后端
- 更新了hunyuan功能
- 改进了GraphVectorStore pydoc中的链接

## 修复问题:
- 修复了ChatGoogleGenerativeAI中使用@tool装饰的方法在使用Gimini进行工具调用时出现的TypeError问题
- 修复了在LangGraph中客户支持代理中避免无限工具调用循环的问题
- 解决了使用请求通用标头代替httpx以避免302重定向错误的问题
- 修复了在指定消息列表中特定图像上使用`get_num_tokens_from_message`会导致302重定向的问题