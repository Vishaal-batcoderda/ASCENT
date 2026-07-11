![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![Groq](https://img.shields.io/badge/Groq-LLM-purple)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-UI-38BDF8)
![Status](https://img.shields.io/badge/Status-Active-success)

# 📈 ASCENT AI

> **ASCENT AI is a multi-agent stock analysis platform that combines live market data, technical indicators, financial news, and large language models to generate structured investment insights through a modular AI workflow.**

---

## Overview

Modern financial analysis rarely depends on a single source of information.

A meaningful investment decision often requires understanding the current market, interpreting technical indicators, reviewing recent news, and finally combining these observations into a coherent conclusion. While large language models are capable of producing convincing answers, asking one model to perform every task in a single prompt often results in systems that are difficult to maintain, extend, and reason about.

ASCENT AI was built to explore a different approach.

Instead of treating an LLM as the application itself, the system treats it as one component within a larger architecture. Responsibilities are divided among specialized agents, each designed to solve a well-defined problem. Market data is gathered independently, technical indicators are calculated separately, financial news is summarized through a dedicated pipeline, and only after these pieces are available does the reporting agent synthesize them into a final investment report.

The objective of this project extends beyond stock analysis. It serves as an exploration of how modern AI applications can be engineered using modular software design, workflow orchestration, and reusable components rather than relying on increasingly complex prompts.

---

## Features

ASCENT currently provides:

* Live stock market data using Yahoo Finance
* Technical analysis using SMA, EMA, RSI, MACD and Bollinger Bands
* Financial news aggregation and AI summarization
* Dynamic multi-agent execution powered by LangGraph
* AI-generated investment reports using Groq LLMs
* Interactive historical stock price visualization
* Modern glassmorphism dashboard built with React
* Modular FastAPI backend architecture

---

## Architecture

ASCENT follows a layered architecture where every component has a single responsibility.

```text
                        User
                          │
                          ▼
                  FastAPI REST API
                          │
                          ▼
                   Planner Agent
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
  Market Agent     Technical Agent     News Agent
        │                 │                 │
        └─────────────────┴─────────────────┘
                          │
                          ▼
                    Report Agent
                          │
                          ▼
                AI Investment Report
```

Unlike traditional sequential pipelines, the workflow is orchestrated through **LangGraph**, allowing execution paths to be built dynamically based on the Planner Agent's decisions.

---

## Technology Stack

### Backend

* Python
* FastAPI
* LangGraph
* Groq API
* yfinance
* Feedparser
* Pandas
* NumPy
* Pydantic

### Frontend

* React
* Vite
* Tailwind CSS
* Framer Motion
* Recharts
* Axios
* React Markdown

---

## Backend Design

The backend follows a modular service-oriented architecture.

Instead of embedding business logic inside API endpoints, responsibilities are separated into dedicated services responsible for:

* Market data retrieval
* Technical indicator computation
* News aggregation
* LLM communication
* Workflow orchestration

This separation allowed the project to evolve naturally from a simple REST API into a dynamic multi-agent platform without major rewrites.

---

## Multi-Agent Workflow

Rather than assigning every responsibility to one prompt, ASCENT distributes work among specialized agents.

### Planner Agent

Determines which agents should participate based on the user's request.

### Market Agent

Retrieves:

* Live stock information
* Historical price data

### Technical Agent

Computes:

* Simple Moving Average (SMA)
* Exponential Moving Average (EMA)
* Relative Strength Index (RSI)
* Moving Average Convergence Divergence (MACD)
* Bollinger Bands

### News Agent

Aggregates and summarizes recent financial news related to the selected company.

### Report Agent

Synthesizes structured outputs from every previous agent into a comprehensive AI-generated investment report.

Because every agent is independent, introducing new capabilities requires minimal changes to the overall architecture.

---

## Frontend Design

The frontend was intentionally developed after establishing the backend architecture.

Instead of building one large page, the interface was progressively refactored into reusable React components including:

* Market Overview Card
* Technical Indicators Card
* Interactive Price Chart
* News Summary Card
* AI Investment Report Card

The dashboard adopts a clean glassmorphism-inspired interface focused on readability, smooth interactions, and modularity.

---

## Engineering Decisions

Several architectural decisions significantly influenced the direction of ASCENT.

### Modularization Before Features

As the application grew, functionality was repeatedly extracted into dedicated services and agents before introducing additional capabilities. This prevented business logic from accumulating inside API routes and improved maintainability.

### Dynamic Workflow Construction

Rather than hardcoding execution paths, LangGraph constructs workflows dynamically according to the Planner Agent's output. This enables future agents to be integrated without redesigning the existing pipeline.

### Configurable Analysis

Technical indicators expose configurable parameters including moving-average windows and RSI periods, allowing different analysis strategies without code modifications.

### Component-Driven Frontend

The dashboard was continuously refactored into reusable React components. This reduced complexity while making future UI improvements significantly easier.

---

## What I Learned

Developing ASCENT AI provided practical experience with:

* Multi-agent AI systems
* LangGraph workflow orchestration
* LLM prompt engineering
* FastAPI backend development
* Financial data processing
* Technical analysis algorithms
* REST API design
* React component architecture
* Interactive data visualization
* Incremental software refactoring

Perhaps the most valuable lesson from this project was recognizing that maintainability often matters more than adding new functionality. Many stages of development were dedicated to improving architecture before expanding capabilities, resulting in a codebase that became progressively easier to understand and extend.

---

## Roadmap

The current implementation forms the foundation for several future improvements.

* [ ] User authentication
* [ ] Portfolio management
* [ ] Saved analysis history
* [ ] Risk Analysis Agent
* [ ] Prediction Agent
* [ ] Reflection Agent
* [ ] Streaming AI responses
* [ ] Mobile responsiveness
* [ ] Light/Dark theme
* [ ] Deployment
* [ ] User-provided Groq API key support

---

## Project Philosophy

ASCENT AI was never intended to be just another stock dashboard.

It was built as an engineering exercise to understand how modern AI applications are structured beyond prompt engineering alone.

Every major milestone focused first on architecture, then functionality, and finally user experience. That philosophy shaped every stage of the project—from modular backend services and specialized AI agents to reusable frontend components and iterative refactoring.

The result is a system that is not only capable of generating investment insights today, but is also intentionally designed to support substantially more sophisticated agents and workflows in the future.

---

## Acknowledgements

ASCENT AI is a personal engineering project created to explore the intersection of software architecture, AI engineering, and financial analysis.

While inspired by modern multi-agent systems, every architectural decision—including the modular FastAPI backend, LangGraph workflow orchestration, reusable React frontend, and iterative refactoring strategy—was implemented as part of a deliberate learning journey focused on understanding how production-oriented AI applications are designed.
