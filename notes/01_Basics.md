# FastAPI and Web API Concepts

## 1. FastAPI

**Definition:**
- FastAPI is a modern, fast, web framework for building APIs with Python 3.7+ based on standard Python type hints.
- It is designed to be easy to use and efficient, with automatic data validation and documentation generation.

**Features and Benefits:**
- **Fast:** High performance, thanks to Starlette and Pydantic.
- **Fast to Code:** Increases developer productivity.
- **Fewer Bugs:** Reduces about 40% of human (developer) induced errors.
- **Intuitive:** Easy to use and learn.
- **Automatic Docs:** Generates interactive API documentation.

## 2. GET vs POST Method

**Definition:**
- **GET:** Used to request data from a specified resource.
- **POST:** Used to send data to be processed to a specified resource.

**Usage:**
- **GET:** Retrieving information from a server.
- **POST:** Submitting data to be processed, often used in forms.

## 3. Path Parameters

**Definition:**
- Part of the URL path that captures and passes data to the endpoint.

**Usage:**
- Accessing specific resources via URL, e.g., `/users/{user_id}`.

## 4. Predefined Values

**Definition:**
- Values set beforehand, often used for limiting choices or providing default values.

**Usage:**
- Specifying default values for parameters, e.g., `page: int = 1`.

## 5. Query Parameters

**Definition:**
- Parameters passed in the URL to modify the request.

**Usage:**
- Filtering, sorting, or paginating results, e.g., `/users?role=admin`.

## 6. Status Code

**Definition:**
- A three-digit code returned by a server to indicate the status of a requested operation.

**Usage:**
- **200 OK:** Successful request.
- **404 Not Found:** Resource not found.
- **500 Internal Server Error:** Server encountered an error.

## 7. Tags

**Definition:**
- A way to categorize and group related endpoints.

**Usage:**
- Improves API organization and documentation, e.g., grouping all blog-related endpoints under the "blog" tag.

## 8. Summary

**Definition:**
- A concise description of what an endpoint does.

**Usage:**
- Provides a quick overview of the endpoint's purpose, e.g., `summary="Retrieve all blogs"`.

## 9. Response Description

**Definition:**
- A detailed description of the expected response from an API endpoint.

**Usage:**
- Helps users understand the structure of the response, e.g., `response_description="The list of available blogs"`.
