---
name: tool-intelligence-router
description: The Tool Intelligence Router is a foundational meta-skill that serves as the cognitive decision-making layer for tool selection in agentic AI workflows.
---

---
name: Tool Intelligence Router
description: A sophisticated meta-skill that enables intelligent selection of optimal tools from extensive MCP servers and API tool catalogs through semantic analysis, multi-criteria evaluation, and adaptive learning for autonomous task execution.
---

# Tool Intelligence Router

## 1. Skill Description and Purpose

### Overview

The Tool Intelligence Router is a foundational meta-skill that serves as the cognitive decision-making layer for tool selection in agentic AI workflows. When an AI agent has access to hundreds or thousands of tools across multiple MCP servers, API endpoints, and integrated services, this skill provides the intelligence to rapidly identify, evaluate, and select the optimal tool(s) for any given task.

### Core Value Proposition

Modern AI agents operate in environments with extensive tool ecosystems—MCP servers exposing dozens of tools each, OpenAPI specifications with hundreds of endpoints, and custom integrations spanning communication, data processing, automation, and domain-specific operations. Without intelligent routing, agents face decision paralysis, suboptimal tool selection, or excessive token consumption scanning through tool lists.

This skill solves these challenges by implementing:

- **Semantic Understanding**: Deeply parsing user intent to understand not just what is requested, but the underlying goal, constraints, and success criteria
- **Intelligent Discovery**: Efficiently cataloging and indexing tools from heterogeneous sources (MCP, REST, GraphQL, SOAP) with rich metadata extraction
- **Multi-Criteria Evaluation**: Scoring tools across capability match, input/output compatibility, performance, cost, and reliability dimensions
- **Adaptive Learning**: Continuously improving selection accuracy based on execution outcomes and user feedback
- **Multi-Tool Orchestration**: Composing complex workflows when single tools are insufficient

### When to Apply This Skill

Invoke the Tool Intelligence Router when:

1. **Large Tool Inventory**: The agent has access to 50+ tools and needs to quickly identify relevant candidates
2. **Ambiguous Requests**: User intent maps to multiple potential tools with overlapping capabilities
3. **Complex Tasks**: Requirements span multiple domains or require tool composition
4. **New Tool Discovery**: Recently added tools need integration into the selection logic
5. **Performance Optimization**: Current tool selections are suboptimal in terms of speed, cost, or reliability
6. **Error Recovery**: Primary tool selection failed and alternatives must be identified

### Architectural Position

The Tool Intelligence Router operates as a pre-execution layer in the agent workflow:

```
User Request → Intent Analysis → Tool Intelligence Router → Tool Execution → Response
                                        ↓
                               [Tool Inventory]
                               [Selection Logic]
                               [Learning System]
```

It maintains persistent state for tool metadata, usage statistics, and learned preferences, enabling increasingly accurate selections over time.

---

## 2. Required Inputs/Parameters

