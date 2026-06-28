# 🐍 Python-Learning

A comprehensive Python learning repository showcasing **core concepts, data structures, AI agents, web frameworks, and real-world projects**. This repository serves as both a learning resource and a portfolio of Python skills spanning beginner to advanced topics.

**License:** MIT  
**Language:** Python 100%  
**Status:** Active (106+ commits)

---

## 📚 Repository Overview

This repository is a **structured learning journey** organized into daily modules and specialized topic folders, covering:

- ✅ **Fundamentals** (Days 1–15): Core Python concepts built progressively
- ✅ **Data Structures & Algorithms** (PYTHON_DSA): DSA implementations and practice
- ✅ **AI & ML Agents**: NVIDIA NIM, FastAPI, LangChain, and Generative AI integrations
- ✅ **Advanced Topics**: Decorators, Regular Expressions, OOP, Automation
- ✅ **Web & APIs**: FastAPI frameworks and API integrations
- ✅ **Containerization**: Docker and deployment workflows

---

## 📁 Directory Structure

| Folder | Purpose |
|--------|---------|
| **Day1–Day15** | Sequential daily Python lessons (fundamentals → intermediate) |
| **PYTHON_DSA** | Data structures and algorithms implementations |
| **py_classes** | Object-oriented programming (OOP) deep dives |
| **pythondecorator** | Decorator patterns and advanced function techniques |
| **py_regex** | Regular expression patterns and matching |
| **numpy_tuto** | NumPy array operations and numerical computing |
| **Nvidia_agent** | NVIDIA NIM API integration for AI agents |
| **FastAPI** | FastAPI web framework and REST API development |
| **python-langchain** | LangChain integrations for LLM workflows |
| **python-genai** | Generative AI implementations and experiments |
| **Skills_Agent** | Advanced AI agent with custom skills |
| **Facebook_Agent** | Social media data agent implementation |
| **automationboringstuff** | Automation scripts for repetitive tasks |
| **container** | Docker containerization and deployment |
| **demo** | Demo scripts and proof-of-concept code |
| **misc** | Miscellaneous utilities and experiments |

---

## 🎯 Learning Path

### Phase 1: Fundamentals (Day 1–15)
Start here if you're **new to Python**:
- Basic syntax, variables, and data types
- Control flow (loops, conditionals)
- Functions and scope
- File I/O and error handling
- Introduction to OOP

**Location:** `Day1/`, `Day2/`, ..., `Day15/`

### Phase 2: Core Concepts
Deepen your understanding:
- **OOP & Classes** → `py_classes/`
- **Data Structures & Algorithms** → `PYTHON_DSA/`
- **Decorators & Functional Programming** → `pythondecorator/`
- **Regular Expressions** → `py_regex/`
- **NumPy & Data Science** → `numpy_tuto/`

### Phase 3: Advanced & Real-World
Apply your skills to production-ready projects:
- **AI/ML Agents** → `Nvidia_agent/`, `Skills_Agent/`, `Facebook_Agent/`
- **Web APIs** → `FastAPI/`, `python-langchain/`
- **Generative AI** → `python-genai/`
- **Automation** → `automationboringstuff/`
- **Deployment** → `container/`

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** installed
- **Git** for cloning the repository
- Optional: **Docker** for running containers

### Clone the Repository
```bash
git clone https://github.com/guppi4u/Python-Learning.git
cd Python-Learning
```

### Install Dependencies
For specific projects, check their individual folders for `requirements.txt`:

```bash
# Example: For FastAPI project
cd FastAPI
pip install -r requirements.txt
```

### Run Your First Script
```bash
# Example: Run a Day 1 script
cd Day1
python hello_world.py
```

---

## 🤖 Key Projects Highlight

### 1. **NVIDIA NIM AI Agent**
Production-ready agent using NVIDIA NIM APIs with tool integration.

**Location:** `Nvidia_agent/`

Features:
- OpenAI SDK integration with NVIDIA NIM
- Custom tool definitions (read/write notes, search, export)
- Persistent conversation history
- Interactive session management

**Setup:**
```bash
cd Nvidia_agent
export MY_NVIDIA_KEY="your_api_key_here"
python agent.py
```

