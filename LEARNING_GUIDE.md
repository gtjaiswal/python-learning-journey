# 📚 WEEK 3 LEARNING GUIDE: Infrastructure Fundamentals

**Foundation Knowledge**

This guide covers the theoretical knowledge you need BEFORE and DURING your hands-on implementation.

---

## **📋 Overview**

**Total Learning Time: 4-5 hours**

This learning guide is organized to be completed alongside your hands-on work:
- Some learning happens BEFORE implementation (prerequisites)
- Some learning happens DURING implementation (just-in-time)
- Some learning happens AFTER implementation (deepening understanding)

---

## **🎯 Learning Objectives**

By the end of this learning guide, you will understand:

1. **PostgreSQL** - Relational database fundamentals and advanced features
2. **SQLAlchemy** - ORM concepts and async patterns
3. **Async Programming** - Event loops, async/await, when to use async
4. **OpenSearch** - Full-text search engine basics
5. **Apache Airflow** - Workflow orchestration concepts
6. **FastAPI Advanced** - Dependency injection, async endpoints, testing

---

## **SECTION 2: Async Programming in Python** ⚡

**Time required:** 30 minutes  
**Priority:** CRITICAL

---

### **2.1 Why Async? (10 min)**

**Core Concept:**
Async programming allows a program to do other work while waiting for I/O operations.

**Video Learning:**
📺 **"Async IO in Python: A Complete Walkthrough"** - ArjanCodes
- URL: https://www.youtube.com/watch?v=2IW-ZEui4h4
- Watch: First 10 minutes (introduction and basics)

**The Problem Async Solves:**

**Synchronous (Blocking):**
```
Request 1 → [Wait for DB] → [Process] → Response 1
                ↓
            Blocked! Can't handle Request 2 yet
```

**Asynchronous (Non-blocking):**
```
Request 1 → [Wait for DB] ←───────┐
               ↓                   │
Request 2 → [Wait for DB]         │
               ↓                   │
Request 3 → [Wait for DB]         │
               ↓                   │
            [Process 1] ←──────────┘
            [Process 2]
            [Process 3]
```

**Key Insight:**
- Database queries take time (10-100ms)
- Network requests take time (100-1000ms)
- During that waiting, CPU is idle
- Async lets you handle other requests during waits

---

### **2.2 Async/Await Syntax (10 min)**

**Video Learning:** Corey Schafer's best animated expalination of sync/awate
https://www.youtube.com/watch?v=oAkLSJNr5zY
- Animated view : https://coreyms.com/asyncio/example_1.html
- change the example_1 through example_5

**Reading:**
📖 **Real Python - Async IO in Python**
- URL: https://realpython.com/async-io-python/
- Read: "The async/await Syntax" section

**Key Syntax:**

**Defining Async Function:**
```python
# Regular function (synchronous)
def get_data():
    return fetch_from_db()

# Async function
async def get_data():
    return await fetch_from_db()
#      ↑              ↑
#   Makes it      Waits for
#   async         async operation
```

**Rules:**
1. `async def` creates an async function (coroutine)
2. `await` can only be used inside `async def`
3. `await` pauses execution until operation completes
4. While paused, event loop can run other code

**Event Loop:**
```
Event Loop (The Manager)
┌─────────────────────────────────┐
│  Running: Task 1               │
│  Waiting: Task 2, Task 3       │
│  Completed: Task 4             │
└─────────────────────────────────┘
     ↓           ↓           ↓
  Active    Paused on    Finished
            await
```

---

### **2.3 When to Use Async (10 min)**

**Key Decision Points:**

**Use Async When:**
- ✅ I/O-bound operations (database, network, files)
- ✅ Handling many concurrent requests (web servers)
- ✅ Waiting for external services
- ✅ Need high throughput with single thread

**Don't Use Async When:**
- ❌ CPU-bound operations (calculations, processing)
- ❌ Blocking libraries (no async support)
- ❌ Simple scripts that run once
- ❌ Learning basic Python (adds complexity)

