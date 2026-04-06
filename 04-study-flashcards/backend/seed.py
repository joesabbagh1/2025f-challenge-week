"""Seed the database with 5 decks and 50 cards (10 per deck).

Run:  python seed.py
"""

from database import init_db, get_db

DECKS = [
    {
        "name": "Python",
        "description": "Core Python concepts: data structures, OOP, functional patterns",
        "cards": [
            ("What is a list comprehension?",
             "A concise syntax to create lists: [expr for item in iterable if condition]. Example: [x**2 for x in range(10) if x % 2 == 0].", 1),
            ("What does the @decorator syntax do?",
             "It applies a higher-order function to the decorated function at definition time. @deco def f(): ... is equivalent to f = deco(f).", 2),
            ("What is a generator and how does it differ from a list?",
             "A generator yields items lazily using 'yield'. It produces values on demand and does not store the full sequence in memory.", 2),
            ("Explain the difference between deepcopy and shallow copy.",
             "A shallow copy (copy.copy) duplicates the outer object but shares references to nested objects. deepcopy recursively copies all nested objects.", 2),
            ("What are *args and **kwargs?",
             "*args collects extra positional arguments into a tuple. **kwargs collects extra keyword arguments into a dictionary.", 1),
            ("How does Python's GIL affect multithreading?",
             "The Global Interpreter Lock allows only one thread to execute Python bytecode at a time, limiting true parallelism for CPU-bound tasks. Use multiprocessing or async I/O to work around it.", 3),
            ("What is the difference between __str__ and __repr__?",
             "__repr__ returns an unambiguous string for developers (used by repr()). __str__ returns a human-readable string (used by print()). If __str__ is not defined, Python falls back to __repr__.", 2),
            ("How do you handle exceptions in Python?",
             "Use try/except blocks. 'try' contains risky code, 'except ExceptionType as e' handles it. Optional 'else' runs if no exception, 'finally' always runs.", 1),
            ("What is a lambda function?",
             "An anonymous, single-expression function: lambda x, y: x + y. It returns the value of the expression automatically.", 1),
            ("Explain Python's method resolution order (MRO).",
             "MRO determines the order in which base classes are searched when calling a method. Python 3 uses C3 linearization. Inspect it with ClassName.__mro__ or ClassName.mro().", 3),
        ],
    },
    {
        "name": "SQL",
        "description": "Relational databases: queries, joins, aggregation, schema design",
        "cards": [
            ("What is the difference between INNER JOIN and LEFT JOIN?",
             "INNER JOIN returns only rows with matches in both tables. LEFT JOIN returns all rows from the left table and matched rows from the right (NULL if no match).", 1),
            ("How does GROUP BY work?",
             "GROUP BY groups rows sharing the same value(s) in specified columns. Aggregate functions (COUNT, SUM, AVG, etc.) are then applied per group.", 1),
            ("What is a subquery?",
             "A query nested inside another query. It can appear in SELECT, FROM, or WHERE clauses. Example: SELECT * FROM t WHERE id IN (SELECT id FROM t2).", 2),
            ("Explain the difference between WHERE and HAVING.",
             "WHERE filters rows before grouping. HAVING filters groups after GROUP BY and aggregation. HAVING can reference aggregate functions; WHERE cannot.", 2),
            ("What is a foreign key constraint?",
             "A foreign key enforces referential integrity by requiring that values in a column match existing values in another table's primary key.", 1),
            ("What does EXPLAIN ANALYZE do?",
             "It executes the query and shows the query execution plan with actual timings, helping identify slow operations like full table scans.", 3),
            ("What is a database index and when should you use one?",
             "An index is a data structure (often B-tree) that speeds up lookups on a column. Use indexes on columns frequently used in WHERE, JOIN, and ORDER BY clauses.", 2),
            ("What is the difference between UNION and UNION ALL?",
             "UNION combines result sets and removes duplicates. UNION ALL keeps all rows including duplicates and is faster because it skips deduplication.", 1),
            ("Explain database normalization up to 3NF.",
             "1NF: atomic values, no repeating groups. 2NF: 1NF + no partial dependencies on composite keys. 3NF: 2NF + no transitive dependencies (non-key columns depend only on the primary key).", 3),
            ("What is a transaction and what are ACID properties?",
             "A transaction groups operations into an atomic unit. ACID: Atomicity (all or nothing), Consistency (valid state), Isolation (concurrent transactions don't interfere), Durability (committed data persists).", 2),
        ],
    },
    {
        "name": "Algorithms",
        "description": "Complexity analysis, sorting, searching, data structures",
        "cards": [
            ("What is Big-O notation?",
             "Big-O describes the upper bound of an algorithm's time or space complexity as input grows. Example: O(n) means linear growth, O(n^2) means quadratic.", 1),
            ("What is the time complexity of binary search?",
             "O(log n). It halves the search space with each comparison, requiring at most log2(n) steps.", 1),
            ("Explain how quicksort works and its average complexity.",
             "Quicksort picks a pivot, partitions elements into less-than and greater-than groups, then recursively sorts each. Average: O(n log n), worst: O(n^2) with bad pivots.", 2),
            ("What is a hash table and what is its average lookup time?",
             "A hash table maps keys to values using a hash function. Average lookup is O(1). Worst case is O(n) due to collisions.", 1),
            ("What is the difference between BFS and DFS?",
             "BFS (breadth-first) explores neighbors level by level using a queue. DFS (depth-first) explores as deep as possible first using a stack or recursion.", 2),
            ("What is dynamic programming?",
             "An optimization technique that breaks problems into overlapping subproblems and stores their solutions (memoization or tabulation) to avoid redundant computation.", 3),
            ("Explain the difference between a stack and a queue.",
             "A stack is LIFO (last in, first out): push/pop from the top. A queue is FIFO (first in, first out): enqueue at back, dequeue from front.", 1),
            ("What is the time complexity of mergesort and is it stable?",
             "Mergesort is O(n log n) in all cases (best, average, worst). It is a stable sort, meaning equal elements retain their original order.", 2),
            ("What is a balanced binary search tree?",
             "A BST where the height difference between left and right subtrees of any node is at most 1 (e.g., AVL tree). This guarantees O(log n) search, insert, and delete.", 2),
            ("Explain the concept of amortized analysis.",
             "Amortized analysis averages the cost of operations over a sequence. Example: dynamic array append is O(1) amortized even though occasional resizes cost O(n).", 3),
        ],
    },
    {
        "name": "Unix",
        "description": "Command line, file system, processes, shell scripting",
        "cards": [
            ("What does the pipe operator (|) do?",
             "It connects the stdout of one command to the stdin of the next. Example: cat file.txt | grep 'error' sends file contents to grep.", 1),
            ("How do Unix file permissions work?",
             "Three groups (owner, group, others) each get read (4), write (2), execute (1) bits. Example: chmod 755 gives rwx to owner, r-x to group and others.", 1),
            ("What is the difference between > and >> in shell redirection?",
             "> redirects output to a file, overwriting it. >> appends to the file without overwriting existing content.", 1),
            ("What does the grep command do?",
             "grep searches for lines matching a regular expression. Common flags: -i (case insensitive), -r (recursive), -n (line numbers), -v (invert match).", 1),
            ("Explain what a process and a signal are in Unix.",
             "A process is a running instance of a program with its own PID and memory. A signal is an asynchronous notification sent to a process (e.g., SIGTERM to request termination, SIGKILL to force kill).", 2),
            ("What is the difference between hard links and symbolic links?",
             "A hard link is another directory entry pointing to the same inode. A symbolic (soft) link is a file containing the path to another file. Hard links cannot cross filesystems; symlinks can.", 2),
            ("How does the find command work?",
             "find searches the directory tree. Example: find /var -name '*.log' -mtime +7 finds .log files in /var modified more than 7 days ago.", 2),
            ("What is a shell environment variable and how do you set one?",
             "An environment variable is a key-value pair available to processes. Set with export VAR=value. View with echo $VAR or env. They are inherited by child processes.", 1),
            ("What does the awk command do?",
             "awk is a text-processing language that operates on fields. Example: awk '{print $1, $3}' file.txt prints the 1st and 3rd fields of each line.", 3),
            ("Explain the Unix process lifecycle: fork, exec, wait.",
             "fork() creates a child process (copy of parent). exec() replaces the child's memory with a new program. The parent calls wait() to collect the child's exit status. This is how shells run commands.", 3),
        ],
    },
    {
        "name": "Networks",
        "description": "TCP/IP, HTTP, DNS, protocols, network architecture",
        "cards": [
            ("What is the difference between TCP and UDP?",
             "TCP is connection-oriented, reliable, and ordered (uses handshakes and retransmission). UDP is connectionless, faster, but unreliable with no guaranteed delivery or order.", 1),
            ("What happens when you type a URL in a browser?",
             "DNS resolves the domain to an IP. The browser opens a TCP connection (TLS if HTTPS). It sends an HTTP GET request. The server responds with HTML. The browser renders the page.", 2),
            ("What is DNS and how does it work?",
             "DNS (Domain Name System) translates domain names to IP addresses. The resolver queries root servers, TLD servers, then authoritative servers in a hierarchical lookup.", 1),
            ("Explain the HTTP request/response cycle.",
             "The client sends a request with a method (GET, POST, etc.), headers, and optional body. The server processes it and returns a status code (200, 404, etc.), headers, and a body.", 1),
            ("What are the layers of the OSI model?",
             "7 layers from bottom: Physical, Data Link, Network, Transport, Session, Presentation, Application. TCP operates at Transport (4), HTTP at Application (7).", 2),
            ("What is a REST API?",
             "A REST API uses HTTP methods (GET, POST, PUT, DELETE) to perform CRUD on resources identified by URLs. It is stateless: each request contains all needed context.", 1),
            ("What is the difference between HTTP and HTTPS?",
             "HTTPS adds TLS/SSL encryption over HTTP. It uses certificates to authenticate the server and encrypts data in transit, preventing eavesdropping and tampering.", 1),
            ("What is a subnet mask and what does it do?",
             "A subnet mask divides an IP address into network and host portions. Example: 255.255.255.0 (/24) means the first 24 bits are the network address, leaving 8 bits (254 usable hosts) for the subnet.", 2),
            ("Explain the TCP three-way handshake.",
             "1) Client sends SYN. 2) Server responds with SYN-ACK. 3) Client sends ACK. The connection is now established and data can flow bidirectionally.", 2),
            ("What is NAT and why is it used?",
             "NAT (Network Address Translation) maps private IPs to a public IP at the router. It conserves public IPv4 addresses and adds a layer of security by hiding internal network topology.", 3),
        ],
    },
]


def seed(db_name: str | None = None):
    """Drop existing data and seed the database with sample decks and cards."""
    init_db(db_name)
    db = get_db(db_name)
    cursor = db.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM cards")
    cursor.execute("DELETE FROM decks")

    for deck in DECKS:
        cursor.execute(
            "INSERT INTO decks (name, description) VALUES (%s, %s)",
            (deck["name"], deck["description"]),
        )
        deck_id = cursor.lastrowid

        for question, answer, difficulty in deck["cards"]:
            cursor.execute(
                "INSERT INTO cards (deck_id, question, answer, difficulty) VALUES (%s, %s, %s, %s)",
                (deck_id, question, answer, difficulty),
            )

    db.commit()
    cursor.close()
    db.close()
    print(f"Seeded {len(DECKS)} decks with {sum(len(d['cards']) for d in DECKS)} cards.")


if __name__ == "__main__":
    seed()
