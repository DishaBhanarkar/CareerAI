import re


# ============================================================
# CAREERAI SKILL VOCABULARY
# ============================================================

SKILL_ALIASES = {

    # --------------------------------------------------------
    # PROGRAMMING LANGUAGES
    # --------------------------------------------------------

    "python": ["python", "python3", "py"],

    "java": ["java", "java se", "java ee", "java programming"],

    "c++": ["c++", "cpp", "cplusplus"],

    "c": ["c programming", "c language"],

    "c#": ["c#", "c sharp", "c-sharp"],

    "javascript": [
        "javascript",
        "java script",
        "js",
        "ecmascript"
    ],

    "typescript": [
        "typescript",
        "type script",
        "ts"
    ],

    "go": [
        "golang",
        "go programming",
        "go language"
    ],

    "rust": [
        "rust",
        "rust programming"
    ],

    "php": [
        "php",
        "php programming"
    ],

    "ruby": [
        "ruby",
        "ruby programming"
    ],

    "kotlin": [
        "kotlin"
    ],

    "swift": [
        "swift",
        "swift programming"
    ],

    "r": [
        "r programming",
        "r language"
    ],

    "scala": [
        "scala"
    ],

    "dart": [
        "dart"
    ],

    "perl": [
        "perl"
    ],

    "matlab": [
        "matlab"
    ],

    "bash": [
        "bash",
        "bash scripting",
        "shell scripting",
        "shell script"
    ],

    "powershell": [
        "powershell"
    ],


    # --------------------------------------------------------
    # WEB DEVELOPMENT
    # --------------------------------------------------------

    "html": [
        "html",
        "html5"
    ],

    "css": [
        "css",
        "css3"
    ],

    "sass": [
        "sass",
        "scss"
    ],

    "tailwind css": [
        "tailwind",
        "tailwind css"
    ],

    "bootstrap": [
        "bootstrap"
    ],

    "react": [
        "react",
        "react.js",
        "reactjs"
    ],

    "next.js": [
        "next.js",
        "nextjs",
        "next js"
    ],

    "angular": [
        "angular",
        "angularjs"
    ],

    "vue.js": [
        "vue",
        "vue.js",
        "vuejs"
    ],

    "svelte": [
        "svelte",
        "sveltekit"
    ],

    "node.js": [
        "node",
        "node.js",
        "nodejs"
    ],

    "express.js": [
        "express",
        "express.js",
        "expressjs"
    ],

    "nestjs": [
        "nestjs",
        "nest.js"
    ],

    "django": [
        "django"
    ],

    "flask": [
        "flask"
    ],

    "fastapi": [
        "fastapi",
        "fast api"
    ],

    "spring": [
        "spring",
        "spring framework",
        "spring boot"
    ],

    "asp.net": [
        "asp.net",
        "aspnet",
        ".net"
    ],

    "graphql": [
        "graphql",
        "graph ql"
    ],

    "rest api": [
        "rest api",
        "restful api",
        "restful apis",
        "rest services"
    ],

    "web development": [
        "web development",
        "web development"
    ],


    # --------------------------------------------------------
    # MACHINE LEARNING
    # --------------------------------------------------------

    "machine learning": [
        "machine learning",
        "machine-learning",
        "ml"
    ],

    "deep learning": [
        "deep learning",
        "deep-learning",
        "dl"
    ],

    "supervised learning": [
        "supervised learning"
    ],

    "unsupervised learning": [
        "unsupervised learning"
    ],

    "reinforcement learning": [
        "reinforcement learning",
        "reinforcement-learning",
        "rl"
    ],

    "scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn"
    ],

    "tensorflow": [
        "tensorflow",
        "tensorflow 2"
    ],

    "pytorch": [
        "pytorch",
        "py torch"
    ],

    "keras": [
        "keras"
    ],

    "xgboost": [
        "xgboost",
        "xg boost"
    ],

    "lightgbm": [
        "lightgbm",
        "light gbm"
    ],

    "catboost": [
        "catboost",
        "cat boost"
    ],

    "mlops": [
        "mlops",
        "ml ops"
    ],

    "model deployment": [
        "model deployment",
        "ml deployment",
        "machine learning deployment"
    ],

    "feature engineering": [
        "feature engineering"
    ],

    "feature selection": [
        "feature selection"
    ],

    "hyperparameter tuning": [
        "hyperparameter tuning",
        "hyperparameter optimization"
    ],

    "cross validation": [
        "cross validation",
        "cross-validation"
    ],

    "time series": [
        "time series",
        "time-series forecasting"
    ],


    # --------------------------------------------------------
    # ARTIFICIAL INTELLIGENCE
    # --------------------------------------------------------

    "artificial intelligence": [
        "artificial intelligence",
        "artificial-intelligence",
        "ai"
    ],

    "natural language processing": [
        "natural language processing",
        "nlp",
        "natural-language processing"
    ],

    "computer vision": [
        "computer vision",
        "computer-vision",
        "cv"
    ],

    "speech recognition": [
        "speech recognition",
        "speech-to-text",
        "speech to text"
    ],

    "image processing": [
        "image processing",
        "digital image processing"
    ],

    "pattern recognition": [
        "pattern recognition"
    ],

    "recommendation systems": [
        "recommendation system",
        "recommendation systems",
        "recommender systems"
    ],

    "generative ai": [
        "generative ai",
        "generative artificial intelligence",
        "gen ai",
        "genai"
    ],

    "large language models": [
        "large language model",
        "large language models",
        "llm",
        "llms"
    ],

    "transformers": [
        "transformers",
        "transformer architecture",
        "transformer models"
    ],

    "hugging face": [
        "hugging face",
        "huggingface"
    ],

    "bert": [
        "bert",
        "bidirectional encoder representations from transformers"
    ],

    "gpt": [
        "gpt",
        "gpt models"
    ],

    "rag": [
        "rag",
        "retrieval augmented generation",
        "retrieval-augmented generation"
    ],

    "prompt engineering": [
        "prompt engineering",
        "prompt design"
    ],

    "fine tuning": [
        "fine tuning",
        "fine-tuning",
        "model fine tuning"
    ],

    "embeddings": [
        "embeddings",
        "text embeddings",
        "vector embeddings"
    ],

    "vector database": [
        "vector database",
        "vector databases",
        "vector db",
        "vector dbs"
    ],

    "langchain": [
        "langchain"
    ],

    "langgraph": [
        "langgraph",
        "lang graph"
    ],

    "llamaindex": [
        "llamaindex",
        "llama index"
    ],

    "agents": [
        "ai agents",
        "ai agent",
        "autonomous agents"
    ],


    # --------------------------------------------------------
    # COMPUTER VISION
    # --------------------------------------------------------

    "opencv": [
        "opencv",
        "open cv"
    ],

    "yolo": [
        "yolo",
        "yolo v5",
        "yolo v8",
        "yolo v9",
        "yolo v10",
        "yolo v11"
    ],

    "object detection": [
        "object detection"
    ],

    "image segmentation": [
        "image segmentation",
        "semantic segmentation",
        "instance segmentation"
    ],

    "image classification": [
        "image classification"
    ],

    "ocr": [
        "ocr",
        "optical character recognition"
    ],

    "face recognition": [
        "face recognition",
        "facial recognition"
    ],

    "face detection": [
        "face detection",
        "facial detection"
    ],

    "cnn": [
        "cnn",
        "convolutional neural network",
        "convolutional neural networks"
    ],

    "resnet": [
        "resnet",
        "resnet50",
        "resnet 50"
    ],

    "densenet": [
        "densenet",
        "densenet121"
    ],

    "unet": [
        "unet",
        "u-net"
    ],

    "grad-cam": [
        "grad-cam",
        "gradcam",
        "grad cam"
    ],


    # --------------------------------------------------------
    # DATA SCIENCE
    # --------------------------------------------------------

    "data science": [
        "data science",
        "data-science"
    ],

    "data analysis": [
        "data analysis",
        "data analytics"
    ],

    "data visualization": [
        "data visualization",
        "data visualisation"
    ],

    "pandas": [
        "pandas"
    ],

    "numpy": [
        "numpy",
        "num py"
    ],

    "scipy": [
        "scipy"
    ],

    "matplotlib": [
        "matplotlib"
    ],

    "seaborn": [
        "seaborn"
    ],

    "plotly": [
        "plotly"
    ],

    "jupyter": [
        "jupyter",
        "jupyter notebook",
        "jupyter notebooks"
    ],

    "statistics": [
        "statistics",
        "statistical analysis"
    ],

    "probability": [
        "probability",
        "probability theory"
    ],

    "data cleaning": [
        "data cleaning",
        "data cleansing"
    ],

    "data preprocessing": [
        "data preprocessing",
        "data pre-processing"
    ],

    "exploratory data analysis": [
        "exploratory data analysis",
        "eda"
    ],


    # --------------------------------------------------------
    # DATABASES
    # --------------------------------------------------------

    "sql": [
        "sql",
        "structured query language"
    ],

    "mysql": [
        "mysql"
    ],

    "postgresql": [
        "postgresql",
        "postgres"
    ],

    "oracle database": [
        "oracle database",
        "oracle db"
    ],

    "mongodb": [
        "mongodb",
        "mongo db"
    ],

    "sqlite": [
        "sqlite"
    ],

    "redis": [
        "redis"
    ],

    "firebase": [
        "firebase"
    ],

    "dynamodb": [
        "dynamodb",
        "dynamo db"
    ],

    "cassandra": [
        "cassandra"
    ],

    "database management": [
        "database management",
        "database management systems",
        "dbms"
    ],

    "nosql": [
        "nosql",
        "no sql"
    ],


    # --------------------------------------------------------
    # CLOUD
    # --------------------------------------------------------

    "aws": [
        "aws",
        "amazon web services"
    ],

    "azure": [
        "azure",
        "microsoft azure"
    ],

    "google cloud": [
        "google cloud",
        "google cloud platform",
        "gcp"
    ],

    "aws ec2": [
        "ec2",
        "aws ec2"
    ],

    "aws s3": [
        "s3",
        "aws s3"
    ],

    "aws lambda": [
        "lambda",
        "aws lambda"
    ],

    "cloud computing": [
        "cloud computing",
        "cloud architecture"
    ],

    "cloud deployment": [
        "cloud deployment"
    ],


    # --------------------------------------------------------
    # DEVOPS
    # --------------------------------------------------------

    "docker": [
        "docker",
        "docker containers",
        "containerization",
        "containerisation"
    ],

    "kubernetes": [
        "kubernetes",
        "k8s"
    ],

    "jenkins": [
        "jenkins"
    ],

    "ci/cd": [
        "ci/cd",
        "ci cd",
        "continuous integration",
        "continuous deployment",
        "continuous delivery"
    ],

    "github actions": [
        "github actions"
    ],

    "gitlab ci": [
        "gitlab ci",
        "gitlab-ci"
    ],

    "terraform": [
        "terraform"
    ],

    "ansible": [
        "ansible"
    ],

    "prometheus": [
        "prometheus"
    ],

    "grafana": [
        "grafana"
    ],

    "nginx": [
        "nginx"
    ],


    # --------------------------------------------------------
    # VERSION CONTROL
    # --------------------------------------------------------

    "git": [
        "git",
        "git version control"
    ],

    "github": [
        "github"
    ],

    "gitlab": [
        "gitlab"
    ],

    "bitbucket": [
        "bitbucket"
    ],

    "version control": [
        "version control",
        "source control"
    ],


    # --------------------------------------------------------
    # MOBILE DEVELOPMENT
    # --------------------------------------------------------

    "android": [
        "android",
        "android development"
    ],

    "android studio": [
        "android studio"
    ],

    "flutter": [
        "flutter"
    ],

    "react native": [
        "react native",
        "react-native"
    ],

    "ios development": [
        "ios development",
        "ios app development"
    ],

    "swiftui": [
        "swiftui",
        "swift ui"
    ],


    # --------------------------------------------------------
    # CYBERSECURITY
    # --------------------------------------------------------

    "cybersecurity": [
        "cybersecurity",
        "cyber security",
        "cyber-security"
    ],

    "network security": [
        "network security"
    ],

    "information security": [
        "information security",
        "infosec"
    ],

    "ethical hacking": [
        "ethical hacking"
    ],

    "penetration testing": [
        "penetration testing",
        "penetration testing",
        "pentesting"
    ],

    "vulnerability assessment": [
        "vulnerability assessment"
    ],

    "cryptography": [
        "cryptography",
        "cryptographic algorithms"
    ],

    "encryption": [
        "encryption"
    ],

    "firewalls": [
        "firewall",
        "firewalls"
    ],

    "siem": [
        "siem",
        "security information and event management"
    ],

    "wireshark": [
        "wireshark"
    ],

    "metasploit": [
        "metasploit"
    ],

    "burp suite": [
        "burp suite",
        "burpsuite"
    ],

    "penetration testing": [
        "penetration testing",
        "pentesting"
    ],


    # --------------------------------------------------------
    # SOFTWARE ENGINEERING
    # --------------------------------------------------------

    "object oriented programming": [
        "object oriented programming",
        "object-oriented programming",
        "oop"
    ],

    "data structures": [
        "data structures",
        "data structure"
    ],

    "algorithms": [
        "algorithms",
        "algorithm design"
    ],

    "design patterns": [
        "design patterns"
    ],

    "software development": [
        "software development"
    ],

    "software engineering": [
        "software engineering"
    ],

    "system design": [
        "system design"
    ],

    "microservices": [
        "microservices",
        "microservice architecture"
    ],

    "api development": [
        "api development"
    ],

    "unit testing": [
        "unit testing",
        "unit tests"
    ],

    "integration testing": [
        "integration testing"
    ],

    "test automation": [
        "test automation"
    ],

    "selenium": [
        "selenium"
    ],

    "pytest": [
        "pytest"
    ],

    "junit": [
        "junit"
    ],


    # --------------------------------------------------------
    # BUSINESS / ANALYTICS
    # --------------------------------------------------------

    "power bi": [
        "power bi",
        "powerbi"
    ],

    "tableau": [
        "tableau"
    ],

    "microsoft excel": [
        "microsoft excel",
        "excel",
        "ms excel"
    ],

    "vba": [
        "vba",
        "visual basic for applications"
    ],

    "business intelligence": [
        "business intelligence",
        "bi"
    ],

    "business analytics": [
        "business analytics"
    ],

    "data analytics": [
        "data analytics"
    ],


    # --------------------------------------------------------
    # PROJECT / MANAGEMENT TOOLS
    # --------------------------------------------------------

    "jira": [
        "jira"
    ],

    "confluence": [
        "confluence"
    ],

    "trello": [
        "trello"
    ],

    "asana": [
        "asana"
    ],

    "slack": [
        "slack"
    ],

    "agile": [
        "agile",
        "agile methodology"
    ],

    "scrum": [
        "scrum"
    ],

    "kanban": [
        "kanban"
    ],

    "project management": [
        "project management"
    ],


    # --------------------------------------------------------
    # OPERATING SYSTEMS
    # --------------------------------------------------------

    "linux": [
        "linux"
    ],

    "ubuntu": [
        "ubuntu"
    ],

    "windows": [
        "windows",
        "windows os"
    ],

    "macos": [
        "macos",
        "mac os"
    ],


    # --------------------------------------------------------
    # HARDWARE / EMBEDDED
    # --------------------------------------------------------

    "arduino": [
        "arduino"
    ],

    "raspberry pi": [
        "raspberry pi",
        "raspberrypi"
    ],

    "embedded systems": [
        "embedded systems",
        "embedded system"
    ],

    "iot": [
        "iot",
        "internet of things"
    ],

    "robotics": [
        "robotics"
    ],

    "arduino ide": [
        "arduino ide"
    ],


    # --------------------------------------------------------
    # QUANTUM COMPUTING
    # --------------------------------------------------------

    "quantum computing": [
        "quantum computing"
    ],

    "qiskit": [
        "qiskit"
    ],

    "quantum machine learning": [
        "quantum machine learning",
        "qml"
    ],

    "quantum algorithms": [
        "quantum algorithms"
    ],


    # --------------------------------------------------------
    # BLOCKCHAIN
    # --------------------------------------------------------

    "blockchain": [
        "blockchain"
    ],

    "ethereum": [
        "ethereum"
    ],

    "solidity": [
        "solidity"
    ],

    "smart contracts": [
        "smart contracts",
        "smart contract"
    ],

    "web3": [
        "web3",
        "web 3"
    ],


    # --------------------------------------------------------
    # SOFT SKILLS
    # --------------------------------------------------------

    "communication": [
        "communication",
        "communication skills",
        "verbal communication"
    ],

    "leadership": [
        "leadership",
        "leadership skills"
    ],

    "teamwork": [
        "teamwork",
        "team work",
        "team collaboration"
    ],

    "problem solving": [
        "problem solving",
        "problem-solving"
    ],

    "critical thinking": [
        "critical thinking"
    ],

    "time management": [
        "time management"
    ],

    "adaptability": [
        "adaptability"
    ],

    "creativity": [
        "creativity"
    ],

    "presentation skills": [
        "presentation skills",
        "presentation"
    ],

    "public speaking": [
        "public speaking"
    ],

    "collaboration": [
        "collaboration"
    ],

    "research": [
        "research",
        "research skills"
    ],

    "analytical thinking": [
        "analytical thinking"
    ]
}


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):
    """
    Makes text easier to search while preserving
    important characters used in technical skills.
    """

    text = text.lower()

    text = text.replace("–", "-")
    text = text.replace("—", "-")
    text = text.replace("’", "'")

    # Normalize repeated whitespace
    text = re.sub(r"\s+", " ", text)

    return text