**Your Use Case (Week 3-4):**
- ✅ **FastAPI endpoints** → Async (many concurrent requests)
- ✅ **Database queries** → Async (I/O waiting)
- ✅ **arXiv API calls** → Async (network I/O)
- ✅ **PDF downloads** → Async (network I/O)

**Common Patterns:**

**Async Database Query:**
```python
async def get_papers():
    async with AsyncSession() as session:
        result = await session.execute(select(Paper))
        #          ↑
        #     Wait for database
        return result.scalars().all()
```

**Async FastAPI Endpoint:**
```python
@app.get("/papers")
async def list_papers(session: AsyncSession = Depends(get_db)):
    #     ↑                                      ↑
    # Async endpoint                    Async dependency
    papers = await get_papers(session)
    #           ↑
    #       Wait for query
    return papers
```

---

## **SECTION 3: PostgreSQL Fundamentals** 🐘

**Time required:** 30 minutes  
**Priority:** HIGH (but you did some yesterday!)

---

### **3.1 PostgreSQL vs Other Databases (5 min)**

**Reading:**
📖 **PostgreSQL Introduction**
- URL: https://www.postgresql.org/about/
- Read: "What is PostgreSQL?" section

**Key Points:**
- Open-source relational database
- SQL compliant
- ACID transactions (Atomicity, Consistency, Isolation, Durability)
- Advanced features: arrays, JSON, full-text search, custom types

**Why PostgreSQL for Your Project:**
- ✅ Arrays for storing authors/categories (no separate tables needed)
- ✅ JSONB for flexible metadata storage
- ✅ Excellent with Python (SQLAlchemy, asyncpg)
- ✅ Production-ready and scalable
- ✅ Strong community and documentation

---

### **3.2 PostgreSQL Array Type (10 min)**

**Video:**
📺 **PostgreSQL Arrays Explained**
- URL: https://www.youtube.com/watch?v=lFKKiMFq6Ao (or search "PostgreSQL arrays tutorial")

**Key Concepts:**

**Why Use Arrays?**
- Store multiple values in single column
- Simpler than junction tables for simple cases
- Fast queries with array operators

**Array Operations:**
```sql
-- Create table with array
CREATE TABLE papers (
    authors TEXT[],
    categories TEXT[]
);

-- Insert array
INSERT INTO papers VALUES (
    ARRAY['John Doe', 'Jane Smith'],
    ARRAY['cs.AI', 'cs.LG']
);

-- Query by array element
SELECT * FROM papers 
WHERE 'cs.AI' = ANY(categories);

-- Array contains
SELECT * FROM papers
WHERE categories @> ARRAY['cs.AI'];
```

**Array vs Separate Table:**

**Arrays (Simple):**
```
papers table:
id | authors[]              | categories[]
1  | [Alice, Bob]          | [cs.AI, cs.LG]
2  | [Charlie]             | [cs.CV]
```

**Separate Tables (Normalized):**
```
papers:        authors:      papers_authors:
id | title     id | name     paper_id | author_id
1  | ...       1  | Alice    1        | 1
2  | ...       2  | Bob      1        | 2
               3  | Charlie  2        | 3
```

**Decision Guide:**
- **Use arrays when:** Simple list, no metadata, querying by element
- **Use separate tables when:** Need author metadata, complex queries, relationships

**For your project:** Arrays are perfect! ✅

---

### **3.3 Indexes and Performance (10 min)**

**Reading:**
📖 **PostgreSQL Indexes**
- URL: https://www.postgresql.org/docs/current/indexes.html
- Read: "Introduction" section

**Key Concepts:**

**What is an Index?**
- Like a book's index
- Speeds up queries
- Makes writes slightly slower
- Takes disk space

**When to Index:**
```sql
-- Primary key (auto-indexed)
id SERIAL PRIMARY KEY

-- Unique constraint (auto-indexed)
arxiv_id VARCHAR UNIQUE

-- Frequently queried columns
CREATE INDEX idx_published_date ON papers(published_date);

-- Array columns (GIN index)
CREATE INDEX idx_categories ON papers USING GIN(categories);
```

