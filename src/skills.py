"""Collects dictionaries of skills needed to build Entity Ruler"""

# TIER 1 - PHRASES, matched in ANY case
# Taxonomy labels, copied as-is.

TIER1_PHRASES = [
    "Systemarkitektur",  # New
    "Verksamhetsutveckling",  # New
    "Cybersäkerhet",  # New
    "Oracle SOA Suite",  # New
    "Docker",
    "IBM Cloud",
    "Sun Java Enterprise System",
    "Windows Server",
    "Associate Android Developer",
    "Oracle Certified Associate",
    "PHP Developer Certification",
    "AWS Certified Solutions Architect",  # New
    "Clojure",
    "ClojureScript",
    "CoffeeScript",
    "Datalog",
    "Elixir",
    "OCaml",
    "OpenEdge Advanced Business Language",
    "PowerScript",
    "TypeScript",
    "Vyper",
    "XQuery",
    "Python",  # New
    "Java",  # New
    "JavaScript",  # New
    "MATLAB",  # New
    "Bash",  # New
    "SQL",  # New
    "GraphQL",  # New
    "Citrix",
    "IBM MQ",
    "TIBCO",
    "Oracle Fusion Middleware",
    "Software AG Integration Suite",
    "Databricks",  # New
    "Informatica",  # New
    "Bower",
    "Grunt",
    "Vagrant",
    "Jenkins",
    "Azure DevOps",
    "ASP.NET Core",
    "ASP.NET MVC",
    "Eclipselink",
    "Hibernate",
    "spaCy",
    "TensorFlow",
    "FastAPI",
    "OpenJPA",
    "Toplink",
    "Amazon Linux",  # New
    "Arch Linux",  # New
    "FreeBSD",  # New
    "Gentoo Linux",  # New
    "Kali Linux",  # New
    "Mac OS X",
    "openEuler",  # New
    "Oracle Linux",  # New
    "BlackBerry",
    "OS/390",
    "OS/400",
    "Rocky Linux",  # New
    "Datawarehouse",
    "Git",  # New
    "Informationsmodellering",
    "Informationsstrategi",
    "Kanban",
    "Masterdata",
    "Parallell programmering",
    "Ubuntu",
    "Scrum",
    "DevOps",
    "ArchiMate",
    # added after validation
    "Snowflake",
    "Terraform",
    "Microsoft Fabric",
    "Lakehouse",
    "Dataverse",
    "Dagster",
    "Ansible",
    "LangSmith",
    "Ragas",
    "LlamaIndex",
    "LangChain",
    "Simulink",
    "Kerberos",
    "Fiori",
    "DP-600",
    "DP-700",
    "Output management",
    "Data storytelling",
    "Systemutveckling",
    "Systemdesign",
    "Kravarbete",
    "Integrationer",
    "Federation",
    "SAP-miljöer",
    "SAP-transaktioner",
    "VMware",
]


# TIER 2 - EXACT CASE, short or ambiguous words
# {canonical skill: [exact spellings]}

TIER2_EXACT_CASE = {
    "A+": ["A+"],
    "Odoo": ["Odoo"],
    "SAP": ["SAP"],
    "R": ["R"],
    "Dart": ["Dart"],
    "Julia": ["Julia"],  # New
    "Scala": ["Scala"],  # New
    "SAS": ["SAS"],  # New
    "Cypher": ["Cypher"],  # New
    "C++": ["C++"],  # New
    "LDAP": ["LDAP"],
    "LINQ": ["LINQ"],
    "MDX": ["MDX"],
    "N1QL": ["N1QL"],
    "SPARQL": ["SPARQL"],
    "DAX": ["DAX"],  # New
    "dbt": ["dbt"],  # New
    "SOAP": ["SOAP"],
    "Ethics": ["ETHICS"],
    "ISAC": ["ISAC"],
    "OOS": ["OOS"],
    "SOLID": ["SOLID"],
    "LSE": ["LSE"],
    "Logic": ["Logic"],
    "SVEA": ["SVEA"],
    "AIX": ["AIX"],  # New
    "CentOS": ["CentOS"],  # New
    "DOS": ["DOS"],
    "GNU": ["GNU"],
    "iOS": ["iOS", "IOS"],
    "IRIX": ["IRIX"],
    "JCL": ["JCL"],
    "MVS": ["MVS"],
    "VSE": ["VSE"],
    "TCP/IP": ["TCP/IP"],
    "HTTP/HTTPS": ["HTTP", "HTTPS", "HTTP/HTTPS"],
    "ISO/IEC 25010": ["ISO/IEC 25010"],
    "ISO/IEC 20000": ["ISO/IEC 20000"],
    "ISO/IEC 12207": ["ISO/IEC 12207"],
    "ISO/IEC 330XX": ["ISO/IEC 330XX", "SPICE"],
    "3G": ["3G"],
    "4G": ["4G"],
    "5G": ["5G"],
    # added after validation
    "API": ["API", "APIs"],
    "DOORS": ["DOORS"],
    "SAML": ["SAML"],
    "SCIM": ["SCIM"],
    "PKI": ["PKI"],
    "LDAP": ["LDAP"],
    "OAuth": ["OAuth", "OAUTH"],
    "SysML": ["SysML"],
    "Hex": ["Hex"],
    "BTP": ["BTP"],
    "aATP": ["aATP"],
}


