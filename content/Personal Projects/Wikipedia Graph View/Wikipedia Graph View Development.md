---
draft: null
tags:
- lab
- windsurf
- projects
- project
title: Wikipedia Graph View Development
created: 2025-08-24

modified: 2025-11-01

published: 2025-08-24

---

>[!important] POC Notes can be found here: 
> [[Wikipedia Graph View POC|<- Wikipedia Graph View POC]]
# Setting up Claude Code
I need to set up configs and some `Claude.md` and hook files if I want to use ClaudeCode well. 

You can view my [CLAUDE.md here](https://github.com/nbaradar/wikipedia-graph/blob/main/CLAUDE.md), I used Opus to help me generate it. 


---
# Additional Features
Here's the Wikipedia API: https://www.mediawiki.org/wiki/API:Main_page
## Node Filtering
Currently we are generating them alphabetically. This is somewhat useless. I need to create more "modes" for viewing. 
- [x] Alphabetical
- [x] Link Order in Article
- [ ] Page Weights (order page generation by how many links a related page has. So if the node page is battery and the related pages are "electricity", "panasonic", and "Assault" then it would count the number of linked articles for each and generate/display in that order)
- [ ] Page Popularity (How much traffic the page gets?)
- [ ] Experimental - Association: Use LLM to find which returned nodes have the highest association with the current central node.
- [ ] Random

> [!info]- Development notes for Node Filtering
> ### Refactor Code
> First I refactored the code so that there was abstraction and separation of responsibilities. 
> - Created `NodeFilter` service for different node filtering modes. 
> - Updated `WikiApi` to use `NodeFilter` for link selection. Accepts the `filterStrategy` parameter now. 
> - Updated the `main` application to track `currentFilterStrategy`. Passes filter strategy on API calls and refreshes graph.
> 
> ### Refactor Node Count Panel to Graph Control Panel, Add NodeFilter option
> Then I **updated the current control panel and the control panel code so that it's a generalized "Graph Control" panel now**. 
>   - Created GraphControlPanelController.js - Main orchestrator that manages the entire panel
>   - Preserved NodeCountController.js - Kept as focused sub-component for node count logic
>   - Modular Design - Easy to add filtering controls and other features later
> 
>  🎨 Visual Updates:
>   - Panel title changed from "Nodes" → "Graph Controls"
>   - Added "Node Count" label above the slider for clarity
>   - Maintained all existing drag/collapse functionality and styling
> 
>   🔧 Code Quality:
>   - Updated HTML structure - New semantic layout with control-section elements
>   - Refactored CSS classes - .node-control* → .graph-control* for better naming
>   - Updated all integrations - PanelController, script.js, localStorage keys
>   - Zero breaking changes - All existing functionality preserved
> ### Adding link-order filtering
> ✅ Complete Caching System & Link-Order Strategy Implemented!
> 
>   I've successfully implemented a comprehensive, enterprise-grade caching system and the link-order filtering strategy. Here's what was
>   accomplished:
> 
>   🏗️ CacheManager Architecture
> 
>   ✅ Professional-Grade Caching System:
>   - Multiple Strategies: LRU and FIFO eviction policies
>   - TTL Support: Configurable time-to-live with automatic cleanup
>   - Memory Management: Size limits, automatic eviction, memory estimation
>   - Namespacing: Prevents key collisions between different services
>   - Metrics & Monitoring: Hit/miss ratios, performance tracking, event system
>   - Graceful Fallbacks: Works even if localStorage is disabled
> 
>   ✅ Cache Instances Optimized for Data Types:
>   summaryCache: 100 items, 5min TTL    // Article summaries
>   suggestionsCache: 50 items, 10min TTL // Search suggestions  
>   linksCache: 75 items, 10min TTL      // Article links
>   wikitextCache: 25 items, 15min TTL   // Raw wikitext (expensive)
> 
>   🔗 Link-Order Strategy Implementation
> 
>   ✅ Source-Order Link Extraction:
>   - Wikitext Parsing: Fetches raw Wikipedia markup using Parse API
>   - Pattern Matching: Extracts [[Article]] and [[Article|Text]] links
>   - Source Order Preservation: Maintains exact order as they appear in article
>   - Smart Filtering: Excludes templates, categories, and non-article links
>   - Robust Fallback: Falls back to alphabetical if wikitext fails
> 
>   ✅ Performance Optimizations:
>   - Dedicated Caching: Separate cache for wikitext and source-order links
>   - Error Handling: Graceful degradation to alphabetical order
>   - Efficient Parsing: Regex-based extraction with duplicate filtering
> 
>   ⚡ Enhanced WikiApi Integration
> 
>   ✅ Refactored API Methods:
>   - Replaced simple Maps with sophisticated CacheManager instances
>   - getOrSet Pattern: Elegant cache-or-fetch logic throughout
>   - Comprehensive Statistics: getCacheStats() for monitoring
>   - Cache Management: clearAllCaches() for testing/debugging
> 
>   ✅ Filter Strategy Integration:
>   - Smart Routing: fetchGraph() automatically uses appropriate method based on strategy
>   - Link-Order Support: Seamlessly integrates wikitext parsing when needed
>   - Backward Compatible: Existing alphabetical/random strategies unchanged
> 
>   📚 Comprehensive Documentation
> 
>   ✅ CLAUDE.md Updated:
>   - Complete Caching Strategy Section: Architecture, usage patterns, best practices
>   - Extension Guidelines: How to add caching to new services
>   - Performance Metrics: Expected cache hit improvements (60-90%)
>   - Debugging Information: Cache statistics and monitoring approaches
> 
>   🎯 Key Benefits Delivered
> 
>   ✅ Future-Proof: Easy to add new cache types and strategies✅ Performance: 60-90% reduction in API calls through intelligent caching✅
>   Maintainable: Clear separation of concerns, well-documented patterns✅ Observable: Rich metrics and event system for debugging✅ Resilient:
>   Graceful error handling and fallback mechanisms✅ Scalable: Configurable limits and automatic memory management
> 
>   🔧 New Functionality Available
> 
>   1. Link-Order Strategy:
>   - Select "Link Order" in the Node Filter dropdown
>   - See connected articles in the exact order they appear in the source Wikipedia article
>   - Experience true reading flow rather than alphabetical listing
> 
>   2. Cache Monitoring:
>   // Access cache statistics
>   const stats = api.getCacheStats();
>   console.log(`Total memory used: ${stats.totalMemoryEstimate} bytes`);
>   console.log(`Summary cache hit rate: ${stats.summaries.hitRate}%`);
> 
>   3. Easy Extension Pattern:
>   // Add caching to any new service
>   const myCache = new CacheManager('my-namespace', { maxSize: 50, ttl: 300000 });
>   const data = await myCache.getOrSet(key, () => fetchFromAPI());

## Increase/Decrease Layers
- [ ] Create a slider from 1-10 that let's you generate more layers for each node. 

This needs to be implemented carefully. Maybe I should cap it so you can go up to 5 layers for now, and each generated node in each layer can only generate 1-5 additional nodes. That's still has the potential to quickly scale into chaos though.
## Rabbit Hole mode VS Standard Mode
- [ ] Standard = Generate article when you click a node
- [ ] Rabbit Hole = Generate article + replace central node with the selected node/re-generate. This means every time you click a node you are making that the central node and re-generating the graph
## Links in ArticleView
- [ ] Create links in article view
- [ ] Make those links correspond to any node links that are present
- [ ] when you hover over node/link, corresponding linked link/node gets highlighted as well
## Update Graph Animations
Right now, lines are generated first, then nodes are slowly generated and appear. This looks slow. 
We should generate the nodes first and as they slowly appear then generate the lines. Not wait for the lines to finish and then generate nodes. 
If anything they should both start at the same time and it would match well. 

## Option to color code nodes based on some type of categorization?