# ============================================================
# SKILL DETECTION
# ============================================================

def contains_skill(text, phrase):
    """
    Checks whether a skill/alias exists as a meaningful
    phrase inside the text.
    """

    phrase = phrase.lower().strip()

    # Technical symbols such as C++, C#, .NET need
    # slightly different matching.
    escaped = re.escape(phrase)

    if phrase in ["c++", "cpp", "cplusplus"]:
        return re.search(r"(?<!\w)c\+\+(?!\w)", text) is not None

    if phrase in ["c#", "c sharp", "c-sharp"]:
        return re.search(r"(?<!\w)c(?:#| sharp|[- ]sharp)(?!\w)", text) is not None

    if phrase in [".net", "asp.net", "aspnet"]:
        return re.search(r"(?<!\w)(?:\.net|asp\.net|aspnet)(?!\w)", text) is not None

    # Normal word/phrase matching
    pattern = r"(?<!\w)" + escaped + r"(?!\w)"

    return re.search(pattern, text) is not None


def extract_skills(text):
    """
    Extract canonical skills from resume or job description.
    """

    text = normalize_text(text)

    found_skills = []

    for canonical_skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            if contains_skill(text, alias):

                found_skills.append(canonical_skill)

                break

    return found_skills


# ============================================================
# MATCH RESUME WITH JOB
# ============================================================

def match_resume_to_job(resume_text, job_description):

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    matched_skills = [
        skill
        for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill
        for skill in job_skills
        if skill not in resume_skills
    ]

    if len(job_skills) > 0:

        match_score = round(
            (len(matched_skills) / len(job_skills)) * 100
        )

    else:

        match_score = 0

    return {

        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "match_score": match_score
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    resume = """
    AI Engineering student with experience in Python,
    SQL, Machine Learning, TensorFlow, OpenCV,
    React, Flask, GitHub, Docker and NLP.
    """

    job = """
    We are looking for an AI/ML Engineer.

    Requirements:

    Python
    SQL
    Machine Learning
    TensorFlow
    PyTorch
    Docker
    NLP
    React
    AWS
    Kubernetes
    """

    result = match_resume_to_job(
        resume,
        job
    )

    print("\n================================")
    print("       CAREERAI MATCH RESULT")
    print("================================\n")

    print("Resume Skills:")
    print(result["resume_skills"])

    print("\nJob Skills:")
    print(result["job_skills"])

    print("\nMatched Skills:")
    print(result["matched_skills"])

    print("\nMissing Skills:")
    print(result["missing_skills"])

    print("\nMatch Score:")
    print(str(result["match_score"]) + "%")