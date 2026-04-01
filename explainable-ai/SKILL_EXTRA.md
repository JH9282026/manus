# Additional Content

This file contains content moved from SKILL.md to keep it under 500 lines.

---

# Create partial dependence plots
features = [0, 1, (0, 1)]  # Individual and interaction
PartialDependenceDisplay.from_estimator(
    model, X_train, features,
    feature_names=feature_names
)
plt.tight_layout()
```

## Model-Specific Explanations

### Random Forest Feature Importance

```python
# Built-in feature importance
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))


## Best Practices

**Choosing Methods**: Use SHAP for comprehensive analysis, LIME for quick local explanations, attention for sequences/images
**Communication**: Tailor to audience, provide multiple explanation types, include uncertainty
**Validation**: Verify domain sense, test stability, involve experts
**Production**: Cache explanations, provide on-demand, log for audits

## Tools

- **SHAP**: Comprehensive framework
- **LIME**: Local explanations
- **InterpretML**: Microsoft toolkit
- **Captum**: PyTorch interpretability
- **Alibi**: Model inspection

## Learning Path

1. **Basics**: Feature importance, visualizations
2. **Intermediate**: SHAP, LIME, attention
3. **Advanced**: Counterfactuals, custom methods
4. **Expert**: Quality metrics, production deployment

## Using the Reference Files

- [./references/method-comparisons.md](./references/method-comparisons.md) — Comprehensive comparison of XAI methods, their strengths, weaknesses, and use cases
- [./references/case-studies.md](./references/case-studies.md) — Real-world applications of explainable AI across different domains and industries
- [./references/implementation-guides.md](./references/implementation-guides.md) — Step-by-step guides for implementing XAI techniques in production systems

---

**Note:** Additional content has been moved to `SKILL_EXTRA.md` to maintain the 500-line limit.
