# Adaptive-Privacy-Preserving-Federated-Graph-Neural-Network
A graph-based federated learning prototype for network anomaly detection using GCN, adaptive aggregation, and privacy-oriented model update perturbation.
# Adaptive Privacy-Preserving Federated Graph Neural Network for Distributed Network Anomaly Detection

## Project Overview

This project implements an **Adaptive Privacy-Preserving Federated Graph Neural Network (GNN)** for network anomaly detection using the CIC-IDS2017 dataset. It combines Graph Convolutional Networks (GCN), Federated Learning (FL), and noise-based privacy mechanisms to classify network traffic as benign or malicious.

Network traffic is represented as a graph, where network entities are represented as nodes and communication flows are represented as edges. An Edge-level Graph Convolutional Network learns from node representations and network flow features to detect anomalous traffic.

The federated learning framework simulates three clients that independently train local models. Their model updates are aggregated using standard FedAvg and an adaptive aggregation approach. A privacy-oriented experiment applies gradient/update clipping and Gaussian noise to client model updates before aggregation.

The project also includes model comparison, performance evaluation, prediction analysis, and a Streamlit dashboard for visualizing detection results.

## Key Features

- **Graph-Based Network Representation:** Represents network traffic using nodes, edges, and flow-level features.
- **Graph Convolutional Network:** Uses an edge-level GCN architecture to classify network flows.
- **Federated Learning:** Simulates three clients performing local model training.
- **Standard FedAvg:** Aggregates client model updates using sample-size-based weighting.
- **Adaptive Aggregation:** Implements an update-magnitude-based adaptive aggregation approach.
- **Privacy-Oriented Training:** Experiments with update clipping and Gaussian noise to reduce direct exposure of client updates.
- **Model Comparison:** Evaluates Standard FedAvg, Adaptive FedAvg, and Private FedAvg.
- **Performance Evaluation:** Uses accuracy, precision, recall, F1-score, ROC-AUC, and PR-AUC.
- **Prediction Analysis:** Examines model predictions, classification errors, and attack probabilities.
- **Streamlit Dashboard:** Provides an interface to visualize saved detection results and model performance.

## Technologies Used

- Python
- PyTorch
- PyTorch Geometric
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Jupyter Notebook

## Dataset

The project uses the **CIC-IDS2017** intrusion detection dataset, which contains network traffic records with benign and attack labels.

The processed graph contains:
- 4,404 nodes
- 286,095 edges
- 67 edge-level features
- Binary classification: Benign and Attack

## Project Workflow

1. Load and preprocess network traffic data.
2. Construct a graph representation of network communication.
3. Extract node relationships and edge-level traffic features.
4. Train an edge-level Graph Convolutional Network.
5. Simulate three federated clients.
6. Train local models and aggregate updates using FedAvg.
7. Apply adaptive aggregation and privacy-oriented update perturbation.
8. Evaluate and compare the trained models.
9. Analyze predictions and classification errors.
10. Visualize the results through a Streamlit dashboard.

## Important Implementation Notes

This is an academic prototype that demonstrates a federated graph-learning workflow. The three clients are simulated on a single machine rather than deployed across independent devices.

The privacy component uses update clipping and Gaussian noise as an experimental privacy-oriented mechanism. It does not currently include formal differential privacy guarantees or privacy-budget accounting.

The dashboard visualizes saved model outputs. Its current detection workflow does not perform live network packet capture or real-time traffic classification.

## Project Objective

The primary objective is to explore how graph neural networks and federated learning can be combined for distributed network anomaly detection while investigating adaptive model aggregation and privacy-oriented protection of client updates.

## Future Scope

- Deployment across multiple independent client devices.
- Integration with live network traffic monitoring.
- Formal differential privacy guarantees with privacy-budget accounting.
- Improved adaptive aggregation strategies.
- Better attack detection performance and false-positive reduction.
- Evaluation on additional network intrusion datasets.
- Real-time monitoring and alert generation.