**GIN Index for Arrays:**
- Generalized Inverted Index
- Fast array containment queries
- Essential for array columns you'll query

**Your Paper Table Needs:**
- ✅ Primary key on `id` (automatic)
- ✅ Unique index on `arxiv_id` (fast lookup, prevent duplicates)
- ✅ GIN index on `categories` (array queries)
- ✅ Index on `published_date` (sorting, filtering)

---

### **3.4 Timestamps and Timezones (5 min)**

**Key Concept:**
Always store timestamps with timezone in UTC.

**Best Practices:**
```sql
-- Good: Timezone aware
created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()

-- Bad: Timezone naive
created_at TIMESTAMP
```

**Why This Matters:**
- Your app might serve users in different timezones
- Server might be in different timezone
- Daylight saving time issues
- International collaboration

**Rule:** Store in UTC, display in user's timezone

---

## **SECTION 4: SQLAlchemy ORM** 🗃️
 
**Time required:** 30 minutes  
**Priority:** CRITICAL

---

### **4.1 What is an ORM? (10 min)**

**Core Concept:**
ORM (Object-Relational Mapping) translates between database tables and Python objects.

**Video:**
📺 **"What is an ORM?"** - Corey Schafer
- URL: https://www.youtube.com/watch?v=AJHzSU0BBBU (or search "ORM explained")

**The Problem ORM Solves:**

**Without ORM (Raw SQL):**
```python
# Execute SQL
cursor.execute("SELECT * FROM papers WHERE id = %s", (1,))
row = cursor.fetchone()

# Manually extract data
paper_id = row[0]
title = row[1]
abstract = row[2]
# ... tedious!
```

**With ORM (SQLAlchemy):**
```python
# Query returns Python objects
paper = session.get(Paper, 1)

# Access as attributes
print(paper.id)
print(paper.title)
print(paper.abstract)
# ... clean!
```

**Benefits:**
- ✅ Write Python, not SQL
- ✅ Type safety and IDE autocomplete
- ✅ Prevents SQL injection
- ✅ Database agnostic (switch databases easier)
- ✅ Relationship management

**Tradeoffs:**
- ❌ Adds abstraction layer
- ❌ Can generate inefficient queries if misused
- ❌ Need to learn ORM syntax

---

### **4.2 SQLAlchemy Core Concepts (10 min)**

**Reading:**
📖 **SQLAlchemy Tutorial - Introduction**
- URL: https://docs.sqlalchemy.org/en/20/tutorial/index.html
- Read: "Overview" section

**Key Components:**

**1. Engine:**
- Connection to database
- Manages connection pool
```python
engine = create_async_engine("postgresql+asyncpg://...")
```

**2. Session:**
- Transaction manager
- "Shopping cart" for changes
```python
async with AsyncSession(engine) as session:
    session.add(paper)
    await session.commit()
```

**3. Model (Declarative Base):**
- Python class representing table
```python
class Paper(Base):
    __tablename__ = "papers"
    id = Column(Integer, primary_key=True)
    title = Column(String)
```

**4. Query:**
- Retrieve data
```python
result = await session.execute(select(Paper))
papers = result.scalars().all()
```

**Session Lifecycle:**
```
1. Create Session
2. Query/Add/Modify objects
3. Commit (saves to database)
4. Close Session
```

---

### **4.3 SQLAlchemy Async Patterns (10 min)**

**Reading:**
📖 **SQLAlchemy Async Documentation**
- URL: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
- Read: "Synopsis - Core" and "Synopsis - ORM" sections

**Key Differences from Sync:**

**Imports:**
```python
# Sync
from sqlalchemy import create_engine, Session

# Async
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
```

**Engine Creation:**
```python
# Sync
engine = create_engine("postgresql://...")

# Async
engine = create_async_engine("postgresql+asyncpg://...")
#                                         ↑
#                                    Async driver
```

