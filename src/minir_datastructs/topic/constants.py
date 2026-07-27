


HEURISTIC_VERSION = '1.3.0'
DEFAULT_KEYWORDS_FILENAME = "topic_keywords.json"

DEFAULT_TOPIC_KEYWORDS = {
    'Machine Learning': ['machine learning', 'ml', 'sklearn', 'tensorflow', 'pytorch', 'keras', 'neural network', 'deep learning', 'classification', 'regression', 'clustering', 'nlp', 'natural language', 'computer vision', 'data science', 'ai', 'artificial intelligence', 'transformer', 'diffusion model', 'llm', 'large language model'],
    'Python': ['python', 'def', 'class', 'import', 'list', 'dict', 'tuple', 'lambda', 'yield', 'async', 'await', 'decorator', 'generator', 'pip', 'conda', 'django', 'flask', 'fastapi', 'pandas', 'numpy', 'scipy', 'asyncio', 'cython', 'pytest'],
    'Web Development': ['html', 'css', 'javascript', 'typescript', 'react', 'angular', 'vue', 'svelte', 'node.js', 'express', 'http', 'https', 'api', 'rest', 'graphql', 'frontend', 'backend', 'server', 'client', 'web', 'docker', 'nginx', 'apache', 'websocket', 'ssr', 'spa', 'pwa'],
    'Data Engineering': ['data', 'pipeline', 'etl', 'elt', 'database', 'sql', 'nosql', 'postgres', 'mysql', 'mongodb', 'spark', 'hadoop', 'kafka', 'airflow', 'dbt', 'big data', 'schema', 'warehouse', 'lakehouse', 'data modeling', 'streaming'],
    'DevOps Infrastructure': ['docker', 'kubernetes', 'k8s', 'aws', 'azure', 'gcp', 'cloud', 'ci/cd', 'jenkins', 'gitlab ci', 'github actions', 'terraform', 'ansible', 'puppet', 'chef', 'monitoring', 'logging', 'prometheus', 'grafana', 'elk', 'infrastructure', 'server', 'network', 'security', 'vpc', 'iam', 'sre'],
    'XML Processing': ['xml', 'xslt', 'xpath', 'schema', 'xsd', 'dtd', 'namespace', 'soap', 'rss', 'atom', 'sax', 'dom', 'etree', 'lxml'],
    'JSON Processing': ['json', 'schema', 'api', 'rest', 'data interchange', 'key', 'value', 'json-ld', 'parsing', 'serialization', 'deserialization'],

    'Documentation Guides': ['guide', 'tutorial', 'documentation', 'readme', 'how-to', 'example', 'introduction', 'reference', 'getting started', 'usage', 'api docs', 'contributing'],
    'Text Analysis NLP': ['text analysis', 'nlp', 'spacy', 'nltk', 'linguistics', 'corpus', 'topic modeling', 'lda', 'sentiment analysis', 'ner', 'named entity recognition', 'pos tagging', 'lemmatization', 'tokenization', 'embeddings', 'word2vec', 'bert'],
    'Testing': ['test', 'testing', 'unittest', 'pytest', 'mock', 'assertion', 'coverage', 'integration test', 'e2e', 'selenium', 'playwright', 'bdd', 'tdd'],
    'Security': ['security', 'vulnerability', 'exploit', 'encryption', 'authentication', 'authorization', 'owasp', 'penetration testing', 'firewall', 'tls', 'ssl', 'jwt', 'oauth'],
    'Algorithms Data Structures': ['algorithm', 'data structure', 'complexity', 'big o', 'sorting', 'searching', 'graph', 'tree', 'hash map', 'linked list', 'dynamic programming'],
    'Operating Systems': ['linux', 'unix', 'windows', 'macos', 'kernel', 'process', 'thread', 'memory management', 'file system', 'bash', 'shell', 'powershell'],
    'Networking': ['network', 'tcp', 'udp', 'ip', 'http', 'dns', 'socket', 'routing', 'subnet', 'firewall', 'vpn'],
}



N_TOP_KEYWORDS = 15
MIN_TFIDF_SCORE = 0.1

CHUNK_SIZE = 1024 * 1024
MAX_FILE_SIZE_FULL_PROCESS = 10 * 1024 * 1024
MAX_SAMPLE_SIZE = 2 * 1024 * 1024





FILE_TYPE_MAPPING = {
    '.py': 'python', '.pyw': 'python', '.txt': 'text', '.md': 'markdown',
    '.markdown': 'markdown', '.json': 'json', '.xml': 'xml', '.log': 'text',
    '.csv': 'text', '.html': 'xml', '.yaml': 'text', '.yml': 'text',
    '.sh': 'text', '.bash': 'text', '.js': 'text', '.ts': 'text',
    '.java': 'text', '.c': 'text', '.cpp': 'text', '.h': 'text', '.cs': 'text'
}