### Primary Input: User Request Context

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_request` | string | Yes | Raw natural language request from the user |
| `conversation_history` | array[Message] | No | Previous conversation turns for context extraction |
| `current_workflow_state` | object | No | State from ongoing multi-step workflows |
| `user_preferences` | object | No | Stored preferences for tool selection |
| `environment_constraints` | object | No | System limitations, permissions, resources |

### Tool Inventory Configuration

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `mcp_servers` | array[MCPServerConfig] | No | List of MCP server connections |
| `openapi_specs` | array[OpenAPISpec] | No | OpenAPI/Swagger specifications to parse |
| `graphql_endpoints` | array[GraphQLEndpoint] | No | GraphQL schemas for introspection |
| `tool_catalog` | ToolCatalog | No | Pre-built searchable tool inventory |
| `tool_embeddings` | EmbeddingIndex | No | Vector embeddings for semantic search |

**MCPServerConfig Schema:**
```json
{
  "server_url": "string (required)",
  "auth_method": "none | api_key | oauth | bearer",
  "auth_credentials": "object",
  "timeout_ms": "integer (default: 30000)",
  "health_check_interval_ms": "integer (default: 60000)",
  "max_retries": "integer (default: 3)"
}
```

**OpenAPISpec Schema:**
```json
{
  "spec_url": "string (URL or file path)",
  "base_url": "string (API base URL)",
  "auth_config": "object",
  "version_preference": "latest | specific",
  "specific_version": "string (optional)"
}
```

### Selection Configuration

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `selection_strategy` | enum | No | "balanced" | Strategy: "speed", "accuracy", "cost_optimized", "balanced" |
| `max_candidates` | integer | No | 5 | Maximum tools to evaluate in detail |
| `confidence_threshold` | float | No | 0.75 | Minimum confidence for auto-selection (0.0-1.0) |
| `allow_multi_tool` | boolean | No | true | Enable multi-tool composition |
| `fallback_enabled` | boolean | No | true | Enable automatic fallback on failure |
| `scoring_weights` | ScoringWeights | No | default | Custom weights for evaluation criteria |

**ScoringWeights Schema:**
```json
{
  "capability_match": 0.35,
  "io_compatibility": 0.25,
  "performance": 0.15,
  "cost": 0.15,
  "reliability": 0.10
}
```

### Context Extraction Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `domain_hints` | array[string] | Domain context hints (e.g., "finance", "healthcare") |
| `time_constraints` | TimeConstraints | Deadline and urgency indicators |
| `budget_constraints` | BudgetConstraints | Cost limits and credit budgets |
| `data_sensitivity` | enum | "public", "internal", "confidential", "restricted" |
| `compliance_requirements` | array[string] | Required compliance (GDPR, HIPAA, PCI-DSS) |

---

## 3. Expected Outputs/Deliverables

### Primary Output: Tool Selection Result

The router produces a structured selection result containing the chosen tool(s), confidence scores, and execution plan.

**ToolSelectionResult Schema:**
```json
{
  "selection_id": "uuid",
  "timestamp": "ISO8601 datetime",
  "status": "selected | ambiguous | no_match | error",
  "selected_tools": [
    {
      "tool_id": "string",
      "tool_name": "string",
      "source": "mcp | openapi | graphql | custom",
      "source_identifier": "string (server URL or spec name)",
      "confidence_score": 0.92,
      "capability_score": 0.95,
      "compatibility_score": 0.88,
      "performance_score": 0.90,
      "cost_score": 0.85,
      "reliability_score": 0.94,
      "selection_rationale": "string explaining why selected",
      "parameter_mapping": {
        "param_name": {
          "value": "extracted or inferred value",
          "source": "user_request | context | default | requires_input",
          "confidence": 0.95
        }
      },
      "estimated_execution_time_ms": 1500,
      "estimated_cost_credits": 0.02
    }
  ],
  "execution_plan": {
    "type": "single | sequential | parallel | conditional",
    "steps": [
      {
        "step_id": 1,
        "tool_id": "tool_a",
        "depends_on": [],
        "input_mapping": {},
        "output_capture": ["result_field"]
      }
    ],
    "data_transformations": [],
    "error_handling": {
      "retry_policy": {},
      "fallback_tools": []
    }
  },
  "alternatives": [
    {
      "tool_id": "string",
      "confidence_score": 0.78,
      "reason_not_selected": "Lower capability match for file format X"
    }
  ],
  "clarification_needed": {
    "required": false,
    "questions": [],
    "options": []
  },
  "metadata": {
    "tools_scanned": 247,
    "candidates_evaluated": 5,
    "selection_time_ms": 145,
    "cache_hit": true
  }
}
```

### Ambiguous Selection Output

When confidence is below threshold, the router produces options for user clarification:

```json
{
  "status": "ambiguous",
  "clarification_needed": {
    "required": true,
    "message": "Multiple tools match your request. Please clarify:",
    "questions": [
      "Are you working with CSV or JSON formatted data?",
      "Do you need real-time streaming or batch processing?"
    ],
    "options": [
      {
        "tool_id": "data_processor_csv",
        "confidence": 0.72,
        "best_for": "CSV files under 100MB with structured columns",
        "limitations": "No JSON support, synchronous only"
      },
      {
        "tool_id": "data_processor_universal",
        "confidence": 0.69,
        "best_for": "Multiple formats, streaming support",
        "limitations": "Higher latency, costs 2x credits"
      }
    ]
  }
}
```

### Multi-Tool Orchestration Plan

For complex tasks requiring tool composition:

```json
{
  "execution_plan": {
    "type": "sequential",
    "total_estimated_time_ms": 4500,
    "total_estimated_cost_credits": 0.08,
    "steps": [
      {
        "step_id": 1,
        "tool_id": "web_scraper",
        "action": "Extract product data from URL",
        "depends_on": [],
        "input_mapping": {
          "url": "${user_request.extracted_url}"
        },
        "output_capture": ["raw_html", "extracted_data"]
      },
      {
        "step_id": 2,
        "tool_id": "data_transformer",
        "action": "Convert to structured JSON",
        "depends_on": [1],
        "input_mapping": {
          "input_data": "${step_1.extracted_data}",
          "output_format": "json"
        },
        "output_capture": ["transformed_data"]
      },
      {
        "step_id": 3,
        "tool_id": "database_writer",
        "action": "Store in database",
        "depends_on": [2],
        "input_mapping": {
          "data": "${step_2.transformed_data}",
          "table": "products"
        },
        "output_capture": ["insert_id", "row_count"]
      }
    ],
    "error_handling": {
      "step_1_failure": {
        "action": "fallback",
        "fallback_tool": "alternative_scraper",
        "max_retries": 2
      },
      "step_3_failure": {
        "action": "queue_retry",
        "delay_ms": 5000
      }
    }
  }
}
```

### Learning Feedback Output

After execution, the router expects feedback to update its models:

```json
{
  "selection_id": "uuid",
  "execution_result": {
    "success": true,
    "execution_time_ms": 1420,
    "actual_cost_credits": 0.019,
    "error_code": null,
    "user_satisfaction": "positive | neutral | negative",
    "output_quality_score": 0.92
  }
}
```

---

## 4. Example Use Cases

### Use Case 1: Selecting from 100+ Data Processing Tools

**Scenario**: User requests "Analyze the sales data in my CSV file and create a summary report with trends."

**Router Process**:

1. **Intent Extraction**:
   - Action: analyze, summarize, identify trends
   - Object: sales data, CSV file
   - Output: summary report

2. **Category Filtering**:
   - Primary: Data Analysis
   - Secondary: File Processing, Reporting

3. **Candidate Identification** (from 247 available tools):
   - `pandas_analyzer` (score: 0.91)
   - `excel_processor` (score: 0.84)
   - `data_studio_tool` (score: 0.82)
   - `sql_analytics` (score: 0.76)
   - `r_statistics` (score: 0.71)

4. **Multi-Criteria Evaluation** for top candidate:
   ```
   pandas_analyzer:
   - Capability Match: 0.95 (full CSV support, trend analysis, summaries)
   - I/O Compatibility: 0.92 (CSV input, JSON/HTML/PDF output)
   - Performance: 0.88 (handles files up to 500MB efficiently)
   - Cost: 0.90 (low credit consumption)
   - Reliability: 0.91 (99.2% success rate)
   
   Weighted Score: 0.91
   ```

5. **Selection Decision**:
   - Confidence: 0.91 > threshold (0.75)
   - Auto-select: `pandas_analyzer`
   - Parameter mapping: `file_path` from context, `output_format` defaulted to "html"

### Use Case 2: Multi-Tool Orchestration for Complex Workflow

**Scenario**: "Download the quarterly report PDF from our SharePoint, extract the financial tables, convert to Excel, and email to the finance team."

**Router Process**:

1. **Task Decomposition**:
   - Subtask 1: Download PDF from SharePoint
   - Subtask 2: Extract tables from PDF
   - Subtask 3: Convert to Excel format
   - Subtask 4: Send email with attachment

2. **Tool Mapping per Subtask**:
   ```
   Subtask 1 → sharepoint_file_downloader (confidence: 0.94)
   Subtask 2 → pdf_table_extractor (confidence: 0.89)
   Subtask 3 → data_to_excel_converter (confidence: 0.92)
   Subtask 4 → email_sender (confidence: 0.96)
   ```

3. **Execution Plan Generation**:
   ```
   Step 1: sharepoint_file_downloader
           Input: {site_url, file_path} from context
           Output: downloaded_file_path
   
   Step 2: pdf_table_extractor (depends_on: Step 1)
           Input: pdf_path = ${step_1.downloaded_file_path}
           Output: extracted_tables[]
   
   Step 3: data_to_excel_converter (depends_on: Step 2)
           Input: data = ${step_2.extracted_tables}
           Output: excel_file_path
   
   Step 4: email_sender (depends_on: Step 3)
           Input: 
             - attachment = ${step_3.excel_file_path}
             - recipients = "finance-team@company.com"
             - subject = "Quarterly Report - Financial Tables"
           Output: send_confirmation
   ```

4. **Error Handling Configuration**:
   - Step 1 fallback: `onedrive_downloader` (if SharePoint fails)
   - Step 2 fallback: `ocr_table_extractor` (for scanned PDFs)
   - Step 4 retry: 3 attempts with exponential backoff

### Use Case 3: Handling Ambiguous Tool Selection

**Scenario**: "Send a notification about the server outage."

**Router Process**:

1. **Intent Analysis**:
   - Action: send notification
   - Subject: server outage
   - Ambiguity: No channel specified (email? Slack? SMS? PagerDuty?)

2. **Candidate Tools**:
   - `slack_notifier` (confidence: 0.68)
   - `email_sender` (confidence: 0.65)
   - `pagerduty_alert` (confidence: 0.63)
   - `sms_sender` (confidence: 0.58)
   - `teams_messenger` (confidence: 0.55)

3. **Confidence Assessment**:
   - Highest confidence: 0.68 < threshold (0.75)
   - Decision: Request clarification

4. **Clarification Response**:
   ```json
   {
     "status": "ambiguous",
     "clarification_needed": {
       "required": true,
       "message": "Multiple notification channels available. Which would you prefer?",
       "options": [
         {
           "tool": "slack_notifier",
           "description": "Send to Slack channel #incidents",
           "best_for": "Team-wide visibility, threaded discussions"
         },
         {
           "tool": "pagerduty_alert",
           "description": "Trigger PagerDuty incident",
           "best_for": "On-call escalation, incident management"
         },
         {
           "tool": "email_sender",
           "description": "Email to operations team",
           "best_for": "Formal documentation, external stakeholders"
         }
       ]
     }
   }
   ```

### Use Case 4: Learning from Usage Patterns

**Scenario**: Over 50 interactions, the router observes:
- User always prefers `fast_image_processor` over `quality_image_processor`
- User's data analysis requests consistently involve financial data
- Tool `legacy_api_caller` has 40% failure rate for this user

**Router Adaptations**:

1. **Preference Learning**:
   ```json
   {
     "user_preferences_learned": {
       "image_processing": {
         "preferred_tool": "fast_image_processor",
         "reason": "Selected 12/12 times when both viable"
       },
       "data_analysis": {
         "domain_context": "finance",
         "boost_tools": ["financial_analyzer", "accounting_report_gen"]
       }
     }
   }
   ```

2. **Reliability Adjustments**:
   ```json
   {
     "tool_reliability_updates": {
       "legacy_api_caller": {
         "previous_score": 0.85,
         "updated_score": 0.51,
         "reason": "40% failure rate in last 50 calls",
         "action": "Deprioritize, suggest migration to new_api_caller"
       }
     }
   }
   ```

3. **Proactive Recommendations**:
   - When user requests image processing: Auto-boost `fast_image_processor` by +0.15
   - When data analysis detected: Add financial domain context to matching
   - When `legacy_api_caller` would be selected: Suggest `new_api_caller` with migration note

### Use Case 5: Error Recovery with Automatic Fallback

**Scenario**: Primary tool `aws_s3_uploader` fails with authentication error during file upload workflow.

**Router Recovery Process**:

1. **Error Detection**:
   ```json
   {
     "tool_id": "aws_s3_uploader",
     "error_type": "authentication_error",
     "error_code": "InvalidAccessKeyId",
     "recoverable": true
   }
   ```

2. **Fallback Selection**:
   - Query fallback registry for `aws_s3_uploader`
   - Candidates: `gcp_storage_uploader`, `azure_blob_uploader`, `generic_http_uploader`
   - Evaluate compatibility with original parameters

3. **Automatic Failover**:
   ```json
   {
     "fallback_selection": {
       "original_tool": "aws_s3_uploader",
       "fallback_tool": "gcp_storage_uploader",
       "confidence": 0.87,
       "parameter_remapping": {
         "bucket": "gcp_bucket_name",
         "key": "object_path",
         "file_path": "local_file_path"
       },
       "user_notification": "AWS S3 upload failed due to authentication. Automatically switched to GCP Storage."
     }
   }
   ```

4. **Learning Update**:
   - Log authentication failure for `aws_s3_uploader`
   - Flag for credential refresh check
   - Update reliability score temporarily

---

## 5. Prerequisites and Dependencies

### Required Infrastructure

| Component | Purpose | Minimum Requirements |
|-----------|---------|---------------------|
| **Vector Database** | Semantic search over tool embeddings | Pinecone, Weaviate, Qdrant, or ChromaDB instance |
| **Tool Catalog Store** | Persistent tool metadata storage | PostgreSQL, MongoDB, or Redis with persistence |
| **Embedding Model** | Generate tool description embeddings | Sentence-BERT, OpenAI Ada-002, or Cohere Embed |
| **Cache Layer** | Performance optimization | Redis or in-memory cache for frequent lookups |

### MCP Server Requirements

- MCP protocol version 1.0+ support
- Valid authentication credentials for each server
- Network connectivity to all MCP endpoints
- Timeout configuration (recommended: 30s default, 120s max)

### API Specification Requirements

- OpenAPI 3.0+ specifications in JSON or YAML format
- Valid base URLs and authentication configurations
- Rate limit awareness and quota tracking capability

### Embedding and Search Dependencies

```python
# Required Python packages
sentence-transformers>=2.2.0    # For generating embeddings
faiss-cpu>=1.7.0               # For vector similarity search
numpy>=1.21.0                   # Numerical operations
pydantic>=2.0.0                 # Schema validation
httpx>=0.24.0                   # Async HTTP client for MCP/API calls
jsonschema>=4.0.0               # JSON Schema validation
pyyaml>=6.0                     # YAML parsing for OpenAPI specs
```

### Knowledge Requirements

The router requires pre-indexed knowledge of:

1. **Tool Taxonomy**: Hierarchical category structure for tool classification
2. **Action Verb Mappings**: Synonym dictionaries for intent matching
3. **Domain Ontologies**: Industry-specific terminology mappings
4. **Parameter Type Mappings**: Common parameter patterns and transformations

### Authentication and Permissions

| Access Type | Required For |
|-------------|--------------|
| MCP Server Credentials | Tool discovery and execution on MCP servers |
| API Keys | REST/GraphQL API tool execution |
| OAuth Tokens | User-context-aware tool access |
| Database Credentials | Tool catalog and metrics persistence |

### Performance Considerations

- **Cold Start**: Initial tool catalog indexing may take 30-60 seconds for 500+ tools
- **Embedding Generation**: ~50ms per tool description for embedding
- **Similarity Search**: <10ms for top-K retrieval with proper indexing
- **Full Selection Cycle**: Target <200ms for complete tool selection

### Monitoring and Observability

Required instrumentation:

- Selection latency metrics
- Tool success/failure rates
- Confidence score distributions
- Cache hit ratios
- Fallback activation frequency

### Initialization Checklist

Before first use, ensure:

- [ ] All MCP servers are reachable and authenticated
- [ ] OpenAPI specs are parsed and indexed
- [ ] Tool embeddings are generated and stored
- [ ] Vector search index is built
- [ ] Category taxonomy is loaded
- [ ] Synonym dictionaries are configured
- [ ] Default scoring weights are set
- [ ] Fallback tool mappings are defined
- [ ] Monitoring dashboards are configured

---

## Appendix: Selection Algorithm Reference

### Core Ranking Formula

```
TotalScore = (w_cap × CapabilityScore) + 
             (w_io × IOCompatibilityScore) + 
             (w_perf × PerformanceScore) + 
             (w_cost × CostScore) + 
             (w_rel × ReliabilityScore)

