# Integration Patterns

Detailed reference content for tool-intelligence-router.

---

## Appendix B: Natural Language Processing Patterns

### Intent Classification Patterns

| User Phrase Pattern | Classified Intent | Primary Tool Categories |
|---------------------|-------------------|------------------------|
| "get/fetch/retrieve/download X" | DATA_RETRIEVAL | Storage, API, Web Scraping |
| "analyze/examine/inspect X" | DATA_ANALYSIS | Analytics, Statistics, ML |
| "create/generate/make X" | DATA_CREATION | Generators, Templates, AI |
| "send/notify/alert about X" | COMMUNICATION | Email, Messaging, Notifications |
| "convert/transform X to Y" | DATA_TRANSFORMATION | Converters, Formatters |
| "schedule/automate X" | AUTOMATION | Schedulers, Workflows |
| "delete/remove/clear X" | DATA_DELETION | Storage, Database, Cleanup |
| "update/modify/change X" | DATA_MODIFICATION | CRUD, Editors, APIs |

### Entity Extraction Patterns

```python
# Common entity patterns for parameter extraction
ENTITY_PATTERNS = {
    "file_path": r"[/\\][\w\-./\\]+\.\w+",
    "url": r"https?://[^\s]+",
    "email": r"[\w.-]+@[\w.-]+\.\w+",
    "date": r"\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{2,4}",
    "number": r"\d+(?:\.\d+)?",
    "json_object": r"\{[^}]+\}",
    "quoted_string": r'"[^"]+"|\'[^\']+\'",
}
```

### Synonym Expansion Dictionary

```yaml
action_synonyms:
  retrieve: [get, fetch, download, pull, obtain, acquire]
  analyze: [examine, inspect, evaluate, assess, review, study]
  create: [generate, make, produce, build, construct, compose]
  send: [transmit, dispatch, deliver, forward, post]
  convert: [transform, change, translate, map, format]
  delete: [remove, erase, clear, purge, destroy]

object_synonyms:
  file: [document, attachment, asset, resource]
  data: [information, records, content, payload]
  message: [notification, alert, communication, note]
  report: [summary, analysis, document, output]
```

---

---

## Appendix C: Error Handling Matrix

### Error Classification and Recovery Actions

| Error Type | Detection Pattern | Recovery Strategy | Escalation |
|------------|-------------------|-------------------|------------|
| **Authentication** | 401, 403, "unauthorized" | Refresh credentials, try fallback | Request new credentials |
| **Rate Limit** | 429, "too many requests" | Exponential backoff, switch tool | Queue for later |
| **Timeout** | Connection timeout | Retry with longer timeout, switch tool | Report service issue |
| **Invalid Input** | 400, validation errors | Fix parameters, request clarification | Cannot proceed |
| **Not Found** | 404, "not found" | Verify resource, try alternative | Resource unavailable |
| **Server Error** | 500, 502, 503 | Retry, switch to fallback | Service degradation |
| **Network** | Connection refused | Check connectivity, retry | Infrastructure issue |

### Retry Configuration by Error Type

```json
{
  "retry_policies": {
    "transient_errors": {
      "max_retries": 3,
      "base_delay_ms": 1000,
      "max_delay_ms": 30000,
      "backoff_multiplier": 2.0,
      "jitter": true
    },
    "rate_limit_errors": {
      "max_retries": 5,
      "base_delay_ms": 5000,
      "respect_retry_after_header": true
    },
    "authentication_errors": {
      "max_retries": 1,
      "action": "refresh_credentials_then_retry"
    }
  }
}
```

---

---

## Appendix E: Integration Patterns

### MCP Server Connection Pattern

```python
async def connect_mcp_server(config: MCPServerConfig) -> MCPConnection:
    """Establish connection to MCP server with health checking."""
    connection = await mcp_client.connect(
        url=config.server_url,
        auth=config.auth_credentials,
        timeout=config.timeout_ms
    )
    
    # Verify connection with health check
    health = await connection.health_check()
    if not health.is_healthy:
        raise MCPConnectionError(f"Server unhealthy: {health.reason}")
    
    # Discover and index available tools
    tools = await connection.list_tools()
    for tool in tools:
        await index_tool(tool, source="mcp", source_id=config.server_url)
    
    return connection
```

### OpenAPI Specification Parsing Pattern

```python
def parse_openapi_spec(spec: OpenAPISpec) -> List[ToolDefinition]:
    """Parse OpenAPI specification into tool definitions."""
    tools = []
    
    for path, operations in spec.paths.items():
        for method, operation in operations.items():
            tool = ToolDefinition(
                id=f"{spec.info.title}_{operation.operationId}",
                name=operation.summary or operation.operationId,
                description=operation.description,
                category=extract_category(operation.tags),
                parameters=parse_parameters(operation.parameters),
                request_body=parse_request_body(operation.requestBody),
                responses=parse_responses(operation.responses),
                auth_required=has_security(operation, spec),
                source="openapi",
                source_id=spec.info.title
            )
            tools.append(tool)
    
    return tools
```

### Tool Execution Wrapper Pattern

```python
async def execute_with_routing(
    user_request: str,
    context: ExecutionContext
) -> ExecutionResult:
    """Main entry point for tool-routed execution."""
    
    # Step 1: Analyze intent
    intent = await analyze_intent(user_request, context)
    
    # Step 2: Select optimal tool(s)
    selection = await select_tools(intent, context)
    
    # Step 3: Handle ambiguity if needed
    if selection.status == "ambiguous":
        return await request_clarification(selection)
    
    # Step 4: Execute with error handling
    try:
        result = await execute_plan(selection.execution_plan)
    except ToolExecutionError as e:
        # Attempt fallback
        if selection.fallback_available:
            result = await execute_fallback(selection, e)
        else:
            raise
    
    # Step 5: Record for learning
    await record_execution(selection, result)
    
    return result
```

This comprehensive skill provides the foundation for intelligent, adaptive tool selection in complex agentic AI systems, enabling autonomous operation across diverse tool ecosystems while maintaining reliability, performance, and user satisfaction.