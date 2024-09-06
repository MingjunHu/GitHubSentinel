# Daily Progress for langchain-ai/langchain - 2024-09-05

## Issues:
- [[Partners-HuggingFace] Breaking Change - impossible to skip login after PR #23309](26085)
- [retry_min_seconds and retry_max_seconds is not work in OpenAIEmbeddings of langchain_openai](26084)
- [ChatGoogleGenerativeAI:  **TypeError** when using @tool decorated methods to perform Tool Calling using Gimini.](26083)
- [DOC: <Issue related to /v0.2/docs/tutorials/chatbot/> How to check LangSmith trace ?](26081)
- [Add PiecesOS LLM integration](26080)
- [Neo4j example cannot use APOC procedures.](26077)
- [huggingface: fix _convert_TGI_message_to_LC_message issue, which will replace all …](26075)
- [Update FeatureTables.js to reflect Cohere's support for JSON mode](26074)
- [[Tests] Clear cache for env-var checks](26073)
- [templates: Aerospike Vector Store RAG template](26066)
- [support epsilla cloud vector database in langchain](26065)
- [core: fix "template" not allowed as prompt param](26060)
- [docs: `integrations` reference updates 16](26059)
- [Can't use mustache/jinja2 templates with an argument named "template"](26058)
- [mongo[major]: upgrade pydantic](26053)
- [BedrockLLM throws LangChainTraver.on_llm_end callback error](26049)
- [Solve #26046: Use requests with common headers rather than httpx to avoid 302 redirect error](26047)
- [`get_num_tokens_from_message` will cause 302 Redirect on specific image in message list](26046)
- [docs: small improvement ChatOllama setup description](26043)
- [fix: Problem with embeddings in new versions of clickhouse.](26041)
- [fix(community): Add support for Bedrock cross-region inference models](26038)
- [docs: update agent_executor.ipynb](26035)
- [core[minor]: Add get_input_jsonschema, get_output_jsonschema, get_config_jsonschema](26034)
- [pgvector - (psycopg.DataError) PostgreSQL text fields cannot contain NUL (0x00) bytes](26033)
- [safe_mode Parameter in ChatMistralAI Class Should Not Be Set to False by default or safe_prompt body parameter not sent to mistral api](26029)
- [ExperimentalMarkdownSyntaxTextSplitter missing in __init__](26028)
- [Python 3.13 needs Numpy > 2.0](26026)
- [DOC: <Issue related to /v0.2/docs/integrations/text_embedding/nomic/>](26022)
- [Refining Skip Count Calculation by Filtering Documents with `session_id`](26020)
- [Prevent Infinite Tool Call Loop in Customer Support Agent (LangGraph)](26019)

## Pull Requests:
- [Add PiecesOS LLM integration](26080)
- [huggingface: fix _convert_TGI_message_to_LC_message issue, which will replace all …](26075)
- [Update FeatureTables.js to reflect Cohere's support for JSON mode](26074)
- [[Tests] Clear cache for env-var checks](26073)
- [templates: Aerospike Vector Store RAG template](26066)
- [support epsilla cloud vector database in langchain](26065)
- [core: fix "template" not allowed as prompt param](26060)
- [docs: `integrations` reference updates 16](26059)
- [mongo[major]: upgrade pydantic](26053)
- [Solve #26046: Use requests with common headers rather than httpx to avoid 302 redirect error](26047)
- [docs: small improvement ChatOllama setup description](26043)
- [fix: Problem with embeddings in new versions of clickhouse.](26041)
- [fix(community): Add support for Bedrock cross-region inference models](26038)
- [docs: update agent_executor.ipynb](26035)
- [core[minor]: Add get_input_jsonschema, get_output_jsonschema, get_config_jsonschema](26034)
- [Refining Skip Count Calculation by Filtering Documents with `session_id`](26020)
- [community: add Sineps modules](26016)
- [langchain-community[major]: Upgrade community to pydantic 2](26011)
- [fix crash when using create_xml_agent with parameterless function as …](26002)
- [docs: `integrations` reference updates 15](25994)
- [infra: ignore docs build in v0.3rc branch](25990)
- [fix: HuggingFacePipeline model_id parameter](25973)
- [langchain_chroma: Pass through kwargs to Chroma collection.delete](25970)
- [community: Add reference doc for Links](25969)
- [langchain: [indexing] [feature] support for mssql backend in indexing](25966)
- [Feature/update hunyuan](25960)
- [community: Fix links in GraphVectorStore pydoc](25959)
- [community: Fix planner_prompt so api_controller defines "action"](25957)
- [Add warning when page_content is empty](25955)
- [MonsterAPI Integration](25948)

## Commits:
- [core,standard-tests[patch]: add Ser/Des test and update serialization mapping (#26042)](https://github.com/langchain-ai/langchain/commit/de97d5064437c98f34dae0b0afa3b61162790726)
- [fmt](https://github.com/langchain-ai/langchain/commit/1241a004cbcddd7794f1a6ba064e8a0ca06e1065)
- [fmt](https://github.com/langchain-ai/langchain/commit/4ba14ae9e5545c3905aded58c0435f10b77f6b02)
- [fmt](https://github.com/langchain-ai/langchain/commit/dba308447d0e18578fbcbf3adfbbeb5d8789c7fe)
- [fmt](https://github.com/langchain-ai/langchain/commit/fdf6fbde186b231a9fc0e5bfde163db882864316)
- [fmt](https://github.com/langchain-ai/langchain/commit/576574c82c21ce3019c05f627b6bf08333d255b2)
- [make](https://github.com/langchain-ai/langchain/commit/7bf54636ff75a8c1bc9899abc084927b36745126)
- [standard-tests[patch]: add Ser/Des test](https://github.com/langchain-ai/langchain/commit/3ec93c2817a03eeb178602d05f84bb41bd49bff5)
- [langchain_openai: Make sure the response from the async client in the astream method of ChatOpenAI is properly awaited in case of "include_response_headers=True" (#26031)](https://github.com/langchain-ai/langchain/commit/af11fbfbf6ae3fae9a2fd0cf6e51b4e8f38c4886)
- [Improvement[Community] Improve args description in api doc of `DocArrayInMemorySearch` (#26024)](https://github.com/langchain-ai/langchain/commit/c8122372177305c964866691a8254cb99c3809d2)
- [Add the option to ignore structured output method to LLM graph transf… (#26013)](https://github.com/langchain-ai/langchain/commit/c649b449d71efdde03a6d9b74e04029d62858c9f)
- [openai[patch]: add back azure embeddings api_version alias (#26003)](https://github.com/langchain-ai/langchain/commit/34fc00aff17d1913a1cfe4b205e732982f98f7b8)
- [openai[patch]: add back azure embeddings api_version alias](https://github.com/langchain-ai/langchain/commit/4b99426a4f8d738c59ce782ecf9eb3fac8fc3c0b)
- [openai[patch]: Upgrade @root_validators in preparation for pydantic 2 migration (#25491)](https://github.com/langchain-ai/langchain/commit/bc3b851f08ee58bba2a6ff2600a26d1e9c964f42)
- [community: delta in openai choice can be None, creates handler for that (#25954)](https://github.com/langchain-ai/langchain/commit/0207dc1431c29379b724f51c09fa49e6b0333639)
- [experimental[patch]: Release 0.0.65 (#25987)](https://github.com/langchain-ai/langchain/commit/9eb9ff52c0e0b601af5b33dc39a48b74fe7af8c3)
- [standard-tests[patch]: test init from env vars (#25983)](https://github.com/langchain-ai/langchain/commit/bc3b02651c4b77e18be30a2e7cfb9252903c15c7)
- [infra: rm ai21 from CI (#25984)](https://github.com/langchain-ai/langchain/commit/ac922105ad8a2cefd0019d54b79c4e862b2ed964)
- [community[patch]: Release 0.2.16 (#25982)](https://github.com/langchain-ai/langchain/commit/0af447c90b98092238c8c8735f19f34e681e36be)
- [community[patch]: change default Neo4j username/password (#25226)](https://github.com/langchain-ai/langchain/commit/f49da71e87f714003f144f3bc7e5beb66339d9a9)
- [milvus[patch]: Release 0.1.5 (#25981)](https://github.com/langchain-ai/langchain/commit/035d8cf51b1a7ddb3298c110361f0e142ad81c4e)
- [langchain[patch]: Release 0.2.16 (#25977)](https://github.com/langchain-ai/langchain/commit/1dfc8c01affc98446592060e62894ee36a3b9446)
- [text-splitters[patch]: Release 0.2.4 (#25979)](https://github.com/langchain-ai/langchain/commit/fb642e1e27655697ba75d362c4ab628b82e3f5a1)
- [mistralai[patch]: Release 0.1.13 (#25978)](https://github.com/langchain-ai/langchain/commit/74579496198e7715cac616bb987ae94ac6d49e5a)
- [core[patch]: Release 0.2.38 (#25974)](https://github.com/langchain-ai/langchain/commit/0c69c9fb3f1870a0dc8eb17fa0ed600dec1e22e2)
- [core[minor]: Add support for multiple env keys for secrets_from_env (#25971)](https://github.com/langchain-ai/langchain/commit/fa8402ea09856c974d4cfdea8d25ee105cb95ba6)
- [`langchain-mistralai` - make base URL possible to set via env variable for `ChatMistralAI` (#25956)](https://github.com/langchain-ai/langchain/commit/fdeaff4149ed2e4bf034ac18bfff49f613a05e6e)
- [community: sambastudio llms api v2 support (#25063)](https://github.com/langchain-ai/langchain/commit/c7154a40457b16b11fdf6c0b2f7f8c3323b62d34)
- [docs: Add missing args in api doc of `WebResearchRetriever` (#25949)](https://github.com/langchain-ai/langchain/commit/8d784db107fc3d7728c9966087d0fe5d120c6291)
- [docs: ChatOpenAI.with_structured_output nits (#25952)](https://github.com/langchain-ai/langchain/commit/da113f63630f4c37ba9271e8580da5b77cbecc83)