**Session Usage:**
```python
# Sync
with Session(engine) as session:
    paper = session.get(Paper, 1)
    session.commit()

# Async
async with AsyncSession(engine) as session:
    #     ↑                          ↑
    # async context          Await everything!
    paper = await session.get(Paper, 1)
    await session.commit()
```

**Query Execution:**
```python
# Sync
papers = session.query(Paper).all()

# Async (SQLAlchemy 2.0 style)
result = await session.execute(select(Paper))
papers = result.scalars().all()
```

**Why Async SQLAlchemy?**
- FastAPI is async
- Better concurrency for web apps
- Non-blocking database operations
- Modern best practice

---

## **SECTION 5: OpenSearch Basics** 🔍

**When to learn:** Flexible - during Week 3 or defer to Week 7  
**Time required:** 30 minutes  
**Priority:** MEDIUM (not needed until Week 7)

---

### **5.1 What is OpenSearch? (10 min)**

**Core Concept:**
OpenSearch is a search and analytics engine for full-text search, logging, and real-time analytics.

**Video:**
📺 **"Introduction to OpenSearch"** - OpenSearch Project
- URL: https://www.youtube.com/watch?v=0WZ4VtKemCc (or search "OpenSearch introduction")

**Key Points:**
- Fork of Elasticsearch
- Full-text search engine
- Distributed and scalable
- RESTful API
- Document-oriented (stores JSON)

**Why OpenSearch in Your Project:**
- ✅ BM25 algorithm for keyword search (Week 7)
- ✅ Vector search for embeddings (Week 8)
- ✅ Hybrid search combining both
- ✅ Fast full-text search in papers
- ✅ Filtering and faceting

---

### **5.2 OpenSearch Core Concepts (10 min)**

**Reading:**
📖 **OpenSearch Documentation - Core Concepts**
- URL: https://opensearch.org/docs/latest/
- Read: "About OpenSearch" section

**Key Concepts:**

**1. Index:**
- Like a database table
- Collection of documents
- Your project: `arxiv-papers` index

**2. Document:**
- JSON object
- Like a database row
- Your project: Each paper is a document

**3. Field:**
- Key-value pair in document
- Like a column
- Your project: title, abstract, categories, etc.

**4. Mapping:**
- Schema definition
- Defines field types
- Like database table schema

**Example:**
```json
{
  "arxiv_id": "2401.12345",
  "title": "Sample Paper",
  "abstract": "This is the abstract...",
  "categories": ["cs.AI", "cs.LG"],
  "vector_embedding": [0.123, 0.456, ...]
}
```

---

### **5.3 BM25 Search Algorithm (10 min)**

**Reading:**
📖 **Understanding BM25**
- URL: Search for "BM25 algorithm explained" or check Wikipedia
- Understand: What it does, not the math

**Key Concepts:**

**What is BM25?**
- Best Match 25 (ranking function)
- Ranks documents by relevance to query
- Considers:
  - Term frequency (TF): How often word appears in document
  - Inverse document frequency (IDF): How rare the word is overall
  - Document length: Longer documents penalized slightly

**Example:**
```
Query: "attention mechanism neural networks"

Paper 1: Mentions "attention" 10 times, short paper
Score: 15.2 (high)

Paper 2: Mentions "attention" 3 times, very long paper  
Score: 8.1 (medium)

Paper 3: Mentions "attention" 1 time, short paper
Score: 3.5 (low)
```

**Why BM25?**
- ✅ Simple and fast
- ✅ Works well for keyword search
- ✅ Industry standard
- ✅ Better than TF-IDF

**Your Usage (Week 7):**
- Papers indexed in OpenSearch
- User searches: "transformer attention"
- BM25 ranks papers by relevance
- Return top 10 results

---

## **SECTION 6: Apache Airflow** 🌬️

**When to learn:** Saturday (during Week 3) or before Week 4  
**Time required:** 60 minutes  
**Priority:** CRITICAL for Week 4

---

### **6.1 What is Workflow Orchestration? (15 min)**

**Core Concept:**
Orchestration = Coordinating multiple tasks to run in a specific order or schedule.

