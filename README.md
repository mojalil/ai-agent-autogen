# AI Research Agents using Autogen Framework

![Python Version](https://img.shields.io/badge/Python-3.11.4-blue?logo=python)
![Framework](https://img.shields.io/badge/Framework-Autogen-brightgreen)
![AI Research](https://img.shields.io/badge/Domain-AI%20Research-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

This project serves as a **Proof of Concept** for developing and deploying autonomous AI research agents using the Autogen framework. These agents are designed to collaboratively work together to complete tasks sent by a user, providing a robust infrastructure for exploring, developing, and testing AI algorithms in a real-world scenario.

## Key Features
- **User-directed Tasks**: Accepts commands from users and processes them to achieve the desired outcomes.
- **Collaborative Agents**: Autonomous agents work together to efficiently complete user-directed tasks.
- **Flexible Framework**: Utilizes the Autogen framework for a modular and scalable infrastructure.
- **Real-world Testing**: Provides a realistic environment for testing and evaluating AI algorithms.

## Project Structure
The project is organized as follows:
- The `agents/` directory contains the implementation of various research agents.
- The `framework/` directory houses the Autogen framework integration.
- The `tests/` directory includes all the test scripts to ensure the system's robustness and correctness.

## Functions
1. `create_agent()`: Creates a new research agent.
2. `process_command()`: Processes a user command and delegates tasks to agents.
3. `collaborate()`: Facilitates collaboration among agents to complete tasks.
4. `evaluate_performance()`: Evaluates the performance of agents and the system as a whole.
5. `report_results()`: Generates and shares reports on task completion and performance.

## Usage
To get started with this Proof of Concept:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `conda install --file requirements.txt`.
4. Run the main script to initiate the research agents: `python main.py`.

## Running Tests
To run individual tests, use the following command:
```bash
python -m unittest discover tests -p '*_test.py'
```
Or, for more verbose output:
```bash
python -m unittest discover tests -p '*_test.py' -v
```

## Contribution
We welcome contributions from the community. Feel free to open issues, propose changes, and submit Pull Requests. For major changes, please open an issue first to discuss the proposed change.

### To do
- Add initial agent logic
- Add requirements doc
- Add test where necessary

---

Designed with ❤️ by [@motypes](https://twitter.com/motypes). Join our [community](https://twitter.com/motypes) for updates and discussions.