Where default weights:
  w_cap = 0.35, w_io = 0.25, w_perf = 0.15, w_cost = 0.15, w_rel = 0.10
```

### Semantic Similarity Calculation

```python
def calculate_semantic_similarity(user_intent: str, tool_description: str) -> float:
    intent_embedding = embedding_model.encode(user_intent)
    tool_embedding = embedding_model.encode(tool_description)
    similarity = cosine_similarity(intent_embedding, tool_embedding)
    return float(similarity)
```

### Confidence Threshold Decision Tree

```
IF confidence >= 0.85:
    → Auto-select, execute immediately
ELIF confidence >= 0.75:
    → Auto-select, notify user of selection
ELIF confidence >= 0.50:
    → Present top 3 options with explanations
ELSE:
    → Request clarification, cannot proceed
```

### Multi-Tool Composition Rules

1. **Sequential**: Use when output of tool A is input to tool B
2. **Parallel**: Use when tools are independent and can execute concurrently
3. **Conditional**: Use when tool B should only execute if tool A succeeds/fails
4. **Loop**: Use when tool should repeat until condition is met

This skill enables sophisticated, context-aware tool selection that improves with usage, handles complexity gracefully, and ensures optimal tool utilization across extensive tool ecosystems.

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

## Appendix D: Performance Benchmarks

### Expected Latency Targets

| Operation | Target Latency | Maximum Acceptable |
|-----------|---------------|-------------------|
| Intent extraction | <20ms | 50ms |
| Category filtering | <10ms | 30ms |
| Semantic similarity search | <30ms | 100ms |
| Multi-criteria scoring (5 tools) | <50ms | 150ms |
| Parameter mapping | <15ms | 50ms |
| Total selection cycle | <150ms | 400ms |

### Scalability Guidelines

| Tool Inventory Size | Indexing Strategy | Expected Selection Time |
|--------------------|-------------------|------------------------|
| <100 tools | In-memory linear scan | <50ms |
| 100-500 tools | In-memory vector index | <100ms |
| 500-2000 tools | Approximate NN (HNSW) | <150ms |
| 2000+ tools | Distributed vector DB | <200ms |

### Cache Configuration Recommendations

```json
{
  "cache_settings": {
    "tool_metadata_ttl_hours": 24,
    "embedding_cache_ttl_hours": 168,
    "selection_result_ttl_minutes": 5,
    "user_preference_cache_ttl_hours": 1,
    "max_cache_size_mb": 512
  }
}
```

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