### 2. **FastAPI Web Framework**
RESTful API development with FastAPI.

**Location:** `FastAPI/`

Features:
- Route definitions and request handling
- Data validation with Pydantic models
- Interactive API documentation (Swagger UI)
- Deployment-ready structure

### 3. **LangChain Integrations**
LLM workflows using LangChain framework.

**Location:** `python-langchain/`

Features:
- Chain-of-thought prompting
- Memory management
- Tool integration with LLMs
- Retrieval-augmented generation (RAG) patterns

### 4. **Generative AI Experiments**
Cutting-edge generative AI implementations.

**Location:** `python-genai/`

### 5. **Data Structures & Algorithms**
Comprehensive DSA implementations for interviews and competitive programming.

**Location:** `PYTHON_DSA/`

---

## 📖 Learning Resources

### Inside This Repository
- **Inline code comments** — Detailed explanations in code files
- **Daily progression** — Build complexity step-by-step
- **Real-world examples** — AI agents, web APIs, automation scripts
- **Multiple frameworks** — FastAPI, LangChain, NVIDIA NIM, Docker

### Recommended Learning Order
1. Start with **Day 1–Day 15** for fundamentals
2. Move to **PYTHON_DSA** for algorithmic thinking
3. Explore **py_classes** and **pythondecorator** for advanced OOP
4. Try **FastAPI** and **python-langchain** for web development
5. Experiment with **Nvidia_agent** and **python-genai** for AI/ML

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|---------------|
| **Core** | Python 3.8+, pip, virtual environments |
| **AI/ML** | NVIDIA NIM, LangChain, OpenAI SDK, Generative AI |
| **Web** | FastAPI, Pydantic, REST APIs |
| **Data** | NumPy, Pandas (via projects) |
| **DevOps** | Docker, GitHub Actions (`.github/workflows/`) |
| **Tools** | VSCode (`.vscode/` config), Git |

---

## 📊 Repository Statistics

- **Total Commits:** 106+
- **Languages:** Python 100%
- **License:** MIT
- **Maintained:** Active

---

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `.gitignore` | Git ignore rules for Python projects |
| `LICENSE` | MIT License terms |
| `gitcmd.txt` | Common Git commands reference |
| `airline_customers.csv` | Sample dataset for practice |
| `numbers.bin` | Binary file example for file I/O |
| `facebook_snapshot.png` | Project documentation screenshot |

---

## 🎓 Use Cases

This repository is ideal for:

✅ **Beginners** — Learn Python from scratch with structured daily lessons  
✅ **Intermediate Learners** — Master data structures, OOP, and design patterns  
✅ **Interview Prep** — Practice DSA problems and algorithm implementations  
✅ **AI/ML Enthusiasts** — Build and deploy AI agents with modern frameworks  
✅ **Web Developers** — Learn FastAPI and REST API development  
✅ **DevOps Engineers** — Understand containerization and deployment  

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create a feature branch** (`git checkout -b feature/your-feature`)
3. **Commit changes** (`git commit -am 'Add new feature'`)
4. **Push to branch** (`git push origin feature/your-feature`)
5. **Open a Pull Request**

---

## 📧 Contact & Support

For questions or suggestions:
- **GitHub Issues** — Open an issue for bugs or feature requests
- **Repository:** [github.com/guppi4u/Python-Learning](https://github.com/guppi4u/Python-Learning)

---

## 📜 License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.

You are free to use, modify, and distribute this code for personal and commercial projects.

---

## 🌟 Acknowledgments

This repository represents a **comprehensive learning journey** combining:
- Structured curriculum (Day-based modules)
- Real-world applications (AI agents, web APIs)
- Industry-standard tools (NVIDIA, FastAPI, LangChain)
- Best practices (containerization, version control)

**Perfect for anyone serious about mastering Python and AI/ML engineering.**

---

## 🗺️ Roadmap

Future enhancements may include:
- [ ] Unit tests and test coverage
- [ ] Complete API documentation
- [ ] Video tutorials linked to each module
- [ ] Jupyter notebooks for interactive learning
- [ ] Community contributions and examples
- [ ] CI/CD pipeline improvements

---

**Happy Learning! 🚀**
