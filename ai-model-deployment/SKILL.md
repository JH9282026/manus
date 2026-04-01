---
name: ai-model-deployment
description: "Deploy AI models to production with serving, inference optimization, and monitoring. Use for model serving (TensorFlow Serving, TorchServe, Triton), API deployment, edge deployment, quantization, and production ML systems."
---

# AI Model Deployment

Deploy AI models to production with efficient serving and monitoring.

## Overview

Model deployment makes trained models available for real-world use. This skill covers serving infrastructure, optimization, monitoring, and production best practices.

## Quick Reference

| Scenario | Recommended Approach | Reference File |
|----------|---------------------|----------------|
| Model serving and API deployment | TensorFlow Serving, TorchServe, FastAPI | `/references/serving.md` |
| Inference optimization | Quantization, pruning, distillation | `/references/optimization.md` |
| Production monitoring | Metrics, logging, drift detection | `/references/monitoring.md` |

## Core Principles

1. **Scalability** - Handle varying load efficiently
2. **Latency** - Minimize response time
3. **Reliability** - High availability and fault tolerance
4. **Monitoring** - Track performance and detect issues
5. **Cost Efficiency** - Optimize resource utilization

## Deployment Patterns

### REST API
Expose model via HTTP endpoints.

**Tools:**
- FastAPI: Modern, async Python framework
- Flask: Simple, lightweight
- TensorFlow Serving: Optimized for TF models
- TorchServe: Native PyTorch serving

**Advantages:**
- Simple integration
- Language-agnostic
- Easy to scale

### Batch Inference
Process large datasets offline.

**Use Cases:**
- Periodic predictions
- Data pipelines
- Non-real-time applications

**Tools:**
- Apache Spark
- AWS Batch
- Kubernetes Jobs

### Edge Deployment
Run models on devices (mobile, IoT).

**Requirements:**
- Model compression (quantization, pruning)
- Optimized runtimes (TFLite, ONNX Runtime)
- Limited resources

## Inference Optimization

### Quantization
Reduce precision (FP32 → INT8).

**Benefits:**
- 4x smaller models
- 2-4x faster inference
- Lower memory usage

**Methods:**
- Post-training quantization
- Quantization-aware training

### Model Pruning
Remove unnecessary weights.

**Types:**
- Unstructured: Remove individual weights
- Structured: Remove entire channels/layers

**Benefits:**
- Smaller models
- Faster inference
- Reduced memory

### Knowledge Distillation
Train smaller student model from larger teacher.

**Process:**
1. Train large teacher model
2. Generate soft labels from teacher
3. Train small student on soft labels

**Benefits:**
- Compact models
- Maintained performance
- Faster inference

## Using the Reference Files

**`/references/serving.md`** — Model serving frameworks (TensorFlow Serving, TorchServe, Triton), API design, containerization (Docker), orchestration (Kubernetes).

**`/references/optimization.md`** — Quantization techniques, model pruning, knowledge distillation, ONNX conversion, TensorRT optimization.

**`/references/monitoring.md`** — Performance metrics (latency, throughput), logging, alerting, model drift detection, A/B testing.

## Best Practices

- Containerize models with Docker
- Use model versioning
- Implement health checks
- Monitor latency and throughput
- Set up alerting for failures
- Use load balancing
- Implement caching where appropriate
- Test under realistic load
- Document API endpoints
- Plan for model updates

## Common Pitfalls to Avoid

- Not testing under production load
- Insufficient error handling
- No model versioning
- Inadequate monitoring
- Ignoring latency requirements
- Not planning for scaling
- Hardcoding configurations
- No rollback strategy
- Insufficient logging
- Not considering costs

## References

- [Monitoring](references/monitoring.md)
- [Optimization](references/optimization.md)
- [Serving](references/serving.md)
