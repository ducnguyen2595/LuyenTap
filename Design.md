Cache: Imagine a web server for a simplified search engine. This system has 100 machines to respond to search queries, which may then call out using processSearch(string query) to another cluster of machines to actually get the result. The machine which responds to the given query is chosen at random, so you cannot guarantee that the same machine will always respond to the same request. The method processSearch is very expensive. Design a caching mechanism for the most recent queries. Be sure to explain how you would update the cache when data changes

[Cracking the Coding Interview pg145](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850)


22 Apr:
Sales Rank: A large eCommerce company wishes to list the best-selling products, overall and by category. For example, one product might be the #1056th best-selling product overall but #13th best-selling product under "Sport and Equiqment" and the #24th best-selling product under "Safety". Describe how you would design this system

[Cracking the Coding Interview pg145](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850)