**Video:**
📺 **"Apache Airflow in 5 Minutes"** - Astronomer
- URL: https://www.youtube.com/watch?v=AHMm1wfGuHE
- Quick overview

**The Problem Airflow Solves:**

**Without Orchestration:**
```
Cron Job 1: Fetch papers at 2am
Cron Job 2: Parse PDFs at 3am (but what if Job 1 fails?)
Cron Job 3: Index in OpenSearch at 4am (but what if Job 2 fails?)
```

**With Airflow:**
```
DAG: Paper Ingestion Pipeline
  ↓
Task 1: Fetch papers → If success → Task 2: Parse PDFs
                                        ↓
                              If success → Task 3: Index
```

**Benefits:**
- ✅ Task dependencies (run B only if A succeeds)
- ✅ Retry logic (auto-retry on failure)
- ✅ Scheduling (daily, hourly, custom)
- ✅ Monitoring (see what failed and why)
- ✅ Backfilling (rerun historical data)

---

### **6.2 Airflow Core Concepts (20 min)**

**Video:**
📺 **"Airflow Tutorial for Beginners"** - Marc Lamberti
- URL: https://www.youtube.com/watch?v=K9AnJ9_ZAXE
- Watch: First 20 minutes (architecture and DAGs)

**Key Concepts:**

