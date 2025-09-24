# Introduction to Kafka-Python and Apache Avro
kafka-python is a pure Python client for Apache Kafka, providing an easy-to-use interface for producing and consuming messages.

## Key Features of kafka-python:
- **Producer and consumer APIs**: Simplifies the creation of producers and consumers to interact with Kafka topics.
- **Support for Kafka protocols**: Fully supports Kafka's binary protocol, ensuring compatibility with Kafka clusters.
- **Thread safety**: Allows safe multi-threaded access, essential for high-performance applications.

# What is Apache Avro?
Apache Avro is a data serialisation system that provides a compact, fast, binary data format. It uses JSON for defining data types and protocols and serialises data into a compact binary format.

## The benefits of using Avro
- **Compact serialisation**: Reduces data size, improving transmission speed.
- **Schema evolution**: Allows schemas to evolve over time without breaking compatibility.
- **Language agnostic**: Supports data interchange between programs written in different languages.

---

# Interacting with Schema Registries
A schema registry is a service that stores and retrieves schemas for data serialisation.<br/>
 It acts as a central repository for schemas, enabling producers and consumers to agree on the structure of the data they exchange.<br/>


## The benefits of using a schema registry
- **Schema management**: Centralises schema storage and versioning.
- **Compatibility checks**: Ensures that producers and consumers are compatible.
- **Reduces overhead**: Avoids the need to include schema definitions with each message.
- **Decoupled schema management**: Producers and consumers retrieve schemas from the registry, reducing dependencies.
- **Automatic serialisation/deserialisation**: Libraries handle the conversion between Python objects and Avro binary format.
- **Schema evolution support**: Consumers can handle changes in data structure according to compatibility rules.

## Introducing Confluent Schema Registry 
Confluent Schema Registry is a popular open-source schema registry that supports Avro, JSON Schema, and Protobuf.

- **RESTful interface**: Interact with the registry using HTTP calls.
- **Multi-format support**: Handles different serialisation formats.
- **Compatibility modes**: Enforce schema evolution rules (e.g., backward, forward, full).


## Implementation Steps
- **Define transaction schema**: Includes fields like transaction_id, account_number, amount, currency, timestamp.
- **Register schema**: Upload the schema to the Schema Registry.
- **Produce Transactions**: Use confluent-kafka-python to produce messages, automatically serialising data according to the schema.
- **Consume transactions**: Consumers retrieve the schema from the registry to deserialise messages.

---

# Scrapy web data collection
A powerful, open-source Python framework for extracting data from websites, designed for speed, efficiency, and extensibility

## Key features of Scrapy
- **Asynchronous processing**: Handles multiple requests concurrently, improving performance.
- **Selective data extraction**: Uses selectors to target specific elements on a page.
- **Extensibility**: Supports middleware, pipelines, and extensions for custom functionality.


## Scrapy implementation Steps    
1    Identify target websites: List the e-commerce sites to scrape, ensuring compliance with their terms of service.
2    Define spiders: Create spiders for each site, handling site-specific structures. Implement logic to navigate pagination and extract relevant data.
3    Data processing pipelines: Clean and normalise data (e.g., currency conversion, standardising units). Store data in a central database or send it to a Kafka topic for further processing.
4    Handling challenges:
    - **IP Blocking**: Implement middleware to rotate proxies or delay requests.
	- **JavaScript rendering**: Use tools like Selenium or Splash if the site relies heavily on JavaScript.

## The benefits of integrating Scrapy with Kafka
- **Real-Time data flow**: Immediately make scraped data available for processing.
- **Scalable processing**: Downstream consumers can process data at scale using Kafka's distributed architecture.

---

# Implementing data validation and processing with Schema registeries
Schema Registries not only store schemas but can also enforce data validation rules, rejecting data that doesn't match the schema

## Validation process
- **Define strict schemas**: Include data types, required fields, default values, and allowed ranges or patterns.
- **Configure compatibility modes**: Set the registry to enforce certain compatibility modes, preventing incompatible schema changes.
- **Implement validation in producers**: Producers validate data against the schema before sending. Errors are caught early, reducing downstream issues.

## Implementing logical types and constraints




---

# Data Quality Techniques
## Preventative and Corrective
| Preventative               		| Corrective                       	|
|--------------------------			|----------------------------------	|
| Data Entry Controls           	|    Automated Correction 			| 
| Data Producer Training        	| Manually Directed Correction 		|
| Rule Definition         			|     Manual Correction            	|
| Demanding HQ data from suppliers  | 									|
| Data Governance and Stewardship   |  									|
| Formal Change Control             |  									|