# TIER 3 - CUSTOM ALIASES
# {canonical skill: {"any_case": [...], "exact_case": [...]}}

TIER3_CUSTOM = {
    "Internet Information Services": {
        "any_case": [
            "Internet Information Services",
            "Internet Information Services (IIS)",
        ],
        "exact_case": ["IIS"],
    },
    "Oracle Cloud Infrastructure": {
        "any_case": [
            "Oracle Cloud Infrastructure",
            "Oracle Cloud Infrastructure (OCI)",
            "Oracle Cloud",
        ],
        "exact_case": ["OCI"],
    },  # New
    "Amazon Web Services": {
        "any_case": ["Amazon Web Services", "Amazon Web Services (AWS)"],
        "exact_case": ["AWS"],
    },
    "Infor": {
        "any_case": ["Infor OS", "Infor CloudSuite"],
        "exact_case": ["Infor"],
    },
    "Microsoft Dynamics 365": {
        "any_case": ["Microsoft Dynamics 365", "Dynamics 365"],
        "exact_case": ["D365"],
    },
    "Office SharePoint Server": {
        "any_case": [
            "Office SharePoint Server",
            "Office SharePoint Server (MOSS)",
            "SharePoint Server",
            "SharePoint",
            "SharePoint Online",
        ],
        "exact_case": ["MOSS"],
    },
    "Oracle JCAPS": {
        "any_case": [
            "Oracle JCAPS",
            "Oracle Java CAPS",
            "Java Composite Application Platform Suite",
        ],
        "exact_case": ["Java CAPS"],
    },
    "Oracle Service Bus": {
        "any_case": ["Oracle Service Bus", "Oracle Service Bus (OSB)"],
        "exact_case": ["OSB"],
    },  # New
    "Oracle NetSuite": {
        "any_case": ["Oracle NetSuite", "NetSuite"],
    },
    "Salesforce Cloud": {
        "any_case": ["Salesforce Cloud", "Service Cloud", "Sales Cloud", "Salesforce"],
    },
    "MuleSoft Anypoint Platform": {
        "any_case": ["MuleSoft Anypoint Platform", "Mulesoft-plattformen", "MuleSoft"],
    },  # New
    "Red Hat OpenShift": {
        "any_case": ["Red Hat OpenShift", "OpenShift"],
    },  # New
    "AZ-204: Developing Solutions for Microsoft Azure": {
        "any_case": [
            "AZ-204: Developing Solutions for Microsoft Azure",
            "Developing Solutions for Microsoft Azure",
        ],
        "exact_case": ["AZ-204"],
    },
    "AZ-900: Microsoft Azure Fundamentals": {
        "any_case": [
            "AZ-900: Microsoft Azure Fundamentals",
            "Microsoft Azure Fundamentals",
        ],
        "exact_case": ["AZ-900"],
    },
    "MB-600: Microsoft Dynamics 365 Power Platform Solution Architect": {
        "any_case": [
            "MB-600: Microsoft Dynamics 365 Power Platform Solution Architect",
            "Dynamics 365 + Power Platform Solution Architect Expert",
        ],
        "exact_case": ["MB-600"],
    },
    "Microsoft 365 Certified: Fundamentals": {
        "any_case": [
            "Microsoft 365 Certified: Fundamentals",
            "Microsoft Certified: Fundamentals",
        ],
        "exact_case": ["MS-900"],
    },
    "Microsoft Certified: Application Developer": {
        "any_case": [
            "Microsoft Certified: Application Developer",
            "Microsoft Certified: Application Developer (MCAD)",
        ],
        "exact_case": ["MCAD"],
    },
    "Microsoft Certified: Database Administrator": {
        "any_case": [
            "Microsoft Certified: Database Administrator",
            "Microsoft Certified: Database Administrator (MCDBA)",
        ],
        "exact_case": ["MCDBA"],
    },
    "Microsoft Certified: Professional": {
        "any_case": [
            "Microsoft Certified: Professional",
            "Microsoft Certified: Professional (MCP)",
        ],
    },
    "Microsoft Certified: Solution Developer": {
        "any_case": [
            "Microsoft Certified: Solution Developer",
            "Microsoft Certified: Solution Developer (MCSD)",
        ],
        "exact_case": ["MCSD"],
    },
    "Microsoft Certified: System Engineer": {
        "any_case": [
            "Microsoft Certified: System Engineer",
            "Microsoft Certified: System Engineer (MCSE)",
        ],
        "exact_case": ["MCSE"],
    },
    "Microsoft Certified: Azure Administrator Associate": {
        "any_case": ["Microsoft Certified: Azure Administrator Associate"],
    },
    "Microsoft Certified: Azure Solutions Architect Expert": {
        "any_case": [
            "Microsoft Certified: Azure Solutions Architect Expert",
            "Azure Solutions Architect Expert",
        ],
    },  # New
    "Oracle Certified Database Administrator": {
        "any_case": [
            "Oracle Certified Database Administrator",
            "Oracle Certified Database Administrator (OCDBA)",
        ],
        "exact_case": ["OCDBA"],
    },
    "Oracle Certified Database Operator": {
        "any_case": [
            "Oracle Certified Database Operator",
            "Oracle Certified Database Operator (DBO)",
        ],
        "exact_case": ["DBO"],
    },
    "Oracle Certified Professional": {
        "any_case": [
            "Oracle Certified Professional",
            "Oracle Certified Professional/OCP",
            "Oracle Certified Professional (OCP)",
        ],
    },
    "Certified Business Analysis Professional": {
        "any_case": [
            "Certified Business Analysis Professional",
            "Certified Business Analysis Professional (CBAP)",
        ],
        "exact_case": ["CBAP"],
    },  # New
    "Entry Certificate in Business Analysis": {
        "any_case": [
            "Entry Certificate in Business Analysis",
            "Entry Certificate in Business Analysis (ECBA)",
        ],
        "exact_case": ["ECBA"],
    },  # New
    "TOGAF-certifiering": {
        "any_case": ["TOGAF-certifiering"],
        "exact_case": ["TOGAF"],
    },  # New
    "Certified JavaScript Developer": {
        "any_case": [
            "Certified JavaScript Developer",
            "JavaScript Developer-certifiering",
        ],
    },  # New
    "Windows Azure": {
        "any_case": ["Microsoft Azure", "Windows Azure", "Azure"],
    },
    "Google Cloud Platform": {
        "any_case": ["Google Cloud", "Google Cloud Platform"],
        "exact_case": ["GCP"],
    },
    "Kubernetes": {"any_case": ["Kubernetes"], "exact_case": ["K8s"]},  # New
    "Apache Kafka": {
        "any_case": ["Apache Kafka", "Kafka"],
    },
    "Apache Tomcat": {
        "any_case": ["Apache Tomcat", "Tomcat"],
    },
    "Weblogic Server": {
        "any_case": ["Weblogic Server", "WebLogic", "Oracle WebLogic"],
    },
    "JBoss Application Server": {
        "any_case": ["JBoss Application Server", "JBoss", "JBoss EAP"],
    },
    "IBM WebSphere": {
        "any_case": ["IBM WebSphere", "WebSphere"],
    },
    "Glassfish Server": {
        "any_case": ["Glassfish Server", "GlassFish"],
    },
    "IBM Domino": {
        "any_case": ["IBM Domino", "HCL Domino", "Lotus Domino"],
    },
    "Java Server Pages (JSP)": {
        "any_case": [
            "Java Server Pages (JSP)",
            "Java Server Pages",
            "JavaServer Pages",
        ],
        "exact_case": ["JSP"],
    },
    "IBM Integration Bus": {
        "any_case": ["IBM Integration Bus"],
        "exact_case": ["IIB"],
    },
    "JBoss Enterprise Middleware Suite (JEMS)": {
        "any_case": [
            "JBoss Enterprise Middleware Suite (JEMS)",
            "JBoss Enterprise Middleware Suite",
        ],
        "exact_case": ["JEMS"],
    },
    "Microsoft BizTalk": {
        "any_case": ["Microsoft BizTalk", "BizTalk"],
    },
    "Oracle Data Integrator": {
        "any_case": ["Oracle Data Integrator"],
        "exact_case": ["ODI"],
    },
    "Software AG webMethods": {
        "any_case": ["Software AG webMethods", "webMethods"],
    },
    "Apache Airflow": {  # New
        "any_case": ["Apache Airflow"],
        "exact_case": ["Airflow"],
    },
    "Azure Data Factory": {  # New
        "any_case": ["Azure Data Factory"],
        "exact_case": ["ADF"],
    },
    "Apache Spark": {  # New
        "any_case": ["Apache Spark", "PySpark"],
        "exact_case": ["Spark"],
    },
    "Apache NiFi": {  # New
        "any_case": ["Apache NiFi", "NiFi"],
    },
    "Power Automate": {  # New
        "any_case": ["Power Automate", "Microsoft Power Automate"],
    },
    "Bluetooth-teknik": {
        "any_case": ["Bluetooth-teknik", "Bluetooth"],
        "exact_case": ["BLE"],
    },
    "IP-telefoniteknik": {
        "any_case": ["IP-telefoniteknik", "IP-telefoni", "VoIP"],
    },
    "IR-teknik": {
        "any_case": ["IR-teknik", "infraröd teknik"],
    },
    "Local Interconnect Network (LIN)": {
        "any_case": [
            "Local Interconnect Network (LIN)",
            "Local Interconnect Network",
            "LIN-buss",
        ],
        "exact_case": ["LIN"],
    },
    "Object Component Model/COM": {
        "any_case": ["Component Object Model", "Object Component Model"],
        "exact_case": ["COM"],
    },
    "REST": {
        "any_case": ["RESTful", "REST API", "REST-API"],
        "exact_case": ["REST"],
    },
    "RFID-teknik": {
        "any_case": ["RFID-teknik", "RFID"],
    },
    "XML Web Services": {
        "any_case": ["XML Web Services", "XML Web Service"],
    },
    "Ledningssystem (ISO 9000-serien)": {
        "any_case": ["Ledningssystem (ISO 9000-serien)", "ISO 9000-serien"],
        "exact_case": ["ISO 9000"],
    },
    "Quality Assurance (QA)": {
        "any_case": ["Quality Assurance (QA)", "Quality Assurance", "kvalitetssäkring"],
        "exact_case": ["QA"],
    },
    "VoLTE": {
        "any_case": ["VoLTE", "Voice over LTE"],
    },
    "IP Multimedia Subsystem (IMS)": {
        "any_case": ["IP Multimedia Subsystem (IMS)", "IP Multimedia Subsystem"],
        "exact_case": ["IMS"],
    },
    "Mobile Core Network": {
        "any_case": [
            "Mobile Core",
            "Core Network",
            "Mobile Core Network",
        ],
    },
    "RAN": {
        "any_case": ["Radio Access Network", "Radio Access Networks"],
        "exact_case": ["RAN"],
    },
    "eSIM": {
        "any_case": ["eSIM", "embedded SIM", "embedded SIM card"],
    },
    "Nätverksdesign": {
        "any_case": [
            "nätverksdesign",
            "network design",
            "design av nätverk",
            "nätverksarkitektur",
        ],
    },
    "Nätverksteknik": {
        "any_case": ["nätverksteknik", "network technology", "networking"],
    },
    "VLAN": {
        "any_case": ["Virtual LAN", "Virtual Local Area Network"],
        "exact_case": ["VLAN"],
    },
    "VPN": {"any_case": ["Virtual Private Network"], "exact_case": ["VPN"]},
    "WLAN / WiFi": {
        "any_case": [
            "Wireless LAN",
            "Wireless Local Area Network",
        ],
        "exact_case": ["WLAN", "WiFi"],
    },
    "Routing & Switching": {
        "any_case": [
            "Routing & Switching",
            "Routing and Switching",
            "routing och switching",
        ],
    },
    "SD-WAN": {
        "any_case": [
            "SD-WAN",
            "Software Defined WAN",
            "Software Defined Wide Area Network",
        ],
    },
    "Microsoft Autopilot": {
        "any_case": ["Microsoft Autopilot", "Windows Autopilot"],
    },
    "Microsoft Intune": {
        "any_case": ["Microsoft Intune", "Intune"],
    },
    "Node": {
        "any_case": ["Node.js", "NodeJS", "Node js"],
        "exact_case": ["Node"],
    },
    "System Center Configuration Manager": {
        "any_case": [
            "System Center Configuration Manager",
            "Configuration Manager",
        ],
        "exact_case": ["SCCM", "MECM", "MEMCM"],
    },
    "Unified Modeling Language": {
        "any_case": ["Unified Modeling Language", "Unified Modelling Language"],
        "exact_case": ["UML"],
    },
    "Visual Studio Code": {
        "any_case": ["Visual Studio Code", "VS Code", "VSCode"],
    },
    "Visual Studio": {
        "any_case": ["Visual Studio", "MS Visual Studio", "Microsoft Visual Studio"],
    },
    "Windows Powershell": {
        "any_case": ["Windows Powershell", "Powershell"],
    },
    "Github": {
        "any_case": ["Github", "git hub"],
    },
    "Atlassian Jira": {
        "any_case": ["Atlassian Jira", "Jira Software", "Jira"],
    },
    "Enterprise JavaBeans": {
        "any_case": ["Enterprise JavaBeans"],
        "exact_case": ["EJB"],
    },
    "Java Persistence API": {
        "any_case": ["Java Persistence API"],
        "exact_case": ["JPA"],
    },
    "scikit-learn": {
        "any_case": ["scikit-learn", "sklearn", "scikit learn"],
    },
    ".NET": {
        "any_case": [".NET", "dotnet"],
    },
    "Entity Framework Core": {
        "any_case": ["Entity Framework Core", "EF Core", "Entity Framework"],
    },
    "Apache Hadoop": {
        "any_case": ["Apache Hadoop", "Hadoop"],
    },
    "Object-oriented analysis (OOA)": {
        "any_case": [
            "Objektorienterad analys",
            "Object-oriented analysis",
            "Object-oriented analysis (OOA)",
        ],
        "exact_case": ["OOA"],
    },
    "Object-Oriented Design (OOD)": {
        "any_case": [
            "Objektorienterad design",
            "Object-Oriented Design (OOD)",
            "Object-Oriented Design",
        ],
        "exact_case": ["OOD"],
    },
    "Open Unified Process": {
        "any_case": ["Open Unified Process", "Open UP", "OpenUP"],
    },
    "Open Source (OSS)": {
        "any_case": [
            "Open Source (OSS)",
            "Open Source",
            "Öppen källkod",
        ],
        "exact_case": ["OSS"],
    },
    "Rational Rose": {
        "any_case": ["Rational Rose", "IBM Rational Rose"],
    },
    "Rational Unified Process (RUP)": {
        "any_case": [
            "Rational Unified Process (RUP)",
            "Rational Unified Process",
            "Unified Process",
        ],
        "exact_case": ["RUP"],
    },
    "Extreme Programming (XP)": {
        "any_case": ["Extreme Programming", "extremprogramming", "extremprogrammering"],
        "exact_case": ["XP"],
    },
    "Test Driven Development": {
        "any_case": [
            "Test Driven Development",
            "testdriven utveckling",
        ],
        "exact_case": ["TDD"],
    },
    "Design Patterns": {
        "any_case": ["Design Patterns", "Designmönster", "Design pattern"],
    },
    "Android": {
        "any_case": [
            "Android OS",
            "Android-operativsystem",
            "Android-plattform",
            "Android-system",
        ],
    },
    "NetBSD": {
        "any_case": ["NetBSD", "Net BSD", "Net-BSD"],
    },
    "NixOS": {
        "any_case": ["NixOs", "Nix OS", "Nix-OS", "Nix operating system"],
    },
    "Operating System Embedded (OSE)": {
        "any_case": [
            "Enea OSE",
            "OSE operating system",
            "OSE OS",
            "Enea OSEck",
            "Operating System Embedded",
        ],
    },
    "pSOS": {
        "any_case": [
            "pSOS+",
            "pSOS OS",
            "pSOS operativsystem",
            "Integrated Systems pSOS",
            "pSOS-system",
        ],
    },
    "Raspberry Pi OS": {
        "any_case": [
            "Raspberry Pi-OS",
            "Raspberry Pi operativsystem",
        ],
    },
    "Solaris": {
        "any_case": [
            "Solaris",
            "Oracle Solaris",
            "Solaris OS",
            "Solaris Operativsystem",
        ],
    },
    "Conversational Monitor System (VM/CMS)": {
        "any_case": [
            "Conversational Monitor System",
            "Conversational Monitor System (VM/CMS)",
        ],
        "exact_case": ["CMS", "VM"],
    },
    "Virtual Memory System (VMS)": {
        "any_case": ["Virtual Memory System", "Virtual Memory System (VMS)"],
        "exact_case": ["VMS"],
    },
    "Virtual Storage Extended (VSE)": {
        "any_case": ["Virtual Storage Extended", "Virtual Storage Extended (VSE)"],
    },
    "VxWorks": {
        "any_case": [
            "VxWorks",
            "Wind River VxWorks",
            "VxWorks RTOS",
        ],
    },
    "Windows mobile": {
        "any_case": ["Windows mobile", "Windows för mobila enheter"],
    },
    "Windows": {
        "any_case": [
            "Microsoft Windows",
            "Windows OS",
            "Windows operativsystem",
            "Windows operating system",
        ],
    },
    "Agile": {
        "any_case": [
            "Agile",
            "Agilt arbetssätt",
            "Agila metoder",
            "Agile method",
        ],
    },
    "Artificial Intelligence": {
        "any_case": [
            "Artificiell intelligens",
            "Artificial Intelligence",
            "AI-lösningar",
            "AI-utveckling",
        ],
        "exact_case": ["AI"],
    },
    "Asset Information Management (AIM)": {
        "any_case": [
            "Asset Information Management (AIM)",
            "Asset Information Management",
            "AIM system",
        ],
        "exact_case": ["AIM"],
    },
    "Automation": {
        "any_case": [
            "Automation",
            "Automatisering",
        ],
    },
    "Distributed Ledger Technology (DLT)": {
        "any_case": [
            "Blockkedjeteknik",
            "Distributed Ledger Technology (DLT)",
            "blockchain",
            "distributed ledger technology",
        ],
        "exact_case": ["DLT"],
    },
    "Budgetansvar": {
        "any_case": [
            "Budgetansvar",
            "budget management",
        ],
    },
    "CASE-verktyg": {
        "any_case": [
            "CASE verktyg",
            "CASE tools",
        ],
        "exact_case": ["CASE"],
    },
    "Configuration Management (CM)": {
        "any_case": [
            "Configuration Management (CM)",
            "Configuration Management",
            "konfigurationshantering",
        ],
        "exact_case": ["CM"],
    },
    "Common Object Request Broker Architecture (CORBA)": {
        "any_case": ["Common Object Request Broker Architecture (CORBA)"],
        "exact_case": ["CORBA"],
    },
    "Database design": {
        "any_case": [
            "Database design",
            "Databasdesign",
            "Databaslösning",
        ],
    },
    "Data modeling": {
        "any_case": [
            "Datamodellering",
            "Data modeling",
        ],
    },
    "General Data Protection Regulation (GDPR)": {
        "any_case": [
            "Dataskyddsförordningen",
            "General Data Protection Regulation",
        ],
        "exact_case": ["GDPR"],
    },
    "Digitalisering": {
        "any_case": ["Digitalisation", "Digitalisering", "Digital transformation"],
    },
    "Technical dokumentation": {
        "any_case": [
            "Teknisk dokumentation",
            "Technical documentation",
        ],
    },
    "Driva workshops": {
        "any_case": [
            "Driva workshops",
            "Facilitera workshops",
            "leda workshops",
            "organisera workshops",
        ],
    },
    "English": {
        "any_case": ["English", "Engelska"],
    },
    "Enterprise Resource Planning (ERP-system)": {
        "any_case": [
            "ERP-system",
            "enterprise resource planning",
            "ERP-systems",
            "SAP ERP",
        ],
        "exact_case": ["ERP"],
    },
    "Troubleshooting tools": {
        "any_case": [
            "Felsökningsverktyg",
            "troubleshooting tools",
            "debugging tools",
            "diagnostic tools",
        ],
    },
    "Change management": {
        "any_case": [
            "Förändringsledning",
            "Förändringsledarskap",
            "Change management",
            "Change leadership",
        ],
    },
    "Geographic Information System (GIS)": {
        "any_case": [
            "geografiskt informationssystem",
            "geographic information system",
        ],
        "exact_case": ["GIS"],
    },
    "Graphical User Interface (GUI)": {
        "any_case": [
            "Graphical User Interface (GUI)",
            "graphical user interface",
            "grafiska gränssnitt",
        ],
        "exact_case": ["GUI"],
    },
    "IANA/ICANN": {
        "any_case": [
            "Internet Assigned Numbers Authority",
            "Internet Corporation for Assigned Names and Numbers",
            "DNS governance",
        ],
        "exact_case": ["IANA", "ICANN"],
    },
    "Information Architecture": {
        "any_case": [
            "information architecture",
            "informationsarkitektur",
        ],
        "exact_case": ["IA"],
    },
    "Interaction Design (IxD)": {
        "any_case": [
            "Interaktionsdesign",
            "interaction design",
            "UX interaction design",
            "design av interaktioner",
        ],
        "exact_case": ["IxD"],
    },
    "Linked Open Data (LOD)": {
        "any_case": [
            "Linked Open Data",
            "länkad data",
            "semantic web",
        ],
        "exact_case": ["LOD"],
    },
    "Leadership": {
        "any_case": [
            "Ledning",
            "leadership",
        ],
    },
    "Machine learning": {
        "any_case": [
            "machine learning",
            "maskininlärning",
        ],
        "exact_case": ["ML"],
    },
    "Human-computer interaction (HCI)": {
        "any_case": [
            "Människa-datorinteraktion (MDI)",
            "människa-datorinteraktion",
            "human-computer interaction",
            "user-computer interaction",
        ],
        "exact_case": ["HCI", "MDI"],
    },
    "Media technology": {
        "any_case": [
            "Medieteknik",
            "media technology",
        ],
    },
    "Model-view-viewmodel (MVVM)": {
        "any_case": [
            "Model-view-viewmodel (MVVM)",
            "Model-View-ViewModel",
        ],
        "exact_case": ["MVVM"],
    },
    "Cloud technology": {
        "any_case": [
            "cloud technology",
            "cloud computing",
            "cloud infrastructure",
            "Molnteknik",
            "molnlösningar",
            "molninfrastruktur",
        ],
    },
    "Offentlighets- och sekretesslagen (OSL)": {
        "any_case": [
            "offentlighets- och sekretesslagen",
            "offentlighets- och sekretesslagstiftningen",
        ],
        "exact_case": ["OSL"],
    },
    "Management model pm3": {
        "any_case": [
            "management model pm3",
            "pm3-modellen",
            "pm3 förvaltningsmodell",
        ],
        "exact_case": ["pm3"],
    },
    "Praktisk ProjektStyrning (PPS)": {
        "any_case": [
            "Praktisk ProjektStyrning (PPS)",
            "Praktisk ProjektStyrning",
            "projektstyrningsmodell PPS",
        ],
        "exact_case": ["PPS"],
    },
    "Predictive analysis": {
        "any_case": [
            "Prediktiv analys",
            "predictive analysis",
            "prediktiv modellering",
            "predictive modeling",
            "prediktiv dataanalys",
        ],
    },
    "IT Project management": {
        "any_case": [
            "IT-projektledning",
            "IT project management",
            "projektledning inom IT",
        ],
    },
    "Projektstyrningsmodell (PROPS)": {
        "any_case": [
            "Projektstyrningsmodell (PROPS)",
            "PROPS-modellen",
            "Ericsson PROPS",
        ],
        "exact_case": ["PROPS"],
    },
    "Säkerhetsanalys": {
        "any_case": [
            "säkerhetsanalys",
            "security analysis",
            "information security analysis",
            "data security",
        ],
    },
    "Scaled Agile Framework (SAFe)": {
        "any_case": [
            "Scaled Agile Framework (SAFe)",
            "Scaled Agile Framework",
            "SAFe Agile",
            "Scaled Agile",
        ],
        "exact_case": ["SAFe"],
    },
    "Swedish": {
        "any_case": [
            "Svenska",
            "Swedish",
        ],
    },
    "System management": {
        "any_case": [
            "Systemförvaltning",
            "system management",
            "application management",
        ],
    },
    "System integreration": {
        "any_case": [
            "Systemintegration",
            "system integration",
            "integration of systems",
            "integrationslösningar",
        ],
    },
    "System analysis": {
        "any_case": [
            "Systemutredning",
            "Systemanalys",
            "systems analysis",
            "system investigation",
        ],
    },
    "Test automation": {
        "any_case": [
            "testautomatisering",
            "test automation",
            "automated testing",
            "automatiserade tester",
        ],
    },
    "Service-oriented architecture (SOA)": {
        "any_case": [
            "Service-oriented architecture (SOA)",
            "service-oriented architecture",
            "tjänsteorienterad arkitektur",
        ],
        "exact_case": ["SOA"],
    },
    "Business analysis (BA)": {
        "any_case": [
            "Business analysis (BA)",
            "Verksamhetsanalys",
            "business analysis",
            "analys av verksamhetsprocesser",
        ],
    },
    "Wireless Application Protocol (WAP)": {
        "any_case": [
            "Wireless Application Protocol (WAP)",
            "WAP-teknik",
            "Wireless Application Protocol",
            "WAP technology",
        ],
        "exact_case": ["WAP"],
    },
    "Web Accessibility Initiative (WAI)": {
        "any_case": ["Web Accessibility Initiative", "W3C WAI"],
        "exact_case": ["WAI"],
    },
    "Web Content Accessibility Guidelines (WCAG)": {
        "any_case": [
            "Web Content Accessibility Guidelines",
            "WCAG compliance",
            "WCAG-kompatibilitet",
        ],
        "exact_case": ["WCAG"],
    },
    "Web development": {
        "any_case": [
            "Webbutveckling",
            "web development",
            "frontend development",
            "backend development",
            "utveckling av webbapplikationer",
        ],
    },
    # added after validation
    "Microsoft 365": {
        "any_case": [
            "Microsoft 365",
            "Office 365",
            "M365 technologies",
        ],
        "exact_case": ["M365"],
    },
    "Entra ID": {
        "any_case": [
            "Entra ID",
            "Azure AD",
            "Azure Active Directory",
        ],
    },
    "Kravhantering": {
        "any_case": [
            "Kravhantering",
            "Kravanalys",
            "säkerhetskrav",
            "kravnedbrytning",
            "kravhanteringsverktyg",
        ]
    },
    "Power Platform": {
        "any_case": ["Power Platform", "Microsoft Power Platform"],
        "exact_case": [],
    },
    "D365 F&O": {
        "any_case": [
            "D365 F&O",
            "D365 Finance & Operations",
            "D365 Finance and Operations",
            "Dynamics 365 Finance and Operations",
        ],
        "exact_case": ["D365FO"],
    },
    "Active Directory": {
        "any_case": ["Active Directory", "Active Directory (AD)"],
        "exact_case": ["AD"],  # risky, short and ambiguous
    },
    "Graph API": {
        "any_case": ["Graph API", "Microsoft Graph API", "Microsoft Graph"],
        "exact_case": [],
    },
    "Teams": {
        "any_case": ["Microsoft Teams", "MS Teams"],
        "exact_case": ["Teams"],
    },
    "PnP (Patterns and Practices)": {
        "any_case": [
            "PnP (Patterns and Practices)",
            "Patterns and Practices",
            "Patterns & Practices",
        ],
        "exact_case": ["PnP"],
    },
    "CDC": {
        "any_case": ["Change Data Capture"],
        "exact_case": ["CDC"],
    },
    "PubSub": {
        "any_case": ["PubSub", "Pub/Sub", "Google Pub/Sub"],
        "exact_case": [],
    },
    "Identity and Access Management (IAM)": {
        "any_case": [
            "Identity and Access Management (IAM)",
            "Identity and Access Management",
            "Identity & Access Management",
        ],
        "exact_case": ["IAM"],
    },
    "IAM platforms": {
        "any_case": ["IAM platforms", "IAM platform", "IAM-plattformar"],
        "exact_case": [],
    },
    "AI & LLM Engineering": {
        "any_case": ["AI & LLM Engineering", "LLM Engineering"],
        "exact_case": [],
    },
    "LLM Orchestration": {
        "any_case": ["LLM Orchestration", "LLM-orkestrering"],
        "exact_case": [],
    },
    "Agentic Frameworks": {
        "any_case": ["Agentic Frameworks", "Agentic framework", "Agentic frameworks"],
        "exact_case": [],
    },
    "LLM evaluation frameworks": {
        "any_case": ["LLM evaluation frameworks", "LLM evaluation"],
        "exact_case": [],
    },
    "LLMs": {
        "any_case": ["Large Language Models", "Large Language Model"],
        "exact_case": ["LLMs", "LLM"],
    },
    "RAG": {
        "any_case": ["Retrieval-Augmented Generation", "Retrieval Augmented Generation"],
        "exact_case": ["RAG"],
    },
    "NLP": {
        "any_case": ["Natural Language Processing", "Språkteknologi"],
        "exact_case": ["NLP"],
    },
    "MLOps fundamentals": {
        "any_case": ["MLOps fundamentals", "MLOps"],
        "exact_case": [],
    },
    "Vector databases": {
        "any_case": ["Vector databases", "Vector database", "Vektordatabaser"],
        "exact_case": [],
    },
    "Graph Databases": {
        "any_case": ["Graph Databases", "Graph database", "Grafdatabaser"],
        "exact_case": [],
    },
    "Frontend frameworks": {
        "any_case": ["Frontend frameworks", "Front-end frameworks", "Frontend-ramverk"],
        "exact_case": [],
    },
    "Data modelling": {
        "any_case": [
            "Data modelling", "Data modeling",
            "Datamodellering", "Datamodell", "Datamodeller",
        ],
        "exact_case": [],
    },
    "A/B testing": {
        "any_case": ["A/B testing", "A/B-testning", "A/B test", "AB testing"],
        "exact_case": [],
    },
    "User experience": {
        "any_case": ["User experience", "Användarupplevelse"],
        "exact_case": ["UX"],
    },
    "SAP Sales/SD": {
        "any_case": ["SAP Sales/SD", "SAP SD", "SAP Sales and Distribution"],
        "exact_case": [],
    },
    "Order-to-Cash": {
        "any_case": ["Order-to-Cash", "Order to Cash"],
        "exact_case": ["O2C"],
    },
        "vSphere": {
        "any_case": ["vSphere", "VMware vSphere"],
    },
    "ITIL-processer": {
        "any_case": ["ITIL-processer", "ITIL-processen", "ITIL processes", "ITIL process"],
        "exact_case": ["ITIL"],
    },
    "Service Integration": {
        "any_case": [
            "Service Integration",
            "Service Integration and Management",
            "Service Integrator",
            "tjänsteintegration",
        ],
        "exact_case": ["SIAM"],
    },
    "IT-miljöer": {
        "any_case": ["IT-miljöer", "IT-miljön", "IT-miljö", "IT environments", "IT environment"],
    },
    "Microsoft-miljöer": {
        "any_case": [
            "Microsoftmiljöer",
            "Microsoft-miljöer",
            "Microsoftmiljö",
            "Microsoft environments",
            "Microsoft environment",
        ],
    },
    "Continuous delivery": {
        "any_case": ["continuous delivery", "kontinuerlig leverans"],
    },
    "Verification & Validation": {
        "any_case": [
            "Verification & Validation",
            "Verification and Validation",
            "verifiering och validering",
        ],
        "exact_case": ["V&V", "VVL", "V&V/VVL"],
    },
    "Self-service solutions": {
        "any_case": [
            "self-service solutions",
            "self-service solution",
            "self service solutions",
            "självbetjäningslösningar",
        ],
    },
    "Design Management Systems": {
        "any_case": ["Design Management Systems", "Design Management System"],
    },
}
