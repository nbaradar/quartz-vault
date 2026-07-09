---
title: Pydantic
tags:
  - reference
created: 2025-07-05

modified: 2025-07-05

published: 2025-07-05

---
# Pydantic
Python library used for **data validation and settings management**. Allows you to define schemas using Python classes and ensures that data adheres to those schemas. Often used in modern Python applications, especially with frameworks like FastAPI, because of its integration and simplicity.
## **What is Pydantic?**
Pydantic is a Python library used for **data validation and settings management**. It allows you to define schemas using Python classes and ensures that data adheres to those schemas. Pydantic is often used in modern Python applications, especially with frameworks like FastAPI, because of its integration and simplicity.
## **General Uses of Pydantic**
1. **Data Validation**:
    - Automatically validates incoming data against predefined schemas.
    - Ensures types, formats, and required fields are correct.
2. **Settings Management**:
    - Simplifies configuration loading (e.g., environment variables, config files).
    - Provides default values and validation for settings.
3. **Serialization and Deserialization**:
    - Converts data between Python objects and JSON or dictionaries seamlessly.
4. **Integration with FastAPI**:
    - Automatically generates API request and response models.
    - Provides validation for endpoint parameters and request bodies.

## **Categories of Pydantic Models**

|Type|Example|Purpose|
|---|---|---|
|**Request Models**|`ImportRequest`, `UserLoginRequest`|Input validation (used in API endpoints)|
|**Response Models**|`ImportResponse`, `MemoryResponse`|Shape of output JSON (often a subset or transformed view of DB model)|
|**Database Models**|`Import`, `User`, `Prompt`, etc.|Reflect data stored in MongoDB|
|**Internal Utility Models**|`NormalizedMemory`, `TagInferenceInput`|Used for internal processing, not exposed to user or stored directly|