**1. DAG (Directed Acyclic Graph):**
- Collection of tasks
- Defines workflow
- No cycles (can't loop back)

```
DAG: Daily Paper Ingestion
┌──────────┐
│ Fetch    │
│ Papers   │
└────┬─────┘
     ↓
┌────┴─────┐
│ Parse    │
│ PDFs     │
└────┬─────┘
     ↓
┌────┴─────┐
│ Store in │
│ Database │
└──────────┘
```

**2. Task:**
- Single unit of work
- Python function or operator
- Can succeed or fail

**3. Operator:**
- Template for a task
- PythonOperator, BashOperator, etc.

**4. Scheduler:**
- Monitors DAGs
- Triggers tasks when ready
- Manages dependencies

**5. Executor:**
- Runs tasks
- LocalExecutor (your setup): Tasks run on same machine
- CeleryExecutor (production): Distributed task execution

---

### **6.3 DAG Structure (15 min)**

**Reading:**
📖 **Airflow DAG Tutorial**
- URL: https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
- Read: "Example DAG definition" section

**Basic DAG Structure:**

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define DAG
dag = DAG(
    dag_id='arxiv_ingestion',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',  # Run once per day
    catchup=False
)

# Define tasks
def fetch_papers():
    # Fetch from arXiv
    pass

def parse_papers():
    # Parse PDFs
    pass

task1 = PythonOperator(
    task_id='fetch',
    python_callable=fetch_papers,
    dag=dag
)

task2 = PythonOperator(
    task_id='parse',
    python_callable=parse_papers,
    dag=dag
)

# Define dependencies
task1 >> task2  # task2 runs after task1
```

**Key Parameters:**

- `dag_id`: Unique name for DAG
- `start_date`: When DAG becomes active
- `schedule_interval`: How often to run (`@daily`, `@hourly`, cron expression)
- `catchup`: Run missed schedules (False = skip missed runs)

---

### **6.4 Your Week 4 Use Case (10 min)**

**What You'll Build:**

**DAG Name:** `arxiv_paper_ingestion`

**Tasks:**
1. **Fetch Metadata** - Call arXiv API for new papers
2. **Download PDFs** - Download paper PDFs
3. **Parse Papers** - Extract text with Docling
4. **Store in Database** - Save to PostgreSQL
5. **Index in OpenSearch** - Add to search engine

**Dependencies:**
```
Fetch → Download → Parse → Store → Index
```

**Schedule:** Daily at 2 AM (weekdays only)

**Error Handling:**
- Retry failed tasks 3 times
- Send alert if all retries fail
- Continue with successful papers even if some fail

**Why Learn Now:**
- Week 4 is all about building this pipeline
- Understanding DAGs helps design the workflow
- Knowing Airflow concepts speeds up implementation

---

## **SECTION 7: FastAPI Advanced Patterns** 🚀

**Time required:** 40 minutes  
**Priority:** MEDIUM-HIGH

---

### **7.1 Dependency Injection (15 min)**

**Reading:**
📖 **FastAPI Dependencies**
- URL: https://fastapi.tiangolo.com/tutorial/dependencies/
- Read: "First Steps" and "Classes as Dependencies"

**Core Concept:**
Dependency injection = Providing dependencies to functions automatically.

**Why Use It?**

**Without DI (Manual):**
```python
@app.get("/papers")
async def get_papers():
    # Manually create session every time
    async with AsyncSession(engine) as session:
        result = await session.execute(select(Paper))
        return result.scalars().all()
```

**With DI (Automatic):**
```python
async def get_db():
    async with AsyncSession(engine) as session:
        yield session

@app.get("/papers")
async def get_papers(db: AsyncSession = Depends(get_db)):
    # Session provided automatically!
    result = await db.execute(select(Paper))
    return result.scalars().all()
```

**Benefits:**
- ✅ Reusable across endpoints
- ✅ Easier testing (mock dependencies)
- ✅ Cleaner code
- ✅ Automatic cleanup

**Common Dependencies:**
- Database sessions
- Authentication/authorization
- Configuration
- Repositories

---

### **7.2 Pydantic Advanced (15 min)**

**Reading:**
📖 **Pydantic Field Validation**
- URL: https://docs.pydantic.dev/latest/concepts/fields/
- Read: "Field customization" section

**Key Concepts:**

**Field Validation:**
```python
from pydantic import BaseModel, Field

class PaperCreate(BaseModel):
    arxiv_id: str = Field(
        ...,  # Required
        pattern=r"^\d{4}\.\d{5}$",  # Regex validation
        description="arXiv ID format: YYMM.NNNNN"
    )
    title: str = Field(..., min_length=1, max_length=500)
    authors: List[str] = Field(..., min_items=1)  # At least one
```

**Custom Validators:**
```python
from pydantic import validator

class PaperCreate(BaseModel):
    published_date: datetime
    
    @validator('published_date')
    def date_not_future(cls, v):
        if v > datetime.now():
            raise ValueError('Published date cannot be in future')
        return v
```

**from_attributes Configuration:**
```python
class PaperResponse(BaseModel):
    id: int
    title: str
    
    model_config = ConfigDict(from_attributes=True)
    # Allows: PaperResponse.model_validate(sqlalchemy_object)
```

**Why This Matters:**
- ✅ Automatic request validation
- ✅ Clear error messages
- ✅ Type safety
- ✅ Self-documenting API

---

### **7.3 Response Models and Status Codes (10 min)**

**Reading:**
📖 **FastAPI Response Models**
- URL: https://fastapi.tiangolo.com/tutorial/response-model/
- Read: Complete page

**Key Concepts:**

**Response Model:**
```python
@app.get("/papers/{paper_id}", response_model=PaperResponse)
async def get_paper(paper_id: int):
    # FastAPI validates response matches PaperResponse
    paper = await get_from_db(paper_id)
    return paper  # Auto-converted to PaperResponse
```

**Status Codes:**
```python
from fastapi import status

@app.post(
    "/papers", 
    response_model=PaperResponse,
    status_code=status.HTTP_201_CREATED  # Return 201 for creation
)
async def create_paper(paper: PaperCreate):
    return await save_to_db(paper)

@app.delete("/papers/{paper_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_paper(paper_id: int):
    await delete_from_db(paper_id)
    return  # No content returned
```

**Common Status Codes:**
- 200 OK - Successful GET/PUT
- 201 Created - Successful POST
- 204 No Content - Successful DELETE
- 400 Bad Request - Client error
- 404 Not Found - Resource not found
- 422 Unprocessable Entity - Validation error
- 500 Internal Server Error - Server error

---

## **SECTION 8: Redis Basics (Optional)** 💾

**Time required:** 20 minutes  
**Priority:** LOW (defer until Week 6)

---

### **8.1 What is Redis? (10 min)**

**Core Concept:**
Redis is an in-memory data store used as a cache, message broker, or database.

**Video:**
📺 **"Redis in 100 Seconds"** - Fireship
- URL: https://www.youtube.com/watch?v=G1rOthIU-uo

**Key Points:**
- In-memory (very fast)
- Key-value store
- Supports various data types (strings, lists, sets, hashes)
- Persistence optional
- Common use: Caching

**Why Redis in Your Project (Week 6):**
- ✅ Cache expensive LLM responses
- ✅ Cache search results
- ✅ Store session data
- ✅ Rate limiting

---

### **8.2 Redis Use Cases (10 min)**

**Reading:**
📖 **Redis Use Cases**
- URL: https://redis.io/docs/about/
- Read: "Use cases" section

**Common Patterns:**

**Caching:**
```
User Query → Check Redis → Cache Hit? Return cached response
                               ↓
                          Cache Miss? Query database → Cache result → Return
```

**Your Usage:**
```python
# Cache RAG response
query = "What are transformers?"
cache_key = f"rag:{hash(query)}"

# Check cache
cached = await redis.get(cache_key)
if cached:
    return cached  # Fast! (~1ms)

# Generate response (slow, ~15s)
response = await generate_rag_response(query)

# Cache for future
await redis.set(cache_key, response, ex=3600)  # Expire in 1 hour
return response
```

**Benefits:**
- ✅ 150-400x faster responses for cached queries
- ✅ Reduce LLM API costs
- ✅ Better user experience

---

## **SECTION 9: Testing with Pytest (Optional)** 🧪

**When to learn:** Week 4 or later  
**Time required:** 30 minutes  
**Priority:** MEDIUM (defer to Week 4)

---

### **9.1 Why Test? (10 min)**

**Core Concept:**
Automated tests verify your code works correctly and prevent regressions.

**Video:**
📺 **"Pytest Tutorial"** - Socratica
- URL: https://www.youtube.com/watch?v=bbp_849-RZ4

**Benefits:**
- ✅ Catch bugs early
- ✅ Safe refactoring
- ✅ Documentation of expected behavior
- ✅ Confidence in deployments

**Types of Tests:**
1. **Unit tests:** Test individual functions
2. **Integration tests:** Test multiple components together
3. **End-to-end tests:** Test entire system

---

### **9.2 Testing Async Code (10 min)**

**Reading:**
📖 **Pytest Async**
- URL: https://pytest-asyncio.readthedocs.io/
- Read: "Quick Start"

**Key Points:**

**Install:**
```bash
pip install pytest pytest-asyncio
```

**Test Async Function:**
```python
import pytest

@pytest.mark.asyncio
async def test_get_paper():
    paper = await get_paper_from_db(1)
    assert paper.id == 1
    assert paper.title is not None
```

**Test FastAPI Endpoint:**
```python
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_list_papers():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/papers")
        assert response.status_code == 200
        assert len(response.json()) > 0
```

---

### **9.3 Testing Best Practices (10 min)**

**Key Principles:**

1. **Arrange-Act-Assert Pattern:**
```python
def test_create_paper():
    # Arrange - Setup test data
    paper_data = {"arxiv_id": "2401.12345", ...}
    
    # Act - Execute the code
    paper = create_paper(paper_data)
    
    # Assert - Verify results
    assert paper.arxiv_id == "2401.12345"
```

2. **Use Fixtures:**
```python
@pytest.fixture
async def test_db():
    # Setup: Create test database
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    yield engine
    # Teardown: Clean up
    await engine.dispose()
```

3. **Test Edge Cases:**
- Valid inputs
- Invalid inputs
- Boundary conditions
- Error conditions

**Your Week 4 Testing:**
- Test arXiv API client
- Test PDF parsing
- Test database operations
- Test API endpoints

---

## **📚 SUPPLEMENTARY RESOURCES**

### **Official Documentation:**

**PostgreSQL:**
- https://www.postgresql.org/docs/current/
- https://www.postgresqltutorial.com/

**SQLAlchemy:**
- https://docs.sqlalchemy.org/en/20/
- Async guide: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html

**FastAPI:**
- https://fastapi.tiangolo.com/
- Async dependencies: https://fastapi.tiangolo.com/async/

**OpenSearch:**
- https://opensearch.org/docs/latest/
- Python client: https://opensearch.org/docs/latest/clients/python/

**Apache Airflow:**
- https://airflow.apache.org/docs/
- Tutorial: https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html

**Pydantic:**
- https://docs.pydantic.dev/latest/

**Pytest:**
- https://docs.pytest.org/
- Pytest-asyncio: https://pytest-asyncio.readthedocs.io/

---

## **📋 LEARNING CHECKLIST**

### **Critical:**
- [ ] Async Python fundamentals (30 min)
- [ ] SQLAlchemy ORM concepts (30 min)
- [ ] FastAPI dependency injection (15 min)

### **Important:**
- [ ] PostgreSQL arrays (15 min)
- [ ] PostgreSQL indexes (10 min)
- [ ] Airflow fundamentals (60 min)
- [ ] Pydantic advanced (15 min)

### **Optional:**
- [ ] OpenSearch basics (30 min)
- [ ] Redis basics (20 min)
- [ ] Testing with pytest (30 min)

---

## **💡 LEARNING TIPS**

### **Active Learning:**
- ✅ Take notes while watching videos
- ✅ Pause and try concepts in Python REPL
- ✅ Draw diagrams to visualize concepts
- ✅ Explain concepts out loud (Feynman technique)

### **Don't Over-Learn:**
- ✅ Understand concepts, not memorize
- ✅ Learn what you need now, defer deep dives
- ✅ Reference docs exist for details
- ✅ Hands-on practice reinforces learning

### **When Stuck:**
- ✅ Re-watch video section
- ✅ Check official documentation
- ✅ Draw it out / explain to rubber duck
- ✅ Try simple example first
- ✅ Ask specific questions

---

## **🎓 SUCCESS CRITERIA**

After completing this learning guide, you should be able to:

**Async Programming:**
- ✅ Explain when to use async vs sync
- ✅ Understand async/await syntax
- ✅ Write async functions and use await correctly
- ✅ Understand event loop concept

**PostgreSQL:**
- ✅ Understand PostgreSQL arrays and when to use them
- ✅ Know how to query arrays
- ✅ Understand indexes and when to create them
- ✅ Handle timestamps with timezones correctly

**SQLAlchemy:**
- ✅ Explain what an ORM is and its benefits
- ✅ Understand SQLAlchemy models and sessions
- ✅ Know difference between sync and async SQLAlchemy
- ✅ Write basic queries with SQLAlchemy

**Airflow:**
- ✅ Explain what workflow orchestration is
- ✅ Understand DAGs, tasks, and operators
- ✅ Know when to use Airflow
- ✅ Can design a simple workflow

**FastAPI Advanced:**
- ✅ Understand dependency injection
- ✅ Know how to validate requests with Pydantic
- ✅ Use proper HTTP status codes
- ✅ Structure endpoints correctly

---

## **🎯 FINAL THOUGHTS**

**Learning is Iterative:**
- First pass: Understand concepts (this guide)
- Second pass: Apply in practice (Steps 1-4)
- Third pass: Deepen through use (Weeks 4+)

**You Don't Need to Master Everything:**
- Understand enough to implement
- Reference docs for details
- Learn deeper as you build

**The Goal:**
Build working systems while understanding WHY they work, not just HOW to make them work.

---

**Document Generated:** December 5, 2025  
**Part of:** 8.5-Month AI/ML Career Transition Plan  
**Current Phase:** Week 3 Infrastructure Learning  
**Companion Documents:** STEP1-4 Hands-On Guides  
**Total Learning Time:** 4-5 hours across Week 3  
**Next:** Integrated Week 3 Master Schedule combining learning + hands-on
