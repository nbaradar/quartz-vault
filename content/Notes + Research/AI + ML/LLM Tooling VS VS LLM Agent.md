---
title: LLM Tooling VS Agents
tags:
  - study
draft:
created: 2025-06-28

modified: 2025-09-19
published: 2025-06-28

---
With both terms now having become industry buzzwords being thrown around ambiguously, let's define the relation between [[LLM Tooling]] and an [[AI Agent]].

Think of LLM Tools as functions that an LLM can use. So if you ask an LLM "What is the weather today in Tokyo" it may end up looking for this function tool:
```java
public static void getWeatherData(String location){
	String weatherData = weatherClient.getLocation24hr("Tokyo");
	return weatherData; 
}
```

An LLM [[AI Agent]] then uses these function calls (Tooling) during their workflow. So if an LLM agent was tasked with writing a weather report of the top 10 cities in the world every day and then analyze the trends over the past 7 days, 14 days, and 30 days, it would take much more than just a `getWeatherData` call to complete that entire workflow. We would need to....
- Gather weather data 10x
- Consult historical weather data
- Compare the data using different statistical methods

Within each step there are multiple tool calls, even if to the same tool. 

**So an LLM Agent is USING LLM Tooling to complete it's task**. It's a one -> many relationship between LLM Agents -> LLM Tooling

![[Pasted image 20250623104032.png|800]]