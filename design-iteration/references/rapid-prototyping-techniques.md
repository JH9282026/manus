# Rapid Prototyping Techniques

## Overview

Rapid prototyping creates quick, testable representations of design concepts. The goal is to learn fast and fail cheap, validating ideas before investing in high-fidelity design or development.

---

## Fidelity Levels

**Low Fidelity**: Paper sketches, wireframes, basic clickable prototypes. Fast to create, easy to change, focuses on structure and flow.

**Medium Fidelity**: Grayscale mockups, basic interactions, placeholder content. Balances speed with enough detail to test key concepts.

**High Fidelity**: Full visual design, realistic content, complex interactions. Looks and feels like final product but still faster than development.

**Choosing Fidelity**: Match fidelity to your questions. Testing navigation flow? Low fidelity works. Testing visual hierarchy? Need medium-high fidelity. Testing micro-interactions? High fidelity required.

---

## Paper Prototyping

**Materials**: Paper, markers, scissors, tape. That's it.

**Process**: Sketch each screen on paper. Cut out interactive elements. During testing, manually swap screens and move elements to simulate interaction.

**Advantages**: Extremely fast, zero learning curve, encourages experimentation, stakeholders understand it's early-stage.

**Limitations**: Can't test complex interactions, requires facilitator to manipulate, doesn't feel realistic.

**Best For**: Early concept exploration, testing basic flows, workshop activities, getting quick stakeholder feedback.

---

## Digital Wireframing

**Tools**: Figma, Sketch, Adobe XD, Balsamiq, Whimsical.

**Approach**: Create low-fidelity screens using basic shapes and placeholder text. Link screens with simple click interactions.

**Speed Techniques**:
- Use UI kits and component libraries
- Duplicate and modify rather than creating from scratch
- Use auto-layout/constraints for responsive behavior
- Keep visual styling minimal

**When to Use**: Testing information architecture, navigation patterns, content hierarchy, basic user flows.

---

## Clickable Prototypes

**Figma Prototyping**: Connect frames with prototype links. Add interactions (click, hover, drag). Set transitions (instant, dissolve, slide). Use overlays for modals and dropdowns.

**Advanced Interactions**: Use variables and conditional logic for complex flows. Create interactive components for reusable patterns. Add smart animate for smooth transitions.

**Testing Setup**: Share prototype link with 'Present' view. Testers interact directly without seeing design tools. Collect feedback through comments or separate tool.

**Limitations**: Can't test real data, performance, or backend integration. Good for interaction patterns, not technical feasibility.

---

## Wizard of Oz Prototyping

**Concept**: Human operator simulates system responses behind the scenes. User thinks they're interacting with working system.

**Example**: Testing a voice assistant. User speaks commands, operator manually triggers appropriate responses. User doesn't know operator is involved.

**Advantages**: Test concepts before building complex functionality. Validate value proposition before technical investment.

**Requirements**: Skilled operator who can respond quickly and consistently. Clear protocol for handling edge cases. Debrief participants afterward.

**Ethics**: Disclose the technique after testing. Explain why it was necessary. Ensure participants are comfortable with the approach.

---

## Code Prototypes

**When to Code**: Testing technical feasibility, performance, or complex interactions that design tools can't simulate.

**Rapid Frameworks**: 
- HTML/CSS/JS: Fast for web prototypes, widely accessible
- React/Vue: Component-based, good for complex interactions
- Framer: Design tool with code capabilities
- CodePen/JSFiddle: Quick experiments without setup

**Keep It Rough**: Prototype code should be disposable. Don't worry about best practices, optimization, or maintainability. Focus on answering specific questions.

**Transition to Production**: If prototype validates concept, rebuild properly for production. Don't try to clean up prototype code—start fresh with proper architecture.

---
